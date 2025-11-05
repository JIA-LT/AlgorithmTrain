def build_linked_list(values):
    """用 for 循环根据列表创建链表"""
    head = None
    prev = None
    for val in values:
        node = ListNode(val)
        if not head:
            head = node
        else:
            prev.next = node
        prev = node
    return head


class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

