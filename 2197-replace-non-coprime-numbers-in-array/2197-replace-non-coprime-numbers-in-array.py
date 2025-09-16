class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for x in nums:
            cur = x
            # 嘗試和 stack 最後的元素合併
            while stack:
                g = math.gcd(stack[-1], cur)
                if g == 1: # 互質就不能合併
                    break
                # 合併成 LCM
                cur = stack[-1] // g * cur
                stack.pop()
            stack.append(cur)
        
        return stack