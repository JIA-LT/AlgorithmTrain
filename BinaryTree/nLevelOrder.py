from collections import deque
from typing import List


class Node:
    def __init__(self,val=None,children:List[Node]=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])

        result = []

        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                for child in node.children:
                    queue.append(child)
            result.append(level)
        return result
if __name__ == "__main__":
    root = Node(1)
    a = Node(2)
    b = Node(3)
    c = Node(4)
    root.children = [a,b]
    a.children = [c]
    solution = Solution()
    print(solution.levelOrder(root))