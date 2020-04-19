方法一：空间换时间
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)<=0:
            return 0
        if len(stones)==1:
            return stones[0]
        arr = [0]*1001
        for i in range(len(stones)):
            arr[stones[i]] += 1   
        j = 1000
        while(j>=0):
            arr[j] %= 2
            if arr[j]==0:
                j -= 1
                continue
            else:
                j_next = j-1
                while(j_next>=0 and arr[j_next]==0):
                    j_next -= 1
                if j_next<0:
                    break
                else:
                    arr[j-j_next] += 1
                    arr[j_next] -= 1
                    j -= 1
        if j<0:
            return 0
        else:
            return j 

方法二：二分排序
from bisect import insort_left
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            r = stones.pop() - stones.pop()
            if r: insort_left(stones, r)
        return stones[0] if stones else 0

方法三：列表
class Solution:
    def lastStoneWeight(self, st: List[int]) -> int:
        while len(st) > 1:
            y = max(st)
            st.remove(y)
            x = max(st)
            st.remove(x)
            if x < y:
                st.append(y - x)
        if len(st) == 0:
            return 0
        else:
            return st[0]
方法四：堆
from heapq import heapify, heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i];
        heapify(stones)
        while len(stones) > 0:
            y = heappop(stones)
            if len(stones) == 0:
                return -y
            x = heappop(stones)
            if x != y:
                heappush(stones, y-x)
        return 0