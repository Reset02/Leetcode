class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 目標是檢查一副手牌是否可以按照給定的組大小（groupSize）分成若干個連續的牌組
        hand_size = len(hand)

        if hand_size % groupSize != 0:
            return False
        
        # Counter to store the count of each card value 計算每張牌的數量
        card_count = Counter(hand)

        # Min-heap to process the cards in sorted order 創建最小堆來儲存牌的值
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap) # 將 min_heap 轉換為最小堆，以便我們能夠以升序處理牌的值

        # Process the cards until the heap is empty
        while min_heap: # 處理所有牌，直到堆空
            current_card = min_heap[0] # Get the smallest card value 取出最小的牌值
            # Check each consecutive sequence of groupSize cards
            for i in range(groupSize):
                if card_count[current_card + i] == 0:
                    return False
                card_count[current_card + i] -= 1
                # 減少每張牌的數量。如果某張牌的數量減少到零，且這張牌並不是堆中的最小值，則返回 False。
                # 否則，從堆中移除這張牌。
                if card_count[current_card + i] == 0: 
                    if current_card + i != heapq.heappop(min_heap):
                        return False
        return True