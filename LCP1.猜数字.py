class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        res = 0
        for i,j in zip(guess,answer):
            if i==j:
                res += 1
        return res