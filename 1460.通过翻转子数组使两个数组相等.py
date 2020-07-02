方法一：
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dic = {}
        for i in target:
            dic[i] = dic.get(i,0)+1
        for j in arr:
            if j not in dic:
                return False
            dic[j] = dic.get(j,0)-1
            if dic[j]<0:
                return False
        return True
方法二：
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target)==sorted(arr)        