class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = []
        for i in range(len(matrix)):
            rowmin = float('inf')
            for j in range(len(matrix[0])):
                rowmin = min(rowmin, matrix[i][j])
            row_min.append(rowmin)

        col_max = []
        for i in range(len(matrix[0])):
            colmax = float('-inf')
            for j in range(len(matrix)):
                colmax = max(colmax, matrix[j][i])
            col_max.append(colmax)
        
        lucky_number = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
                    lucky_number.append(matrix[i][j])
        
        return lucky_number
        