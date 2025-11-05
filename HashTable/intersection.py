"""
349 intersection between two array
nums1 = [1,2,3,1]
nums2 = [2,3,4,5]
"""


def intersect(nums1,nums2):
    table ={}
    for num in nums1:
        table[num] = table.get(num, 0) + 1
    res=set()
    for num in nums2:
        if num in table:
            res.add(num)
            del table[num]
    return res

def intersect_2(nums1,nums2):
    return list(set(nums1) & set(nums2))

if __name__ == '__main__':
    nums1 = [1,2,3,1]
    nums2 = [2,3,4,5]
    print(intersect(nums1,nums2))
    print(intersect_2(nums1,nums2))