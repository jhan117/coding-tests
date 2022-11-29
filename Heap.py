import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        h = []
        [heapq.heappush(h, -s) for s in stones]

        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]
