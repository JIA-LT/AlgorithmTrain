from collections import deque
from typing import List


class MyQueue:
    def __init__(self):
        self.queue = deque()
    def pop(self,value):
        if self.queue and self.queue[0] == value:
            return self.queue.popleft()

    def push(self,value):
        while self.queue and self.queue[-1] < value:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]

class solution:
    def maxSlidingWindow(self, num: List[int], k: int) -> List[int]:
        queue = MyQueue()
        result = []
        for i in range(k):
            queue.push(num[i])
        result.append(queue.front())
        for i in range(k, len(num)):
            queue.pop(num[i - k])
            queue.push(num[i])
            result.append(queue.front())
        return result
if __name__ == "__main__":
    s = [1,3,-1,-3,5,3,6,7]
    print(solution().maxSlidingWindow(s, 3))


