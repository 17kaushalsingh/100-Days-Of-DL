# Perceptron Notation

## Architecture
![alt text](../../README_Assets/01-ANN/02-MultiLayerPerceptron/image.png)

### Number of Trainable Parameters
    At each level
    Weights = nodes in prev level * nodes in curr level
    Bias = nodes in curr level
![alt text](../../README_Assets/01-ANN/02-MultiLayerPerceptron/image-1.png)

## Weights Notation
W<sup>k</sup><sub>i j</sub>

    k: jis weight ki bat ho rhi hai, wo konse layer me ghus raha hai
    i: jis layer se niakl rha h uska node number in that layer
    j: jis layer me ghus rha h uska node number in that layer
![alt text](../../README_Assets/01-ANN/02-MultiLayerPerceptron/image-4.png)

## Bias Notation
B<sub>i j</sub> <br>

    i: Layer Number
    j: Node Number in the particular layer
![alt text](../../README_Assets/01-ANN/02-MultiLayerPerceptron/image-2.png)

## Output Notation
    Output of a particular node is the Input to the next layer node
    Each node may produce more than 1 output
O<sub>i j</sub> <br>

    i: Layer Number
    j: Node Number in the particular layer
![alt text](../../README_Assets/01-ANN/02-MultiLayerPerceptron/image-3.png)

# Multilayer Perceptron
![alt text](../../README_Assets/01-ANN/02-MultiLayerPerceptron/image-5.png)

# How to Change the Neural Network Architecture
    1. Increase the num of nodes (perceptrons) in the hidden layers
    2. Add more nodes to Input Layer (only when input features increase)
    3. Add more nodes to Output Layer (only in case of multiclass classification/regression)
    4. Increase the number of hidden layers (Helps capture non linearity in data)