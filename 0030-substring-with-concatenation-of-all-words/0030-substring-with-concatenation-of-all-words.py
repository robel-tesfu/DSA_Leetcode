from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        target = Counter(words)
        result = []

        for offset in range(word_len):
            left = offset
            right = offset
            window = defaultdict(int)
            matched = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word not in target:
                    window.clear()
                    matched = 0
                    left = right
                    continue

                window[word] += 1
                matched += 1

                while window[word] > target[word]:
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    matched -= 1
                    left += word_len

                if matched == word_count:
                    result.append(left)

                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    matched -= 1
                    left += word_len

        return result