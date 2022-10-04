# Solution 1: Top-down with Memoization
def calculateFibonacci(n):
    memoize = [-1 for x in range(n + 1)]
    return calculateFibonacciRecur(memoize, n)


def calculateFibonacciRecur(memoize, n):
    if n < 2:
        return n

    # if we have already solved this subproblem, simply return the result from the cache
    if memoize[n] >= 0:
        return memoize[n]

    memoize[n] = calculateFibonacciRecur(memoize, n - 1) + calculateFibonacciRecur(
        memoize, n - 2
    )
    return memoize[n]


# Solution 2: Bottom-up with Tabulation
def calculateFibonacci(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[n]


import unittest


class TestNthFibonacciNumber(unittest.TestCase):
    def test_Fibonacci(self):
        self.assertEqual(calculateFibonacci(5), 5)
        self.assertEqual(calculateFibonacci(6), 8)
        self.assertEqual(calculateFibonacci(7), 13)


if __name__ == "__main__":
    unittest.main()
