import re
from unittest import TestCase, main


class Tests(TestCase):
    def test_금액(self):
        result1 = Submit().만들_수_없는_금액([3, 2, 1, 1, 9])
        self.assertEqual(result1, 8)
        result2 = Submit().만들_수_없는_금액([3, 5, 7])
        self.assertEqual(result2, 1)
        result1 = Solution().만들_수_없는_금액([3, 2, 1, 1, 9])
        self.assertEqual(result1, 8)
        result2 = Solution().만들_수_없는_금액([3, 5, 7])
        self.assertEqual(result2, 1)

    def test_볼링공(self):
        result1 = Submit().볼링공_고르기(5, 3, [1, 3, 2, 3, 2])
        self.assertEqual(result1, 8)
        result2 = Submit().볼링공_고르기(8, 5, [1, 5, 4, 3, 2, 4, 5, 2])
        self.assertEqual(result2, 25)
        result1 = Solution().볼링공_고르기(5, 3, [1, 3, 2, 3, 2])
        self.assertEqual(result1, 8)
        result2 = Solution().볼링공_고르기(8, 5, [1, 5, 4, 3, 2, 4, 5, 2])
        self.assertEqual(result2, 25)

    def test_럭키(self):
        result1 = Submit().럭키_스트레이트(123402)
        self.assertEqual(result1, 'LUCKY')
        result2 = Submit().럭키_스트레이트(7755)
        self.assertEqual(result2, 'READY')

    def test_재정렬(self):
        result1 = Submit().문자열_재정렬('K1KA5CB7')
        self.assertEqual(result1, 'ABCKK13')
        result2 = Submit().문자열_재정렬('AJKDLSI412K4JSJ9D')
        self.assertEqual(result2, 'ADDIJJJKKLSS20')
        result1 = Solution().문자열_재정렬('K1KA5CB7')
        self.assertEqual(result1, 'ABCKK13')
        result2 = Solution().문자열_재정렬('AJKDLSI412K4JSJ9D')
        self.assertEqual(result2, 'ADDIJJJKKLSS20')


class Submit:
    """내가 작성한 코드"""

    def __init__(self) -> None:
        self.문자열_test = ['K1KA5CB7', 'AJKDLSI412K4JSJ9D']

    def 만들_수_없는_금액(self, nums: list[int]):
        """
        여러가지로 접근하는 건 좋았으나 해결책을 찾아도 어딘가 엉성함 ㅋㅋ
        """
        ans = 0

        nums.sort()

        for num in nums:
            if ans + 1 < num:
                break
            ans += num

        return ans + 1

    def 볼링공_고르기(self, n: int, m: int, nums: list[int]):
        """
        나는 규칙 찾는다고... 계산을 조지게 했는데... 쉽게 풀 수 있는 법이 있었네 ㅋ
        """
        ans = (n * (n-1) / 2) - (n - len(set(nums)))
        return ans

    def 럭키_스트레이트(self, n: int):
        """
        본인이 좀 더... 간단하게 쓴 거 같음! LeetCode에서 애먹었던 부분이라 빠르게 풀 수 있었음.
        """
        nums = list(map(int, str(n)))
        mid = len(nums) // 2
        r = mid
        for i in range(mid - 1):
            nums[i + 1] += nums[i]
            nums[r + 1] += nums[r]
            r += 1

        if nums[mid - 1] == nums[-1]:
            return 'LUCKY'
        return 'READY'

    def 문자열_재정렬(self, s: str):
        """
        흠...
        """
        nums = re.findall('\d', s)

        s = sorted(list(s))
        s = s[len(nums):]

        nums = map(int, nums)
        return ''.join(s) + str(sum(nums))


class Solution:
    """더 좋은 코드"""

    def 만들_수_없는_금액(self, nums: list[int]):
        """
        접근 방식은 유사했는데 좀 더 깔끔하게 접근한 방식임
        """
        ans = 1

        nums.sort()
        for num in nums:
            if ans < num:
                break
            ans += num

        return ans

    def 볼링공_고르기(self, n: int, m: int, nums: list[int]):
        """
        한 놈을 고정 시키고 경우의 수 따지는 게... 천천히 순차적으로 따져야 겠다.
        """
        arr = [0] * 11
        ans = 0

        for num in nums:
            arr[num] += 1

        for i in range(1, m + 1):
            n -= arr[i]
            ans += arr[i] * n

        return ans

    def 문자열_재정렬(self, s: str):
        """
        흠... 이게 더 나은 듯...
        """
        ans = []
        value = 0

        for string in s:
            if string.isalpha():
                ans.append(string)
            else:
                value += int(string)

        ans.sort()

        if value != 0:
            ans.append(str(value))

        return ''.join(ans)


if __name__ == '__main__':
    main()
