class BinaryTree(object):
    def __init__(self):
        # Get input for arithmetic expression
        self.expression = input("Enter arithmetic expression \n")

        # Change string to list
        self.exp_list=[]
        substring=''
        for i in range(len(self.expression)):
            if self.expression[i] >= '0' and self.expression[i] <= '9':
                if self.expression[i+1] >= '0' and self.expression[i] <= '9':
                    substring += self.expression[i]
                else:
                    substring += self.expression[i]
                    self.exp_list.append(int(substring))
                    substring=''
            else:
                self.exp_list.append(self.expression[i])

        # Find out the level of binary tree
        count=0
        self.level=0
        for i in range(len(self.exp_list)):
            if self.exp_list[i] == '(':
                count += 1
                self.level = max(self.level, count)
            if self.exp_list[i] == ')':
                count -= 1

        # Make binary tree using list
        self.tree = [[] for i in range(self.level+1)]
        current_level = 0
        for i in range(len(self.exp_list)):
            if self.exp_list[i] == '(':
                current_level += 1
            elif self.exp_list[i] == ')':
                current_level -=1
            elif type(self.exp_list[i]) == int:
                if current_level != self.level:
                    self.repeat = 2
                    for k in range(current_level+1, self.level+1):
                        for r in range(self.repeat):
                            self.tree[k].append(None)
                        self.repeat = self.repeat * 2
                self.tree[current_level].append(self.exp_list[i])
                current_level -= 1
            else:
                self.tree[current_level].append(self.exp_list[i])
                current_level +=1
    def Evaluate(self):
        for i in range(self.level, -1, -1):
            j = 0
            while j < 2**i:
                if self.tree[i][j] == None:
                    j += 2
                else:
                    if self.tree[i-1][j//2] == '+':
                        self.tree[i-1][j//2] = self.tree[i][j] + self.tree[i][j+1]
                    elif self.tree[i-1][j//2] == "-":
                        self.tree[i-1][j//2] = self.tree[i][j] - self.tree[i][j+1]
                    elif self.tree[i-1][j//2] == "*":
                        self.tree[i-1][j//2] = self.tree[i][j] * self.tree[i][j+1]
                    elif self.tree[i-1][j//2] == "/":
                        if self.tree[i][j+1] == 0:
                            return "Report: There is division by zero."
                        self.tree[i-1][j//2] = self.tree[i][j] / self.tree[i][j+1]
                    j += 2
        return self.tree[0][0]


bt = BinaryTree()
print(bt.Evaluate())



