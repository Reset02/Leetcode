class Solution {
public:
    bool hasSameDigits(string s) {
        vector<int> digits;
        for (char c : s) digits.push_back(c - '0');

        while (digits.size() > 2){
            vector<int> next;
            for (int i = 0; i + 1 < digits.size(); ++i){
                next.push_back((digits[i] + digits[i + 1]) % 10);
            }
            digits = next;
        }
        return digits[0] == digits[1];
    }
};