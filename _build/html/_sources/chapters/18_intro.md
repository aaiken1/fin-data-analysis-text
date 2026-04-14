# Trading strategies and backtesting

> I think that good quant investment managers ... can really be thought of as financial economists who have codified their beliefs into a repeatable process. They are distinguished by diversification, sticking to their process with discipline, and the ability to engineer portfolio characteristics.
> — Cliff Asness of AQR (2007)

Broadly speaking, **quantitative investing** tries to turn an investment thesis into a repeatable process. The thesis is often **model driven**, perhaps related to some economic rationale that repeats itself. For example, maybe stocks with certain characteristics generate positive risk-adjusted returns, on average.

This process means using **historical** or **simulated** data to test a hypothesis. This is called **backtesting** -- there's an entire literature on the best way to do this. We'll look at two complementary approaches: building and testing trading strategies with the `bt` package, and evaluating alpha factors with `alphalens`.

```{note}
Backtesting is seductive. It's easy to find strategies that "work" in historical data but fail going forward. A healthy skepticism of backtest results is one of the most important things you can develop.
```

## What you'll learn

By the end of this chapter, you should be able to:

- Build and backtest trading strategies in Python using the `bt` package
- Construct signal-based strategies like SMA crossovers and momentum
- Evaluate strategy performance using Sharpe ratio, drawdowns, and other metrics
- Understand the pitfalls of backtesting: overfitting, look-ahead bias, survivorship bias
- Use `alphalens` to analyze whether a factor (like momentum) actually predicts returns
- Interpret factor tear sheets: returns by quantile, information coefficient, and turnover

## Chapter structure

| Section | Topic | Key Ideas |
|---------|-------|-----------|
| **Backtesting with BT** | Building and testing trading strategies | Equal-weight, SMA crossover, momentum, transaction costs, in-sample vs. out-of-sample |
| **Factor Analysis with Alphalens** | Evaluating alpha factors | Momentum factor, long-short portfolios, quantile returns, information coefficient, tear sheets |

## Key references

- [Efficiently Inefficient by Lasse Pedersen](https://press.princeton.edu/books/hardcover/9780691166193/efficiently-inefficient) -- Chapter 3.3 introduces quantitative equity strategies
- [bt package documentation](https://pmorissette.github.io/bt/) -- the backtesting framework we use
- [alphalens-reloaded documentation](https://alphalens.ml4trading.io) -- factor analysis toolkit from the Quantopian ecosystem
- [Jegadeesh and Titman (1993)](https://doi.org/10.1111/j.1540-6261.1993.tb04702.x) -- the original momentum paper

## Using AI for trading strategies

AI tools are particularly helpful here:

- **Writing bt strategies**: "Help me build a bt strategy that buys stocks above their 200-day moving average"
- **Interpreting results**: Paste backtest output into Claude and ask "Is this strategy any good?"
- **Debugging**: "Why is my backtest throwing an error about NaN prices?"
- **Factor construction**: "How do I calculate a 12-1 momentum factor for a universe of stocks?"

```{tip}
When asking AI about trading strategies, be specific about your universe (what stocks?), your signal (what triggers a trade?), and your rebalancing frequency (how often?). Vague prompts lead to generic answers.
```
