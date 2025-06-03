class Solution {
public:
    int maxCandies(vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, vector<vector<int>>& containedBoxes, vector<int>& initialBoxes) {
        int n = status.size();
        unordered_set<int> haveKeys;
        unordered_set<int> visited;
        unordered_set<int> boxes(initialBoxes.begin(), initialBoxes.end());
        queue<int> q;
        for (int b : initialBoxes) q.push(b);
        
        int totalCandies = 0;

        while (!q.empty()) {
            int size = q.size();
            bool openedThisRound = false;

            for (int i = 0; i < size; ++i) {
                int box = q.front(); q.pop();

                if (visited.count(box)) continue;

                // 可以打開：本身打開或有鑰匙
                if (status[box] == 1 || haveKeys.count(box)) {
                    visited.insert(box);
                    totalCandies += candies[box];
                    openedThisRound = true;

                    // 拿鑰匙
                    for (int key : keys[box]) {
                        if (!haveKeys.count(key)) {
                            haveKeys.insert(key);
                            if (boxes.count(key) && !visited.count(key)) {
                                q.push(key);
                            }
                        }
                    }

                    // 拿到的子箱子
                    for (int newBox : containedBoxes[box]) {
                        boxes.insert(newBox);
                        if (status[newBox] == 1 || haveKeys.count(newBox)) {
                            q.push(newBox);
                        } else {
                            // 雖然現在開不了，但先放進去等待鑰匙
                            q.push(newBox);
                        }
                    }
                } else {
                    // 還開不了，之後再處理
                    q.push(box);
                }
            }

            if (!openedThisRound) break;  // 沒新箱子被打開 → 結束
        }

        return totalCandies;
    }
};