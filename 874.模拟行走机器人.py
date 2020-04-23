class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        x = y = di = 0
        obstacleSet = set(map(tuple,obstacles))
        ans = 0
        for cmd in commands:
            if cmd==-2:
                di = (di-1)%4
            elif cmd==-1:
                di = (di+1)%4
            else:
                for k in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)
        return ans     
时间复杂度：O(N+K)，其中 N,K 分别是 commands 和 obstacles 的长度。
空间复杂度：O(K)，用于存储 obstacleSet 而使用的空间。      