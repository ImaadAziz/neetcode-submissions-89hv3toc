class MinStack:

    def __init__(self):
        self.mins = []
        self.stack = []


    def push(self, val: int) -> None:
        if len(self.mins) == 0:
            self.mins.append(val)
        elif val < self.mins[-1]:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])
        self.stack.append(val)
        

    def pop(self) -> None:
        self.mins.pop()
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
