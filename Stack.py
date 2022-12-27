class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def __len__(self):
        return len(self.items)


class MyQueue:
    def __init__(self):
        self.new_stack = Stack()
        self.old_stack = Stack()

    def is_empty(self):
        return len(self) == 0

    def shift_stacks(self):
        if self.old_stack.is_empty():
            while not self.new_stack.is_empty():
                self.old_stack.push(self.new_stack.pop())

    def add(self, value):
        return self.new_stack.push(value)

    def peek(self):
        if self.is_empty():
            return False
        self.shift_stacks()
        return self.old_stack.peek()

    def remove(self):
        if self.is_empty():
            return False
        self.shift_stacks()
        return self.old_stack.pop()

    def __len__(self):
        return len(self.new_stack) + len(self.old_stack)


def solution(s1: Stack):
    s2 = Stack()

    while not s1.is_empty():
        temp = s1.pop()
        while not s2.is_empty() and (s2.peek() > temp):
            s1.push(s2.pop())
        s2.push(temp)

    while not s2.is_empty():
        s1.push(s2.pop())


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_text = []
        t_text = []

        for i in s:
            if i != "#":
                s_text.append(i)
            elif s_text:
                s_text.pop()

        for j in t:
            if j != "#":
                t_text.append(j)
            elif t_text:
                t_text.pop()

        return s_text == t_text

    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curStr = ''

        for w in s:
            if w == '[':
                stack.append(curStr)
                stack.append(curNum)
                curNum = 0
                curStr = ''
            elif w == ']':
                num = stack.pop()
                prevStr = stack.pop()
                curStr = prevStr + num * curStr
            elif w.isdigit():
                curNum = curNum * 10 + int(w)
            else:
                curStr += w
        return curStr
