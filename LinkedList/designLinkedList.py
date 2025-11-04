
"""
get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
"""
from LinkedList.ListNode import ListNode


# by single linkedlist
class MyLinkedListS:
    def __init__(self):
        self.dummyHead = ListNode()
        self.size = 0
    def get(self,index:int)-> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            current = self.dummyHead
            while index > 0:
                current = current.next
                index -= 1
        return current.val

    def add_at_head(self,val:int)-> None:
        self.dummyHead.next = ListNode(val,self.dummyHead.next)
        self.size += 1

    def add_at_tail(self,val:int)-> None:
        cur = self.dummyHead
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(val)
        self.size += 1


    def add_at_index(self,index:int,val)-> None:
        if index < 0 or index > self.size:
            return
        else:
            current = self.dummyHead
            while index > 0:
                current = current.next
            current.next = ListNode(val,current.next)
        self.size += 1


    def delete_at_index(self,index:int)-> None:
        if index < 0 or index >= self.size:
            return
        else:
            cur = self.dummyHead
            while index > 0:
                cur = cur.next
            cur.next = cur.next.next
        self.size -= 1

obj = MyLinkedListS()
for i in range(11):
    print(i)
    obj.add_at_tail(i)
print(obj.size)
for j in range(1,obj.size):
    print(j,end=" ")
    print(obj.get(j))