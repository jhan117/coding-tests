class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        binary search tree (BST)는 왼쪽이 현재 노드보다 적은 수, 오른쪽이 현재 노드보다 많다는 것을 이용했어야 했다...

        1. root.val이 p, q보다 크다면 왼쪽 root 탐색 이동
        2. root.val이 p, q보다 작으면 오른쪽 root 탐색하고 이동한다.
        3. root를 반환한다.
        """
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
