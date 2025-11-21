class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int n = s.size();

        vector<int> left(26, -1), right(26, -1);

        // 找每個字元最左 & 最右出現位置
        for (int i = 0; i < n; i++){
            int c = s[i] - 'a';
            if (left[c] == -1)
                left[c] = i;
            right[c] = i;
        }

        int ans = 0;
        // 對每個字母 a 計算 'a b a'
        for (int c = 0; c < 26; c++){
            int l = left[c];
            int r = right[c];

            if (l != -1 && r != -1 && l < r){
                vector<bool> seen(26, false);
                for (int i = l + 1; i < r; i++){
                    seen[s[i] - 'a'] = true;
                }
                for (bool x: seen){
                    if(x) ans++;
                }
            }
        }
        return ans;
    }
};