import unittest
import json

import solution

s = solution.Solution()

class TestSolution(unittest.TestCase):
    def test_longestSquareStreak(self):
        # Example 1
        nums = [4,3,6,16,8,2]

        self.assertEqual(
            s.longestSquareStreak(nums),
            3
        )

        # Example 2
        nums = [2,3,5,6,7]

        self.assertEqual(
            s.longestSquareStreak(nums),
            -1
        )

        # Additional test cases
        nums = [1,3,5,7,9,11,13]

        self.assertNotEqual(
            s.longestSquareStreak(nums),
            -1
        )

        nums = [1,3,5,7,11,13]

        self.assertEqual(
            s.longestSquareStreak(nums),
            -1
        )

        nums = [81,3,9,8,16,-32,-64]

        self.assertEqual(
            s.longestSquareStreak(nums),
            3
        )

        with open('large_test.json', mode='r', encoding='utf-8') as f:
            nums = json.loads(f.read())

            self.assertEqual(
                s.longestSquareStreak(nums),
                2
            )


if __name__ == '__main__':
    unittest.main()
