方法一：检查位置
具体地，我们用 (rec[0], rec[1]) 表示矩形的左下角，(rec[2], rec[3]) 表示矩形的右上角，与题目描述一致。对于「左侧」，即矩形 rec1 在 x 轴上的最大值不能大于矩形 rec2 在 x 轴上最小值。对于「右侧」、「上方」以及「下方」同理。因此我们可以翻译成如下的代码：
左侧：rec1[2] <= rec2[0]；
右侧：rec1[0] >= rec2[2]；
上方：rec1[1] >= rec2[3]；
下方：rec1[3] <= rec2[1]。
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top
时间复杂度：O(1)。
空间复杂度：O(1)，不需要额外的空间。

方法二：检查区域
矩形 rec1 和 rec2 的水平边投影到 
x 轴上的线段分别为 (rec1[0], rec1[2]) 和 (rec2[0], rec2[2])。
根据数学知识我们可以知道，当 min(rec1[2], rec2[2]) > max(rec1[0], rec2[0]) 时，这两条线段有交集。
对于矩形 rec1 和 rec2 的竖直边投影到 y 轴上的线段，
同理可以得到，当 min(rec1[3], rec2[3]) > max(rec1[1], rec2[1]) 时，这两条线段有交集。

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))

时间复杂度：O(1)。
空间复杂度：O(1)，不需要额外的空间。

方法三：
区间不重叠的条件：e1 <= s2 || e2 <= s1。将条件取反即为区间重叠的条件。

def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    x_overlap = not(rec1[2] <= rec2[0] or rec2[2] <= rec1[0])
    y_overlap = not(rec1[3] <= rec2[1] or rec2[3] <= rec1[1])
    return x_overlap and y_overlap