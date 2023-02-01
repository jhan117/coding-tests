class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, b in enumerate(nums):
            # a + b = target -> a = target - b
            a = target - b
            if a in seen:
                return [seen[a], i]
            seen[b] = i

    def getHint(self, secret: str, guess: str) -> str:

        # The main idea is to understand that cow cases contain the bull cases

        # This loop will take care of "bull" cases
        bull = 0
        for i in range(len(secret)):
            bull += int(secret[i] == guess[i])

            # This loop will take care of "cow" cases
        cows = 0
        for c in set(secret):
            cows += min(secret.count(c), guess.count(c))

        return f"{bull}A{cows-bull}B"
