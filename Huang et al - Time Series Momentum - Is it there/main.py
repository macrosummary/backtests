# region imports
from AlgorithmImports import *
from datetime import timedelta

class TimeSeriesMomentumAlgorithm(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(1990, 1, 1)  # Set Start Date
        self.SetEndDate(2024, 1, 1)    # Set End Date
        self.SetCash(100000)           # Set Strategy Cash
        
        # Add equity assets
        self.equities = ['SPY', 'QQQ', 'IWM']
        for ticker in self.equities:
            self.AddEquity(ticker, Resolution.Daily)
        
        self.lookback = 252 # Trading days in a year, approximating 12 months
        self.Schedule.On(self.DateRules.MonthStart(self.equities[0]), 
                         self.TimeRules.At(10, 0), 
                         Action(self.RebalancePortfolio))

    def RebalancePortfolio(self):
        for ticker in self.equities:
            history = self.History([ticker], self.lookback, Resolution.Daily)
            if not history.empty:
                # Calculate returns over the lookback period
                start_price = history.iloc[0]['close']
                end_price = history.iloc[-1]['close']
                performance = (end_price - start_price) / start_price
                
                # Implement TSM strategy
                if performance > 0:
                    self.SetHoldings(ticker, 1.0 / len(self.equities))
                else:
                    self.Liquidate(ticker)
