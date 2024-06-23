class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            # 更新最大值雙端隊列
            while max_deque and nums[right] > max_deque[-1]:
                max_deque.pop()
            max_deque.append(nums[right])
            
            # 更新最小值雙端隊列
            while min_deque and nums[right] < min_deque[-1]:
                min_deque.pop()
            min_deque.append(nums[right])
            
            # 檢查最大值和最小值的差值 
            # 當窗口內的最大值和最小值的差值超過 limit 時，我們需要縮小窗口的左邊界
            while max_deque[0] - min_deque[0] > limit:
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
        