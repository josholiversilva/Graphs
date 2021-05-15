# Dijkstra's algorithm 
# Time: O(V*E) -> simple implementation
# Time: O(E*Log(V)) -> using min heap
#                 12
#        (B)-----------------
#     5/    6\              |
# (A)         (D)           |
#    \      /     \2       3|
#  10 \   /2       (E) --- (F)
#      \ /                  |
#      (C)------------------|
#               3
import time

class Node:
    def __init__(self, nodeLetter, adjacencyMap={}):
        self.nodeLetter = nodeLetter
        self.adjacencyMap = adjacencyMap

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('F')
H = Node('F')
I = Node('F')
A.adjacencyMap = {B: 5, C:5}
B.adjacencyMap = {D: 3, F:3}
C.adjacencyMap = {D:2, F:4}
D.adjacencyMap = {E: 2}
E.adjacencyMap = {F: 3, G: 4}
F.adjacencyMap = {H: 5, I: 8}
H.adjacencyMap = {I:2}

# Simple Implementation O(N^2)
def dijkstra(graph, sourceNode, destNode):
    start = time.time()
    vertexMap = {vertex: {'shortestPath': float('inf'), 'prev': None} for vertex in graph}
    vertexMap[sourceNode] = {'shortestPath': 0, 'prev': None}
    visited = set()
    nextNode = sourceNode
    shortest = float('inf')

    while graph:
        currNode = graph.pop(graph.index(nextNode))
        visited.add(currNode)

        for child,cost in currNode.adjacencyMap.items():
            if child not in visited:
                vertexMap[child] = {'shortestPath': min(vertexMap[currNode]['shortestPath']+cost,vertexMap[child]['shortestPath']), 'prev': currNode}
                print(child.nodeLetter + " Cost: " + str(min(vertexMap[currNode]['shortestPath']+cost,vertexMap[child]['shortestPath'])))

        for vertex in vertexMap:
            if vertex not in visited and shortest >= vertexMap[vertex]['shortestPath']:
                nextNode = vertex
                shortest = vertexMap[vertex]['shortestPath']

        print("Next Node: " + nextNode.nodeLetter)

        shortest = float('inf')

    for node,cost in vertexMap.items():
        print(node.nodeLetter + ' - ' + str(cost['shortestPath']))

    #shortestPath = [destNode.nodeLetter]
    #prev = vertexMap[destNode]['prev']
    #while prev:
    #    shortestPath.append(prev.nodeLetter)
    #    prev = vertexMap[prev]['prev']

    #shortestPath.reverse()
    #shortestPath = '->'.join(shortestPath)
    #print("Shortest Path: " + shortestPath)
    print("Cost From " + str(sourceNode.nodeLetter) + " -> " + str(destNode.nodeLetter) + ": " + str(vertexMap[destNode]['shortestPath']))
    elapse = time.time() - start
    print('time: ' + str(elapse))

# Heap Implementation
# Create hashmap: O(V)
# Create list for heap: O(E)
# Convert list back to hashmap: O(E)
# Heapify: O(VLogV)
# Time: O(2E+2VLogV) -> O(NLogN)
import heapq
import collections
def dijkstraFast(graph, sourceNode, destNode):
    start = time.time()
    vertices = {}
    for x in range(len(graph)):
        if graph[x] == sourceNode:
            vertices[graph[x]] = 0
        else:
            vertices[graph[x]] = float('inf')
    visited = set()
    nextNode = sourceNode
    shortest = float('inf')

    while vertices:
        verticesList = [(value,key) for key,value in vertices.items()]
        heapq.heapify(verticesList)
        currNode = heapq.heappop(verticesList)
        visited.add(currNode)
        tmp = {}
        for value,key in verticesList:
            tmp[key] = value
        vertices = dict(tmp)

        for child,cost in currNode[1].adjacencyMap.items():
            if child in vertices:
                vertices[child] = min(currNode[0]+cost, vertices[child])
                print(child.nodeLetter + ' - ' + str(vertices[child]))

    cost = -1
    for visit in visited:
        if visit[1] == destNode:
            cost = visit[0]

    print("Cost From " + sourceNode.nodeLetter + " -> " + destNode.nodeLetter + ': ' + str(cost))
    elapse = time.time() - start
    print('time: ' + str(elapse))

graph = [A,B,C,D,E,F,G,H,I]
print("Simple Implementation")
dijkstra(graph, A, I)
print('')


graph = [A,B,C,D,E,F,G,H,I]
print("Heap Implementation")
dijkstraFast(graph, A, I)