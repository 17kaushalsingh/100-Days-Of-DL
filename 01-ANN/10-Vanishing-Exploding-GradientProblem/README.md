# Vanishing Gradient Problem
    - Occurs mostly in ANN

![alt text](../../README_Assets/01-ANN/10-Vanishing-Exploding-GradientProblem/image.png)

## How to Tackle Vanishing GD Problem
    - 1. Reduce model complexity
        + Use a shallower model if a deeper model gives the problem
        + Generally, this approach is not used, because the reason we add more layers is to capture non linearity
    - 2. Using ReLU activation function
        + Iska derivative ya to 0 hoga ya 1 hoga, to small values ki problem nhi hogi
        + Problems: Dying ReLU
![alt text](../../README_Assets/01-ANN/10-Vanishing-Exploding-GradientProblem/image-1.png)

    - 3. Proper weight initialization
    - 4. Batch Normlaization
    - 5. Using a Residual Network

# Exploding Gradient Problem
    - Occurs mostly in RNN
    - If all derivatives are larger than 1, the overall change is very large