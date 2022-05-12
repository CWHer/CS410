# Lab 3: Constraint Satisfaction Problems

> CS410: Artificial Intelligence
> Shanghai Jiao Tong University, Fall 2021

### Exercise 2: Sudoku (Filtering)

> Compare the efficiency of two filtering strategies for solving Sudoku. Discuss and explain your findings.

`AC3()` generally takes more time than `forward_checking()`. However, it can find a solution with fewer backtracks.

### Exercise 3: N-Queens (Hill Climbing)

> Try using `min_conflicts()` for Sudoku problems. Discuss and explain your findings. You can evaluate it with

For Sudoku, standard hill-climbing fails to find a solution in bounded time due to the large search space of Sudoku.

