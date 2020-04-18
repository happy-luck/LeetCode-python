方法一：
class Solution:
    def gardenNoAdj(self, N: int, paths):
        color=[1]*N
        graph=[[] for i in range(N)]
        print(graph)
        for path in paths:
            if path[0]>path[1]:
                graph[path[0]-1].append(path[1]-1)
            else:
                graph[path[1]-1].append(path[0]-1)
            print(graph)
        for i in range(1,N):
            flower=[1,2,3,4]
            for node in graph[i]:
                if color[node] in flower:
                    flower.remove(color[node])
            color[i]=flower[0]
        return color
方法二：
class Solution:
    def gardenNoAdj(self, N: int, paths):
        from collections import defaultdict
        color=[1]*N
        graph=defaultdict(list)
        for path in paths:
            if path[0]>path[1]:
                graph[path[0]-1].append(path[1]-1)
            else:
                graph[path[1]-1].append(path[0]-1)
        graph=sorted(graph.items())
        print(graph)
        for i,n in graph:
            flower=[1,2,3,4]
            for node in n:
                if color[node] in flower:
                    flower.remove(color[node])
            color[i]=flower[0]
        return color
