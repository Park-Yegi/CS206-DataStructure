import time

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

infix = input("Input a fully parenthesized infix form : ")
start_time = time.time()

Number = Stack(100)       # Stack for Numbers
Operation = Stack(100)    # Stack for Operations
for i in range(len(infix)):
    element = infix[i]
    if "0" <= element <= "9":
        if "0" <= infix[i-1] <= "9":
            before_element = str(Number.Pop())
            element = int(before_element + str(element))
        else:
            pass
        Number.Push(element)
    elif element == "(":
        pass
    elif element == ")":
        second_num = int(Number.Pop())
        first_num = int(Number.Pop())
        operation = Operation.Pop()
        if operation == "+":
            Number.Push(first_num + second_num)
        elif operation == "-":
            Number.Push(first_num - second_num)
        elif operation == "*":
            Number.Push(first_num * second_num)
        elif operation == "/":
            if second_num == 0:
                print("This expression cannot be evaluated. \nDivisor cannot be zero.")
                break
            else:
                result = first_num // second_num
                Number.Push(result)
        else:
            pass
    else:
        Operation.Push(element)

    if i == len(infix)-1:
        print("The result of evaluation is " + str(Number.Top()))

    else:
        pass

end_time = time.time()
elapsed_time = end_time - start_time
print("The time elapsed to execute this code is", elapsed_time, 'seconds.')
