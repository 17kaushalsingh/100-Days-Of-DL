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
