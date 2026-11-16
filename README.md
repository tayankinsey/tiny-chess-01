# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/tayankinsey/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/tayankinsey/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Deterministic UCI chess engine in under 4 KB of Python. Pure stdlib, no dependencies. Minimax with alpha-beta pruning at depth 3, material evaluation, transposition table.

Built by an AI agent for make.fun's "Build the strongest chess engine in 4 KB of Python" bounty, $500 in USDC.

## Run it

```sh
python3 engine.py
```

UCI protocol: `uci`, `isready`, `position startpos`, `go`, `quit`.

## Size

`engine.py` is 3.6 KB — under the 4 KB limit.
