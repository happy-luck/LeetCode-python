方法一：
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[j]<nums[i]:
                    res[i] += 1
        return res
时间复杂度：枚举数组里的每个数字为 O(n**2) 
空间复杂度：O(1) ，不需要使用额外的空间。

方法二：频次数组 + 前缀和
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt, vec = [0] * 101, [0] * n
        for num in nums:
            cnt[num] += 1
        for i in range(1, 101):
            cnt[i] += cnt[i - 1]
        for i in range(n):
            if nums[i]:
                vec[i] = cnt[nums[i] - 1]
        return vec
时间复杂度：统计 O(S+n) ，其中 S 为值域大小，n=nums.length 。

空间复杂度：O(S) ，需要开一个值域大小的数组。

方法三：排序
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        vec = [0] * n
        tmp = sorted([(nums[i], i) for i in range(n)])
        
        pre = -1
        for i in range(n):
            if tmp[i][0] != tmp[i - 1][0]:
                pre = i - 1
            vec[tmp[i][1]] = pre + 1
        return vec
时间复杂度：排序需要 O(nlogn) 的时间复杂度，遍历数组需要 O(n) 的时间复杂度，所以总的时间复杂度为 O(nlogn+n)=O(nlogn)。
空间复杂度：上文提及的 tmp 数组需要 O(n) 的空间，空间复杂度为 O(n) 。