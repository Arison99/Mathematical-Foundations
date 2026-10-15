"""Iterative Euclidean GCD and LCM.

Mathematical specification: see
``mathematics/number-theory/gcd/theory.md`` at the repository root.
"""

from __future__ import annotations

import operator


def _as_integer(value: object, name: str) -> int:
    """Return an integer index value, rejecting floats and other coercions."""
    if isinstance(value, bool):
        raise TypeError(f"{name} must be an integer, not bool")
    try:
        return operator.index(value)
    except TypeError as exc:
        raise TypeError(f"{name} must be an integer") from exc


def gcd(a: int, b: int) -> int:
    """Return the nonnegative GCD of integer inputs.

    Negative operands are normalized by magnitude; ``gcd(0, 0)`` is defined
    as 0 by this module's computational convention. Inputs must implement
    Python's integer index protocol; booleans and floats are rejected.
    """
    left = abs(_as_integer(a, "a"))
    right = abs(_as_integer(b, "b"))
    while right:
        left, right = right, left % right
    return left


def lcm(a: int, b: int) -> int:
    """Return the nonnegative LCM; return 0 if either integer is zero.

    Inputs follow the same contract as :func:`gcd`. Python integers have
    arbitrary precision, subject to available memory and runtime.
    """
    left = abs(_as_integer(a, "a"))
    right = abs(_as_integer(b, "b"))
    if left == 0 or right == 0:
        return 0
    return (left // gcd(left, right)) * right
