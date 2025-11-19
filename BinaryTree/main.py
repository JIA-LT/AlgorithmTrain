class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def preorderTraversal(self, root):
        res = []

        def dfs(node):
            if node is None:
                return

            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res

    def inorderTraversal(self, root):
        res = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

    def postorderTraversal(self, root):
        res = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res
