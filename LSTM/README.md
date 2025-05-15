# LSTM
## Problems with RNNs
- RNNs suffer from managing both long term and short term dependencies in a single state
- Mostly it is the short term context/memory which superseeds the long term context/memory
- Also, it suffers from vanishing and exploding gradients
- RNNs are not used much with sequential data because:
    1. Problem of long term dependencies <br>
    The higher order derivative terms have very loss contribution in gradient calculations (vanishing gradients)
    2. Stagnated training and Unstable gradients <br>
    Happens because of exploding gradients

## Solutions to RNNs:
- For long term dependencies
    - Use ReLU or some other activation
    - Use better weights initialization techniques
    - Use skip RNNs
- For stagnated training/exploding gradients
    - Gradient clipping
    - Controlled learning rate

# LSTM (Long Short Term Memory)
- Maintains two state, one for short term context, the other for long term
- Eliminates the problem of vanishing/exploding gradients
- Has major architectural difference in order to have proper communication between short term and long term context
![alt text](image.png)

## Gates in LSTM
![alt text](image-1.png)
- `FORGET GATE`: based on current input and short term context, it decides what to remove from long term memory
- `INPUT GATE`: based on current input and short term context, it decides what to add in the long term memory
- `OUTPUT GATE`: based on current input, it decides what to extract from long term memory and show it as output <br>
It also creates the short term context at each input
