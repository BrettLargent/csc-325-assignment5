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
