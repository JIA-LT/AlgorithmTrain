from BinaryTree.TreeNode import TreeNode, build_tree_by_array


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if left is None and right is not None:
            return False
        elif left is not None and right is None:
            return False
        elif left is None and right is None:
            return True
        elif left.val != right.val:
            return False

        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        return outside and inside

if __name__ == "__main__":
    array = [5, 3, 3, 7, None, None, 7]
    root = build_tree_by_array(array)
    sol = Solution()
    print(sol.isSymmetric(root))