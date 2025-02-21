from palindrome import Solution
import unittest


class TestSolution(unittest.TestCase):
    def test_if_palindrome(self):
        str1 = Solution("race car")
        str2 = Solution("how did this happen")
        str3 = Solution("mom")
        self.assertTrue(str1.is_palindrome())
        self.assertFalse(str2.is_palindrome())
        self.assertTrue(str3.is_palindrome())


if __name__ == "__main__":
    unittest.main()
