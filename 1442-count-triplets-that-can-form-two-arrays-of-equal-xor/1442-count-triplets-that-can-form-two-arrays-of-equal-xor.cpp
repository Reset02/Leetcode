class Solution {
public:
    int countTriplets(vector<int>& arr) {
        int count = 0;

        // Iterate over each possible starting index i
        for (int start = 0; start < arr.size() - 1; start++){
            // Initialize XOR value for the subarray from start to mid-1
            int xor_A = 0;

            // Iterate over each possible middle index j
            for (int mid = start + 1; mid < arr.size(); mid++){
                // Update xorA to include arr[mid - 1]
                xor_A ^= arr[mid - 1];

                // Initialize XOR value for the subarray from mid to end
                int xor_B = 0;

                // Iterate over each possible ending index k (starting from mid)
                for (int end = mid; end < arr.size(); end++){
                    xor_B ^= arr[end];

                    // found a valid triplet (start, mid, end)
                    if (xor_A == xor_B){
                        count++;
                    }
                }
            }
        }
        return count;
    }
};