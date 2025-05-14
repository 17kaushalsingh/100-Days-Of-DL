# Types of RNNs
1. Many to One
2. One to Many
3. Many to Many
4. One to One

## Many to One
- Input: SEQUENTIAL DATA
- Output: SCALAR
- Use case: SENTIMENT ANALYSIS, RATING PREDICTION
![alt text](image.png)

## One to Many
- Input: NON SEQUENTIAL DATA (fed at once)
- Output: SEQUENTIAL DATA (generates data in form of timestamps)
- Use case: IMAGE CAPTIONING, MUSIC GENERATION

## Many to Many (Sequence to Sequence Model)
- Input: SEQUENTIAL DATA
- Output: SEQUENTIAL DATA (generates data in form of timestamps)
- Two types
    1. Same length many to many
        Use case: PARTS OF SPEECH TAGGING, NAMED ENTITY RECOGNITION
    2. Variable length many to many (Also called encoder - decoder)
        Use case: MACHINE TRANSLATION

## One to One
- Not an RNN
- Input: NON SEQUENTIAL DATA (fed at once)
- Output: NON SEQUENTIAL DATA (output at once)
- Use case: IMAGE CLASSIFICATION
