方法一：
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        ch = {}
        for c in chars:
            ch[c] = ch.get(c,0) + 1
        for w in words:
            wc = {}
            target = 1
            for c in w:
                wc[c] = wc.get(c,0) + 1
                if wc[c]>ch.get(c,0):
                    target = 0
                    break
            if target==1:
                ans += len(w)
        return ans

方法二：
显然，对于一个单词 word，只要其中的每个字母的数量都不大于 chars 中对应的字母的数量，
那么就可以用 chars 中的字母拼写出 word。所以我们只需要用一个哈希表存储 chars 中每个字母的数量，
再用一个哈希表存储 word 中每个字母的数量，最后将这两个哈希表的键值对逐一进行比较即可
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        ch = collections.Counter(chars)
        for w in words:
            wc = collections.Counter(w)
            for c in w:
                if wc[c]>ch[c]:
                    break
            else:
                ans += len(w)
        return ans
时间复杂度：O(n)，其中 n 为所有字符串的长度和。我们需要遍历每个字符串，
包括 chars 以及数组 words 中的每个单词。

空间复杂度：O(S)，其中 S 为字符集大小，在本题中 S 的值为 26（所有字符串仅包含小写字母）。
程序运行过程中，最多同时存在两个哈希表，使用的空间均不超过字符集大小S，因此空间复杂度为O(S)

