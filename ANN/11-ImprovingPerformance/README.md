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
    
- Exploding gradients
    + Gradient clipping

- Not enough data
    + Transfer learning
    + Unsupervised pretraining
    + Data augmentation

- Slow training
    + Choosing right optimizers
    + Learning rate scheduler (warming up the LR)

- Overfitting
    + L1 and L2 Regularization
    + Dropouts
    + Early Stopping

- Normalization
    + Normalizing inputs
    + Batch normalizing
    + Normalizing activations