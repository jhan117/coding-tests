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
