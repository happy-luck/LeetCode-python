方法一：
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5:0,10:0}
        for i in bills:
            if i==5:
               dic[5] = dic.get(5,0) + 1
            elif i==10:
                dic[10] = dic.get(10,0) + 1
                dic[5] = dic.get(5,0) - 1
                if dic[5]<0:
                    return False
            else:
                if dic[10]>0:
                    dic[5] = dic.get(5,0) - 1
                    dic[10] = dic.get(10,0) - 1
                else:
                    dic[5] = dic.get(5,0) - 3
                if dic[5]<0 or dic[10]<0:
                    return False
        return True


方法二：
class Solution(object): #aw
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True        