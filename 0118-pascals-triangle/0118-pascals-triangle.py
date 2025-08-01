class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1] * (i + 1) # 頭尾都是 1，中間預設先填 1
            for j in range(1, i): # 從第二個元素到倒數第二個
                row[j] = res[i - 1][j - 1] + res[i- 1][j]
            res.append(row)
        return res