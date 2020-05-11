class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        l_s1 = list(s1)
        l_s1.sort()
        l_s2 = list(s2)
        l_s2.sort()
        t_less = True
        t_more = True
        for i in range(len(l_s2)):
            if l_s1[i] < l_s2[i]:
                t_more = False
                break
        for i in range(len(l_s2)):
            if l_s1[i] > l_s2[i]:
                t_less = False
                break
        return t_less or t_more