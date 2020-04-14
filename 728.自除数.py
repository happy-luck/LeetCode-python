class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        if left == 0:
            left += 1
        for i in range(left,right+1):
            tar = True
            t = i
            while(t):
                tmp = t%10
                if tmp==0 or i%tmp != 0:
                    tar = False
                    break
                else:
                    t //= 10
            if tar:
                res.append(i)
        return res