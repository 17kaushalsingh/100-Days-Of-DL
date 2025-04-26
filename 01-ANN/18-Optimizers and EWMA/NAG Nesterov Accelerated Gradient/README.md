# NAG
    - Kind of a damped oscillation
    
![alt text](../../../README_Assets/01-ANN/18-Optimizers and EWMA/NAG Nesterov Accelerated Gradient/image.png)
![alt text](../../../README_Assets/01-ANN/18-Optimizers and EWMA/NAG Nesterov Accelerated Gradient/image-1.png)

    - First the update happens using velocity (momentum term)
    - Then, the update happens using the gradient at new location

## Look ahead term
![alt text](../../../README_Assets/01-ANN/18-Optimizers and EWMA/NAG Nesterov Accelerated Gradient/image-2.png)

## Disadvantage
    - May lead to being stuck in local minima