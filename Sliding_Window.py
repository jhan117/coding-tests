from collections import Counter
from unittest import TestCase, main, skip


class Tests(TestCase):
    @skip
    def test_characterReplacement1(self):
        result = Solution().characterReplacement('AABABBA', 1)
        self.assertEqual(result, 4)

    def test_characterReplacement2(self):
        result = Solution().characterReplacement('ABAB', 2)
        self.assertEqual(result, 4)


class Solution:
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

    def characterReplacement(self, s: str, k: int) -> int:
        maxlen, largestCount = 0, 0
        arr = Counter()
        for idx in range(len(s)):
            arr[s[idx]] += 1
            largestCount = max(largestCount, arr[s[idx]])
            if maxlen - largestCount >= k:
                arr[s[idx - maxlen]] -= 1
            else:
                maxlen += 1
        return maxlen


if __name__ == '__main__':
    main()
