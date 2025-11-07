"""
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
"""

class Solution:
    def sortedSquares(self, nums):
        left, right, i = 0, len(nums) - 1,len(nums) - 1
        result = [float('inf')] * len(nums)
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                result[i] = nums[right]**2
                right -= 1
            else:
                result[i] = nums[left] ** 2
                left += 1
            print(result[i])
            i -= 1
        return result
if __name__ == "__main__":
    nums = [-4,-1,0,3,10]
    print(Solution().sortedSquares(nums))