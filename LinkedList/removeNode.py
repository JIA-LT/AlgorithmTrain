class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
values=[1,2,3,4,5,6,7,8,9,4]
targetValue = 4
head = ListNode(values[0])
dummyHeader = ListNode(0,next=head)
current = head
for i in range(1, len(values)):
    current.next = ListNode(values[i])
    current = current.next
cur = dummyHeader
while cur.next is not None:
    if cur.next.val == targetValue:
        cur.next = cur.next.next
    else:
        cur = cur.next
show = head
while show:
    print(show.val)
    show = show.next


