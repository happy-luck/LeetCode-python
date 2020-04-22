class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(1,len(points)):
            res += max(abs(points[i][0]-points[i-1][0]),abs(points[i][1]-points[i-1][1]))
        return res
时间复杂度：O(N)，其中 N 是数组的长度。

空间复杂度：O(1)        