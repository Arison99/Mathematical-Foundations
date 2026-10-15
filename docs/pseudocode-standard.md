# Pseudocode standard

Pseudocode should express the algorithm independently of programming-language syntax. Define nonstandard notation and input assumptions near the algorithm; use mathematical operators consistently and distinguish assignment from equality.

- Use `←` for assignment and `=` for equality in conditions.
- Use `IF` / `ELSE` / `END IF`, `WHILE` / `END WHILE`, and `FOR` / `END FOR` with explicit blocks.
- Write functions with named inputs and an explicit `RETURN` value.
- State whether indexing starts at zero or one, and specify interval endpoints.
- Use standard mathematical notation such as `×`, `≤`, `≠`, and `mod`; define any ambiguity.
- State input domains, preconditions, output behavior, and relevant edge cases.

Example:

```text
FUNCTION gcd(a, b)
    WHILE b ≠ 0
        (a, b) ← (b, a mod b)
    END WHILE
    RETURN a
END FUNCTION
```

This example assumes nonnegative integer inputs and illustrates notation only; input policy and correctness should be established in the relevant concept documentation.
