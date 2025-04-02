# Gradient Descent
    - Batch Gradient Descent
    - Stochastic Gradient Descent
    - Mini Batch Gradient Descent

    - For the same number of epochs, model takes more time to learn no Stochastic GD than on Batch GD
    - For the same number of epochs, accuracy of Stochastic GD is better than Batch GD

    - Loss decreases haphazaedly in Stochastic GD
    - Loss decreases smoothly in Batch GD
    - This haphazaedness in SGD is sometimes better as it helps to capture GLOBAL MINIMA, whereas BGD may get trapped in LOCAL MINIMA
![alt text](image-1.png)

# Batch Gradient Descent
    - Vanilla Gradient Descent
    - Works on entire dataset
        - And then update the weights and biases at end of each epoch
        - Num of updates = Num of epochs
    - batch_size = n
    - Uses vectorization to perform calculations
    - Vectorization may not be helpful for large datasets

# Stochastic Gradient Descent
    - Num of updates = Num of rows * Num of epochs
    - batch_size = 1

![alt text](image.png)


# Mini Batch Gradient Descent
    - Middle ground of Batch and Stochastic GD
