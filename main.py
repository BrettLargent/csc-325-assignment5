#!/usr/bin/python

#****************************************************************************************************
# csc325 - Assignment 5
# Dijkstra's Single Source Shortest Path Algorithm
# Authors:  Lauren Tallerico
#           Brett Largent
#           Rish Russel
#****************************************************************************************************


#****************************************************************************************************
#
# Read adjacency list into a dictionary
#
#****************************************************************************************************

fname = input("Please provide a filename containing an adjacency list:\n")
#fname = "test1.txt"

d = {}                              # Declare dictionary d
with open(fname) as inFile:         # Open file
    for line in inFile:             
        valueList = []              # Empty valueList at start of each line
        edgeList = line.split()     # Split line into key and its values
        key = int(edgeList[0])      # Pull key from list
        del edgeList[0]             #   and remove it
        for edge in edgeList:
            edges = edge.split(',')                     # Separate edges into neighbor and its path weight
            edgeTuple = (int(edges[0]), int(edges[1]))  # Create a tuple from it
            valueList.append(edgeTuple)                 # Store the tuple into a list
        d[key] = valueList                              # Assign that list to its key in the dict

"""
# Displays dictionary in viewer-friendly format
    for key in d:
        print(key, ": ", d[key])
print('\n')
"""

#****************************************************************************************************
#
# Dijkstra's Single Source Shortest Path Algorithm
#
#****************************************************************************************************

startVertex = input("Please provide a start vertex label (1..n):\n")
#startVertex = 1

visited = {int(startVertex)}    # Declare set visited
pathLengths = [0] * len(d)      # Declare list pathLengths w/zeros and a length equal to that of d

while len(visited) != len(d):   # While not all nodes visited
    iteration = []              # Empty all edges considered at start of each iteration
    for v in visited:                       # of all edges (v, w) where
        for i in range(len(d[v])):          #   v is visited, and
            if d[v][i][0] not in visited:   #   and w is not visited
                iteration.append([v, d[v][i][0], d[v][i][1]])       # Send [v, w, Path Length] to iteration   
                iteration[len(iteration)-1][2] += (                 # Update Path Length in iteration to reflect lvw +
                    pathLengths[iteration[len(iteration)-1][0]-1])  #   pathLengths[v]
    minEdge = min(iteration, key = lambda t: t[2])                  # Pick the minimum Path Length and call (v*, w*) minEdge
    visited.add(minEdge[1])                                         # Add w* to visited
    pathLengths[minEdge[1]-1] = minEdge[2]                          # Set pathLengths[w*] = pathLengths[v*] + lvw

for i in pathLengths:                           # Print all path lengths as a comma separated list
    str(i)
print(','.join(str(s) for s in pathLengths))
