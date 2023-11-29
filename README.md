# 1 Deep Learning Examples

This is a collection of deep learning examples, tests and related material. Some of the examples are based on courses and tests I've done
along the years, which I'd like to mention here:

* [Deep Learning (Coursera)](https://www.coursera.org/specializations/deep-learning?)
* [Deep Learning: Advanced Computer Vision by Lazy Programmer (Udemy)](https://www.udemy.com/course/advanced-computer-vision)
* [Deep Learning: Financial Engineering and Artificial Intelligence in Python by Lazy Programmer](https://deeplearningcourses.com/c/ai-finance)

All of the above are fantastic courses and if you're interested in those subjects, you should consider taking them.

---

# 2 Folder Structure

## 2.1 Virtual Environments and Docker Images

* **[Virtualenv](./virtualenv/README.md)** instructions for setting up virtual environments using `virtualenv`
* **[Docker](./docker/README.md)** contains files for creating Docker container for running the examples
* **[Conda](./conda/README.md)** contains files for creating Conda virtual environments for running the examples

## 2.2 Generic Explanations

* **[Documentation](./documentation/README.md)**

## 2.3 Deep Learning and Related Examples

* **[TensorFlow](./TensorFlow/README.md)** deep learning examples using TensorFlow 2
* **[PyTorch](./PyTorch/README.md)** deep learning examples using PyTorch
* **[Financial Engineering](./FinancialEngineering/README.md)** financial engineering using Python and Ai
* **[Hugging Face](./HuggingFace/README.md)** examples of using models from Hugging Face

---

# 3 Testing Environment

Testing and executing the examples has been done in a system with the following characteristics:

* **OS** Ubuntu 20.04
* **GPU** GeForce GTX 1070

## 3.1 Pre-commit

This repo uses pre-commit git-hooks to verify the code before it is pushed. After cloning
the repo, install the pre-commit package into your Python environment:

```shell
pip install pre-commit
```

and then install the pre-commit checks:

```shell
pre-commit install
```

Pre-commit is run automatically every time code is committed. You can also run pre-commit manually as follows:

```shell
pre-commit run --all-files
```

---

# 4 Running the Examples

You can either create a Conda virtual environment, or a Docker container, for running the examples. In order to do so,
take a look at the instructions in [conda](./conda/README.md) and [docker](./docker/README.md) directories.

---

# 5 Additional Documentation

Additional [documentation](./documentation/README.md) regarding the notation, neural network model etc. can be found [here](./documentation/README.md)

---

