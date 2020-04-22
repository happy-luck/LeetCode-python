class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target
时间复杂度：O(n**2)。
空间复杂度：这里没有使用到辅助空间，故渐进空间复杂度为 O(1)        