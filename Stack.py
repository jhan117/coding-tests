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
