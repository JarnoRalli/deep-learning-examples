# Deep Learning Examples

This is a collection of deep learning examples, tests and related material. Some of the examples are based on courses and tests I've done
along the years, which I'd like to mention here:

* [Deep Learning (Coursera)](https://www.coursera.org/specializations/deep-learning?)
* [Deep Learning: Advanced Computer Vision by Lazy Programmer (Udemy)](https://www.udemy.com/course/advanced-computer-vision)

# Folder Structure

* **[conda](./conda/README.md)** contains files for creating Conda virtual environments
* **[TensorFlow](./TensorFlow/README.md)** deep learning examples using TensorFlow 2

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

# Additional Documentation

Additional [documentation](./documentation/README.md) regarding the notation, neural network model etc. can be found [here](./documentation/README.md)

---




