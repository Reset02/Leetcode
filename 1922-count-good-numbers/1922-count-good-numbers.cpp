class Solution {
private:
    static constexpr int mod = 1000000007;

    // Fast exponentiation function
    long long fast_pow(long long base, long long exp) {
        long long result = 1;
        while (exp > 0) {
            if (exp % 2 == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp /= 2;
        }
        return result;
    }

public:
    int countGoodNumbers(long long n) {
        long long even_positions = (n + 1) / 2;  // 偶數位置個數（包含 index 0）
        long long odd_positions = n / 2;         // 奇數位置個數

        long long even_ways = fast_pow(5, even_positions);  // 每個偶數位置有 5 種數字（0, 2, 4, 6, 8）
        long long odd_ways = fast_pow(4, odd_positions);    // 每個奇數位置有 4 種質數（2, 3, 5, 7）

        return (even_ways * odd_ways) % mod;  // 最後取 mod
    }
};