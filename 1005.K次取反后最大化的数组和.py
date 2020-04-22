方法一：
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        j = 0
        min_ = A[-1]
        while i<len(A) and j<K:
            if A[i]<0:
                A[i] = -A[i]
                j += 1
                i += 1
            else:
                if (K-j)%2==1:
                    if A[i-1]<A[i]:
                        A[i-1] = -A[i-1]
                    else:
                        A[i] = -A[i]
                j = K
        return sum(A)


方法二：
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        change_times = 0
        while A[change_times] < 0:
            A[change_times] *= -1
            change_times += 1
            if change_times >= K: 
                break
        return sum(A) - min(A)*2 if (K - change_times)%2 else sum(A)