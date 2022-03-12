# Deep Learning Examples

This is a collection of deep learning examples, tests and related material. Some of the examples are based on courses and tests I've done
along the years, which I'd like to mention here:

* [Deep Learning (Cousera)](https://www.coursera.org/specializations/deep-learning?)
* [Deep Learning: Advanced Computer Vision by Lazy Programmer (Udemy)](https://www.udemy.com/course/advanced-computer-vision)

# Folder Structure

* **[conda](./conda/README.md)** contains Conda virtual environment files
* **[large_files](./large_files/README.md)** some of the examples download training and testing images to this folder

# Testing Environment

Testing and executing the exaples has been done in a system with the following characteristics:

* **OS** Ubuntu 20.04
* **GPU** GeForce GTX 1070

# Setting Up a Virtual Environment

Most of the examples can be run using an environment with the official TensorFlow 2. Those examples that
use the Object Detection API, require the API to be installed separately.

## TensorFlow 2 Version 2.6.0

First download and install Anaconda or Miniconda. After this create a virtual environment with TensorFlow 2, OpenCV and related packages:

```bash
cd conda
conda env create -f tensorflow2_gpu.yml
```

Activate the environment, and start Jupyter

```bash
conda activate tensorflow2-gpu
jupyter notebook
```

## TensorFlow 2 with Object Detection API

These instructions create an environment with both TensorFlow 2 and 
the Object Detection API. First create an environment with TensorFlow 2,
and test the installation:

```bash
cd conda
conda env create -f tensorflow_object_detection.yml
conda activate tensorflow-object-detection
python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```

Clone the Object Detection API repo, install it using pip, and
test that it works:

```bash
sudo apt-get install protobuf-compiler
cd TensorFlow
git clone https://github.com/tensorflow/models.git
cd models
git checkout 68039be4aa31fc0d8472a86f536c04e565cb1817
cd research
protoc object_detection/protos/*.proto --python_out=.
cp object_detection/packages/tf2/setup.py .
python -m pip install .
python object_detection/builders/model_builder_tf2_test.py
```
