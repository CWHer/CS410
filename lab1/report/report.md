# Lab1 Report

### Exercise 1: 

Implementation of `Stack` and `Queue`, nothing special.

### Exercise 2:

I mainly follow the general search framework discussed during class and use `Stack` to store frontier. Besides, I add `Node()` class to implement a trivial linked list to store directions and generate solution.

However, naive DFS would encounter infinite loop when it goes along a circle in the maze. Thus, I add `visited` data structure to record all the position that have been visited to avoid visit them again.

<img src="assets/framework.png" style="zoom: 50%;" /> 

### Exercise 3:

BFS uses `Queue` to store frontier and the above`visited` is not needed here as BFS searches layer after layer.

### Exercise 4:

The following maze makes DFS fail to reach optimal answer. It yields `cost=12`, but apparently the optimal answer is `cost=2`

```
%%%%%%%%%%
%%%S     %
%%% %%%% %
%%%G     %
%%%%%%%%%%
```

