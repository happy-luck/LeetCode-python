方法一：双指针
class Solution:
    def compressString(self, S: str) -> str:
        i = 0
        new_S = ''
        while i<len(S):
            j = i
            new_S += S[j]
            while j+1<len(S) and S[j+1] == S[j]:
                j += 1
            new_S += str(j-i+1)
            i = j+1
        if len(new_S)<len(S):
            return new_S
        else:
            return S

方法二：双指针
class Solution:
    def compressString(self, S: str) -> str:
        i = 0
        new_S = ''
        while i<len(S):
            num = 1
            j = i
            new_S += S[j]
            while j+1<len(S) and S[j+1] == S[j]:
                num += 1
                j += 1
            new_S += str(num)
            i += num
        if len(new_S)<len(S):
            return new_S
        else:
            return S

方法三：我们从左往右遍历字符串，用 ch 记录当前要压缩的字符，cnt 记录 ch 出现的次数，
如果当前枚举到的字符 s[i] 等于 ch ，我们就更新 cnt 的计数，即 cnt = cnt + 1，
否则我们按题目要求将 ch 以及 cnt 更新到答案字符串 ans 里，即 ans = ans + ch + cnt，完成对 ch 字符的压缩。
随后更新 ch 为 s[i]，cnt 为 1，表示将压缩的字符更改为 s[i]。
class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return ""
        ch = S[0]
        ans = ''
        cnt = 0
        for c in S:
            if c == ch:
                cnt += 1
            else:
                ans += ch + str(cnt)
                print(c)
                ch = c
                cnt = 1
        ans += ch + str(cnt)
        return ans if len(ans) < len(S) else S
