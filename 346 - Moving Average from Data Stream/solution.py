from collections import deque
class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque([])
        self.size = size
        self.length = 0
        self.total = 0

    def next(self, val: int) -> float:
        if self.length == self.size:
            self.total -= self.queue.popleft()
            self.length -= 1
        self.total += val
        self.queue.append(val)
        self.length += 1
        return self.total/self.length


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)