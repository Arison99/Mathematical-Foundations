# GCD: theory and conventions

## Divisibility and common divisors

For integers `d` and `n`, `d` divides `n` (written `d | n`) when there is an integer `k` such that `n = dk`. In particular, every nonzero integer divides zero, and zero divides only zero. A common divisor of integers `a` and `b` divides both of them.

For integers not both zero, their greatest common divisor, written `gcd(a, b)`, is the greatest positive common divisor. Equivalently, it is the unique nonnegative generator of the set of their integer linear combinations. This project extends the computational convention to `gcd(0, 0) = 0`; since every integer divides zero, there is no greatest positive common divisor of `(0, 0)` under the usual definition. Other mathematical treatments leave this value undefined or handle it separately.

For arbitrary signed integer inputs, the GCD is nonnegative and `gcd(a, b) = gcd(|a|, |b|)`. Implementations in this repository accept signed integers and normalize their magnitudes.

## Remainders and the Euclidean identity

For `a ≥ 0` and `b > 0`, division with remainder gives unique integers `q` and `r` such that `a = qb + r` and `0 ≤ r < b`. The value `r` is `a mod b` in this document.

The key Euclidean identity is

`gcd(a, b) = gcd(b, a mod b)` for integers `a ≥ b > 0`.

It expresses preservation of the common divisors when replacing `(a, b)` by `(b, r)`: because `r = a - qb`, any divisor of `a` and `b` divides `r`; because `a = qb + r`, any divisor of `b` and `r` divides `a`. The proof worksheet identifies the propositions to establish; this explanation is not a claim that the repository owner has completed a formal proof.

The identity is a mathematical statement. The Euclidean algorithm is an executable procedure that applies this identity repeatedly until the remainder becomes zero.

## Terminal case and algorithm

For nonnegative integer `a`, `gcd(a, 0) = a`, including the repository convention for `a = 0`. The algorithm maintains a pair `(a, b)`, replacing it with `(b, a mod b)` while `b > 0`; it returns `a` at termination. The pseudocode page specifies signed-input normalization, LCM behavior, and invalid-input handling.

Example: `48 = 2·18 + 12`, `18 = 1·12 + 6`, `12 = 2·6 + 0`, so the successive pairs are `(48,18)`, `(18,12)`, `(12,6)`, `(6,0)` and the result is `6`.

## GCD and LCM

For nonzero integers `a` and `b`,

`lcm(a, b) = |ab| / gcd(a, b)`.

The LCM is conventionally the least positive common multiple. In implementation, the equivalent form `(|a| / gcd(a,b)) · |b|` reduces intermediate growth; a zero operand is handled separately and returns zero. The mathematical formula above is only stated for nonzero operands. The C++ implementation detects a result that cannot fit in `uint64_t`.

## Termination and complexity

Whenever `b > 0`, the remainder satisfies `0 ≤ a mod b < b`, so the second component strictly decreases through nonnegative integers and eventually reaches zero. A standard bound on the number of remainder operations is logarithmic in the smaller positive input: `O(log(min(a,b)))`, with `O(1)` auxiliary space in the conventional arithmetic-operation model. Actual runtime also depends on operand size and the cost of remainder and other arithmetic operations; Python arbitrary-precision operations are not constant-time as operands grow.

The classical worst-case remainder sequence is attained by consecutive Fibonacci numbers. The worksheet leaves the details of deriving the operation bound for independent study.
