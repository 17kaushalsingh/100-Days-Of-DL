# Transfer Learning

![alt text](../../README_Assets/03-CNN/14-Transfer-Learning/image.png)

    - We freeze the convolutional part
    - We change the architecture of our fully connected layers as per our use case
    - Training happens only for fully connected layers, not the convolutional part


## Types of Transfer Learning

    1. Feature Extraction
        + Freezing the convolutional part, changing the structure of fully connected part
        + Used when labels in the specific use case are similar to the ones on which main model was trained
    2. Fine Tuning
        + A few convolutional layers are unfreezed and those layers get trained
        + Used when the labels in the specific use case are different than the ones on which main model was trained