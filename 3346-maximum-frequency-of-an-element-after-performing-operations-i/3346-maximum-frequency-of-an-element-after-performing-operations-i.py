# 引入 bisect 用於二分搜尋
import bisect

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # 先對 nums 排序，方便後續用區間判斷
        nums.sort()

        ans = 0  # 儲存目前找到的最大頻率
        num_count = {}  # 用來記錄每個數字的出現次數
        last_num_index = 0  # 用來標記某一段相同數字的起始位置

        # === 第一步：統計每個數字的出現次數 ===
        for i in range(len(nums)):
            # 當目前數字與起始位置的數字不同，代表前一段結束
            if nums[i] != nums[last_num_index]:
                # 記錄該數字出現次數
                num_count[nums[last_num_index]] = i - last_num_index
                # 更新目前最大頻率
                ans = max(ans, i - last_num_index)
                # 更新新的起始位置
                last_num_index = i

        # 處理最後一段（因為 for 迴圈結束後還沒記錄最後一組）
        num_count[nums[last_num_index]] = len(nums) - last_num_index
        ans = max(ans, len(nums) - last_num_index)

        # === 第二步：枚舉每個可能成為「最終統一值」的目標數字 i ===
        # 範圍是從 nums[0] 到 nums[-1]（也就是最小值到最大值）
        for i in range(nums[0], nums[-1] + 1):

            # 找出所有能「調整成 i」的數字範圍
            # 即所有在 [i - k, i + k] 範圍內的數字都能變成 i
            l = bisect.bisect_left(nums, i - k)
            r = bisect.bisect_right(nums, i + k) - 1

            # 若這個 i 本來就存在於 nums 中
            if i in num_count:
                # 那最大頻率 = 可調整進來的元素數量 or (原本次數 + 可修改數量)
                temp_ans = min(r - l + 1, num_count[i] + numOperations)
            else:
                # 若 i 不在 nums 中，只能靠修改進來的數
                temp_ans = min(r - l + 1, numOperations)

            # 更新答案
            ans = max(ans, temp_ans)

        # 回傳最大可能頻率
        return ans
