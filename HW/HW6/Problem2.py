num = input("Enter the number of nodes: ")

print("The name of node is 0,1,2,3,... in order.")
matrix = []  # matrix is adjacency matrix
for i in range(int(num)):
    row_input = input("Enter the row of adjacency matrix(0 or 1): ")
    row = []
    for j in range(int(num)):
        row.append(int(row_input[j]))
    matrix.append(row)

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
print("\nAll connected components of the graph is")
print(connect)
