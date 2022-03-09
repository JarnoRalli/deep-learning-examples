# Deep Learning Examples

This is a collection of deep learning examples, tests and related material. Some of the examples are based on courses and tests I've done
along the years, which I'd like to mention here:

* [Deep Learning from Cousera](https://www.coursera.org/specializations/deep-learning?)
* [Deep Learning: Advanced Computer Vision from Udemy](https://www.udemy.com/course/advanced-computer-vision)

# Folder Structure

* **conda** contains Conda virtual environment files
* **large_files** some of the examples download training and testing images to this folder

# Testing Environment

Testing and executing the exaples has been done in a system with the following characteristics:

* **OS** Ubuntu 20.04
* **GPU** GeForce GTX 1070

# Setting Up a Virtual Environment

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
