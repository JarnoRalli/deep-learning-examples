# 1 Conda Virtual Environments

In the past I have mostly used miniconda for creating and handling virtual environments. As of 2023, using Ubuntu 20.04, I have
had lots of issues with both installing miniconda and creating virtual environments.


## 1.1 Libmamba Solver

Conda's own solver is very slow, so I recommend using `Libmamba`. To use the new solver, first update conda in the base environment:

```bash
conda update -n base conda
```

Then install and activate `Libmamba` as the solver:

```bash
conda install -n base conda-libmamba-solver
conda config --set solver libmamba
```

## 1.2 Environments

Following YAML configuration files for Conda environments are available:

Following YAML configuration files have been defined:

* [tensorflow2_gpu.yml](./tensorflow2_gpu.yml)
  * **Environment name:** tensorflow2
* [tensorflow2_object_detection.yml](./tensorflow2_object_detection.yml)
  * **Environment name:** tensorflow2-object-detection
  * This is a base environment for installing the Object Detection API
* [pytorch_gpu.yml](./pytorch_gpu.yml)
  * **Environment name:** pytorch
  * Environment with PyTorch (GPU)
* [finance.yml](./financial.yml)
  * **Environment name:** financial
  * Environment for financial engineering.
* [huggingface_gpu.yml](./huggingface_gpu.yml)
  * **Environment name:** huggingface_gpu
  * Environment for using PyTorch and TensorFlow models from Hugging Face

You can create a new virtual environment as follows:

```bash
conda env create -f <NAME-OF-THE-FILE>
```

Once the environment has been created, you can activate it by executing the following command:

```bash
conda activate <NAME-OF-THE-ENVIRONMENT>
```

## 1.3 Updating System Paths for TensorFlow Environments

Official TensorFlow installation [guide](https://www.tensorflow.org/install/pip) mentions that the `LD_LIBRARY_PATH` needs to be updated
when a TensorFlow-environments are used. This can be automated. First you need to activate the environment, and then execute the following:

```bash
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
source $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
```

## 1.4 Test GPU/CUDA Support

### 1.4.1 PyTorch

Activate the pytorch virtual environment and execute the following in Python:

```python
import torch
torch.cuda.is_available()
```

You'll get `True/False` output indicating whether acceleration is available.

### 1.4.2 TensorFlow 2

Activate the tensorflow 2 virtual environment and execute the following:

```bash
python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

