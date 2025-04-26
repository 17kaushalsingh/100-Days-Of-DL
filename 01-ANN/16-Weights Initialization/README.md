# Weight Initialization Techniques

# What NOT TO DO
    - Zero initialization
        + If weight initialized to 0, and activation is relu or tanh ==> no updation of weights will happen, all weights will always remain 0
        + In case of sigmoid, a group of derivatives will always remain same ==> it will make some nodes (all nodes at the same level) redundant as their weights will always remain same ==> The network just acts as a perceptron (plain linear model)
<br>

    - Non Zero Constant Value
        + Will lead to some nodes having same set of weights ==> Makes the model linear

<br>

    - Random Initialization with Small vals
        + leads to vanishing gradients in case of sigmoid and tanh activation
        + leads to ultra slow convergence in case of relu activation

<br>

    - Random Initialization with Large vals [0 to 1]
        + leads to saturated activations resulting in slower convergence or (vanishing gradients in worst case) in case of sigmoid and tanh activations
        + leads to slower convergence due to unstable gradients in case of relu activation
        + Vanishing gradients in case of sigmoid and tanh
        + Exploding fradient in case of relu

## Conclusion
    - DO NOT DO: Zero, Constant non zero , small random vals, large random vals

# What TO DO
    - Xavier-Glorat Initialization
        + Normal
        + Uniform

    - He Initialization
        + Normal
        + Uniform

    - With tanh and sigmoid
        => Xavier init gives better result

    - With relu
        => He init gives better result

## Xavier-Glorat Normal
![alt text](../../README_Assets/01-ANN/16-Weights Initialization/image.png)

    + Variance of weights initialized should be 1/n, where n = no of inputs being recieved at a given layer
    + factor in multiplication with rand values should be root of 1/n, that is the std

## He Normal
![alt text](../../README_Assets/01-ANN/16-Weights Initialization/image-1.png)

    + Variance of weights initialized should be 2/n, where n = no of inputs being recieved at a given layer
    + factor in multiplication with rand values should be root of 2/n, that is the std

## Xavier-Glorat Uniform
![alt text](../../README_Assets/01-ANN/16-Weights Initialization/image-2.png)

## He Unifrom
![alt text](../../README_Assets/01-ANN/16-Weights Initialization/image-3.png)

# Keras

    - Default in keras: glorot_unoform
    

![alt text](../../README_Assets/01-ANN/16-Weights Initialization/image-4.png)
