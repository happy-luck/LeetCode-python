class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num = 0
        balance = 0
        for i in range(len(s)):
            if s[i]=='L':
                balance += 1
            if s[i]=='R':
                balance-= 1
            if balance==0:
                num+= 1
        if num==0:
            return 1
        else:
            return num