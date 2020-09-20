class Vertex(object):
    def __init__(self):
        self.degree = 0

class Graph(object):
    def WUG(self):
        self._count_vertex = 0
        self._count_edge = 0
        self._adjacencylist = []
        self._vertex_list = []
        self._edge_list = []
        self._vertex_hashtable = {}
        self._edge_hashtable = {}


    def vertexCount(self):
        return self._count_vertex


    def edgeCount(self):
        return self._count_edge


    def getVertices(self):
        vertices = []
        for v in self._vertex_list:
            vertices.append(v)
        return vertices


    def addVertex(self, vertex):
        self._count_vertex += 1
        self._vertex_list.append(vertex)
        self._adjacencylist.append([])
        self._vertex_hashtable[vertex] = []


    def removeVertex(self, vertex):
        self._count_edge = self._count_edge - vertex.degree
        self._count_vertex -= 1
        index1 = self._vertex_list.index(vertex)
        neighbors = self._vertex_hashtable[vertex]
        for e in neighbors:
            index2 = self._vertex_list.index(e)
            self._vertex_hashtable[e].remove(vertex)
            if self._edge_hashtable.get((vertex, e), "not") != "not":
                weight = self._edge_hashtable[(vertex, e)]
                del self._edge_hashtable[(vertex, e)]
                self._edge_list.remove((vertex, e))
                self._adjacencylist[index2].remove((vertex, weight))
            else:
                weight = self._edge_hashtable[(e, vertex)]
                del self._edge_hashtable[(e, vertex)]
                self._edge_list.remove((e, vertex))
                self._adjacencylist[index2].remove((vertex, weight))

        self._adjacencylist.remove(self._adjacencylist[index1])
        self._vertex_list.remove(vertex)
        del self._vertex_hashtable[vertex]


    def isVertex(self, vertex):
        if self._vertex_hashtable.get(vertex, "not") == "not":
            return False
        else:
            return True


    def degree(self, vertex):
        return vertex.degree


    def getNeighbors(self, vertex):
        neighbors = []
        for n in self._vertex_hashtable[vertex]:
            neighbors.append(n)
        return neighbors


    def addEdge(self, vertex1, vertex2, weight):
        vertex1.degree += 1
        vertex2.degree += 1
        self._count_edge += 1
        index1 = self._vertex_list.index(vertex1)
        index2 = self._vertex_list.index(vertex2)
        self._adjacencylist[index1].append((vertex2, weight))
        self._adjacencylist[index2].append((vertex1, weight))
        self._edge_list.append((vertex1, vertex2))
        self._vertex_hashtable[vertex1].append(vertex2)
        self._vertex_hashtable[vertex2].append(vertex1)
        self._edge_hashtable[(vertex1, vertex2)] = weight


    def removeEdge(self, vertex1, vertex2):
        vertex1.degree -= 1
        vertex2.degree -= 1
        self._count_edge -= 1
        if self._edge_hashtable.get((vertex1, vertex2), "not") != "not":
            self._edge_list.remove((vertex1, vertex2))
            weight = self._edge_hashtable[(vertex1, vertex2)]
            del self._edge_hashtable[(vertex1, vertex2)]
        elif self._edge_hashtable.get((vertex2, vertex1), "not") != "not":
            self._edge_list.remove((vertex2, vertex1))
            weight = self._edge_hashtable[(vertex2, vertex1)]
            del self._edge_hashtable[(vertex2, vertex1)]
        index1 = self._vertex_list.index(vertex1)
        index2 = self._vertex_list.index(vertex2)
        self._adjacencylist[index2].remove((vertex1, weight))
        self._adjacencylist[index1].remove((vertex2, weight))


    def isEdge(self, vertex1, vertex2):
        if self._edge_hashtable.get((vertex1, vertex2), "not") != "not" or self._edge_hashtable.get((vertex2, vertex1), "not") != "not" :
            return True
        else:
            return False


    def weight(self, vertex1, vertex2):
        if self._edge_hashtable.get((vertex1, vertex2), "not") != "not":
            return self._edge_hashtable[(vertex1, vertex2)]
        elif self._edge_hashtable.get((vertex2, vertex1), "not") != "not":
            return self._edge_hashtable[(vertex2, vertex1)]
        else:
            return "The edge is not in the graph."

    def minSpanTree(self):
        edge_list = [[0 for col in range(3)] for row in range(2 * self.vertexCount() ** 2)]
        t = 0
        for i in range(self.vertexCount()):
            for j in range(self.vertexCount()):
                if i != j:
                    if self.isEdge(v[i + 1], v[j + 1]):
                        edge_list[t][0] = i + 1
                        edge_list[t][1] = j + 1
                        edge_list[t][2] = self.weight(v[i + 1], v[j + 1])
                        t += 1
        while True:
            if edge_list[-1][2] == 0:
                edge_list.pop()
            else:
                break
        r = []
        for n in range(len(edge_list)):
            for m in range(len(edge_list)):
                if m != n:
                    if (m - n) * (edge_list[m][2] - edge_list[n][2]) < 0:
                        r = edge_list[m]
                        edge_list[m] = edge_list[n]
                        edge_list[n] = r
        edge_list2 = [[0 for col in range(3)] for row in range(2 * self.vertexCount() ** 2)]
        t = 0

        list = [[z + 1] for z in range(g.vertexCount())]
        for k in range(len(edge_list)):
            count = 0
            for j in range(self.vertexCount()):
                if not ((edge_list[k][1] in list[j]) and (edge_list[k][0] in list[j])):
                    count += 1
                    if count == self.vertexCount():
                        edge_list2[t] = edge_list[k]
                        for b in range(self.vertexCount()):
                            if edge_list[k][0] in list[b]:
                                list[b].append(edge_list[k][1])
                            if edge_list[k][1] in list[b]:
                                list[b].append(edge_list[k][0])
                        t += 1

        while True:
            if edge_list2[-1][2] == 0:
                edge_list2.pop()
            else:
                break
        if len(edge_list2) != self.vertexCount() - 1:
            print("There are no spanning tree")
        else:
            print("I change graph as minimun spanning tree using Kruskal's Algorithm\n")
            for i in range(self.vertexCount()):
                for j in range(self.vertexCount()):
                    if self.isEdge(v[i], v[j]):
                        self.removeEdge(v[i], v[j])
            for i in range(len(edge_list2)):
                self.addEdge(v[edge_list2[i][0]], v[edge_list2[i][1]], v[edge_list2[i][2]])
                print("vertex V[" + str(edge_list2[i][0]) + "] and V[" + str(
                    edge_list2[i][1]) + "] are connected and value of edge is " + str(edge_list2[i][2]) + "\n")

v = [0 for col in range(7)]
v[1] = Vertex()
v[2] = Vertex()
v[3] = Vertex()
v[4] = Vertex()
v[5] = Vertex()
v[6] = Vertex()

g = Graph()
g.WUG()
g.addVertex(v[1])
g.addVertex(v[2])
g.addVertex(v[3])
g.addVertex(v[4])
g.addVertex(v[5])
g.addVertex(v[6])
g.addEdge(v[1], v[2], 5)
g.addEdge(v[2], v[3], 4)
g.addEdge(v[2], v[5], 2)
g.addEdge(v[6], v[3], 3)
g.addEdge(v[5], v[4], 4)
g.addEdge(v[1], v[3], 1)
g.addEdge(v[1], v[6], 1)

g.minSpanTree()