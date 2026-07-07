class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {

        int m = matrix.size();
        int n = matrix[0].size();

        bool firstColZero = false;

        // Step 1: Use first row and first column as markers
        for (int i = 0; i < m; i++) {

            if (matrix[i][0] == 0)
                firstColZero = true;

            for (int j = 1; j < n; j++) {

                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        // Step 2: Fill inner matrix
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {

                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            }
        }

        // Step 3: First row
        if (matrix[0][0] == 0) {
            for (int j = 0; j < n; j++)
                matrix[0][j] = 0;
        }

        // Step 4: First column
        if (firstColZero) {
            for (int i = 0; i < m; i++)
                matrix[i][0] = 0;
        }
    }
};