from AlgorithmImports import *

class GAPMAlgorithm(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(1990, 1, 1)
        self.SetEndDate(2023, 1, 1)
        self.SetCash(100000)
        
        self.symbol = self.AddEquity("QQQ", Resolution.Daily).Symbol
        
        self.period = 40
        self.signalPeriod = 20
        
        self.upGaps = []
        self.downGaps = []
        self.gapRatios = RollingWindow[float](self.signalPeriod)
        
        self.Schedule.On(self.DateRules.EveryDay(self.symbol), 
                         self.TimeRules.BeforeMarketClose(self.symbol, 10), 
                         self.CheckGAPM)

    def OnData(self, data):
        # Placeholder for required method
        pass

    def CheckGAPM(self):
        history = self.History(self.symbol, self.period + 2, Resolution.Daily)
        
        if not history.empty:
            self.upGaps.clear()
            self.downGaps.clear()
            
            for i in range(1, len(history) - 1):
                gap = history['open'][i] - history['close'][i - 1]
                if gap > 0:
                    self.upGaps.append(gap)
                elif gap < 0:
                    self.downGaps.append(-gap)
            
            upGapsSum = sum(self.upGaps)
            downGapsSum = sum(self.downGaps)
            
            gapRatio = 100 * upGapsSum / downGapsSum if downGapsSum != 0 else 1
            self.gapRatios.Add(gapRatio)
            
            if self.gapRatios.IsReady:
                currentRatio = self.gapRatios[0]
                previousRatio = self.gapRatios[1]
                
                # Enter long position if the GAPM ratio is rising
                if currentRatio > previousRatio and not self.Portfolio[self.symbol].Invested:
                    self.SetHoldings(self.symbol, 1.0)
                    self.Debug(f"Entering long position on {self.Time.date()}")
                
                # Exit long position if the GAPM ratio is falling
                elif currentRatio < previousRatio and self.Portfolio[self.symbol].Invested:
                    self.Liquidate(self.symbol)
                    self.Debug(f"Exiting long position on {self.Time.date()}")
