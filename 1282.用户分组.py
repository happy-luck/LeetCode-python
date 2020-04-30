方法一：
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        b=sorted(enumerate(groupSizes), key=lambda x:x[1])
        res = []
        i = 0
        while i<len(groupSizes):
            n = b[i][1]
            ans = []
            while n:
                ans.append(b[i][0])
                n -= 1
                i += 1
            res.append(ans)
        return res

方法二：
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = collections.defaultdict(list)
        for i, _id in enumerate(groupSizes):
            groups[_id].append(i)
        ans = []
        for gsize, users in groups.items():
            for it in range(0, len(users), gsize):
                ans.append(users[it : it + gsize])
        return ans
时间复杂度：O(N)。
空间复杂度：O(N)。               