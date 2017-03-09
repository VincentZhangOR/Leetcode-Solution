# coding=utf-8
class MinStack(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    # @return an integer
    def push(self, x):
        self.stack1.append(x)
        if len(self.stack2) == 0 or x <= self.stack2[-1]:
            self.stack2.append(x)

    # @return nothing
    def pop(self):
        top = self.stack1[-1]
        self.stack1.pop()
        if top == self.stack2[-1]:
            self.stack2.pop()
        
    # @return an integer
    def top(self):
        return self.stack1[-1]

    # @return an integer
    def getMin(self):
        return self.stack2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
