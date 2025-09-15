class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        // 用 unordered_set 存壞掉的字母，查詢 O(1)
        unordered_set<char> broken(brokenLetters.begin(), brokenLetters.end());

        stringstream ss(text); // 用 stringstream 切單字
        string word;
        int count = 0;

        while (ss >> word){
            // 逐字讀取
            bool canType = true;
            for (char ch : word){
                if (broken.count(ch)){
                    // 單字含有壞掉字母
                    canType = false;
                    break; // 提早跳出，省時間
                }
            }
            if (canType) count++;
        }
        return count;
    }
};