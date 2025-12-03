from collections import deque


class MyStack(object):
    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def empty(self):
        return len(self.queue_in) == 0

    def push(self, num):
        self.queue_in.append(num)

    def pop(self)->int:

        if self.empty():
            return -1

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())

        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return self.queue_out.popleft()

    def top(self)->int:

        if self.empty():
            return -1

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())

        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        temp = self.queue_out.popleft()
        self.queue_in.append(temp)
        return temp

