from collections import defaultdict


class Solution:
    def canConstruct(self, nums1: str, nums2: str) -> bool:
        record1 = [0] * 26
        record2 = [0] * 26
        for num in nums1:
            record1[ord(num) - ord('a')] += 1
        for num in nums2:
            record2[ord(num) - ord('a')] += 1
        return all(record1[i] <= record2[i] for i in range(26))

    def canCons(self,nums1:str,nums2:str)->bool:
        hashmap = defaultdict(int)
        for num in nums2:
            hashmap[num] += 1
        for num in nums1:
            value = hashmap.get(num)
            if not value:
                return False
            else:
                hashmap[num] -= 1
        return True

if __name__ == '__main__':
    nums1 = "acdng"
    nums2 = "acngdef"
    print(Solution().canConstruct(nums1,nums2))
    print(Solution().canCons(nums1,nums2))
