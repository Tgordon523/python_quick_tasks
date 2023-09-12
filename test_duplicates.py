from duplicates import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_if_duplicates(self):
        list_1 = Solution([4, 3, 2, 1, 5])
        list_2 = Solution([5,4, 3, 2, 1, 5])
        list_3 = Solution([7,4, 3, 2, 1, 5])
        self.assertTrue(list_1.contains_duplicates())
        self.assertFalse(list_2.contains_duplicates())
        self.assertTrue(list_3.contains_duplicates())

if __name__=='__main__':
	unittest.main()