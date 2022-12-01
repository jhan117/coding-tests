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
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])

        return min(cost[-2], cost[-1])

    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]

        for j in range(1, m):
            for i in range(1, n):
                d[j][i] = d[j - 1][i] + d[j][i - 1]
        return d[-1][-1]


if __name__ == '__main__':
    main()
