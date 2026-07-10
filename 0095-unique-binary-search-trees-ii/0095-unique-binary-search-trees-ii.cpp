class Solution {
public:
    vector<TreeNode*> generate(int start, int end) {

        if (start > end)
            return {nullptr};

        vector<TreeNode*> trees;

        for (int root = start; root <= end; root++) {

            vector<TreeNode*> leftTrees = generate(start, root - 1);
            vector<TreeNode*> rightTrees = generate(root + 1, end);

            for (TreeNode* left : leftTrees) {
                for (TreeNode* right : rightTrees) {

                    TreeNode* node = new TreeNode(root);

                    node->left = left;
                    node->right = right;

                    trees.push_back(node);
                }
            }
        }

        return trees;
    }

    vector<TreeNode*> generateTrees(int n) {
        return generate(1, n);
    }
};