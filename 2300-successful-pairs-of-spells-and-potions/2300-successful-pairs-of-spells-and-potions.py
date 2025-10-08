class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []

        for spell in spells:
            # 找到第一個 potion[j] >= success / spell
            target = success / spell
            idx = bisect_left(potions, target)
            res.append(m - idx)
        
        return res