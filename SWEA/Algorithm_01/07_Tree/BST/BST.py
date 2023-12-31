# 완전 이진 트리 구현

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 삽입
def insert(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


# 중위순회
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)


# 정렬되지 않은 배열
arr = [13, 2, 8, 7, 9, 17, 6, 1]
root = TreeNode(arr[0])

for value in range(1, len(arr)):
    insert(root, value)

inorder(root)
