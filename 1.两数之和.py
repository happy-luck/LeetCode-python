方法一：
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,num in enumerate(nums):
            if target-num in d:
                return [d[target-num],i]
            d[num] = i
时间复杂度：O(n)，我们只遍历了包含有 n 个元素的列表一次。
在表中进行的每次查找只花费 O(1) 的时间。

空间复杂度：O(n)，所需的额外空间取决于哈希表中存储的元素数量，该表最多需要存储 n 个元素。

           
方法二：
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
	    hashmap={}
	    for ind,num in enumerate(nums):
	        hashmap[num] = ind
	    for i,num in enumerate(nums):
	        j = hashmap.get(target - num)
	        if j is not None and i!=j:
	            return [i,j]          

时间复杂度：O(n)，我们把包含有 n 个元素的列表遍历两次。
由于哈希表将查找时间缩短到 O(1) ，所以时间复杂度为 O(n)。

空间复杂度：O(n)，所需的额外空间取决于哈希表中存储的元素数量，该表中存储了 n 个元素。	            