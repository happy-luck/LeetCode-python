class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            tar = 0
            while(num != 0):
                num = num // 10
                tar += 1
            if tar%2==0:
                res += 1
        return(res)

方法一：枚举 + 字符串

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)

时间复杂度：O(N)，其中 N 是数组 nums 的长度。这里假设将整数转换为字符串的时间复杂度为 O(1)。
空间复杂度：O(1)。

方法二：枚举 + 数学

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if int(math.log10(num) + 1) % 2 == 0)

时间复杂度：O(N)，其中 N 是数组 nums 的长度。
空间复杂度：O(1)。
