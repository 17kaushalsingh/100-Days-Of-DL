# Regularization
- Helps reduce overfitting
- Try applying regularization whenever overfitting occurs
![alt text](image.png)

## L1 Regularization (LASSO)
- Adds a penalty to the loss function proportional to the absolute value of the weights
- This encourages sparsity in the model, effectively driving some weights to zero and performing feature selection
- Penalty is the L1 norm
- Mathematical representation of the penalty term: λ∑∣w<sub>i</sub>∣
- The penalty is the sum of mod of weights
- L1 regularization gives a more sparse model than the L2 regularization

## L2 Regularization (RIDGE)
- Adds a penalty to the loss function proportional to the square of the weights
- This encourages smaller weights but rarely forces them to zero.
- It helps to reduce the impact of large weights and makes the model less sensitive to individual features
- Penalty is the L2 norm
- Mathematical representation of the penalty term: λ∑w<sub>i</sub><sup>2</sup>​
- Most commonly used between all regularization techniques
- Also called as weight decay parameter
- The penalty is the sum of square of weights
- The biases are not considered in regularization
- Lambda is a hyperparameter
- Increasing lambda increases the weightage of regularization penalty in the loss function

## Elastic Net Regularization
- Combines L1 and L2 regularization, adding both penalties to the loss function
- This can provide a balance between feature selection (L1) and weight shrinkage (L2)
- Mathematical representation of the penalty term: λ<sub>1</sub> ∑∣w<sub>i</sub>∣ +λ<sub>2</sub> ∑w<sub>i<sup>2</sup></sub>