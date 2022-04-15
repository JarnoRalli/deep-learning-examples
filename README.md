# Deep Learning Examples

This is a collection of deep learning examples, tests and related material. Some of the examples are based on courses and tests I've done
along the years, which I'd like to mention here:

* [Deep Learning (Coursera)](https://www.coursera.org/specializations/deep-learning?)
* [Deep Learning: Advanced Computer Vision by Lazy Programmer (Udemy)](https://www.udemy.com/course/advanced-computer-vision)

# Folder Structure

* **[conda](./conda/README.md)** contains Conda virtual environment files
* **[large_files](./large_files/README.md)** some of the examples download training and testing images to this folder
* **[TensorFlow](./TensorFlow/README.md)** a directory where you can clone TensorFlow Object Detection API

---

# Testing Environment

Testing and executing the examples has been done in a system with the following characteristics:

* **OS** Ubuntu 20.04
* **GPU** GeForce GTX 1070

---

# Setting Up a Virtual Environment

In order to run the Jupyter notebooks, install Anaconda or Miniconda, and create the required virtual environment(s) as
per these [instructions](./conda/README.md). Once you have installed a virtual environment, you can activate it as follows:

```bash
conda activate <NAME-OF-THE-ENVIRONMENT>
```

You can get a list of installed environment by executing the following command:

```bash
conda env list
```

Once the virtual environment is activated, you can open any of the Jupyter notebooks by
executing the following command in the root directory of this repo:

```bash
jupyter notebook
```

---

# Examples

* [Simple classification example](./simple_classification_example.ipynb)
* [Simple linear regression example](./simple_linear_regression_example.ipynb)
* [ANN handwritten number classification example](./ANN-handwritten-digits-classification.ipynb)
* [CNN cifar 10 classification example](./CNN_cifar_10_classification.ipynb)
* [VGG transfer learning example](./VGG_transfer_learning_fruit_data.ipynb)
* [ResNet transfer learning example](./ResNet_transfer_learning_fruit_data.ipynb)
* [ResNet implementation in TensorFlow/Keras](./ResNet_implementation.ipynb)
* [Image embedding example using Fiftyone](./Fiftyone_image_embedding_example.ipynb)
* [Tensorflow Object Detection API (SSD) example](./SSD_tensorflow2_object_detection_example.ipynb)
* [Neural style transfer part 1, reproducing content](./Neural_style_transfer_part_1.ipynb)
* [Neural style transfer part 2, reproducing style](./Neural_style_transfer_part_2.ipynb)
* [Neural style transfer part 3, reproducing content and style](./Neural_style_transfer_part_3.ipynb)
* [Class activation maps](./class_activation_maps.ipynb)


