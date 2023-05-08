# TensorFlow Examples

This folder contains deep-learning examples, implemented using TensorFlow 2.

# 1 Folder Structure

* **[object_detection_api](./object_detection_api/README.md)** a directory where you can install the TensorFlow Object Detection API
* **[large_files](./large_files/README.md)** some of the examples download training and testing images to this folder

---

# 2 TensorFlow 2 Basics

These notebooks introduce basic concepts of TensorFlow and TensorFlow 2

* [Data type basics](./Basics_data_type_tutorial.ipynb)
* [Automatic differentiation](./Basics_automatic_differentiation.ipynb)
* [TensorFlow 2 functional API](./Basics_functional_api.ipynb)
* [Tensor shapes in Keras](./Basics_tensor_shapes_in_keras.ipynb)

---

# 3 Deep Learning Examples

Examples of typical problems where deep-learning is used.

## 3.1 Datasets

Some of the examples use data from Kaggle. In order to automatically download the data, you need to create an account in Kaggle and create an API key. opendatasets uses the Kaggle API to download datasets. For more information, take a look at here.

## 3.2 Classification

* [Simple classification example](./simple_classification_example.ipynb)
  * Simple linear classification example that uses the breast cancer dataset
* [ANN handwritten number classification example](./ANN-handwritten-digits-classification.ipynb)
  * Example of a fully-connected, with input size of (28, 28), network for handwritten number classification
* [CNN cifar 10 classification example](./CNN_cifar_10_classification.ipynb)
  * Example of using a CNN to classify input images into 10 different categories. Uses [CIFAR-10](https://www.kaggle.com/c/cifar-10) dataset.
* [Classification using imbalanced data sets](./Classification_on_imbalanced_data.ipynb)
  * Example showing how to use class weights with imbalanced classification data sets
* [Classification using autoencoder](./Classification_autoencoder.ipynb)
  * Example showing how to use autoencoder to detect abnormal data

## 3.3 Regression

* [Simple linear regression example](./simple_linear_regression_example.ipynb)
  * Example of linear regression using the diabetes data set from Sklearn.

## 3.4 Transfer Learning

* [VGG transfer learning example](./VGG_transfer_learning_fruit_data.ipynb)
  * Example of transfer learning, using a fully trained VGG16 from TensorFlow. New classification head is trained on the [Fruits 360](https://www.kaggle.com/moltean/fruits) data
* [ResNet transfer learning example](./ResNet_transfer_learning_fruit_data.ipynb)

## 3.5 Neural Style Transfer

* [Neural style transfer part 1, reproducing content](./Neural_style_transfer_part_1.ipynb)
* [Neural style transfer part 2, reproducing style](./Neural_style_transfer_part_2.ipynb)
* [Neural style transfer part 3, reproducing content and style](./Neural_style_transfer_part_3.ipynb)

## 3.6 Object Detection

* [Tensorflow Object Detection API (SSD) example](./SSD_tensorflow2_object_detection_example.ipynb)

## 3.7 Miscellaneous

* [ResNet implementation in TensorFlow/Keras](./ResNet_implementation.ipynb)
* [Image embedding example using Fiftyone](./Fiftyone_image_embedding_example.ipynb)
* [Class activation maps](./class_activation_maps.ipynb)

## 3.8 GAN (Generative Adversial Network)

* [GAN for generating MNIST digits](./GAN_mnist_digits_plain.ipynb)
  * Example of a GAN learning to generate hand written digits, based on MNIST dataset.
* [DCGAN for generating MNIST digits](./DCGAN_mnist_digits.ipynb)
  * Example of a Deep Convolutional GAN learning to generate hand written digits, based on MNIST dataset.
