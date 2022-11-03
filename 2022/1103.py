from collections import Counter


def isBadVersion(version: int) -> bool:
    """
    테스트로 4로 고정해둠
    """
    return version == 4


class Submit:
    def longestPalindrome(self, s: str) -> int:
        """
        뭔가 주구난방한 코드...
        """
        count = 0
        have_odd = False

        s_list = list(s)
        s_counter = dict(sorted(Counter(s_list).items(),
                         key=lambda x: x[1], reverse=True))

        for k, v in s_counter.items():
            if v % 2 != 0:
                if not have_odd:
                    have_odd = True
                    count += v
                else:
                    count += v - 1
            else:
                count += v
        return count

    def runningSum(self, nums: list[int]) -> list[int]:
        """
        간단하고 좋았지만... [0:0]은 아무것도 가져오지 못한다는 걸 기억하자.
        어차피 i + 1할꺼면 range를 1부터 시작하는 것도 깔끔할 것 같다.
        sum이 O(N)... 너무 남발하진 말자...

        Time: O(N^2), Space: O(N)
        """
        ans = [sum(nums[:i+1]) for i in range(len(nums))]
        # ans = [sum(nums[:i]) for i in range(1, len(nums))]
        return ans

    def pivotIndex(self, nums: list[int]) -> int:
        """
        기존의 코드는 너무 예외 처리를 너무 많이 해야 해서 힌트 봤는데 시간 복잡도 때문에 커트 됨. 그래서 엄청난 고민 끝에 해낸 결과인데...
        코드가 이쁘지 않음.
        """
        nums = [0] + nums + [0]
        sumLeft = 0
        sumRight = sum(nums[2:])
        idx = 0

        for i in range(2, len(nums)):
            if sumLeft == sumRight:
                return idx

            sumLeft += nums[i - 1]
            sumRight -= nums[i]
            idx += 1
        return -1

    def containsDuplicate(self, nums: list[int]) -> bool:
        if list(sorted(Counter(nums).values(), reverse=True))[0] > 1:
            return True
        else:
            return False

    def maxSubArray(self, nums: list[int]) -> int:
        """
        시간 초과
        고민을 해도 떠오르지 않았음...
        """
        ans = float('-inf')
        for i in range(len(nums)):
            sum_sub = 0
            for sub_n in nums[i:]:
                sum_sub += sub_n
                if ans < sum_sub:
                    ans = sum_sub
        return ans

    def search(self, nums: list[int], target: int) -> int:
        """
        재귀 함수를 쓸지... while 문을 쓸지 고민쓰
        다른 함수 만들었다가 클래스 지저분해지는 거 싫어서 그냥 while 씀.
        """
        start, end = 0, len(nums) - 1
        while True:
            if start > end:
                return -1

            mid = (start + end) // 2

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid

    def firstBadVersion(self, n: int) -> int:
        """
        # The isBadVersion API is already defined for you.
        # def isBadVersion(version: int) -> bool:
        """
        start, end = 1, n
        mid = -1
        while start <= end:
            mid = (start + end) // 2
            if not isBadVersion(mid):
                start = mid + 1
            else:
                end = mid - 1

        if isBadVersion(mid):
            return mid
        else:
            return mid + 1

    def searchInsert(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return start


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Counter에 리스트 변환 하지 않아도 됨. 정렬 안해도 되는 카운트 방법임.
        """
        ans = 0

        for v in Counter(s).values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans

    def runningSum(self, nums: list[int]) -> list[int]:
        """
        기존 배열을 변경하는 코드임.
        시간 복잡도랑 공간 복잡도가 내가 작성한 코드보다 효율적이어서 넣어봤음.

        Time: O(N), Space: O(1)
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

    def pivotIndex(self, nums):
        """
        허허.. 나 왜이렇게 복잡하게 생각했을까... 나는 처음부터 피벗 인덱스 값은 제외했는데 여기는 포함하고 나중에 처리함. 그래서 좀 깔끔한듯.

        Time: O(N), Space: O(1)
        """
        sumLeft, sumRight = 0, sum(nums)

        for idx, num in enumerate(nums):
            sumRight -= num
            if sumLeft == sumRight:
                return idx
            sumLeft += num
        return -1

    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        굉장한 코드를 발견했다... 꼭 기억해놨다가 써먹자!
        """
        return len(nums) != len(set(nums))

    def maxSubArray(self, nums: list[int]) -> int:
        """
        for문으로 계산할 생각 밖에 안 떠올랐는데... 이런 간단한 방법이! 꼭 기억하자.
        약간 DP랑 관련 깊은 것 같은데... 역시 DP는 좀 취약한 것 같다. 좀 더 자주 풀어보자!
        하위 항목과 비교 부분... 흠.. 쉽게 잘 안 떠오르기도 하다.. 계속 자주 보면서 익히자.
        """
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum

    def search(self, nums: list[int], target: int) -> int:
        """
        어차피 똑같지만... 괜히 코드 깔끔하게 쓰고 싶어서 수정해봄.
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return -1

    def firstBadVersion(self, n: int) -> int:
        """
        너무 mid를 반환하려고 애씀... 다른 변수도 있는데!!
        변수를 만들어서 true 일때마다 저장하는 방법도 있고 False이면 알아서 1 더해주고, True면 그 위치가 맞으니 start값이 시작 위치라고 할 수도 있음.
        """
        start, end = 1, n
        while start <= end:
            mid = (start + end) // 2
            if not isBadVersion(mid):
                start = mid + 1
            else:
                end = mid - 1
        return start


if __name__ == '__main__':
    # test_case = [1, 2, 3, 4]
    # test_case = [1, 7, 3, 6, 5, 6]
    # test_case = [2, 1, -1]
    # test_case = [-1, -1, -1, -1, -1, 0]
    # test_case = [-1, -1, 0, 1, 1, 0]
    # test_case = [-1, -1, -1, 1, 1, 1]
    # test_case = [1, 2, 3, 1]
    # test_case = [2, 14, 18, 22, 22]
    # test_case = [1, 2, -3, 4]
    # test_case = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # test_case = [-1]

    # print(Submit().runningSum(test_case))
    # print(Solution().runningSum(test_case))
    # print(Submit().pivotIndex(test_case))
    # print(Submit().containsDuplicate(test_case))
    # print(Submit().maxSubArray(test_case))
    # print(Solution().maxSubArray(test_case))
    # print(Submit().search([-1, 0, 3, 5, 9, 12], 9))
    # print(Submit().searchInsert([1, 3, 5, 6], 5))
    print(Submit().searchInsert([1, 3, 5, 6], 2))
