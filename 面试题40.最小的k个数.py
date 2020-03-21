方法一：
class Solution:
    def sort(seft,arr):
        middle = arr[0]
        left = [x for x in arr[1:] if x <= middle]
        right = [x for x in arr[1:] if x > middle]
        return left,middle,right

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        if k > len(arr) or len(arr)==0:
            return []
        left,middle,right = self.sort(arr)
        m = len(left)
        if m==k:
            return left
        if m==k-1:
            left.append(middle)
            return left
        if m< k-1:
            left.append(middle)
            return left+self.getLeastNumbers(right, k-m-1)
        return self.getLeastNumbers(left, k)
方法二：排序
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]
时间复杂度：O(nlogn)，其中 n 是数组 arr 的长度。算法的时间复杂度即排序的时间复杂度。

空间复杂度：O(logn)，排序所需额外的空间复杂度为 O(logn)。

方法三：堆
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans

时间复杂度：
O(nlogk)，其中 n 是数组 arr 的长度。由于大根堆实时维护前 k 小值，所以插入删除都是 O(logk) 的时间复杂度，
最坏情况下数组里 n 个数都会插入，所以一共需要 O(nlogk) 的时间复杂度。
空间复杂度：O(k)，因为大根堆里最多 k 个数。

方法四：快排
class Solution:
    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def randomized_partition(self, nums, l, r):
        i = random.randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return self.partition(nums, l, r)

    def randomized_selected(self, arr, l, r, k):
        pos = self.randomized_partition(arr, l, r)
        num = pos - l + 1
        if k < num:
            self.randomized_selected(arr, l, pos - 1, k)
        elif k > num:
            self.randomized_selected(arr, pos + 1, r, k - num)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()
        self.randomized_selected(arr, 0, len(arr) - 1, k)
        return arr[:k]
        
时间复杂度：期望为 O(n) ，由于证明过程很繁琐，所以不再这里展开讲。具体证明可以参考《算法导论》第 9 章第 2 小节。
最坏情况下的时间复杂度为 O(n^2)。情况最差时，每次的划分点都是最大值或最小值，一共需要划分 n−1 次，
而一次划分需要线性的时间复杂度，所以最坏情况下时间复杂度为 O(n^2)。

空间复杂度：期望为 O(logn)，递归调用的期望深度为 O(logn)，每层需要的空间为 O(1)，只有常数个变量。
最坏情况下的空间复杂度为 O(n)。最坏情况下需要划分 n 次，即 randomized_selected 函数递归调用最深 
n−1 层，而每层由于需要 O(1) 的空间，所以一共需要 O(n) 的空间复杂度。
