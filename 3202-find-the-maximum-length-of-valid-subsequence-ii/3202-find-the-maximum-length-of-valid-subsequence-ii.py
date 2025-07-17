class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = defaultdict(dict)  # dp[mod][last_num] = max length
        res = 1

        for i in range(len(nums)):
            curr = nums[i]
            local = defaultdict(int)

            for j in range(i):
                prev = nums[j]
                mod = (prev + curr) % k
                prev_len = dp[mod].get(prev, 1)
                local[(mod, curr)] = max(local[(mod, curr)], prev_len + 1)
                res = max(res, local[(mod, curr)])

            for (mod, num), length in local.items():
                dp[mod][num] = max(dp[mod].get(num, 1), length)

            for mod in range(k):
                dp[mod].setdefault(curr, 1)

        return res