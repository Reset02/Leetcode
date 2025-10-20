class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int X = 0;
        for (string op : operations){
            if (op.find("++") != string:: npos)
                X += 1;
            else
                X -= 1;
        }
        return X;
    }
};