# [-9,-2,-1,0,1,4,6,10,17]
# binary search
from typing import List


def binary_search(nums:List[int], target:int)->int:
    left=0
    right= len(nums) - 1
    while left<=right:
        mid = left + (right - left)//2
        if nums[mid]>target:
            right = mid - 1
        elif nums[mid]<target:
            left = mid + 1
        else:
            return mid
    return -1



if __name__ == "__main__":
    nums = [-9,-2,-1,0,1,4,6,10,17]
    target = 4
    print(binary_search(nums, target))