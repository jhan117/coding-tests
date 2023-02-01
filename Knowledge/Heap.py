import heapq
from collections import Counter


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        h = []
        [heapq.heappush(h, -s) for s in stones]

        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]

    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counts = Counter(words)
        result = sorted(counts, key=lambda word: (-counts[word], word))
        return result[:k]
