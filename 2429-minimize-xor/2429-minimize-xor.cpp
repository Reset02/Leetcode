class Solution {
public:
    int minimizeXor(int num1, int num2) {
        // 計算 num2 的 set bits 數量
        int k = __builtin_popcount(num2);

        // 初始化結果 x
        int x = 0;

        // 遍歷 num1 的每一位
        for (int i = 31; i >= 0; i--){ // 從高位到低位
            if (k > 0 && (num1 & (1 << i))){// 如果 num1 的該位是 1，且還需要 set bits
                x |= (1 << i);// 將 x 的該位設為 1
                k -= 1;
            }
        }
        // 如果還有剩餘的 set bits
        for (int i = 0; i < 32; i++){// 從低位到高位填充剩餘的 set bits
            if (k > 0 && !(x & (1 << i))){// 如果 x 的該位是 0
                x|= (1 << i); // 將 x 的該位設為 1
                k -= 1;
            }
        }
        return x;
    }
};