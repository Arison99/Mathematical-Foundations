# GCD and LCM pseudocode

## Contract

Inputs are integers; normalize both to nonnegative magnitudes before applying the procedures. The GCD result is nonnegative and uses `gcd(0, 0) = 0` as a computational convention. LCM returns `0` when either input is zero. Non-integer inputs are invalid and must be rejected by an implementation rather than silently converted. The C++ fixed-width input limits are documented alongside its implementation.

## Iterative GCD

```text
FUNCTION GCD(a, b)
    REQUIRE a and b are integers
    a ← |a|
    b ← |b|
    WHILE b ≠ 0
        (a, b) ← (b, a mod b)
    END WHILE
    RETURN a
END FUNCTION
```

Here `mod` returns the unique remainder `r` with `0 ≤ r < b` for `a ≥ 0`, `b > 0`. Termination occurs when `b = 0`; the return value then follows the terminal convention `gcd(a, 0) = a`.

## LCM using GCD

```text
FUNCTION LCM(a, b)
    REQUIRE a and b are integers
    IF a = 0 OR b = 0
        RETURN 0
    END IF
    g ← GCD(a, b)
    RETURN (|a| / g) × |b|
END FUNCTION
```

The division is exact for integer inputs. An implementation with bounded integer types must detect overflow in the multiplication and report it; arbitrary-precision implementations are limited by available resources. No other variant is included.
