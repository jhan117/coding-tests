from unittest import TestCase, main, skip
from typing import Optional


class Tests(TestCase):

    @skip
    def test_maxProfit1(self):
        result = Submit().maxProfit([7, 1, 5, 3, 6, 4])
        self.assertEqual(result, 5)

    @skip
    def test_maxProfit2(self):
        result = Submit().maxProfit([7, 6, 4, 3, 1])
        self.assertEqual(result, 0)

    @skip
    def test_maxProfit3(self):
        result = Submit().maxProfit([2, 1, 4])
        self.assertEqual(result, 3)

    def test_maxProfit4(self):
        result = Submit().maxProfit([2, 1, 2, 1, 0, 1, 2])
        self.assertEqual(result, 2)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Submit:
    """내가 작성한 코드"""

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        풀이

        1일 때, 1
        2일 때, 1 | 2
        3일 때, 1 | 2, 3
        4일 때, 1, 2 | 3, 4

        길이가 짝수일 때마다 head 값이 변함을 이용했다.
        """
        # Definition for singly-linked list.
        length = 0

        node = head
        while node:
            node = node.next
            length += 1

            if length % 2 == 0:
                head = head.next
        return head

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        노드의 숫자가 전부 다른 경우에는 작동하지만 같은 경우에는 작동하지 않는다.
        two pointers가 관련 topic으로 되어 있어서 어떻게 이용해볼까? 했는데 떠오르지 않았다.
        """
        arr = []
        fast = slow = head
        arr_idx = -1
        while fast:
            if fast.val in arr:
                arr_idx = arr.index(fast.val)
                print(arr_idx)
                break

            arr.append(fast.val)
            fast = fast.next

        for _ in range(arr_idx):
            slow = slow.next

        if arr_idx != -1:
            return slow

        return None

    def maxProfit(self, prices: list[int]) -> int:
        """
        첫번째, 두번째를 넣고 값을 갱신하는 방법을 이용함.
        문제점 : buy 값보다 적을 때를 고려 못함
        """
        profit = sell = 0
        buy = prices[0]

        if len(prices) == 1:
            return profit

        sell = prices[1]
        if len(prices) == 2:
            if buy < sell:
                profit = sell - buy
            return profit

        for p in prices[2:]:
            if buy < sell:
                if sell < p:
                    sell = p

                profit = sell - buy
            else:
                buy = sell
                sell = p

        if buy < sell:
            profit = sell - buy

        return profit


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        two pointers 배워갑니다.

        Think of two pointers technique with slow runner and fast runner.
        Both slow runner and fast runner are initialized to head node.
        Each iteration, fast runner moves two steps forward while the slow one moves one steps only.
        When fast runner meets the empty node (i.e., NULL) on the tail, the slow one will be right on the node of midpoint.

        풀이

        1. slow는 하나씩 이동
        2. fast는 두 칸씩 이동
        3. fast가 끝까지 도달할 때까지 반복
        4. slow를 반환하면 중간 위치가 될 것!
        """
        slow = fast = head

        # when fast runner meets the empty node
        while fast and fast.next:
            slow = slow.next  # one step
            fast = fast.next.next  # two steps
        return slow

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        이거 떠올릴 수 있는 문젠가..? 그냥 외우지 뭐 while...else문이 있음

        slow moves 1 step at a time, fast moves 2 steps at a time.
        when slow and fast meet each other, they must be on the cycle
        x denotes the length of the linked list before starting the circle
        y denotes the distance from the start of the cycle to where slow and fast met
        C denotes the length of the cycle
        when they meet, slow traveled (x + y) steps while fast traveled 2 * (x + y) steps, and the extra distance (x + y) must be a multiple of the circle length C
        note that x, y, C are all lengths or the number of steps need to move.
        head, slow, fast are pointers.
        head moves x steps and arrives at the start of the cycle.
        so we have x + y = N * C, let slow continue to travel from y and after x more steps, slow will return to the start of the cycle.
        At the same time, according to the definition of x, head will also reach the start of the cycle after moving x steps.
        so if head and slow start to move at the same time, they will meet at the start of the cycle, that is the answer.

        풀이

        1. slow 한 칸, fast 두 칸씩 이동
        2. slow와 fast가 만나는 지점이 사이클임
        3. head랑 위에서 만난 slow지점이 사이클 시작 지점임
        """
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        else:
            return None  # if not (fast and fast.next): return None
        while head != slow:
            head, slow = head.next, slow.next
        return head

    def maxProfit(self, prices: list[int]) -> int:
        """
        접근법은 좋았으나 세부적으로 이해는 못해서 예외처리를 너무 많이 해야 했음.

        [7,1,5,3,6,4]

        sell buy profit
        7 inf -inf
        1 7 -6
        5 1 4
        3 1 2
        6 1 5
        4 1 3

        풀이

        1. 먼저 기존 vs 갱신 중 어떤 수익이 더 큰지를 계산함. 즉, 수익이 커질 때까지 sell 인덱스 움직임
        2. 기존 buy vs 현재 값 중 어떤 값이 더 작은지 갱신. 즉, buy 값이 더 작은 게 있으면 바로 그 값으로 갱신! -> 순서 고려 안해도 됨.
        """
        low = float('inf')
        profit = 0
        for i in prices:
            profit = max(profit, i-low)
            low = min(low, i)
        return profit


if __name__ == '__main__':
    main()
