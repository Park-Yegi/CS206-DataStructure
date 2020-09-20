class BinaryTree(object):
    # Make list for Binary Tree
    # The form is [[A],[B,C],[D,E,F,G],....]
    # If the node is empty, "None" is inserted to the list
    def __init__(self, height):
        self.height = height
        self.tree = []
        for i in range(height):
            level = []
            for j in range(2**i):
                item = input("Enter element of binary tree. \nPress Enter if you want to remain empty. \n")
                if item == "":
                    item = None
                level.append(item)
            self.tree.append(level)
        print(self.tree)

    # Function to print out the pre-order traversal of binary tree in nonrecursive way
    def preorder(self):
        position = 0
        level = 0
        self.current = self.tree[level][position]
        stack = [self.current]
        while True:
            if len(stack) != 0:
                for i in range(len(self.tree)):
                       if stack[-1] in self.tree[i]:
                        level = i
                        position = self.tree[level].index(stack[-1])
                        break
                if stack[-1] != None:
                    print(stack.pop() + " ", end="")
                    if level != self.height-1:
                        stack.append(self.tree[level+1][2*position+1])
                        stack.append(self.tree[level+1][2*position])

                else:
                    stack = stack[:-1]
            else:
                break

    # Function to print out the post-order traversal of binary tree in nonrecursive way
    def postorder(self):
        position = 0
        level = 0
        self.current = self.tree[level][position]
        stack1 = [self.current]
        stack2 = []
        while len(stack1) != 0:
            a = stack1.pop()
            stack2.append(a)
            if level < self.height -1:
                if self.tree[level+1][2*position] != None:
                    stack1.append(self.tree[level+1][2*position])
                if self.tree[level+1][2*position+1] != None:
                    stack1.append(self.tree[level+1][2*position+1])
            if len(stack1) != 0:
                for i in range(len(self.tree)):
                    if stack1[-1] in self.tree[i]:
                        level = i
                        position = self.tree[level].index(stack1[-1])
                        break
        for i in range(len(stack2)-1, -1, -1):
            if stack2[i] != None:
                print(stack2[i]+" ", end="")


height = input("Set the height of the binary tree ")
tree = BinaryTree(int(height))
print("Pre-order traversal is")
tree.preorder()
print("\n")
print("Post-order traversal is")
tree.postorder()
