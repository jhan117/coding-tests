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
        ans = []
        p_len = len(p)

        p_cnt = Counter(p)
        s_cnt = Counter(s[:p_len])

        if s_cnt == p_cnt:
            ans.append(0)

        for i in range(len(s) - p_len):
            s_cnt[s[i]] -= 1
            if s_cnt[s[i]] == 0:
                del s_cnt[s[i]]

            s_cnt[s[i + p_len]] += 1

            if s_cnt == p_cnt:
                ans.append(i + 1)

        return ans

    def characterReplacement(self, s: str, k: int) -> int:
        cnt = Counter()
        maxLen, left = 0, 0

        for i in s:
            cnt[i] += 1
            cur = maxLen - cnt.most_common(1)[0][1]
            if k <= cur:
                cnt[s[left]] -= 1
                left += 1
            else:
                maxLen += 1

        return maxLen


if __name__ == '__main__':
    main()
