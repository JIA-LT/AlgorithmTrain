from collections import defaultdict
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic = defaultdict(int)
        tdic = defaultdict(int)
        for ch in s:
            sdic[ch] += 1
        for ch in t:
            tdic[ch] += 1
        return sdic == tdic

    def isAnagram_array(self, s: str, t: str) -> bool:
        arr = [0]*26
        for ch in s:
            arr[ord(ch) - ord('a')] += 1
        for ch in t:
            arr[ord(ch) - ord('a')] -= 1
        if any(arr):
            return False
        return True

    def isAnagram_Count(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        return s_counter == t_counter

if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram_Count('abcdnth', 'cbdanth'))
    print(s.isAnagram('abcdnth', 'cbdanth'))
    print(s.isAnagram_array('abcd', 'abcde'))
