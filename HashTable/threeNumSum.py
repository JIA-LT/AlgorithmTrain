from typing import List


class Solution:
    def threeSumDict(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            if nums[i] == nums[i-1]:
                continue
            dict = {}
            for j in range(i,len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                target = 0 - nums[i] - nums[j]
                if target in dict:
                    res.append([nums[i],nums[j],target])
                    dict.pop(target)
                else:
                    dict[nums[j]] = j
        return res
    def twoSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] >0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                right -=1
                left += 1
        return res


if __name__ == "__main__":
    nums = [-1,0,1,1,1,1,2,-1,-4]
    solution = Solution()
    res = solution.threeSumDict(nums)
    print(res)
    res2 = solution.twoSum(nums)
    print(res2)