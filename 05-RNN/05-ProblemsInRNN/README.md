# Problems in RNNs

RNNs are not used much with sequential data because:

1. Problem of long term dependencies
The higher order derivative terms have very loss contribution in gradient calculations (vanishing gradients)
2. Stagnated training and Unstable gradients
Happens because of exploding gradients
Solutions:
    + Gradient clipping
    + Controlled learning rate