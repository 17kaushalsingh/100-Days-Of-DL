# 100 Days of Deep Learning

## Creating a conda env
Run the following command in conda base env
```sh
conda env create -f tf.yml
```
To verify if tensorflow is installed properly, run the below command and check for tensorflow version
```sh
conda activate tf && python -c "import tensorflow as tf; print(f'TensorFlow version: {tf.__version__}')"
```

## References
1. [Campus X Official Notes for 100 Days of Deep Learning](https://drive.google.com/file/d/1PlYzQX_P8NPK9Qel6RA7TZhlZ9SPMz-k/view?usp=drive_link)