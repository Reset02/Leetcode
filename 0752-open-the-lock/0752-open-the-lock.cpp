class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        // 起始鎖組合為 '0000'
        string start = "0000";
        // 將死亡組合轉換為無序集合，方便查找
        unordered_set<string> dead(deadends.begin(), deadends.end());
        // 如果起始組合就是死亡組合或者目標組合是死亡組合，則無法解鎖，返回-1
        if (dead.count(start) || dead.count(target)) return -1;
        
        // 建立 BFS 用的佇列，將起始組合和步數（0步開始）加入佇列
        queue<pair<string, int>> q;
        q.push({start, 0});
        // 設置已經訪問過的鎖組合，避免重複訪問
        unordered_set<string> visited;
        visited.insert(start);
        
        while (!q.empty()) {
            auto [current, steps] = q.front();
            q.pop();
            // 如果當前組合等於目標組合，則返回步數
            if (current == target) return steps;
            
            // 對當前組合的每個轉輪進行轉動，得到相鄰組合
            for (int i = 0; i < 4; ++i) {
                // 向上轉動一位
                string up = current;
                up[i] = (up[i] - '0' + 1) % 10 + '0';
                // 向下轉動一位
                string down = current;
                down[i] = (down[i] - '0' + 9) % 10 + '0';
                
                // 如果相鄰組合不在死亡組合中且沒有訪問過，則加入佇列中並標記為已訪問
                if (!dead.count(up) && !visited.count(up)) {
                    q.push({up, steps + 1});
                    visited.insert(up);
                }
                if (!dead.count(down) && !visited.count(down)) {
                    q.push({down, steps + 1});
                    visited.insert(down);
                }
            }
        }
        
        // 如果無法解鎖，返回-1
        return -1;
        
    }
};