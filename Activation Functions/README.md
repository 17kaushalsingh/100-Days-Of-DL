# Activation Functions

![alt text](image.png)

    - Activation function should be non linear
    - Activation function should be differentiable
    - Activation function should not be computationally expensive
    - Derivative calculation for activation function should be fast, easy and efficient
    - Activation function should be ZERO CENTRED (eg: tan_h)
        - Mean of Activations ~= 0
    - Activation function should be non saturating
        - Saturating activation functions: sigmoid, tanh ==> squeeze the inputs within a certain range
        - Saturating functions cause VANISHING GRADIENTS
        - Non Saturating activation functions: relu ==> DO NOT squeeze the inputs within a certain range

<br><br><br>

# Types of Activation

## LINEAR

<br><br>

## SIGMOID
![alt text](image-3.png) </br>

$\sigma(x) = \frac{1}{1 + e^{-x}}$

    - Range: (0, 1)

    - Advantages
        + Range is [0, 1]: can be modelled as probability
        + Non linear function
        + Differentiable

    - Disadvantages
        + Saturating function, hence leads to vanishing gradients
        + Sigmoid activation is NOT ZERO CENTRED
        + Computationally expensive
<br><br>

## TANH
![alt text](image-5.png) </br>
![alt text](image-6.png)

    - Range: (-1, 1)

    - Advantages
        + Non linear
        + Differentiable
        + ZERO CENTRED

    - Disadvantages
        + Saturating function, hence leads to vanishing gradients
        + Computationally expensive
<br><br>

## RELU
![alt text](image-7.png) <br>
![alt text](image-8.png)

    - Range: (0, inf]

    - Best choice for hidden layers

    - Advantages
        + Non linear
        + Non Saturating function in the positive region
        + Computationally inexpensive
        + Convergence is faster than sigmoid and tanh functions

    - Disadvantages
        + Not differentiable at 0
        + NOT ZERO CENTRED ==> Use batch normalization
        + Dying ReLU

<br><br>

## Dying ReLU Problem
    - Some neurons always output 0
    - They become dead neurons
    - 