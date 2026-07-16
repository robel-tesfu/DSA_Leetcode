import java.util.*;

class Solution {

    private int preIndex = 0;
    private Map<Integer, Integer> inorderMap = new HashMap<>();

    public TreeNode buildTree(int[] preorder, int[] inorder) {

        for (int i = 0; i < inorder.length; i++)
            inorderMap.put(inorder[i], i);

        return build(preorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] preorder, int left, int right) {

        if (left > right)
            return null;

        int rootValue = preorder[preIndex++];
        TreeNode root = new TreeNode(rootValue);

        int index = inorderMap.get(rootValue);

        root.left = build(preorder, left, index - 1);
        root.right = build(preorder, index + 1, right);

        return root;
    }
}