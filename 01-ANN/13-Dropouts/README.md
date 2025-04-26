# Dropouts

    - Randomly turn off a few nodes in each epoch
    - It is kind of in each epoch, the neural network architecture is different
    - So it kind of ensemble learning
    - Random forest is similar to Dropouts
![alt text](../../README_Assets/01-ANN/13-Dropouts/image.png)

    - Dropouts is applied only at the time of training, not at the time of testing
![alt text](../../README_Assets/01-ANN/13-Dropouts/image-1.png)

# Tips
    - If overfitting, increase parameter 'p' for Dropouts
    - If underfitting, decrease parameter 'p' for Dropouts
    - Do not apply Dropouts to all layers at first
        - First try out Dropouts with the last layer
        - If it gives favourable results, try applying to other layers as well
    - For CNN: p should be 0.4 to 0.5
    - For RNN: p should be from 0.2 to 0.3
    - For ANN: p should be from 0.1 to 0.5

# Drawbacks
    - Convergence is delayed when using Droputs
    - It delays model training
    - Loss function changes during applying Dropouts