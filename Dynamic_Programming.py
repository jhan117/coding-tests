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

        
if __name__ == '__main__':
    main()