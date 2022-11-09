from unittest import TestCase, main, skip
from typing import Optional


class Tests(TestCase):

    def test_mergeTwoLists1(self):
        result = Submit().mergeTwoLists(
            ListNode([1, 2, 4]), ListNode([1, 3, 4]))
        self.assertEqual(result, [1, 1, 2, 3, 4, 4])


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def isempty(self):
        return not self.head

    def output(self) -> list:
        arr = []
        temp = self.head
        while temp:
            arr.append(temp.val)
            temp = temp.next

        return arr

    def add_last(self, new_data):
        if not self.isempty():
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = ListNode(new_data)
        else:
            self.head = ListNode(new_data)

    def pop_first(self):
        temp = self.head
        if temp.next:
            self.head = temp.next
        else:
            self.head = None

    def toLinkedList(self, list):
        for l in list:
            self.add_last(l)


class Submit:
    """내가 작성한 코드"""

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Definition for singly-linked list.
        못품
        """
        # ans = LinkedList()
        print(list1.val < list2.val)

        # llist1 = LinkedList()
        # llist1.toLinkedList(list1)
        # print(llist1.isempty())

        # llist2 = LinkedList()
        # llist2.toLinkedList(list2)
        # print(llist2.output())

        # while llist1.isempty() == False and llist2.isempty() == False:
        #     if llist1.head.val <= llist2.head.val:
        #         ans.add_last = ListNode(llist1.head)
        #         llist1.pop_first()
        #     else:
        #         ans.add_last = ListNode(llist2.head)
        #         llist2.pop_first()

        # print(llist1.isempty())
        # while llist1.isempty():
        #     print('ans', ans.output())
        #     print('llist', llist1.output())
        #     ans.add_last = ListNode(llist1.head)
        #     llist1.pop_first()
        # while llist2.isempty() == True:
        #     ans.add_last = ListNode(llist2.head)
        #     llist2.pop_first()

        # print(ans.output())


class Solution:
    """더 좋은 코드"""

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Definition for singly-linked list.
        반복문 쓰는 경우도 있었음.
        어째서.. 클래스 구조를 먼저 파악하지 않은거야..! 이 바보 멍청이!
        """
        # 재귀 함수
        if not list1 or not list2:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def reverseList(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        """
        간단한 건데 재귀보다 그냥 반복문을 쓸걸 그랬음.
        """
        # recursive
        # if not head:
        #     return prev
        # temp = head.next
        # head.next = prev
        # return self.reverseList(temp, head)

        # iterative
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


if __name__ == '__main__':
    main()
