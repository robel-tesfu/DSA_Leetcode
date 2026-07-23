# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Returns all root-to-leaf paths where the sum of node values equals targetSum.
        Each path is a list of integers (node values).
        """
        result = []          # Stores all valid paths
        current_path = []    # Stores nodes along current DFS branch

        def dfs(node, remaining_sum):
            if not node:
                return

            # Add current node to the path
            current_path.append(node.val)
            remaining_sum -= node.val

            # If it's a leaf and sum matches, add a copy of the path
            if not node.left and not node.right and remaining_sum == 0:
                result.append(current_path[:])   # copy needed for backtracking

            # Recurse into children
            dfs(node.left, remaining_sum)
            dfs(node.right, remaining_sum)

            # Backtrack: remove current node from path before returning to parent
            current_path.pop()

        dfs(root, targetSum)
        return result