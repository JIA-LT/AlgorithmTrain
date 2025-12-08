from collections import deque
from typing import List

from BinaryTree.TreeNode import TreeNode, build_tree_by_array


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []
        queue = deque([root])

        average = []
        while queue:
            size = len(queue)
            level_sum = 0
            for i in range(size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            average.append(level_sum / size)
        return average
if __name__ == "__main__":
    array = [5, 3, 9, 4, 6, 15, 7]
    root = build_tree_by_array(array)
    solution = Solution()
    print(solution.averageOfLevels(root))