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
if len(connect) ==1:
    connected = True
else:
    connected = False
    print("The graph is not connected.")

# Make a breadth first spanning tree.
if connected:
    visited = [0 for i in range(int(num))]
    list = []  # adjacency list
    for i in range(int(num)):
        a = []
        for j in range(int(num)):
            if matrix[i][j] == 1:
                a.append(j)
        list.append(a)

    queue = [0]
    queue2 = []
    while len(queue) != 0:
        for i in range(len(list[queue[0]])):
            if (visited[list[queue[0]][i]] == 0):
                if list[queue[0]][i] in queue:
                    pass
                else:
                    queue.append(list[queue[0]][i])
                    queue2.append((queue[0], list[queue[0]][i]))
        visited[queue[0]] = 1
        queue.pop(0)

    tree_matrix = [[0 for i in range(int(num))] for j in range(int(num))]
    for i in range(len(queue2)):
        tree_matrix[queue2[i][0]][queue2[i][1]] = 1
        tree_matrix[queue2[i][1]][queue2[i][0]] = 1

    print("The adjacency matrix for breadth first spanning tree is")
    for i in range(len(tree_matrix)):
        print(tree_matrix[i])
