from unittest import TestCase, main, skip


class Tests(TestCase):

    @skip
    def test_isIsomorphic1(self):
        result = Submit().isIsomorphic("egg", "add")
        self.assertEqual(result, True)

    @skip
    def test_isIsomorphic2(self):
        result = Submit().isIsomorphic("badc", "baba")
        self.assertEqual(result, False)

    @skip
    def test_isIsomorphic3(self):
        result = Submit().isIsomorphic("foo", "bar")
        self.assertEqual(result, False)

    @skip
    def test_isIsomorphic4(self):
        result = Submit().isIsomorphic("paper", "title")
        self.assertEqual(result, True)

    @skip
    def test_isIsomorphic5(self):
        result = Submit().isIsomorphic("abcdefghijklmnopqrstuvwxyzva",
                                       "abcdefghijklmnopqrstuvwxyzck")
        self.assertEqual(result, False)

    def test_isSubsequence1(self):
        result = Submit().isSubsequence("abc", "ahbgdc")
        self.assertEqual(result, True)

    def test_isSubsequence2(self):
        result = Submit().isSubsequence("axc", "ahbgdc")
        self.assertEqual(result, False)

    def test_isSubsequence3(self):
        result = Submit().isSubsequence("b", "c")
        self.assertEqual(result, False)

    def test_isSubsequence4(self):
        result = Submit().isSubsequence("", "ahbgdc")
        self.assertEqual(result, False)

    def test_isSubsequence4(self):
        result = Submit().isSubsequence("aaaaaa", "bbaaaa")
        self.assertEqual(result, False)


class Submit:
    """내가 작성한 코드"""

    def isIsomorphic(self, s: str, t: str) -> bool:
        s_arr, t_arr = [], []
        s_ans, t_ans = [], []

        for s_s, t_s in zip(s, t):
            if s_s not in s_arr:
                s_arr.append(s_s)
            if t_s not in t_arr:
                t_arr.append(t_s)

            s_ans.append(str(s_arr.index(s_s)))
            t_ans.append(str(t_arr.index(t_s)))

        return s_ans == t_ans

    def isSubsequence(self, s: str, t: str) -> bool:
        arr = [None] * len(s)
        for i, s_str in enumerate(s):
            for t_str in t:
                if s_str == t_str:
                    if not arr[i]:
                        arr[i] = t.index(t_str)
                        break
                    else:

        return False


class Solution:
    """더 좋은 코드"""

    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        도대체 이런 생각은 어떻게 해야 나오는거지???? 개똑똑한놈들...
        """
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


if __name__ == '__main__':
    main()
