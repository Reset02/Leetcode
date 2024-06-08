class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod = 0 # 初始化了一個變數 prefix_mod，用來表示目前遍歷到的子陣列的總和除以 k 的餘數
        mod_seen = {0: -1} # 初始時，將餘數 0 的索引設為 -1

        for i in range(len(nums)):
            # 每一次迭代中，將目前子陣列的總和加上當前元素 nums[i]，然後取除以 k 的餘數，更新 prefix_mod
            prefix_mod = (prefix_mod + nums[i]) % k

            if prefix_mod in mod_seen: # 檢查目前的 prefix_mod 是否已經在 mod_seen 字典中出現過
                # ensures that the size of subarray is at least 2
                if i - mod_seen[prefix_mod] > 1: # 檢查是否存在一個子陣列的長度至少為 2，使得該子陣列的總和可以被 k 整除
                    return True
            else:
                # 如果不存在這樣的子陣列，則更新 mod_seen[prefix_mod] 的值為目前的索引 i
                # mark the value of prefix_mod with the current index.
                mod_seen[prefix_mod] = i
        return False