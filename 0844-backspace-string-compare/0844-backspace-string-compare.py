class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def build(string):
            stack = []
            for c in string:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return ''.join(stack)
        
        return build(s) == build(t)