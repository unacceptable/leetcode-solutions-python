#!/usr/bin/env python3
# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,invalid-name
import unittest

import solution

s = solution.Solution()

class TestFindFirstOccurrence(unittest.TestCase):
    # Example 1
    def test_strStr(self):
        self.assertEqual(
            s.strStr("sadbutsad", "sad"),
            0
        )

    # Example 2
    def test_strStr_not_found(self):
        self.assertEqual(
            s.strStr("leetcode", "leeto"),
            -1
        )

    # Additional test cases
    def test_strStr_not_first_index(self):
        self.assertEqual(
            s.strStr("hello", "ll"),
            2
        )


    def test_strStr_mississippi(self):
        self.assertEqual(
            s.strStr("mississippi", "issip"),
            4
        )


    def test_strStr_abaa(self):
        self.assertEqual(
            s.strStr("aabaabbbaabbbbabaaab", "abaa"),
            1
        )

if __name__ == '__main__':
    unittest.main()
