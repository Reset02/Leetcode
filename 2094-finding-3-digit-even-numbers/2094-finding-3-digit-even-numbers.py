class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        nums = set()

        # 找出所有長度為 3 的排列組合（不重複 index）
        for a, b, c in permutations(digits, 3):
            # 檢查是否為合法的三位偶數
            if a != 0 and c % 2 == 0:
                num = a * 100 + b * 10 + c
                nums.add(num)

        return sorted(nums)