"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
nums = [2, 7, 11, 15]
"""
from typing import List


class Solution:
    def twoNumsSum(self, nums: List[int],target:int) -> List[int]:
        record = dict()

        for i,v in enumerate(nums):
            if target - v in record:
                return [record[target-v],i]
            else:
                record[v] = i
        return []

if __name__ == '__main__':
    nums = [2,11,15,7]
    target = 9
    print(Solution().twoNumsSum(nums,target))