方法一：
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        arr = [m * [0] for i in range(n)]
        for indice in indices:
            for i in range(m):
                arr[indice[0]][i] += 1
            for j in range(n):
                arr[j][indice[1]] += 1

        res = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j]%2==1:
                    res += 1
        return res

方法二：计数
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [False] * n
        cols = [False] * m
        res = 0

        for r, c in indices:
            rows[r] = not rows[r]
            cols[c] = not cols[c]
        
        # rows数组里，True和False的个数
        rows_true = rows.count(True)
        rows_false = n - rows_true

        cols_true = cols.count(True)
        cols_false = m - cols_true

        res = rows_true * cols_false + rows_false * cols_true
        return res