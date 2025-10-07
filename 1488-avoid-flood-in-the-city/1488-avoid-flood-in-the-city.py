class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lake_day = {} # lake -> 上次下雨的日子
        dry_days = [] # 可用乾旱日（升序
        n = len(rains)
        ans = [-1] * n

        for i, lake in enumerate(rains):
            if lake > 0:
                # 如果湖已滿，需要找出下一個可乾的日子
                if lake in lake_day:
                    prev_day = lake_day[lake]
                    # 找出在 prev_day 之後的乾旱日
                    idx = bisect_right(dry_days, prev_day)
                    if idx == len(dry_days):
                        return [] # 沒有可以乾的日子 → 洪水
                    dry_day = dry_days.pop(idx)
                    ans[dry_day] = lake # 乾這個湖
                lake_day[lake] = i
            else:
                # 可乾旱的日子
                insort(dry_days, i)
                ans[i] = 1 # 先填預設值
        
        return ans