# Time Series Momentum Analysis and Backtest

This repository hosts an in-depth analysis and implementation of the trading strategy discussed in the paper "Time Series Momentum: Is it there?" by Dashan Huang, Jiangyuan Li, Liyao Wang, and Guofu Zhou. Additionally, it includes a QuantConnect backtest algorithm that executes a simplified version of the Time Series Momentum (TSM) strategy, as outlined in the paper.

## Paper Summary

The paper investigates the presence of time series momentum (TSM) across various asset classes. It challenges previous findings on TSM's effectiveness, arguing that evidence supporting TSM is weak, especially when considering asset-by-asset time series regressions both in and out of sample. Through comprehensive analysis, the study suggests that the profitability associated with TSM strategies might not stem from predictability based on past returns but could be attributed to other factors like the historical mean returns of assets.

### Overview of Time Series Momentum (TSM) Strategy
* TSM Strategy: It involves buying assets that have had positive returns over the past 12 months and selling (or avoiding) assets with negative returns over the same period. This approach is based on the premise that assets with positive momentum will continue to perform well, while those with negative momentum will continue to perform poorly.
* Comparison with Time Series History (TSH): The study introduces a Time Series History (TSH) strategy as a comparison to TSM. TSH strategy involves buying assets with historically positive mean returns and selling those with negative mean returns, without relying on predictability based on past 12-month returns. The performance of TSM is closely compared to TSH to evaluate the necessity of predictability in executing a profitable trading strategy.

### Key Findings and Analysis
* Weak Evidence of TSM: The study finds little evidence supporting TSM when conducting time series regressions asset-by-asset. Both in-sample and out-of-sample analyses reveal weak predictability of future returns based on past returns.
* Comparison of TSM and TSH Strategies: The empirical comparison shows that the TSM strategy's profitability is nearly identical to that of the TSH strategy. This suggests that the success attributed to TSM might not necessarily stem from the predictability but could be due to other factors, such as the assets' inherent risk premiums.
* Statistical Significance: The paper critically analyzes the statistical methods used in previous studies to claim the presence of TSM. Through various bootstrap methods and controlling for fixed effects, it demonstrates that the significant t-statistics reported in previous studies might not reliably indicate the presence of TSM.
* Performance Across Asset Classes: The study does not find consistent evidence of TSM across different asset classes (commodities, equities, bonds, and currencies), further questioning the ubiquity of TSM.
* Volatility Scaling: It also touches upon the role of volatility scaling in assessing the performance of TSM strategies. Volatility scaling is a technique used to adjust the position size based on the asset's volatility, intending to normalize the risk across different assets.

### Conclusion
The paper concludes that the evidence supporting the existence of Time Series Momentum across a large cross-section of assets is weak. It suggests that the profitability observed in TSM strategies might not be due to the predictability of returns based on past performance but could be attributed to other factors like the historical mean returns of assets. This challenges the notion that TSM is a pervasive and exploitable phenomenon across global financial markets.

## QuantConnect Backtest Algorithm

The QuantConnect backtest algorithm is a Python script designed to test the TSM strategy on a set of selected assets. It follows a simple rule: buy assets that had positive returns over the past 12 months and sell (or avoid) assets with negative returns over the same period. The algorithm is implemented in QuantConnect, a cloud-based backtesting platform that allows for testing trading strategies over historical data.

## How to Run
* Sign up for a QuantConnect account if you haven't already.
* Navigate to the Algorithm Lab and create a new Python algorithm.
* Copy the Python script main.py and paste it into the QuantConnect code editor.
* Adjust the symbols list in the script to include the assets you wish to test.
* Click "Build" to compile the algorithm and then "Backtest" to run it over the specified period.

## Results and Discussion

The backtest results can be found in the directory, including performance metrics and comparisons to benchmark indices.

## Citation

If you use the contents of this repository in your research, please cite the original paper:
Huang, D., Li, J., Wang, L., & Zhou, G. (2020). Time series momentum: Is it there? Journal of Financial Economics, 135(3), 774-794.

## Acknowledgments

Thanks to the authors of the paper for their insightful analysis on the time series momentum phenomenon.
Appreciation goes to QuantConnect for providing the platform to test and validate trading strategies.
