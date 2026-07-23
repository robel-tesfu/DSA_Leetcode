from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Returns the minimum depth of the binary tree.
        Minimum depth is the number of nodes on the shortest path
        from the root to the nearest leaf.
        """
        if not root:
            return 0

        # BFS level-order traversal
        queue = deque([(root, 1)])   # (node, current_depth)

        while queue:
            node, depth = queue.popleft()

            # If this node is a leaf, we found the minimum depth
            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return 0