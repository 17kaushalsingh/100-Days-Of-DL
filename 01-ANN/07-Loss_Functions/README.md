# Loss Function
![alt text](../../README_Assets/01-ANN/07-Loss_Functions/image.png)

# Loss Functions in DL

## Regression
    - mean_squared_error
    - mean_absolute_error
    - huber_loss

## Classification
    - binary_cross_entropy
    - categorical_crossentropy
    - sparese_categoricalcross_entropy
    - hinge_loss

## Autoencoders
    - kl_divergence

## Generative Adverserial Neural Network
    - discriminator_loss
    - min_max_gan

## Object Detection
    - focal_loss

## Embeddings
    - triplet_loss

# Loss Function vs Cost Function
    - Loss function is calculated for a single training example
    - Cost function is calculated for the entire training batch

# Mean Squared Error

    - Also called mse
    - Also called Squared Loss
    - Also called L2 Loss
    - Magnifies those points 
    - Activation function should be linear to use mse as loss

Advantages

    - Easy to interpret
    - Differentiable
    - Only one local minima, which is also the global minima

Disadvantages

    - The error has its units squared
    - Not robust to outliers

# Mean Absolute Error

    - Also called mae
    - Also called Absolute Loss
    - Also called L1 Loss

Advantages

    - Easy to interpret and intuitive
    - Unit of errors is same as input
    - Robust to outliers

Disadvantages

    - The curve is not differentiable
    - Need to calculate sub gradients instead of gradients to apply Gradient Descent

# Huber Loss
![alt text](../../README_Assets/01-ANN/07-Loss_Functions/image-2.png)
![alt text](../../README_Assets/01-ANN/07-Loss_Functions/image-6.png)

Advantages

    - mae treats outliers as normal points
    - mse magnifies loss at outliers
    - Huber loss balances both using hyperparameter delta
    - Works best when significant number of outliers are present in data
    - Derivable at all points

# Binary Cross Entropy

    - Also called log loss
    - Used in Binary Classification Problems
    - Example: used in logistic regression
    - Activation function should be sigmoid to use log loss as loss

## Mathematical Formulation of Loss Function
![alt text](../../README_Assets/01-ANN/07-Loss_Functions/image-3.png)

## Mathematical Formulation of Cost Function
![alt text](../../README_Assets/01-ANN/07-Loss_Functions/image-4.png)

Advantages

    - Differentiable

Disadvantages

    - Not straightforward and intuitive
    - Multiple local minimas

# Categorical Cross Entropy

    - Used in Multi Class Classification Problems
    - Example: used in softmax regression
    - Activation function should be softmax
    - One Hot Encode the output column

## Mathematical Formulation of Loss Function
![alt text](../../README_Assets/01-ANN/07-Loss_Functions/image-5.png)

## Mathematical Formulation of Cost Function

    - Take average of all losses


# Sparse Categorical Cross Entropy
    - Similar to categorical cross entropy
    - Categorical Cross Entropy: ONE HOT ENCODE
    - Sparese Categorical Cross Entropy: INTEGER ENCODE
    - Sparse Categorical Cross Entropy is Faster than Categorical Cross Entropy