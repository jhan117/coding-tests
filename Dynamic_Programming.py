from unittest import TestCase, main, skip
from collections import Counter


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

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

    def findAnagrams(self, s: str, p: str) -> list[int]:
        # take counter of first n elements in s_dict with n = len(p) - 1
        s_dict = Counter(s[:len(p)-1])
        # counter of p, this should not be changed
        p_dict = Counter(p)
        start = 0
        # final result list
        res = []
        # We iterate over the string s, and in each step we check if s_dict and p_dict match
        for i in range(len(p)-1, len(s)):
            # updating the counter & adding the character
            s_dict[s[i]] += 1
            # checking if counters match
            if s_dict == p_dict:
                res.append(start)
            # remove the first element from counter
            s_dict[s[start]] -= 1
            # if element count = 0, pop it from the counter
            if s_dict[s[start]] == 0:
                del s_dict[s[start]]
            start += 1

        return res


if __name__ == '__main__':
    main()
