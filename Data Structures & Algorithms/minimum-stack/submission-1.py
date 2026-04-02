class MinStack:

    def __init__(self):
        self.min_stack = []
        self.min_items = []

    def push(self, val: int) -> None:
        minitem = min(self.min_items[-1], val) if self.min_items else val
        self.min_stack.append(val)
        self.min_items.append(minitem)

    def pop(self) -> None:
        self.min_stack.pop()
        self.min_items.pop()

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.min_items[-1]
