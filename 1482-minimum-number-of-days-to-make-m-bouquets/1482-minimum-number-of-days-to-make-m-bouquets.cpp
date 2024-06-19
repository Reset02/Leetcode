class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        // 使用 long long 來防止整數溢出
        if (static_cast<long long>(m) * k > bloomDay.size()) {
            return -1;
        }

        int left = *min_element(bloomDay.begin(), bloomDay.end());
        int right = *max_element(bloomDay.begin(), bloomDay.end());
        
        while (left < right){
            int mid = left + (right - left) / 2;
            if (canMakeBouquets(bloomDay, m, k, mid)){
                right = mid;
            } else{
                left = mid + 1;
            }
        }
        return canMakeBouquets(bloomDay, m, k, left) ? left: -1;
    }
private:
    bool canMakeBouquets(const vector<int>& bloomDay, int m, int k, int days){
        long long bouquets = 0, flowers = 0;
        for (int bloom : bloomDay) {
            if (bloom <= days) {
                flowers++;
                if (flowers == k) {
                    bouquets++;
                    flowers = 0;
                }
            } else {
                flowers = 0;
            }
        }
        return bouquets >= m;
    }
};