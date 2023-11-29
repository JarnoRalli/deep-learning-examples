# 1 Virtualenv

Virtualenv is a tool for creating isolated virtual Python environments.

## 1.1 Requirement Files

* **[financial.txt](./financial.txt)**. Requirements for the FinancialEngineering examples.
* **[tensorflow2.txt](./tensorflow2.txt)**. Requirements for TensorFlow 2 examples

If you want NVidia GPU support for TensorFlow or PyTorch, you need to install the required drivers and CUDA.

## 1.2 Installation

The proposed method for installing `virtualenv` is using `pipx`

```bash
pipx install virtualenv
```

## 1.3 Create a New Environment and Activate It

In order to create a new virtual environment, execute the following command in the directory
where you want the virtual environment to created:

```bash
virtualenv <NAME-OF-THE-ENVIRONMENT>
```

Above command will create a directory called `<NAME-OF-THE-ENVIRONMENT>`, inside the current directory, that contains all the packages etc.
of the virtual environment. In order to activate the virtual environment, execute the following:

```bash
source <NAME-OF-THE-ENVIRONMENT>/bin/activate
```

Once you have activated the virtual environment, you can install Python packages to it

```bash
pip install -r <PATH-TO-THE-REQUIREMENTS-FILE>
```

## 1.4 Deactivate an Environment

You can deactivate an activ virtual environment as using the following command:

```bash
deactivate
```

## 1.5 Test GPU/CUDA Support

### 1.5.1 PyTorch

Activate the pytorch virtual environment and execute the following in Python:

```python
import torch
torch.cuda.is_available()
```

You'll get `True/False` output indicating whether acceleration is available.

### 1.5.2 TensorFlow 2

Activate the tensorflow 2 virtual environment and execute the following:

```bash
python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```
