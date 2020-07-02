方法一：
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        target = False
        for i in range(m):
            for j in range(n):
                if grid[i][j]<0:
                    if j!=0:
                        res += n - j
                        break
                    else:
                        target = True
                        break
            if target==True:
                res += (m-i)*n
                break
        return res
方法二：
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        pos = n
        for i in range(m):
            for j in range(pos):
                if grid[i][j]<0:
                    res += n - j
                    pos = j+1
                    break
            if pos==1:
                res += (m-i-1)*n
                break
        return res