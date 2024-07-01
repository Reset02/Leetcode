class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive_odd = 0
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                consecutive_odd += 1
            else:
                consecutive_odd = 0
            
            if consecutive_odd == 3:
                return True
        return False
            
        