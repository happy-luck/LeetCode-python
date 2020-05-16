class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_ = 0
        for trip in trips:
            max_ = max(trip[2],max_)
        line = [0]*max_
        for trip in trips:
            for i in range(trip[1],trip[2]):
                line[i] += trip[0]
        for l in line:
            if l>capacity:
                return False
        return True 

方法二：（更快）       
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        travel = []
        for i in trips:
            travel.append([i[1], i[0]])
            travel.append([i[2], -i[0]])
        travel.sort(key = lambda x:(x[0], x[1])) #注意先下后上
        people_in_car = 0
        for i in travel:
            people_in_car += i[1]
            if people_in_car > capacity: return False
        return True        