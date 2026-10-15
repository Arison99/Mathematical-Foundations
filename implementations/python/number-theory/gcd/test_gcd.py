import random
import unittest

from gcd import gcd, lcm


class GcdTests(unittest.TestCase):
    def test_required_examples_and_boundaries(self):
        cases = [
            ((48, 18), 6),
            ((54, 24), 6),
            ((17, 13), 1),
            ((21, 0), 21),
            ((0, 21), 21),
            ((0, 0), 0),
            ((13, 13), 13),
            ((24, 6), 6),
            ((6, 24), 6),
            ((-48, 18), 6),
            ((48, -18), 6),
            ((-48, -18), 6),
        ]
        for operands, expected in cases:
            with self.subTest(operands=operands):
                self.assertEqual(gcd(*operands), expected)

    def test_large_arbitrary_precision_values(self):
        scale = 10**150
        self.assertEqual(gcd(48 * scale, 18 * scale), 6 * scale)
        self.assertEqual(lcm(48 * scale, 18 * scale), 144 * scale)

    def test_invalid_types_are_rejected(self):
        for value in (1.0, "1", None, True):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    gcd(value, 2)
                with self.assertRaises(TypeError):
                    lcm(2, value)

    def test_lcm_cases(self):
        self.assertEqual(lcm(48, 18), 144)
        self.assertEqual(lcm(-4, 6), 12)
        self.assertEqual(lcm(0, 21), 0)
        self.assertEqual(lcm(0, 0), 0)

    def test_reproducible_properties(self):
        generator = random.Random(20261016)
        for _ in range(500):
            a = generator.randrange(0, 1000)
            b = generator.randrange(0, 1000)
            result = gcd(a, b)
            with self.subTest(a=a, b=b):
                self.assertEqual(result, gcd(b, a))
                self.assertEqual(result, gcd(b, a % b) if b else a)
                if a and b:
                    self.assertEqual(a % result, 0)
                    self.assertEqual(b % result, 0)
                    largest_common_divisor = max(
                        divisor
                        for divisor in range(1, min(a, b) + 1)
                        if a % divisor == 0 and b % divisor == 0
                    )
                    self.assertEqual(result, largest_common_divisor)
                else:
                    self.assertEqual(result, max(a, b))


if __name__ == "__main__":
    unittest.main()
