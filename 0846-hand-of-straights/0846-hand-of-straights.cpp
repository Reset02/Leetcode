class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        int handSize = hand.size();
        if (handSize % groupSize != 0){
            return false;
        }
        
        //計算每張牌的數量
        map<int,int> cardCount;
        for (int i = 0; i < handSize; i++){
            cardCount[hand[i]]++;
        }
        //處理所有牌，直到堆空：
        while (!cardCount.empty()){
            // 取出最小的牌值
            int currentCard = cardCount.begin()->first;
            // 檢查每一組連續的牌
            for (int i = 0; i < groupSize; i++){
                // 如果某張牌的數量為零，則無法形成所需的組
                if (cardCount[currentCard + i] == 0){
                    return false;
                }
                cardCount[currentCard + i]--;
                if (cardCount[currentCard + i] < 1){
                   // 從堆中移除這張牌
                   cardCount.erase(currentCard + i);
                }
            }
        }
        return true;
    }
};