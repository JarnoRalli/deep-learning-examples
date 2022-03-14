# Conda Virtual Environments

* **tensorflow2_gpu.yml**. Contains the following packages:
  * Jupyter
  * OpenCV
  * TensorFlow (GPU)
  * TensorFlow datasets
* **tensorflow_object_detection.yml**. This is a base environment for installing the Object Detection API. Contains the following packages:
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

You can create a new virtual environment as follows:

```bash
conda env create -f <NAME-OF-THE-FILE>
```

Once the environment has been created, you can activate it by executing the following command:

```bash
conda activate <NAME-OF-THE-ENVIRONMENT>
```

---

# Installing TensorFlow 2 with Object Detection API

These instructions create an environment with both TensorFlow 2 and 
the Object Detection API. In order to create an environment with TensorFlow 2,
execute the following from the root directory of this repo:

```bash
cd conda
conda env create -f tensorflow_object_detection.yml
conda activate tensorflow-object-detection
python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```

In order to install the TensorFlow Object Detection API, clone the repo, compile the Protobuf
definitions, and install it using pip, execute the following from the root directory of this repo:

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

---
