class Solution {
public:
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        // Sort by end asc, start desc
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b){
            if (a[1] != b[1]) return a[1] < b[1];   // end asc
            return a[0] > b[0];                     // start desc
        });

        int p1 = -1;  // largest picked
        int p2 = -1;  // second largest picked
        int ans = 0;

        for (auto &v : intervals){
            int s = v[0];
            int e = v[1];

            // Case 1: already two points inside interval
            if (p2 >= s) continue;

            // Case 2: one point inside interval
            if (p1 >= s){
                ans += 1;
                p2 = p1;
                p1 = e;
            }
            else{
                ans += 2;
                p2 = e - 1;
                p1 = e;
            }
        }
        return ans;
    }
};