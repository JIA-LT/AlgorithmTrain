class MyQueue:
    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]
    def push(self,x:int):
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self)->int:
        ans = self.pop()
        self.stack_out.append(ans)
        return ans


    def empty(self):
        return not (self.stack_in or self.stack_out)

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9]
    my_queue = MyQueue()
    for num in nums:
        my_queue.push(num)
    print(my_queue.peek())
    print(my_queue.pop())
    print(my_queue.peek())