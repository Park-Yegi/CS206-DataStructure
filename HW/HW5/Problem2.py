class BinarySearchTree(object):
    def __init__(self):
        file = input("Enter file name : ")

        # Change file to list
        f=open(file, 'r')
        lines = f.readlines()
        for i in range(len(lines)):
            if lines[i][-1] == "\n":
                lines[i] = lines[i][:-1]

        # make binary search tree
        self.tree = []
        for i in range(len(lines)):
            self.tree.append([None for j in range(2**i)])
        for i in range(len(lines)):
            current = [0, 0]
            if i == 0:
                self.tree[current[0]][current[1]] = lines[i]
            else:
                for j in range(len(self.tree)):
                    if self.tree[current[0]][current[1]] == None:
                        self.tree[current[0]][current[1]] = lines[i]
                        break
                    if lines[i] < self.tree[current[0]][current[1]]:
                        current[0] += 1
                        current[1] = 2*current[1]
                    elif lines[i] > self.tree[current[0]][current[1]]:
                        current[0] += 1
                        current[1] = 2*current[1] +1

    # Print the tree in breadth first order
    def breadth_first_order(self):
        for i in range(len(self.tree)):
            string = ""
            for j in range(len(self.tree[i])):
                if self.tree[i][j] != None:
                    string += self.tree[i][j]
                    string += " "
            if len(string) != 0:
                print(string)

# main
bst = BinarySearchTree()
bst.breadth_first_order()
