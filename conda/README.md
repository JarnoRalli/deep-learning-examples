# Conda Virtual Environments

In the past I have mostly used miniconda for creating and handling virtual environments. As of 2023, using Ubuntu 20.04, I have
had lots of issues with both installing miniconda and creating virtual environments. I will leave these here for historical reasons, but
I will move onto using something more stable.

* **tensorflow2_gpu.yml**. Contains the following packages:
  * Jupyter
  * OpenCV
  * TensorFlow (GPU)
  * TensorFlow datasets
* **tensorflow2_object_detection.yml**. This is a base environment for installing the Object Detection API. Contains the following packages:
  * Jupyter
  * OpenCV
  * TensorFlow
  * TensorFlow datasets
* **machine-vision**. Contains the following packages:
  * Jupyter
  * OpenCV
  * TensorFlow (GPU)
  * TensorFlow datasets
  * PyTorch
  * Torchvision
  * umap-learn
* **finance.yml**. Contains the following packages:
  * numpy
  * jupyter
  * scikit-learn
  * matplotlib
  * pandas
  * yfinance

You can create a new virtual environment as follows:

```bash
conda env create -f <NAME-OF-THE-FILE>
```

Once the environment has been created, you can activate it by executing the following command:

```bash
conda activate <NAME-OF-THE-ENVIRONMENT>
```

## Testing TensorFlow

Following tests the CPU implementation:

```bash
python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```

Following tests the GPU implementation:

```bash
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

