class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        num1 = 0
        num2 = 0
        for i in chips:
            if i%2 == 0:
                num1 += 1
            else:
                num2 += 1
        return min(num2,num1)