class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies)
        res = []
        for i in range(len(candies)):
            if max_-candies[i]<=extraCandies:
                res.append(True)
            else:
                res.append(False)
        return res