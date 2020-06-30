class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_one = max(nums[0],nums[1])
        max_two = min(nums[0],nums[1])
        for i in range(2,len(nums)):
            if nums[i]>max_one:
                max_two = max_one
                max_one = nums[i]
            elif nums[i]>max_two:
                max_two = nums[i]
        return (max_one-1)*(max_two-1)