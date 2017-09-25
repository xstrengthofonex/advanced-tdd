import unittest
from typing import List


class PrimeFactorTest(unittest.TestCase):
    def assertPrimeFactors(self, n: int, prime_factors: List[int]):
        self.assertEqual(prime_factors, self.of(n))

    def test_can_refactor_into_primes(self):
        self.assertPrimeFactors(1, [])
        self.assertPrimeFactors(2, [2])
        self.assertPrimeFactors(3, [3])
        self.assertPrimeFactors(4, [2, 2])
        self.assertPrimeFactors(5, [5])
        self.assertPrimeFactors(6, [2, 3])
        self.assertPrimeFactors(7, [7])
        self.assertPrimeFactors(8, [2, 2, 2])
        self.assertPrimeFactors(9, [3, 3])
        self.assertPrimeFactors(2 * 2 * 3 * 3 * 5 * 7 * 11 * 11 * 13,
                                [2, 2, 3, 3, 5, 7, 11, 11, 13])

    @staticmethod
    def of(n: int) -> List[int]:
        factors = []
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.append(divisor)
                n /= divisor
            divisor += 1
        return factors
