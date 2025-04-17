# Architecture and Forward Propagation in RNNs
    - Unlike ANNs (where all data is fed at once), RNNs take input based on timestamps
    - ANN is a feed forward network, RNN has a state which provides feedback to previous layers

## Data structure for RNNs
    - (batch_size, time_steps, input_features)
![alt text](image.png)

## RNN Mechanism
    - Input is fed according to timestamps
    - At time t=1, only x11 is fed, at t=2 x12 is fed and so on
    - When the forward prop for t=2 happens, the network recieves two inputs x=12, and the outputs of the previous activations from the same layer
    - For the first timestamp, the feedback could be zeros or random numbers
    - The recurrent connections also have weights

![alt text](image-2.png)
![alt text](image-3.png)

## Forward Propagation in RNNs
### Unfolding Through Time
    - Basically means that the recurrent layer works as a loop
    - Uses concept of parameter or weights sharing
    - Helps process the information in sequences
    