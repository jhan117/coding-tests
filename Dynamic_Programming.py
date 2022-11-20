from unittest import TestCase, main, skip


class Tests(TestCase):
    def test_fib1(self):
        result = Solution().fib(2)
        self.assertEqual(result, 1)

    def test_fib2(self):
        result = Solution().fib(3)
        self.assertEqual(result, 2)

    def test_fib3(self):
        result = Solution().fib(4)
        self.assertEqual(result, 3)


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

    def climbStairs(self, n: int) -> int:
        d = [0] * (n + 1)

        d[1], d[2] = 1, 2
        for i in range(2, n + 1):
            d[i] = d[i - 1] + d[i - 2]

        return d[-1]

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * n

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[-1], dp[-2])


if __name__ == '__main__':
    main()
