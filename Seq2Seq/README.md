# Encoder - Decoder Models or Sequence2Sequence Models
![alt text](image.png)

## Challenges in Seq2Seq Problem Statements
Eg: Machine Translation Eng --> Hindi
- Variable length inputs
- Variable length outputs
- No guarantee that input_len == output_len

## High Level Overview
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)

- Training of weights and bias happens together for encoder and decoder block

- `TEACHER FORCING`: In the decoder block, we always send the correct input to each LSTM cell (irrespective of whether the last cell's output was correct or not)

- Teacher forcing is only followed during the train time

- At the test time, the actual outputs recieved are propagated to the next cells. That is, teacher forcing is not applied