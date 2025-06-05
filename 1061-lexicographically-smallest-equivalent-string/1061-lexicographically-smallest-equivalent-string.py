class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))  # 'a' to 'z'

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            # always keep smaller lexicographical root
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))

        result = []
        for c in baseStr:
            rep = find(ord(c) - ord('a'))
            result.append(chr(rep + ord('a')))

        return ''.join(result)