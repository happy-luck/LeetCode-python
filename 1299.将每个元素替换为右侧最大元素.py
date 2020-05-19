class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            temp = max_
            max_ = max(max_,arr[i])
            arr[i] = temp
        return arr