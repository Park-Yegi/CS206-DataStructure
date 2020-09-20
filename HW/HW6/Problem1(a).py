num = input("Enter the number of nodes: ")

# Make an adjacency matrix.
print("The name of node is 0,1,2,3,... in order.")
matrix = []  # matrix is adjacency matrix
for i in range(int(num)):
    row_input = input("Enter the row of adjacency matrix(0 or 1): ")
    row = []
    for j in range(int(num)):
        row.append(int(row_input[j]))
    matrix.append(row)

# Check the graph is connected or not.
a = []  # a is collection of lists which contain connected nodes of that node.
for x in range(int(num)):
    com = []
    com.append(x+1)
    for y in range(int(num)):
        if matrix[x][y] == 1:
            com.append(y+1)
            com.sort()
    a.append(com)
connect = []
for i in range(len(a)):
    c = 0
    if i == 0:
        connect.append(set(a[i]))
    else:
        for k in range(len(connect)):
            for j in range(len(a[i])):
                if a[i][j] in connect[k]:
                    connect[k].update(a[i])
                    c += 1
                    break
        if c == 0:
            connect.append(set(a[i]))
if len(connect) == 1:
    connected = True
else:
    connected = False
    print("The graph is not connected.")

# Make a depth first spanning tree.
count = 0
if connected:
    visited = [0 for i in range(int(num))]
    list = []  # adjacency list
    for i in range(int(num)):
        a = []
        for j in range(int(num)):
            if matrix[i][j] == 1:
                a.append(j)
        list.append(a)

    stack = [0]
    stack2 = []
    visited[0] = 1
    while 0 in visited:
        for i in list[stack[-1]]:
            if visited[i] == 0:
                stack2.append((stack[-1], i))
                stack.append(i)
                visited[i] = 1
                break
            if i == list[stack[-1]][-1]:
                stack.pop()

    tree_matrix = [[0 for i in range(int(num))] for j in range(int(num))]
    for i in range(len(stack2)):
        tree_matrix[stack2[i][0]][stack2[i][1]] = 1
        tree_matrix[stack2[i][1]][stack2[i][0]] = 1

    print("The adjacency matrix for depth first spanning tree is")
    for i in range(len(tree_matrix)):
        print(tree_matrix[i])