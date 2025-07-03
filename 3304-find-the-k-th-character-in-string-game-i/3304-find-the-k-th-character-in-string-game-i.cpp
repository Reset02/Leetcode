class Solution {
public:
    char kthCharacter(int k) {
        int shift = 0; // 表示這個字元經歷了幾次 +1

        while (k > 1){
            int length = 1;
            while(length * 2 < k){
                length *= 2; // 找出最接近 k 的 2 的冪次
            }

            if (k > length){
                k -= length; // 往前推回原字串位置
                shift += 1; // 多一次 shift (+1)
            }else{
                // k 在前半段 → 無需改變，只是來自上一層
            }
        }
        // 最後一定會回到 k = 1 → 對應字母 'a'
        // 根據 shift 決定偏移幾個字母（z 之後回到 a，所以 mod 26）
        return (char)((shift % 26) + 'a');
    }
};