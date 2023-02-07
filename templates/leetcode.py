from typing import List


class Solution:
    def problemName(self, nums: List[int], target: int) -> List[int]:
        return [1, 2]


def main() -> None:
    s = Solution()

    # Example Input
    nums: List[int] = [2, 7, 11, 15]
    target: int = 9

    result: List[int] = s.problemName(nums, target)

    # Example Output
    print(f"[{result[0]}, {result[1]}]")


main()
