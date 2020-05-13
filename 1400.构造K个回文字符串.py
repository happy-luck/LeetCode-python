class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0)+1
        if len(s)<k:
            return False
        num = 0
        for i in dic.values():
            if i%2!=0:
                num += 1
        if num<=k:
            return True
        else:
            return False