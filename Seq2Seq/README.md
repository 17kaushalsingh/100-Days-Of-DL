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

# Improving Performance of Seq2Seq Models
1. Use embeddings
    - Embeddings are low dimensional dense representaions of the vectors
    - Use embeddings in both the encoder block as well as the decoder block
    - May use pretrained embeddings as well as trainable embedding layers

2. Use Deep LSTM cells while formulating the architecture
    - Helps capture long term dependencies (useful in long inputs such as paragraphs, books, etc)
    - Increases overall model capability to learn very minute features (provided enough training data is there to mitigate overfitting)
    - Helps learn the heirarchical representation of the data

3. Reverse the input vector
    - Eg: Input: Think About It, Output: Soch Lo
    - We could send it as: Input: It About Think, Output: Lo Soch
    - This is not helpful always, but for languages like english where the initial words do the heavylifting this may be helpful
    - The idea is to reduce the distance of Think and Soch, weird but works