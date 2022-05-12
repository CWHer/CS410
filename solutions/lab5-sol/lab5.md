# Lab 5:  Regression &  Neural Networks

> CS410: Artificial Intelligence
> Shanghai Jiao Tong University, Fall 2021

### Exercise 1: Linear Regression

It is not hard to compute $\hat{Y}$ . One way to verify the geometric interpretation is to compute and show that $X^\top(Y-\hat{Y})\approx\mathbf{0}$.



### Exercise 2: Logistic Regression

Please refer to the code. Reasonable discussions are acceptable.



### Exercise 3: L1/L2 Regularization

Ridge regression:

![reg_0](C:\Users\Spider X\Downloads\reg_0.png)

Lasso regression:

![reg_1](C:\Users\Spider X\Downloads\reg_1.png)

Discussions:

1. Theoretically, Lasso regression requires more complex optimization techniques, which is usually computationally expensive. However, such difference may not be observed at this scale.
2. Lasso regression.
3. There is a trade-off. You can discuss it based on the results.

### Exercise 4: Two-layer Perceptron Network

`hidden_dim=2`: 

![Figure_0](C:\Users\Spider X\Downloads\Figure_0.png)

`hidden_dim=10`: 

![Figure_1](C:\Users\Spider X\Downloads\Figure_1.png)

Generally speaking, larger `hidden_dim` leads to better fitting (in terms of error and stability).

Any reasonable discussions are acceptable.
