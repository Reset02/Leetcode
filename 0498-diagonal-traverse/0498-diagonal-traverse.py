class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        i, j, dir = 0, 0, 1  # dir=1 表示往右上, dir=-1 表示往左下

        for i in range(m * n):
            result.append(mat[i][j])
            if dir == 1: # 往右上
                if j == n - 1: # 右邊界
                    i += 1
                    dir = -1
                elif i == 0: # 上邊界
                    j += 1
                    dir = -1
                else:    # 往右上走
                    i -= 1
                    j += 1
            else: # dir == -1，往左下
                if i == m - 1: # 下邊界
                    j += 1
                    dir = 1
                elif j == 0: # 左邊界
                    i += 1
                    dir = 1
                else:   # 往左下走
                    i += 1
                    j -= 1
        return result

