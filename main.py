#!/usr/bin/python

#**************************************************
# csc325 - Assignment 5
# Dijkstra's Single Source Shortest Path Algorithm
# Authors:  Lauren Tallerico
#           Brett Largent
#           Rish Russel
#**************************************************

#fname = input("Please provide a filename containing an adjacency list:\n")
fname = "test1.txt"

d = {}
with open(fname) as inFile:
    for line in inFile:
        valueList = []
        edgeList = line.split()
        key = int(edgeList[0])
        del edgeList[0]
        for edge in edgeList:
            edges = edge.split(',')
            edgeTuple = (int(edges[0]), int(edges[1]))
            valueList.append(edgeTuple)
        d[key] = valueList

    for key in d:
        print(key, ": ", d[key])


#startVertex = input("Please provide a start vertex label (1..n):\n")
startVertex = 1
visited = {startVertex}
pathLengths = [0] * len(d)

#while len(visited) != len(d):
iteration = []
for v in visited:
    for i in range(len(d[v])):
        if d[v][i][0] not in visited:
            iteration.append((v, d[v][i]))
minEdge = min(iteration, key = lambda t: t[1][1])
print(iteration)
print("Minimum edge is:", minEdge)
visited.add(minEdge[1][0])
pathLengths[minEdge[1][0]-1] = pathLengths[minEdge[0]-1] + minEdge[1][1]
print(visited)
print(pathLengths)
