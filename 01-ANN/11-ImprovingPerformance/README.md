# How to Improve Neural Network

![alt text](image.png)

## Hyperparameters
    - Number of hidden layers
    - Numnber of nodes in hidden layers
    - Learning rate (also affect slow training)
    - Optimizer (also affect slow training)
    - Batch size
    - Activation function (also affects vanishing/exploding gradients)
    - Epochs

## By Solving Problems
    - Vanishing/Exploding gradients
        + Weights initialization
        + Change activation function
        + Batch normalization
        + Gradient clipping (for exploding)
    - Not enough data
        + Transfer learning
        + Unsupervised pretraining
    - Slow training
        + Optimizers
        + Learning rate scheduler
    - Overfitting
        + L1 and L2 loss
        + Dropouts


## Performance Improvement Checklist

    - 1. Overfitting
        + Dropout Layers
        + Regularization
        + Early Stopping


    - 2. Normalization
        + Normalizing inputs
        + Batch normalizing
        + Normalizing activations


    - 3. Vanishing Gradients
        + Activation functions
        + Weight initialization


    - 4. Gradient Checking and Clipping


    - 5. Optimizers