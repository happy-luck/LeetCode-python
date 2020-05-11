方法一：
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = {}
        for p in paths:
            dic[p[0]] = p[1]
        k = paths[0][0]
        while k:
            v = k
            k = dic.get(k,0)
        return v

方法二：
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        allCity = set()
        beginCity = set()
        for path in paths:
            allCity.add(path[0])
            allCity.add(path[1])
            beginCity.add(path[0])
        return (allCity - beginCity).pop()