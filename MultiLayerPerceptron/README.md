# Perceptron Notation

### Architecture
![alt text](image.png)

### Number of Trainable Parameters
    At each level
    Weights = nodes in prev level * nodes in curr level
    Bias = nodes in curr level
![alt text](image-1.png)

### Weights Notation
W<sup>k</sup><sub>i j</sub>

    k: jis weight ki bat ho rhi hai, wo konse layer me ghus raha hai
    i: jis layer se niakl rha h uska node number in that layer
    j: jis layer me ghus rha h uska node number in that layer
![alt text](image-4.png)

### Bias Notation
B<sub>i j</sub> <br>

    i: Layer Number
    j: Node Number in the particular layer
![alt text](image-2.png)

### Output Notation
    Output of a particular node is the Input to the next layer node
    Each node may produce more than 1 output
O<sub>i j</sub> <br>

    i: Layer Number
    j: Node Number in the particular layer
![alt text](image-3.png)

# Multilayer Perceptron
