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
        curString = ''

        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
            print(stack, curNum, curString)
        return curString
