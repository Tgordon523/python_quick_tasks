class Solution:
    ### If len of values are the same, there are no duplicates and it returns true
    def __init__(self, s) -> None:
        self.s = s

    def is_palindrome(self) -> bool:
        # Need to check for space and numerics 
        new_s = [w for w in self.s if w.isalnum()]
        return new_s == new_s[::-1]


word1 = "race car"
word2 = "not correct"
a = Solution(word2).is_palindrome()
print(a)
