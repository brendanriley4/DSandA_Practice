import unittest

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class TestMinStack(unittest.TestCase):
    def test_min_stack(self):
        min_stack = MinStack()

        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        self.assertEqual(min_stack.getMin(), -3)  # Min is -3

        # Test popping elements
        min_stack.pop()
        self.assertEqual(min_stack.getMin(), -2)  # Min is now -2

        # Test top operation
        self.assertEqual(min_stack.top(), 0)  # Top is 0

        # Test further popping
        min_stack.pop()
        self.assertEqual(min_stack.getMin(), -2)  # Min is still -2

        # Test edge case with empty stack
        min_stack.pop()
        self.assertIsNone(min_stack.top())  # Top should be None
        self.assertIsNone(min_stack.getMin())  # Min should be None

if __name__ == '__main__':
    unittest.main()