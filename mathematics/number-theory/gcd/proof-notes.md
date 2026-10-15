# Proof worksheet: Euclidean algorithm

This worksheet is for independent study and handwritten derivations. It states goals and prompts, not completed proofs. Fill in each argument and check its hypotheses before treating a claim as established.

## 1. Common divisors under Euclidean reduction

**Proposition to establish:** For integers `a ≥ b > 0`, the common divisors of `(a,b)` are exactly the common divisors of `(b, a mod b)`.

**Definitions to use:** `a = qb + r`, `0 ≤ r < b`, and divisibility `d | n` iff `n = dk` for some integer `k`.

**Questions:** If `d | a` and `d | b`, what can you conclude about `d | (a - qb)`? Conversely, if `d | b` and `d | r`, what can you conclude about `d | (qb + r)`? Which equality connects these expressions to the remainder and to `a`?

## 2. Termination

**Proposition to establish:** Starting with nonnegative `a,b`, repeated replacement `(a,b) ← (b, a mod b)` reaches a pair whose second component is zero after finitely many steps.

**Facts to use:** Every nonzero remainder is a nonnegative integer strictly less than the divisor.

**Questions:** What quantity decreases at every nonterminal step? Why can it not decrease strictly forever while remaining a nonnegative integer? Handle the initial cases `b = 0` and `a = 0`.

## 3. Terminal value is the GCD

**Proposition to establish:** The algorithm's returned value is the nonnegative greatest common divisor of the original inputs under the repository convention.

**Facts to use:** Common-divisor preservation at every reduction, the terminal condition `gcd(x,0)=x` for `x ≥ 0`, and termination.

**Questions:** How does the set of common divisors relate between the initial and final pairs? At termination, which nonnegative integers divide both components? How does the `(0,0)` convention fit the computational result, and why does it differ from “greatest positive common divisor” as a definition?

## 4. Time complexity

**Proposition to establish:** For positive inputs, the number of remainder operations is `O(log(min(a,b)))` in the conventional arithmetic-operation model.

**Facts to investigate:** The remainders decrease; the slowest Euclidean sequences are related to consecutive Fibonacci numbers.

**Questions:** What lower bound on the initial smaller operand follows from a sequence of `k` remainder steps? How does the Fibonacci recurrence yield an exponential lower bound in `k`? Translate that bound into a logarithmic upper bound on `k`. How does the analysis change when arithmetic costs depend on operand bit length?

## 5. GCD–LCM relationship

**Proposition to establish:** For nonzero integers `a,b`, `lcm(a,b) = |ab|/gcd(a,b)`.

**Definitions to use:** Positive least common multiple, prime factorization or divisibility, and the GCD's prime exponents.

**Questions:** For each prime, how do its exponents in the GCD and LCM relate to its exponents in `|a|` and `|b|`? Why does multiplying the GCD and LCM recover `|ab|`? Why must zero inputs be treated separately for the formula and the chosen LCM convention?
