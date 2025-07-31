class Solution {
public:
    int subarrayBitwiseORs(vector<int>& arr) {
        unordered_set<int> result;
        set<int> prev;// 使用 set 自動去重，也可以用 unordered_set

        for (int num : arr){
            set<int> cur;
            cur.insert(num);
            for (int x: prev){
                cur.insert(x | num);
            }
            prev = cur;
            for (int x : cur){
                result.insert(x);
            }
        }
        return result.size();
    } 
};