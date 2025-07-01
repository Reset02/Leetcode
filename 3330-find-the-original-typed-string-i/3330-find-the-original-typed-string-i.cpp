class Solution {
public:
    int possibleStringCount(string word) {
        unordered_set<string> possible;
        possible.insert(word); // 原始輸入也可能是正確的

        int n = word.size();
        int i = 0;

        while(i < n){
            int j = i;
            // 找出連續相同的字元區段
            while(j < n && word[j] == word[i]){
                j++;
            }
            int len = j -i;
            if (len >= 2){
                // 將這段中的多餘字元刪除，只保留第一個
                for (int k = 1; k < len; ++k){
                    string new_word = word.substr(0, i) + word.substr(i + k);
                    possible.insert(new_word);
                }
            }
            i = j;
        }
        return possible.size();
    }
};