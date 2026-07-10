class Solution {
public:
    vector<string> ans;
    vector<string> path;

    void backtrack(string &s, int index) {

        // If we already have 4 parts
        if (path.size() == 4) {
            if (index == s.size()) {

                string ip = path[0];
                for (int i = 1; i < 4; i++)
                    ip += "." + path[i];

                ans.push_back(ip);
            }
            return;
        }

        // Try segment lengths 1, 2, 3
        for (int len = 1; len <= 3; len++) {

            if (index + len > s.size())
                break;

            string segment = s.substr(index, len);

            // Leading zero
            if (segment.size() > 1 && segment[0] == '0')
                break;

            int num = stoi(segment);

            if (num > 255)
                continue;

            path.push_back(segment);

            backtrack(s, index + len);

            path.pop_back();
        }
    }

    vector<string> restoreIpAddresses(string s) {

        backtrack(s, 0);

        return ans;
    }
};