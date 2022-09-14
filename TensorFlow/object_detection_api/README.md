# TensorFlow 2 Object Detection API

Un-official TensorFlow components, like the Object Detection API, can be downloaded into this folder for
installation purposes. All the contents of this folder will be ignored by `.gitignore`.

---

# Installing TensorFlow 2 with Object Detection API

## Creating a Virtual Environment Using YAML file

Following instructions create a Conda environment where the Object Detection API can
be installed later on. Execute the following commands from the root directory of this repo:

```bash
cd conda
conda env create -f tensorflow2_object_detection.yml
conda activate tensorflow2-object-detection
python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

The `tensorflow2-object-detection` environment doesn't contain `TensorRT`, so you're likely
to see warnings saying that `libnvinfer.so.*` is not found. Since `TensorRT` is optional, missing
`libnvinfer.so.*` should not matter.

## Installing Object Detection API

You can install TensorFlow 2 Object Detection API by executing the following commands from
the root directory of this repo:

```bash
cd TensorFlow
cv object_detection
sudo apt-get install protobuf-compiler
git clone https://github.com/tensorflow/models.git
cd models
git checkout 68039be4aa31fc0d8472a86f536c04e565cb1817
cd research
protoc object_detection/protos/*.proto --python_out=.
cp object_detection/packages/tf2/setup.py .
python -m pip install .
python object_detection/builders/model_builder_tf2_test.py
```

