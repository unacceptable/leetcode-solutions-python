# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring,invalid-name

from typing import List

import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        checked = []
        streaks = []
        max_num = 10**(5/2)

        streak = 1

        valid_nums = [
            num for num in nums if ( num > 1 and num < max_num )
        ]

        for num in valid_nums:
            if num in checked:
                continue

            while True:
                next_num = num**2

                if next_num > max_num:
                    streaks.append(streak)
                    streak = 1
                    break

                if next_num in nums:
                    logging.info('%s goes to %s', num, num**2)
                    streak += 1

                    checked.append(num)

                    num = num**2
                else:
                    if streak > 1:
                        streaks.append(streak)

                        streak = 1

                    break

            checked.append(num)

        return max(streaks) if streaks else -1


if __name__ == '__main__':
    s = Solution()
    # Example 1
    numbers = [4,3,6,16,8,2]
    logging.info(s.longestSquareStreak(numbers)) # should be 3

    # Example 2
    numbers = [2,3,5,6,7]
    logging.info(s.longestSquareStreak(numbers)) # should be -1
