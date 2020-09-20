
# Make Stack class
class Stack(object):
    # Create Stack
    def __init__(self, max_stack_size):
        self.stack = []
        self.top = -1
        self.max_stack_size = max_stack_size

    # Function IsFull
    def IsFull(self):
        if self.top >= self.max_stack_size-1:
            return True
        else:
            return False

    # Function IsEmpty
    def IsEmpty(self):
        if self.top < 0:
            return True
        else:
            return False

    # Function Push
    def Push(self, item):
        if self.IsFull():
            return "Stack is full, cannot add element"
        else:
            item_list = [item]
            self.stack += item_list
            self.top += 1
            return self.stack

    # Function Pop
    def Pop(self):
        if self.IsEmpty():
            return "Stack is empty, cannot pop element"
        else:
            pop = self.stack[len(self.stack)-1]
            self.stack = self.stack[:len(self.stack)-1]
            return pop

    # Function Top
    def Top(self):
        if self.IsEmpty():
            return "Stack is empty, don't have top element"
        else:
            return self.stack[len(self.stack)-1]
