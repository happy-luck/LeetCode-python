class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0]-x[1])
        total = 0
        n = len(costs)//2
        for i in range(n):
            total += costs[i][0]+costs[i+n][1]
        return total

时间复杂度：O(N)，需要对 price_A - price_B 进行排序。
空间复杂度：O(1)。        