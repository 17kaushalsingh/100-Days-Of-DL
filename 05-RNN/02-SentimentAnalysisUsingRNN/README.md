## Integer Encoding
    - Form vocabulary of all unique words
    - Encode each word with a unique integer
![alt text](../../README_Assets/05-RNN/02-SentimentAnalysisUsingRNN/image.png)

    - But since words are of different sizes
    - We do padding
![alt text](../../README_Assets/05-RNN/02-SentimentAnalysisUsingRNN/image-1.png)

## Embeddings
    - The vectors generated in this case are real valued vectors
    - These are generated based on the complete document and its meaning
    - This representation is dense vector
    - It can capture semantic meaning (meaning of a word in context)
    - Eg: word2vec, glove
    - In keras, we have a dedicated layer for embeddings, which can learn embedding from data
    - For embeddin, the data should be integer encoded
![alt text](../../README_Assets/05-RNN/02-SentimentAnalysisUsingRNN/image-2.png)

    - Generally, the custom embeddings are better than pretrained word2vec or glove embeddings