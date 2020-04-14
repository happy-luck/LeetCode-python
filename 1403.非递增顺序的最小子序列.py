方法一：
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if sum(nums[0:i])>sum(nums[i:len(nums)]):
                return nums[0:i]
        return nums

方法二：
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        curSum, total = 0, sum(nums)
        res = []
        nums = sorted(nums, reverse=True)
        for i in range(len(nums)):
            curSum += nums[i]
            res.append(nums[i])
            if curSum > total - curSum:
                break
        return res