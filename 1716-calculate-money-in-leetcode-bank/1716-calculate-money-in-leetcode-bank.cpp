class Solution {
public:
    int totalMoney(int n) {
        int weeks = n / 7;
        int days = n % 7;

        // 完整週的總和（等差數列公式）
        int total = 28 * weeks + 7 * (weeks * (weeks - 1)) / 2;

        // 最後一週剩餘天數（從 weeks+1 開始）
        total += days * (weeks + 1) + (days * (days - 1)) / 2;

        return total;
    }
};