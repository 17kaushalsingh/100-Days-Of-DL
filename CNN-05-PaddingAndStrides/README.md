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
    - Feature map size with stride = s ===> (n - f ) / s + 1
    - Feature map size with stride and padding   ===> (n - f + 2p) / s + 1

    - If stride > 1 ==> It is called strided convolution

    - Use strides when we need high level features
    - Use strides to reduce computing complexity, and training time

