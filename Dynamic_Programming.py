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


if __name__ == '__main__':
    main()
