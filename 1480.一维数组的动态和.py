class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums)==0 or len(nums)==1:
            return nums
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums