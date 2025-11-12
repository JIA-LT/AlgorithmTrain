from typing import List


class solution:
    def reverseString(self, strs: List[str]) -> None:
        left, right = 0, len(strs) - 1
        while left < right:
            strs[left], strs[right] = strs[right], strs[left]
            left += 1
            right -= 1
if __name__ == "__main__":
    s = solution()
    target =["h","e","l","l","o"]
    s.reverseString(target)
    print(target)