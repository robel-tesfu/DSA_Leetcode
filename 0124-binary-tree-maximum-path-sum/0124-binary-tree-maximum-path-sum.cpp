class Solution {
public:
    int ans = INT_MIN;

    int dfs(TreeNode* node) {
        if (node == nullptr)
            return 0;

        int left = max(0, dfs(node->left));
        int right = max(0, dfs(node->right));

        // Maximum path passing through this node
        ans = max(ans, left + right + node->val);

        // Return one branch to the parent
        return node->val + max(left, right);
    }

    int maxPathSum(TreeNode* root) {
        dfs(root);
        return ans;
    }
};