class Solution:
    def fourSum(self,nums1,nums2,nums3,nums4):
        hashMap = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hashMap:
                    hashMap[n1 + n2] += 1
                else:
                    hashMap[n1 + n2] = 1
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = -n3 - n4
                if key in hashMap:
                    count += hashMap[key]
        return count
if __name__ == '__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(Solution().fourSum(A,B,C,D))