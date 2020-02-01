class Graph:

    def __init__(self):
        self.vertices = {}

    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.label not in self.vertices:
            self.vertices[vertex.label] = vertex
            return True
        else:
            return False

    def addEdge(self, ver, adj):
        if ver in self.vertices and adj in self.vertices:
            self.vertices[ver].addAdj(adj)
            self.vertices[adj].addAdj(ver)
            return True
        else:
            return False

    def DFS(self):
        # We need to loop each vertex to make sure that we visited all vertices
        visitedList = [] # this list will save the DFS solution
        for i in self.vertices:
            if not self.vertices[i].wasVisited:
                visitedList = visitedList + self.applyDFS(self.vertices[i], [])
        return visitedList

    def applyDFS(self, source, visitedList):
        visitedList.append(source.label)
        source.wasVisited = True
        for adjacent in source.adjacence:
            if not self.vertices[adjacent].wasVisited:
                visitedList = visitedList + self.applyDFS(self.vertices[adjacent], [])

        return visitedList


class Vertex:
    def __init__(self, label):
        self.label = label
        self.adjacence = []
        self.wasVisited = False

    def addAdj(self, adj):
        self.adjacence.append(adj)
        self.adjacence.sort()
