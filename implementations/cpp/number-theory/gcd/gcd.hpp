#ifndef MATHEMATICAL_FOUNDATIONS_GCD_HPP
#define MATHEMATICAL_FOUNDATIONS_GCD_HPP

#include <cstdint>
#include <limits>
#include <stdexcept>

namespace mathematical_foundations {

// Inputs are signed 64-bit integers. Results use uint64_t so that the
// magnitude of INT64_MIN (2^63) is representable. See the canonical
// specification at mathematics/number-theory/gcd/theory.md.
inline std::uint64_t gcd(std::int64_t a, std::int64_t b) noexcept {
    const auto magnitude = [](std::int64_t value) noexcept -> std::uint64_t {
        // Negating INT64_MIN in the signed type would overflow. Offset by one
        // before negation, then add one in the unsigned result.
        return value < 0
                   ? static_cast<std::uint64_t>(-(value + 1)) + 1U
                   : static_cast<std::uint64_t>(value);
    };

    std::uint64_t left = magnitude(a);
    std::uint64_t right = magnitude(b);
    while (right != 0U) {
        const std::uint64_t remainder = left % right;
        left = right;
        right = remainder;
    }
    return left;
}

// Returns zero when either operand is zero. Throws overflow_error if the
// exact nonnegative LCM does not fit in uint64_t.
inline std::uint64_t lcm(std::int64_t a, std::int64_t b) {
    const std::uint64_t left = a < 0
                                   ? static_cast<std::uint64_t>(-(a + 1)) + 1U
                                   : static_cast<std::uint64_t>(a);
    const std::uint64_t right = b < 0
                                    ? static_cast<std::uint64_t>(-(b + 1)) + 1U
                                    : static_cast<std::uint64_t>(b);
    if (left == 0U || right == 0U) {
        return 0U;
    }

    const std::uint64_t reduced = left / gcd(a, b);
    if (reduced > std::numeric_limits<std::uint64_t>::max() / right) {
        throw std::overflow_error("LCM does not fit in uint64_t");
    }
    return reduced * right;
}

}  // namespace mathematical_foundations

#endif  // MATHEMATICAL_FOUNDATIONS_GCD_HPP
