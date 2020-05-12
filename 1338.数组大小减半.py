class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic = {}
        for i in arr:
            dic[i] = dic.get(i,0) + 1
        dic_val = sorted(dic.values(),reverse=True)
        sum_ = 0
        n = len(arr)
        for i in range(len(dic_val)):
            sum_ += dic_val[i]
            if n-sum_<=n/2:
                return i+1