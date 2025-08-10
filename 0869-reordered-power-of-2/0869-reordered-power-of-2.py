class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def sort_digits(x):
            return ''.join(sorted(str(x)))
        
        # 預先計算所有 2 的冪
        power_set = [sort_digits(1 << i) for i in range(31)]

        return sort_digits(n) in power_set