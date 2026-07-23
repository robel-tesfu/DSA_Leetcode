class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, targetSum - root.val)]
        
        while stack:
            node, curr_sum = stack.pop()
            
            # Check if leaf and sum matches
            if not node.left and not node.right and curr_sum == 0:
                return True
            
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
        
        return False