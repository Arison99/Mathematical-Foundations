# Greatest common divisor

The greatest common divisor (GCD) of two integers is the greatest nonnegative integer dividing both. The iterative Euclidean algorithm computes it by repeatedly replacing a pair with the smaller value and the remainder. Under the nonnegative remainder convention, `gcd(48, 18) = gcd(18, 12) = gcd(12, 6) = gcd(6, 0) = 6`.

## Study materials

- [Theory and conventions](theory.md)
- [Language-independent pseudocode](pseudocode.md)
- [Worked examples](examples.md)
- [Proof worksheet](proof-notes.md) — questions and propositions for independent proof writing; these proofs are not completed here.
- [Applications](problems/applications.md)

## Implementations and tests

- [Python](../../../implementations/python/number-theory/gcd/gcd.py): `python -m unittest discover -s implementations/python/number-theory/gcd -p "test_*.py"`
- [C++](../../../implementations/cpp/number-theory/gcd/gcd.hpp): compile and run its standalone test with `g++ -std=c++17 -Wall -Wextra -pedantic implementations/cpp/number-theory/gcd/test_gcd.cpp -o gcd-test` followed by `./gcd-test` (PowerShell: `.\gcd-test.exe`).

Both implementations accept signed integer inputs, normalize each operand to its absolute value, and define `gcd(0, 0) = 0`. Their LCM functions return zero when either input is zero. Python integers grow as needed subject to available memory. C++ uses `std::int64_t` for inputs and `std::uint64_t` for GCD and LCM results; the LCM function detects when the mathematical result exceeds `uint64_t` and throws `std::overflow_error` rather than overflowing. See the [theory](theory.md) for mathematical conventions and complexity.

## Complexity

For positive inputs, GCD takes `O(log(min(a, b)))` remainder operations and `O(1)` auxiliary space under the conventional arithmetic-operation model. Actual runtime depends on integer representation and arithmetic costs. LCM adds multiplication/division, with fixed-width overflow checked in C++.

## Possible follow-up topics

- Extended Euclidean algorithm and Bézout coefficients.
- Modular inverses and linear Diophantine equations.
- Binary GCD and comparison of remainder-operation costs.
