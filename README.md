 Assignment #5, Dijkstra's Single Source Shortest Path Algorithm
Due by Apr 11, 2019 11:00 PM

Contents


1  Assignment Overview

2  Dijkstra's Single Source Shortest Path Algorithm

  2.1  Input File
  2.2  Your program
3  Example

4  Submitting Your Code and PDF

Assignment Overview

This assignment has two parts:

    Answer the question in this PDF.
    Code Dijkstra's Single Source Shortest Path Algorithm.

This assignment will be submitted in two places: your code must be uploaded to AutoGradr and your PDF must be submitted to gradescope.

This assignment is worth 20 points in total:

    8 points for correct answers to the question found in the PDF
    7 points for correct output on your program
    2 points for having the names of all group members at the top of the code that you submit to AutoGradr
    3 points for having code that is readable and easy to understand

Additional notes:

    AutoGradr allows you to submit your code as many times as you'd like. Only the final submission will be graded.
    You are strongly encouraged to work in groups of up to three students. You can choose your partners, and if you need help finding a partner you should make a post on Slack.

Dijkstra's Single Source Shortest Path Algorithm

Your program will prompt users for a filename and a start vertex number and it will output the shortest path from the start vertex to all other vertices.
Input File

The file will include all of the information needed to create a directed graph.

The format of this file is referred to as an adjacency list. Here is an example of such a file:

1 2,1 8,2
2 1,1 3,1
3 2,1 4,1
4 3,1 5,1
5 4,1 6,1
6 5,1 7,1
7 6,1 8,1
8 7,1 1,2

Each line of the file contains the following information: a vertex identifier (a value from 1 to n) and then a list of edges where each edge contains a pair of values (the connecting vertex and an integer value for the edge weight).

For example, on the third line above (3 2,1 4,1) we can see that vertex 3 is connected to vertex 2 with a weight of 1, and vertex 3 is also connected to vertex 4 with a weight of 1. The graph for the above adjacency list is shown below:

Example graph for Dijkstra's Algorithm Assignment

Although the above example only shows two edges per node, there can be any number of edges. For example, look at the adjacency list below:

1 2,3 3,2
2 4,4
3 2,1 4,2 5,3
4 5,2 6,1
5 6,2
6 1,9

Additionally, the spacing between edges might not be consistent. Your program should handle any kind of whitespace between edges (i.e., multiple spaces and tabs).
Your program

Personally, I found this assignment quite a bit easier to do in Python than in any of the other options. Your filename should be main.{py,cpp,rs,...}. You are required to write the names of all partners in comments at the top of the file.

You do not need to worry about using a Heap to reduce the running time (though you should give it a try if you have time), but instead implement the O(mn) version. This is a general outline for your program:

Step 1. Open the input file and read in the contents. I read the data into a Python dictionary where each key was a vertex identifier and each value was a list of edges (you could do this with a std::map in C++). For instance, this is what my dictionary looks like for the example pictured above:

{
    1: [(2, 1), (8, 2)],
    2: [(1, 1), (3, 1)],
    3: [(2, 1), (4, 1)],
    4: [(3, 1), (5, 1)],
    5: [(4, 1), (6, 1)],
    6: [(5, 1), (7, 1)],
    7: [(6, 1), (8, 1)],
    8: [(7, 1), (1, 2)]
}

Step 2. Next you should initialize the two variables needed for Dijkstra's algorithm: an array that holds all of the path lengths, and an initially empty set for holding the visited vertices. You will need to prompt the user to provide a start vertex.

Step 3. In the next step you need to implement the loop in Dijkstra's Algorithm. Remember, you will need to loop until every vertex has been visited. Here are the highlights of what this loop does:

    An edge (v,w) should only be considered if v is in your set and w is not.

    Thus, for each vertex already in your set you will need to check each of the vertices to which it is connected (loop through the list of its edges).

    Calculate Dijkstra's greedy criterion for each of the considered edges and save the edge with the smallest value (the shortest path length).

    Add the appropriate vertex to your set and update the vertex's path length.

Step 4. After the loop, you should print all path lengths as a comma separated list. For instance, the correct output for the example graph (pictured above) is:

0,1,2,3,4,4,3,2

Example

Yellow lines indicate things that you would type; all other lines are output from the programs that were run.

prompt> cat example_input.txt
1 2,1 8,2
2 1,1 3,1
3 2,1 4,1
4 3,1 5,1
5 4,1 6,1
6 5,1 7,1
7 6,1 8,1
8 7,1 1,2
prompt> ./main.py
Please provide a filename containing an adjacency list:
example_input.txt
Please provide a start vertex label (1..n):
1
0,1,2,3,4,4,3,2

Submitting Your Code and PDF

Your submission includes two parts: (1) your code must be submitted to AutoGradr and your PDF must be submitted to gradescope. If you have any difficulties please ask for help on on Slack.

For AutoGradr:

    Only one partner needs to upload the code to AutoGradr. If multiple partners submit code then please leave a comment at the top of your code stating that I should not grade it if you want me to grade a different student's submission. I'm tired of searching for the correct submission.
    The names of all partners must be in comments at the top.

For gradescope:

    You should print the PDF and write your answers directly on the printed sheet (this will help me during the grading process).
    Please ensure that the partner that uploads to gradescope adds the other partners after submission.
    If you have any questions please ask them on Slack.

Additional details for using gradescope can be found here:

    A general video about submitting homework.
    This PDF is about about scanning your documents, which may be useful in the future.
    Finally, here is a video showing how to submit a group assignment.

formatted by Markdeep 1.04  ✒