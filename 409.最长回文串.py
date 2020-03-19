方法一：
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        ans = 0
        for char in s:
            dic[char] =dic.get(char,0)+1
            if dic[char]==2:
                ans += 2
                dic[char]-=2
        for i in dic:
            if dic[i]==1:
                return ans+1
        return ans
方法二：
如果有任何一个字符 ch 的出现次数 v 为奇数（即 v % 2 == 1），那么可以将这个字符作为回文中心。
在代码中，我们用 ans 存储回文串的长度，由于在遍历字符时，ans 每次会增加 v / 2 * 2，因此 ans 一直为偶数。
但在发现了第一个出现次数为奇数的字符后，我们将 ans 增加 1，这样 ans 变为奇数，在后面发现其它出现奇数次的字符时，我们就不改变 ans 的值了。

class Solution:
    def longestPalindrome(self, s):
        ans = 0
        count = collections.Counter(s)
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans

时间复杂度：O(N)，其中 N为字符串 s 的长度。我们需要遍历每个字符一次。
空间复杂度：O(S)，其中 S为字符集大小。