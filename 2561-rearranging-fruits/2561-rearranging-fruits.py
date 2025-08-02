class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq1 = Counter(basket1)
        freq2 = Counter(basket2)
        total = freq1 + freq2

        for fruit in total:
            if total[fruit] % 2 != 0:
                return -1
        

        move_from_b1 = []
        move_from_b2 = []
        for fruit in total:
            diff = freq1[fruit] - freq2[fruit]
            if diff > 0:
                move_from_b1.extend([fruit] * (diff // 2))
            elif diff < 0:
                move_from_b2.extend([fruit] * (-diff // 2))

        move_from_b1.sort()
        move_from_b2.sort(reverse=True)
        min_val = min(basket1 + basket2)

        cost = 0
        for a, b in zip(move_from_b1, move_from_b2):
            cost += min(min(a, b), 2 * min_val)

        return cost