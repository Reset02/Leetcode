class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)  # 節點數量

        # 對每個節點計算如果做一次 XOR k，數值會增加多少
        netChange = [(nums[i] ^ k) - nums[i] for i in range(n)]
        # 初始總和：不做任何操作的情況下的總和
        nodeSum = sum(nums)

        # 將變化量從大到小排序，這樣我們可以優先挑選對總和有正向貢獻的節點
        netChange.sort(reverse=True)

        # 每次配對兩個變化量，如果兩個加起來仍大於 0，就做這筆操作
        for i in range(0, n, 2):
            # 若剩下一個節點就沒辦法配對了（因為操作需要兩個節點）
            if i + 1 == n:
                break
            pairSum = netChange[i] + netChange[i + 1]
            # 如果配對後能提升總和，就執行操作（把提升值加進 nodeSum）
            if pairSum > 0:
                nodeSum += pairSum

        return nodeSum  # 回傳最大總和