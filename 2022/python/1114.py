from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        DFS => 재귀함수
        첫 번째를 떠올리는 게 포인트 였을듯...

        1. 첫 번째는 root, min_val=-inf, max_val=inf를 넣는다.
        2. 범위를 넘으면 return False, 그렇지 않으면 왼쪽 오른쪽 root 수행
        3. root가 없으면 return True
        """
        def valid_bst(root, min_val, max_val):
            if not root:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
            return valid_bst(root.left, min_val, root.val) and valid_bst(root.right, root.val, max_val)
        return valid_bst(root, float('-inf'), float('inf'))
