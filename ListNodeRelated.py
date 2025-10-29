class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
k = int(input("please input a index"))
values =[1,2,3,4,5,6,7,8,9]
head = ListNode(values[0])
current = head
for i in range(1,len(values)):
    current.next = ListNode(values[i])
    current = current.next
dummyHead = ListNode(0, head)
slow=fast= dummyHead
for i in range(k):
    fast = fast.next
while fast:
    slow = slow.next
    fast = fast.next
print(slow.val)

