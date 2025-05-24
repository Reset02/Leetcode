class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> result;
        int n = words.size();
        for (int i = 0; i < n; ++i){
            if (words[i].find(x) != string::npos){
                result.push_back(i);
            }
        }
        return result;
    }
};