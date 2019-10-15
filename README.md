# Breadth First Search Pathfinding-Visual

This is my personal project where I attempt to create a visualization of the breadth first search pathfinding algorithm. I created a grid where the user can click to select a starting node, an ending node, and some walls. After hitting play, the grid will update and show its step by step process of searching the grid until it finds the ending node. Once the end node is found, it will show all the checked nodes and the fastest route. 

# Explanation of the Breadth First Search Algorithm

The BFS Algorithm is an algorithm that traverses an entire of level of children nodes starting from the root node. When the entire level is accounted for, the next level is traversed. When it comes to pathfinding, every possible move starting from the initial node is checked and stored until the end node is found. Then the shortest list of movements is returned.

# Controls:
+ Press 'S', 'E', 'W', or 'P' keys to change the status of the node to Start, End, Wall, and Play respectively 

![](BFS.gif)
