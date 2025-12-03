from collections import deque
from typing import List, Optional

from BinaryTree.TreeNode import TreeNode, build_tree_by_array


def bfs(root:Optional[TreeNode])->List[List[int]]:
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            cur = queue.popleft()
            level.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        result.append(level)
    return result

# 199
def right_side_view(root: Optional[TreeNode])->List[List[int]]:
    if not root:
        return []
    queue = deque([root])
    right_side_view = []
    while queue:
        queue_len = len(queue)
        for i in range(queue_len):
            node = queue.popleft()
            if i == queue_len - 1:
                right_side_view.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return right_side_view

# 104
def max_level(root: Optional[TreeNode])->int:
    if not root:
        return 0
    depth = 0
    queue = deque([root])

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth

def min_level(root: Optional[TreeNode])->int:
    if not root:
        return 0
    queue = deque([root])
    min_level = 0
    while queue:
        min_level += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if not node.left and not node.right:
                return min_level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return min_level

if __name__ == '__main__':
    array = [5,3,9,None,None,15,7]
    root = build_tree_by_array(array)
    print(bfs(root))
    print(right_side_view(root))
    print(max_level(root))
    print(min_level(root))

