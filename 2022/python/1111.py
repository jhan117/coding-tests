from typing import Optional
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Submit:
    def dfs(self, root, v, visited):
        visited.append(v)
        for c in root.children:
            if c.val not in visited:
                self.dfs(c, c.val, visited)

    def preorder(self, root: 'Node') -> list[int]:
        """
        같은 숫자가 중복 되어 있으면 작동 안하는 문제 발생
        """
        if not root:
            return None

        visited = []
        self.dfs(root, root.val, visited)

        return visited

    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """
        BFS는 구현했으나 같은 층끼리만 따로 넣는 법을 모르겠음.
        """
        queue = deque([root])
        ans = []
        while queue:
            root = queue.popleft()
            ans.append(root.val)

            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        print(ans)


class Solution:
    def dfs(self, root, output):
        """
        1. root가 비어 있으면 None 반환
        2. 현재 노드의 값 넣기
        3. 자식 노드가 있으면 자식 root를 넣고 순회하면서 1-2 반복
        """
        if root is None:
            return None

        output.append(root.val)

        for child in root.children:
            self.dfs(child, output)

    def preorder(self, root: 'Node') -> list[int]:
        """
        앗.. 바본가? 리스트 중복 허용 되는 거 까먹었네... 근데.. 방문 처리 안하는 구나

        - DFS는 재귀함수 이용
        - root랑 root.val 따로 넣어 줄 필요 없이 root를 인자로 넣기
        """
        output = []
        self.dfs(root, output)
        return output

    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """
        root를 전부 넣는다는 점이 신기했다. 난 val값만 넣어서 연결이 안된듯.

        1. deque에 root를 넣는다.
        2. queue 길이와 row 값을 초기화 한다.
        3. queue에서 왼쪽 노드를 뺸다.
        4. 그 노드의 값을 row에 넣는다.
        5. left 또는 right값이 있다면 queue에 넣는다.
        6. 3-5 과정을 queue 길이 만큼 반복 한다. => 한 층만큼 반복
        7. 정답에 한 층의 배열을 넣는다.
        8. 2-7 과정을 queue가 없을 때까지 반복한다.
        """
        queue, ans = deque([root] if root else []), []
        while queue:
            qlen, row = len(queue), []
            for _ in range(qlen):
                curr = queue.popleft()
                row.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(row)
        return ans
