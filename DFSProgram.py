from GraphClass import Graph, Vertex

"""
Course: CPCS 331
Section: GE
Group:
    Member 1: Turki Alzubaidi
    Member 2: Ammar Joharji
    Member 3: Mohammad Alghafli
"""

try:
    graph = Graph()
    numberOfVertices = int(input("How many Vertices: "))

    # we loop to add each vertex into a list to to insert the vertices in the alphabetical order
    verticesList = []
    i = 0
    while i < numberOfVertices:
        verLabel = input("Enter vertex number %d: " % (i + 1))
        if verLabel not in verticesList:
            verticesList.append(verLabel)
            i += 1
        else:
            print("This vertex is already inserted")
    verticesList.sort()  # to sort the list
    # adding all vertices into the graph
    for i in verticesList:
        graph.addVertex(Vertex(i))
    print()
    print("All vertices added successfully...")

    # now we should add the edges
    print()
    numberOfEdges = int(input("How many Edges: "))
    for i in range(0, numberOfEdges):
        print()
        addV = True
        while addV:
            ver1 = input("Enter Source label: ")
            if ver1 not in verticesList:
                print("This character is not in the graph")
            else:
                addV = False

        addV = True
        while addV:
            ver2 = input("Enter Destination label: ")
            if ver2 not in verticesList:
                print("This character is not in the graph")
            else:
                addV = False

        graph.addEdge(ver1, ver2)
        print()
        print("Edge " + ver1 + " to " + ver2 + " added successfully...")

    print()
    print("Depth first search result is:")
    print(graph.DFS())
except:
    print()
    print(" >> Error: Mismatch input...")