class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output

时间复杂度：O(N**2)。排序使用了 O(NlogN) 的时间，每个人插入到输出队列中需要 O(k) 的时间，其中 k 是当前输出队列的元素个数。
空间复杂度：O(N)，输出队列使用的空间。