方法一：
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        div = 1
        while(x/div>=10):
            div *= 10
        while(x>0):
            left = x//div
            right = x%10
            if left!=right:
                return False
            x = (x%div)//10
            div /= 100
        
        return True

方法二：
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        reverseN = 0
        while(x>reverseN):
            reverseN = reverseN*10 + x%10
            x = x//10
        return x==reverseN or x==reverseN//10

时间复杂度：O(log 10(n))，对于每次迭代，我们会将输入除以10。
空间复杂度：O(1)