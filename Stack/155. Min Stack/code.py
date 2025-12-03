class MinStack:

    def __init__(self):
        self.arr = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.arr.append(val)

        if not self.minStack: # If minStack is empty, just append the value
            self.minStack.append(val)
        else:
            # If not, append the minimum between the new value and the current minimum
            # So that the top of minStack always has the minimum value
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        # Pop from both stacks to keep them in sync
        self.arr.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minStack[-1] # Returns the top of the minStack


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()