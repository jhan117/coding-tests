class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_BST(root, min_val=None, max_val=None):
    if not root:
        return True
    if (min_val and root.data < min_val) or (max_val and root.data >= max_val):
        return False
    return is_BST(root.left, min_val, root.data) and is_BST(root.right, root.data, max_val)


if __name__ == '__main__':
    notBST = Tree(3)
    notBST.left = Tree(2)
    notBST.right = Tree(5)
    notBST.right.left = Tree(1)
    notBST.right.right = Tree(4)

    BST = Tree(6)
    BST.left = Tree(3)
    BST.right = Tree(9)
    BST.left.left = Tree(1)
    BST.left.right = Tree(5)
    BST.right.left = Tree(7)
    BST.right.right = Tree(11)

    print(is_BST(notBST))
    print(is_BST(BST))
