class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odds = []
        evens = []

        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)

        # Case 1: All odds → 所有奇數形成的序列是合法的（因為 (奇+奇)%2 == 0）
        # Case 2: All evens → (偶+偶)%2 == 0
        max_same = max(len(odds), len(evens))

        # Case 3: Alternating 奇偶奇偶奇偶 → (奇+偶)%2 == 1, (偶+奇)%2 == 1
        max_alternating = 1
        last = nums[0] % 2
        for i in range(1, len(nums)):
            if nums[i] % 2 != last:
                max_alternating += 1
                last = nums[i] % 2

        return max(max_same, max_alternating)