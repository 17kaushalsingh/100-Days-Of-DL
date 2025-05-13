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