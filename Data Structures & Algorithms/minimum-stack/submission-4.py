from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.stack_min = deque()

    def push(self, val: int) -> None:
        if self.stack_min:
            self.stack_min.append(min(val,self.stack_min[-1]))
        else:
            self.stack_min.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.stack_min.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack_min:
            return self.stack_min[-1]
