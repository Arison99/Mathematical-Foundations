# GCD examples

## Euclidean reductions

For `48` and `18`:

| Pair | Division with remainder |
| --- | --- |
| `(48, 18)` | `48 = 2·18 + 12` |
| `(18, 12)` | `18 = 1·12 + 6` |
| `(12, 6)` | `12 = 2·6 + 0` |

The final pair is `(6, 0)`, so the algorithm returns `6` by the terminal convention. This traces the procedure; see [proof notes](proof-notes.md) for open proof questions.

## Boundary cases

- `gcd(21, 0) = 21` and `gcd(0, 21) = 21`.
- `gcd(0, 0) = 0` by this repository's computational convention.
- Equal magnitudes return that magnitude, for example `gcd(13, 13) = 13`.
- If one magnitude divides the other, for example `gcd(24, 6) = 6`.
- Signed inputs are normalized, so `gcd(-48, 18) = 6`.
- `lcm(a, 0) = 0` for every integer `a` in the implementation contract.

## LCM example

For nonzero `48` and `18`, `gcd(48,18) = 6`, so `lcm(48,18) = (48/6)·18 = 144`. The reduced product form avoids computing `48·18` before division.
