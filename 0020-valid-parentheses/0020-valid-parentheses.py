class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values(): # 開括號
                stack.append(char)
            elif char in mapping: # 關括號
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False # 非法字元（根據題目不會出現）
        
        return not stack