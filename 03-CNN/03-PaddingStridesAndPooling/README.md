# Padding, Strides and Pooling

# Padding and Strides

## Why padding
- Middle wai pixels har convolution operation me appear kregi, but corner wali kam me
- Leads to information loss at corners
- If corner wale pixels have the most important information, it is lost in convolution
- We do not change the shape of filter so we change the shape of image by padding it
-  Image NxN, Filter FxF ==> Feature Map (N-F+1) x (N-F+1), but we want it NxN
- So we add F-1 x F-1 zero padding uniformaly on all four sides of input image

## Strides: What and Why
- Filter movement size is called stride
- Feature map size with stride = s ===> $\frac{n - f}{s} + 1$
- Feature map size with stride and padding   ===> $\frac{n - f + 2p}{s} + 1$
- If stride > 1 ==> It is called strided convolution
- Using strides means
    - Considering high level features
    - Reducing computational complexity
    - Reducing traioning time

# Pooling Layers
Problems with Convolution Operation
- Need to0 much memory in CPU
- Translattional Variance - feature kaha h usse farak padta h
- Pooling is basically, selecting one value from a smaller matrix to represent the entire matrix

## Advantages of Pooling
- Reduces size of feature map
- Enhanced feature map, only in case of MaxPooling

## Types of Pooling
- Max Pooling
- Min Pooling
- Global Pooling (can be used just before sending to fully connected layers)
    - Global Max Pooling
    - Global Average Pooling
- Average Pooling
- L2 Pooling (takes L2 norm of the entire window)