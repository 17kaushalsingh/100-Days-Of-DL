# Exponentially Weighted Moving Average
    - Used in time series forecasting, financial forecasting, signal processing
    - Used in momentum optimizer

    - The latest data points have higher weights as compared to the earlier points
    - The weightage of previous points decays over time

## Formula
![alt text](image-1.png)

    - V is the EWMA
    - Theta is the independent variable
    - Beta is the param (0 to 1)
    - The EWMA can be thought of as noraml average of last 1/(1 - beta) days
        ==> Jitna jyada beta ka val, purame points ko utna importance
        ==> Beta ka val lkam --> latest points k nazdeek line hogi
    
    - Generally, beta is 0.9 in DL algorithms and optimization problems

![alt text](image-2.png)