# Convolutional Neural Network
- Inspired by huamn visual cortex
![alt text](image.png)
- Why ANNs fail over image data
![alt text](image-1.png)
- What Does a CNN See: VIsualizing CNNs
https://machinelearningmastery.com/how-to-visualize-filters-and-feature-maps-in-convolutional-neural-networks/

## Layers in CNN
- Convolutional Layer
- Pooling Layer
- Fully Connected Layer

# CNNs vs ANNs
## Differences
- Computational cost
- Overfitting
- Loss of spatial features

## Similarities
- Nodes of ANN are similar to Filters in CNN
- Dot product and activation functions

## Trainable params in CNN
- Weights: Num filters * Channels * Filter Size
- Bias: Num filters
- In CNN, num of trainable params depends on architecture, not on input data
- In ANN, increasing image resolution increases num of trainable params, hence increases training time