# Optimizers in Deep Learning
![alt text](../../README_Assets/01-ANN/18-Optimizers and EWMA/image.png)

    - Most commonly used optimizer is GD
    - Types of GD: Batch, Stochastic, Mini batch

## Challenges in GD
    - Deciding an optimum value of learning rate
    - Learning rate scheduler, predefined values of learning rate
    - Same learning rate in all directions, this may result in slower convergence
    - Local minima, we may get stuck in local minima sometimes and get a sub optimum minima
    - Cannot tackle Saddle point

## Prerequisites
    - EMWA (Exponentially Weighted Moving Average)
# Types of Optimizers
    - Momentum
    - Adagrad
    - NAG
    - RMS Prop
    - Adam

# Keras Implementation
![alt text](../../README_Assets/01-ANN/18-Optimizers and EWMA/image-3.png)

# Summary
    - Start with Adam
    - Then try RMSProp
    - Hyperparameter tuning