#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isBalanced(int num) {
        string s = to_string(num);
        vector<int> count(10, 0);

        // 計算每個數字出現的次數
        for (char c : s) {
            count[c - '0']++;
        }

        // 檢查每個出現過的數字是否平衡
        for (char c : s) {
            int d = c - '0';
            if (count[d] != d) return false;
        }

        return true;
    }

    int nextBeautifulNumber(int n) {
        int num = n + 1;
        while (true) {
            if (isBalanced(num)) return num;
            num++;
        }
    }
};

