class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.helper)==0 or x<self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])
    def pop(self) -> None:
        if self.data:
            self.helper.pop()
        return self.data.pop()
    def top(self) -> int:
        if self.data:
            return self.data[-1]
    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]
时间复杂度：O(1)，“出栈”、“入栈”、“查看栈顶元素”的操作不论数据规模多大，都只是有限个步骤，因此时间复杂度是：O(1)。
空间复杂度：O(N)，这里 N 是读出的数据的个数。            