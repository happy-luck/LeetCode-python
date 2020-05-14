数值一样的位置不用变动，直接先排除掉
然后统计(x, y), (y, x)两种二元组出现的次数
两个(x, y)或者两个(y, x)交换一次可以变成一样的消掉
最后如果(x, y)和(y, x)在两两配对后分别都还剩一个，还需要额外两次交换

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        dif1 = 0
        dif2 = 0
        res =0
        for i in range(len(s1)):
            if s1[i] == "x":
                if s1[i] != s2[i]:
                    dif1 = dif1 + 1
            else:
                if s1[i] != s2[i]:
                    dif2 = dif2 + 1
        if (dif1 + dif2)%2 != 0:
            return -1
        else:
            return dif1%2 + dif2%2 + int(dif1/2) + int(dif2/2)
           