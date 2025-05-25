class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string, int> count;
        int length = 0;
        bool has_center = false;

        // 統計每個字串出現次數
        for (const string& word : words) {
            count[word]++;
        }

        for (auto& [word, freq] : count) {
            string rev = word;
            reverse(rev.begin(), rev.end());

            if (word != rev) {
                // 如果有對應的反轉字，進行配對
                if (count.find(rev) != count.end()) {
                    int pair = min(freq, count[rev]);
                    length += pair * 4;
                    count[word] -= pair;
                    count[rev] -= pair;
                }
            } else {
                // 自己就是回文（例如 "gg"）
                int pair = freq / 2;
                length += pair * 4;
                count[word] -= pair * 2;

                if (count[word] > 0) {
                    has_center = true;
                }
            }
        }

        if (has_center) {
            length += 2; // 可放在中心的回文
        }

        return length;
    }
};