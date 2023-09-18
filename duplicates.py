class Solution:
    ### If len of values are the same, there are no duplicates and it returns true
    def __init__(self, nums) -> None:
        self.nums = nums

    def contains_duplicates(self) -> bool:
        result = len(self.nums) == len(set(self.nums))
        return result


list1 = [5, 6, 1, 2, 4, 5]
a = Solution(list1).contains_duplicates()
print(a)
