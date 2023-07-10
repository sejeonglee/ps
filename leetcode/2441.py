"""
https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
"""
from typing import List, Dict, Optional


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        waiting_pair: Dict[int, int] = {}
        max_k: int = -1
        for num in nums:
            if num in waiting_pair:
                max_k = max(max_k, abs(num))
            else:
                waiting_pair[-num] = num
        return max_k


def main() -> None:
    sol = Solution()

    # Example Input
    nums: List[int] = [-10, 8, 6, 7, -2, -3]

    result: int = sol.findMaxK(nums)

    # Example Output
    print(f"{result}")


main()
