# AdaGrad (Adaptive Gradient)
    - Works better when
        + Scale of input features is different
        + Features are sparse (Most of the values are 0), leading to elongated bowl problem

## Sparse features cause elongated bowl problem
![alt text](image.png)
![alt text](image-1.png)

    - Sparsity in a feature leads to slower updates of params

## AdaGrad
    - Learning rate is different for each trainable param
    - Adjust the lr of a param to a smaller value if the gradient is too large
    - Adjust the lr of a param to a larger value if the gradient is too small

## Mathematical formulation
![alt text](image-2.png)

    - Epsilon is a very small no, kept just to avoid 0 in denominator

## Disadvantage
    - Adagrad reaches near the soln, but fails to reach exactly there
