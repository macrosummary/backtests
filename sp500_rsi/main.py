from AlgorithmImports import *

class SP500RSIStrategyWithUniverseAndRiskManagement(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(1998, 1, 1)  # Start date
        self.SetEndDate(2024, 3, 1)    # End date
        self.SetCash(100000)           # Initial capital

        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.maximumLeverage = 0.02  # Adjusted for individual stocks, assuming equal weight
        self.trailingStopRisk = 0.02  # 2% trailing stop
        self.symbolsData = {}  # Dictionary to hold SymbolData objects

        self.AddUniverse(self.Universe.QC500)
        self.Schedule.On(self.DateRules.EveryDay(self.spy), self.TimeRules.BeforeMarketClose(self.spy, 10), self.Rebalance)

    def OnSecuritiesChanged(self, changes):
        for added in changes.AddedSecurities:
            if added.Symbol not in self.symbolsData:
                symbolData = SymbolData(added.Symbol, self)
                self.symbolsData[added.Symbol] = symbolData

                # Implementing dynamic leverage based on volatility or other factors could go here

        for removed in changes.RemovedSecurities:
            if removed.Symbol in self.symbolsData:
                if self.Portfolio[removed.Symbol].Invested:
                    self.Liquidate(removed.Symbol)
                del self.symbolsData[removed.Symbol]

    def Rebalance(self):
        totalEquity = self.Portfolio.TotalPortfolioValue
        # Margin buffer to prevent margin calls, adjust according to strategy needs
        marginBuffer = totalEquity * 0.1  # Maintaining a 10% buffer
        availableMargin = self.Portfolio.MarginRemaining - marginBuffer

        for symbol, symbolData in self.symbolsData.items():
            if not symbolData.RSI.IsReady:
                continue

            # Adjust the target percent per stock based on dynamic conditions if necessary
            targetPercentPerStock = self.maximumLeverage

            if not self.Portfolio[symbol].Invested and symbolData.RSI.Current.Value < 20:
                # Calculate the size not to exceed the available margin
                quantity = min(self.CalculateOrderQuantity(symbol, targetPercentPerStock), availableMargin / self.Securities[symbol].Price)
                self.SetHoldings(symbol, quantity / totalEquity)
            elif self.Portfolio[symbol].Invested and symbolData.IsExitConditionMet():
                self.Liquidate(symbol)

            # Implement trailing stop loss logic
            if self.Portfolio[symbol].Invested:
                investedQuantity = self.Portfolio[symbol].Quantity
                averagePrice = self.Portfolio[symbol].AveragePrice
                stopPrice = averagePrice * (1 - self.trailingStopRisk)
                if self.Securities[symbol].Price < stopPrice:
                    self.Liquidate(symbol)

class SymbolData:
    def __init__(self, symbol, algorithm):
        self.Symbol = symbol
        self.RSI = algorithm.RSI(symbol, 3, MovingAverageType.Simple, Resolution.Daily)
        self.PreviousHigh = None
        self.Algorithm = algorithm

    def IsExitConditionMet(self):
        currentHigh = self.Algorithm.Securities[self.Symbol].High
        price = self.Algorithm.Securities[self.Symbol].Price
        if self.PreviousHigh is None or price > self.PreviousHigh:
            self.PreviousHigh = max(self.PreviousHigh or float('-inf'), currentHigh)
            return price > self.PreviousHigh
        return False
