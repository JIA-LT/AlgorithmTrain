from LinkedList.ListNode import ListNode, build_linked_list

"""
interSectVal=8
listA=[4,1,8,4,5]
listB=[5,0,1,8,4,5]
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        lenA, lenB = 0, 0
        cur = headA
        while cur:
            cur = cur.next
            lenA += 1
        cur = headB
        while cur:
            cur = cur.next
            lenB += 1
        curA, curB = headA, headB
        if lenA > lenB:
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA
        for _ in range(lenB - lenA):
            curB = curB.next
        while curA:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None
if __name__ == "__main__":
    # 公共部分：8 -> 4 -> 5
    common_vals = [8, 4, 5]
    common_head = build_linked_list(common_vals)

    # 链表A前缀：4 -> 1
    listA_prefix = build_linked_list([4, 1])

    # 链表B前缀：5 -> 0 -> 1
    listB_prefix = build_linked_list([5, 0, 1])

    # 将前缀的尾部连接到公共部分
    tailA = listA_prefix
    headA = listA_prefix
    while tailA.next:
        tailA = tailA.next
    tailA.next = common_head

    tailB = listB_prefix
    headB = listB_prefix
    while tailB.next:
        tailB = tailB.next
    tailB.next = common_head
    solution = Solution()
    print(solution.getIntersectionNode(headA, headB).val)