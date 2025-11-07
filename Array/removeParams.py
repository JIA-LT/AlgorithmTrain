# array val remove all params equal to val return new length
from typing import List


class Solution:
    def removeParams(self, nums: List[int], target: int) -> int:
        slow, fast = 0,0
        while fast < len(nums):
            if nums[fast] != target:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9,10]

    target = 2
    solution = Solution()
    print(solution.removeParams(nums, target))