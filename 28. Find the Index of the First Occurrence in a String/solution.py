#!/usr/bin/env python3
# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,invalid-name
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        for index, _ in enumerate(haystack):
            substring = haystack[index:]

            if substring.startswith(needle):
                return index

        # or
        #
        # return haystack.index(needle)


if __name__ == '__main__':
    solution = Solution()
    logging.info(solution.strStr("sadbutsad", "sad"))  # 0
    logging.info(solution.strStr("leetcode", "leeto")) # -1
