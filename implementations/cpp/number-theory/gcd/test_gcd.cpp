#include "gcd.hpp"

#include <cassert>
#include <cstdint>
#include <limits>
#include <stdexcept>

int main() {
    using mathematical_foundations::gcd;
    using mathematical_foundations::lcm;

    assert(gcd(48, 18) == 6U);
    assert(gcd(54, 24) == 6U);
    assert(gcd(17, 13) == 1U);
    assert(gcd(21, 0) == 21U);
    assert(gcd(0, 21) == 21U);
    assert(gcd(0, 0) == 0U);
    assert(gcd(13, 13) == 13U);
    assert(gcd(24, 6) == 6U);
    assert(gcd(6, 24) == 6U);
    assert(gcd(-48, 18) == 6U);
    assert(gcd(-48, -18) == 6U);
    assert(gcd(std::numeric_limits<std::int64_t>::min(), 0) ==
           (std::uint64_t{1} << 63U));

    assert(lcm(48, 18) == 144U);
    assert(lcm(-4, 6) == 12U);
    assert(lcm(0, 21) == 0U);
    assert(lcm(0, 0) == 0U);
    assert(lcm(std::numeric_limits<std::int64_t>::min(), 1) ==
           (std::uint64_t{1} << 63U));

    bool overflow_reported = false;
    try {
        (void)lcm(std::numeric_limits<std::int64_t>::min(), -3);
    } catch (const std::overflow_error&) {
        overflow_reported = true;
    }
    assert(overflow_reported);
}
