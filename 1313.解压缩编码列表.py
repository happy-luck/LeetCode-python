方法一：
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0,len(nums),2):
            t = nums[i]
            while t>0:
                ans.append(nums[i+1])
                t -= 1
        return ans

方法二：模拟
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = list()
        for i in range(0, len(nums), 2):
            ans.extend([nums[i + 1]] * nums[i])
        return ans
时间复杂度：O(N+∑nums even)
空间复杂度：O(∑nums even)。
