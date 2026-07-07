class Solution {
public:
    vector<vector<int>> dp;

    int solve(int i, int j, string &a, string &b) {

        if (i == a.size())
            return b.size() - j;

        if (j == b.size())
            return a.size() - i;

        if (dp[i][j] != -1)
            return dp[i][j];

        if (a[i] == b[j])
            return dp[i][j] = solve(i + 1, j + 1, a, b);

        int insertOp = solve(i, j + 1, a, b);
        int deleteOp = solve(i + 1, j, a, b);
        int replaceOp = solve(i + 1, j + 1, a, b);

        return dp[i][j] = 1 + min({insertOp, deleteOp, replaceOp});
    }

    int minDistance(string word1, string word2) {

        dp.assign(word1.size(), vector<int>(word2.size(), -1));

        return solve(0, 0, word1, word2);
    }
};