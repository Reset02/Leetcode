class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = defaultdict(dict) # dp[mod][last_num] = max_length
        res = 1

        for i in range(len(nums)):
            curr = nums[i]
            local_updates = defaultdict(int)

            for j in range(i):
                prev = nums[j]
                mod = (prev + curr) % k
                prev_len = dp[mod].get(prev, 1)
                local_updates[(mod, curr)] = max(local_updates[(mod, curr)], prev_len + 1)
                res = max(res, local_updates[(mod, curr)])
            

            # 將更新套入 dp
            for (mod, num), length in local_updates.items():
                dp[mod][num] = max(dp[mod].get(num, 1), length)
            
            # 單一元素本身也可以成為長度為 1 的 subsequence
            for mod in range(k):
                dp[mod].setdefault(curr, 1)
        
        return res