方法一：
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        res = []
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res

方法二：     
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window,res = [],[]
        for i in range(len(nums)):
            while window and nums[window[-1]]<nums[i]:
                window.pop()
            window.append(i)
            if window[0] == i-k:
                window.pop(0)
            if i >=k-1:
                res.append(nums[window[0]])
        return res

方法三：
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        temp0 = float('-inf') #负穷大
        temp = temp0
        for i in range(len(nums)):     
            temp = max(temp, nums[i])   #窗口的最后一个值与前缀最大值比较
            if i > k-2:                 #判断到达窗口长度
                res.append(temp)
                if temp <= nums[i-k+1]: #如果即将滑出窗口的值可能是最大值，重新计算下个窗口前缀temp的值
                    temp = temp0
                    for j in range(k-1):
                        temp = max(temp, nums[i-j])
                    
        return res      