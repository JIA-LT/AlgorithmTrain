from typing import List


class Solution:
    def reverse(self, strs: List[str]) -> list[str]:
        left, right = 0, len(strs) - 1
        while left < right:
            strs[left], strs[right] = strs[right], strs[left]
            left += 1
            right -= 1
        return strs
    def reverseString(self, s: str,k:int) -> str:
        res = list(s)
        so = Solution()
        for cur in range(0, len(s), 2* k):
            res[cur:cur + k] = so.reverse(res[cur:cur + k])

        return ''.join(res)
if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    solution = Solution()
    res = solution.reverseString(s, k)
    print(res)