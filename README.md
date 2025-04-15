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

# Creating a conda env with GPU Support
Run the following command in conda base env
```sh
conda create --name tf_gpu python=3.9
conda deactivate
conda activate tf_gpu
```
Install CUDA toolkit and CuDNN
```sh
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
```
Install Tensorflow
```sh
pip install --upgrade pip
pip install "tensorflow<2.11" OR pip install https://storage.googleapis.com/tensorflow/versions/2.19.0/tensorflow-2.19.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
```

Check installation
```sh
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```