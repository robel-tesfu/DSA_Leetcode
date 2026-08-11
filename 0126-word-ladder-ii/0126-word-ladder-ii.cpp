class Solution {
public:
    vector<vector<string>> ans;
    unordered_map<string, vector<string>> parents;
    unordered_map<string, int> dist;

    vector<vector<string>> findLadders(
        string beginWord,
        string endWord,
        vector<string>& wordList
    ) {
        unordered_set<string> words(wordList.begin(), wordList.end());

        // endWord must exist in the dictionary
        if (!words.count(endWord))
            return {};

        queue<string> q;
        q.push(beginWord);
        dist[beginWord] = 0;

        while (!q.empty()) {
            string word = q.front();
            q.pop();

            int currentDist = dist[word];

            // Change one character at a time
            for (int i = 0; i < word.size(); i++) {
                string next = word;

                for (char c = 'a'; c <= 'z'; c++) {
                    if (c == word[i])
                        continue;

                    next[i] = c;

                    // Word must be in dictionary
                    if (!words.count(next))
                        continue;

                    // First time seeing this word
                    if (!dist.count(next)) {
                        dist[next] = currentDist + 1;
                        parents[next].push_back(word);
                        q.push(next);
                    }

                    // Another shortest way to reach next
                    else if (dist[next] == currentDist + 1) {
                        parents[next].push_back(word);
                    }
                }
            }
        }

        // No path exists
        if (!dist.count(endWord))
            return {};

        vector<string> path;
        path.push_back(endWord);

        backtrack(endWord, beginWord, path);

        return ans;
    }

private:
    void backtrack(
        string word,
        string beginWord,
        vector<string>& path
    ) {
        // We reached the beginning
        if (word == beginWord) {
            vector<string> sequence = path;

            reverse(sequence.begin(), sequence.end());

            ans.push_back(sequence);
            return;
        }

        // Follow every possible shortest parent
        for (string parent : parents[word]) {
            path.push_back(parent);

            backtrack(parent, beginWord, path);

            path.pop_back();
        }
    }
};