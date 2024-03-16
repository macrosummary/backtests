# Time Series Momentum Analysis and Backtest

This repository hosts an in-depth analysis and implementation of the trading strategy discussed in the paper "Time Series Momentum: Is it there?" by Dashan Huang, Jiangyuan Li, Liyao Wang, and Guofu Zhou. Additionally, it includes a QuantConnect backtest algorithm that executes a simplified version of the Time Series Momentum (TSM) strategy, as outlined in the paper.

## Paper Summary

The paper investigates the presence of time series momentum (TSM) across various asset classes. It challenges previous findings on TSM's effectiveness, arguing that evidence supporting TSM is weak, especially when considering asset-by-asset time series regressions both in and out of sample. Through comprehensive analysis, the study suggests that the profitability associated with TSM strategies might not stem from predictability based on past returns but could be attributed to other factors like the historical mean returns of assets.

## QuantConnect Backtest Algorithm

The QuantConnect backtest algorithm is a Python script designed to test the TSM strategy on a set of selected assets. It follows a simple rule: buy assets that had positive returns over the past 12 months and sell (or avoid) assets with negative returns over the same period. The algorithm is implemented in QuantConnect, a cloud-based backtesting platform that allows for testing trading strategies over historical data.

## How to Run
* Sign up for a QuantConnect account if you haven't already.
* Navigate to the Algorithm Lab and create a new Python algorithm.
* Copy the Python script from /backtest and paste it into the QuantConnect code editor.
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
