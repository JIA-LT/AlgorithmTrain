from LinkedList.ListNode import ListNode

values = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
head = ListNode(values[0])
current = head
for i in range(1, len(values)):
    current.next = ListNode(values[i])
    current = current.next

def reverse_list(node:ListNode)->ListNode:
    cur = node
    pre = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre
def reverse_list_rec(self, cur_node:ListNode, pre_node)->ListNode:
    if cur_node is None:
        return pre_node
    tmp = cur_node.next
    cur_node.next = pre_node
    return self.reverse_list(cur_node, pre_node)




