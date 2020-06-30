方法一（自己）：
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
                res.append(nums[i])
                res.append(nums[i+n])
        return res
方法二：
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            m = n - i    
            for k in range(i):
                nums[m], nums[m+1] = nums[m+1], nums[m]
                m += 2    
        return nums