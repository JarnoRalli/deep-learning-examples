# 1 PyTorch Examples

This folder contains deep-learning examples, implemented using PyTorch.

---

# 2 PyTorch Basics

Following notebooks introduce basic concepts of PyTorch.

* [PyTorch tensors](./tutorial_tensors.ipynb)
* [PyTorch quickstart guide](./quickstart_tutorial.ipynb)

---

# 3 Deep Learning Examples

Examples of typical problems where deep-learning is used.

## 3.1 Datasets

Some of the examples use data from Kaggle. In order to automatically download the data, you need to create an account in Kaggle and create an API key. opendatasets uses the Kaggle API to download datasets. For more information, take a look at [here](https://github.com/Kaggle/kaggle-api).

## 3.2 Language Models

### 3.2.1 Andrej Karpathy's Makemoore Series

* [Bigram language model](./Bigram_language_model.ipynb)
  * Andrej Karpathy's example regarding a Bigram character level language model.
* [MLP, Bengio 2003, part 1](./MLP_language_model_Bengio_2003_part_1.ipynb)
  * Andrej Karpathy's example regarding an MLP character level language model, based [Bengio et al.'s (2003)](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf) model.
  * This is the initial model.
* [MLP, Bengio 2003, part 2](./MLP_language_model_Bengio_2003_part_2.ipynb)
  * Andrej Karpathy's example regarding an MLP character level language model, based [Bengio et al.'s (2003)](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf) model.
  * This example introduces batch normalization.
* [MLP, Bengio 2003, part 3](./MLP_language_model_Bengio_2003_part_3.ipynb)
  * Andrej Karpathy's example regarding an MLP character level language model, based [Bengio et al.'s (2003)](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf) model.
  * Same as part 2, but the code has been PyTorchified, i.e. the code mimics PyTorch layers.
  * Visualises the following:
    * Activation distribution
    * Gradient distribution
    * Weight gradient distribution
    * Update to weights ratio, see [1]
* [MLP, Bengio 2003, manual back-propagation](./MLP_language_model_Bengio_2003_manual_backprop.ipynb)
  * Builds backpropagation manually, step by step, without using autograd.
  * This is not complete yet, perhaps one day I'll complete it...
* [Implementation of the Wavenet for NLP](./Van_den_Oord_wavenet.ipynb)
  * Andrej Karpathy's example of a wavenet implementation for NLP, based on [van den Oord et al.'s (2016)](https://arxiv.org/pdf/1609.03499.pdf) model.

[1] Update to weights ratio $\dfrac{lr \cdot \nabla}{weight}$, where $lr$ is the learning rate and $\nabla$ is the gradient

## 3.3 Regression

* [House price prediction](./house_price_prediction.ipynb)
  * House price prediction

## 3.4 Recommendation

* [RecSys Challenge 2015](./GNN_recommendation_system.ipynb)
  * This example is related to the 2015 RecSys challenge, the idea being to associate clicks leading to purchase events in a web-shop.
  This information can then be used as a basis for a recommender system
  * This approach uses a GNN
