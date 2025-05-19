# LSTM Architecture

![alt text](image.png)

- `Cell State: ` Long Term Memory
- `Hidden State: ` Short Term Memory

## LSTM is like a small computer
- Input
    - X<sub>it</sub>: Input features for current timestamp
    - C<sub>t-1</sub>: Cell state (long term context) from the previous timestamp
    - H<sub>t-1</sub>: Hidden state (short term context) from the previous timestamp

- Process
    - Update C<sub>t</sub>: `Remove unnecessary info` and `Add new info`
    - Calculate H<sub>t</sub>

- Output
    - C<sub>t</sub>: Cell state (long term context) for the current timestamp
    - H<sub>t</sub>: Hidden state (short term context) for the current timestamp

# Gates in LSTM
![alt text](image-1.png)

- FORGET GATE: To remove something from C<sub>t-1</sub>
- INPUT GATE: To add something to C<sub>t-1</sub>
- OUTPUT GATE: To calculate H<sub>t</sub>


## Imp
- H<sub>t</sub> and C<sub>t</sub> are vectors of equal dimension
- Forget gate has f<sub>t</sub>
- Input gate has i<sub>t</sub> and $\bar{C}$<sub>t</sub>
- Output gate has O<sub>t</sub>>
- All, H, C, f, i, C, O, are of equal dimensions

## PointWise Operations
Eg: X = [x1, x2, x3] and Y = [y1 y2 y3]
- `Pointwise multiplication(X, Y) = [x1*y1 x2*y2 x3*y3]` 
- `Pointwise addition(X, Y) = [x1+y1 x2+y2 x3+y3]` 
- `Pointwise tanh(X) = [tanh(x1) tanh(x2) tanh(x3)]` 

## Yellow rectangular boxes
- These are neural network layers
- The sign represents the activation of that layer
- The number of nodes in each layer is always equal to each other
- The dimensions of cell state, hidden state, etc is equal to the number of nodes in thd neural layers

# The `FORGET GATE`
- First calculate f<sub>t</sub>
- f<sub>t</sub> = sigmoid (W<sub>f</sub> . concat(h<sub>t-1</sub>, X<sub>t</sub>) + B<sub>f</sub>)
- REMOVAL OF INFO FROM C<sub>t-1</sub>: Do a pointwise multiplication of f<sub>t</sub> with C<sub>t-1</sub>

# The `INPUT GATE`
- First calculate candidate cell state ($\bar{C}$<sub>t</sub>)
- $\bar{C}$<sub>t</sub> = tanh (W<sub>c</sub> . concat(h<sub>t-1</sub>, X<sub>t</sub>) + B<sub>c</sub>)
- This is the potential information which can be added to the cell state
- But we filter it further
- Calculate i<sub>t</sub>
- i<sub>t</sub> = sigmoid (W<sub>c</sub> . concat(h<sub>t-1</sub>, X<sub>t</sub>) + B<sub>c</sub>)
- Now do: i<sub>t</sub> pointwise multiplication with $\bar{C}$<sub>t</sub>
- ADDITION OF INFO TO C<sub>t-1</sub>: Do a pointwise addition of above result with C<sub>t-1</sub>
- Now we get C<sub>t</sub>

# The `OUTPUT GATE`
- First do a pointwise tanh of C<sub>t</sub>
- Then calculate O<sub>t</sub>
- O<sub>t</sub> = sigmoid (W<sub>o</sub> . concat(h<sub>t-1</sub>, X<sub>t</sub>) + B<sub>o</sub>)
- Now get h<sub>t</sub>
- h<sub>t</sub> = pointwise multiplication of O<sub>t</sub> with tanh(C<sub>t</sub>)