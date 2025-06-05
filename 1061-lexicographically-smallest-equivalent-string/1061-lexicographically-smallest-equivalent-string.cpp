class Solution {
public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        vector<int> parent(26);
        // 初始化，每個字母都是自己的代表
        for (int i = 0; i < 26; ++i) {
            parent[i] = i;
        }

        // Find：尋找代表元素，帶 path compression
        function<int(int)> find = [&](int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        };

        // Union：合併兩個字元的等價集合，讓字典序小的作為代表
        auto unionSet = [&](int x, int y) {
            int px = find(x);
            int py = find(y);
            if (px == py) return;
            if (px < py) {
                parent[py] = px;
            } else {
                parent[px] = py;
            }
        };

        // 建立等價集合
        for (int i = 0; i < s1.length(); ++i) {
            unionSet(s1[i] - 'a', s2[i] - 'a');
        }

        // 轉換 baseStr 中的每個字元為其最小等價字元
        string result;
        for (char c : baseStr) {
            char smallestChar = find(c - 'a') + 'a';
            result += smallestChar;
        }

        return result;
    }
};