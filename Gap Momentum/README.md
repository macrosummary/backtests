# Gap Momentum System Backtest

This repository contains a QuantConnect algorithm for backtesting the Gap Momentum System, as presented by Perry Kaufman. The system leverages opening gap data to create a momentum strategy, focusing on the accumulation of positive and negative gap values. This README provides an overview of the system, setup instructions, and how to run the backtest.

## System Overview

The Gap Momentum System calculates the gap momentum by comparing the sum of positive gaps to the sum of negative gaps over a specified period. This gap ratio is added to a cumulative series similar to the On-Balance Volume (OBV) but specifically for gap openings. A simple moving average of this series forms the "signal line," providing the basis for the following trading signals:

- **Enter Long:** When the signal line is moving higher.
- **Exit Trade:** When the signal line is moving lower.

This strategy is inspired by both J. Welles Wilder and Joseph Granville's OBV, emphasizing the significance of gap movements in the market.

## Installation

1. **Clone the Repository**: Clone this repository to your local machine or QuantConnect research environment.
`git clone https://github.com/your-username/gap-momentum-system.git`

2. **QuantConnect Setup**: Ensure you have a QuantConnect account and have set up the Lean Engine if you plan to run this backtest locally.

## Running the Backtest

### QuantConnect Cloud

1. Upload the `GapMomentumSystem.py` to your QuantConnect account.
2. Create a new project and add the uploaded algorithm file.
3. Set the backtest period and cash amount according to your preference.
4. Run the backtest and analyze the results.

### Local Environment

If you have the Lean Engine set up locally:

1. Place `GapMomentumSystem.py` in the Lean `Algorithm.Python` directory.
2. Configure your backtest in the `backtest.json` file.
3. Run the following command:
`lean backtest "GapMomentumSystem"`

4. Review the backtest results in the `Backtest` directory.

## Configuration

The strategy parameters such as gap period and signal line period can be adjusted in the `GapMomentumSystem.py` file. These input parameters are crucial for tuning the strategy to different markets or conditions.

## Contributions

Contributions to improve the strategy or its implementation are welcome. Please follow the standard pull request process to propose your changes.

## Disclaimer

This algorithm is provided for educational purposes only. Investing in financial markets involves risk, and this or any strategy may not be suitable for all investors. Perform your due diligence before live trading.

## References

- Kaufman, P. (2024). "Gap Momentum." Traders' Tips - January 2024.
- Additional insights on the system and its background are derived from the implementation guidelines as discussed in various financial software languages, including MetaStock formulas and TradingView's Pine Script.
