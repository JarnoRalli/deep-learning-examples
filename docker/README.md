# 1 Docker

Instead of using an virtual environment, such as Conda etc., for installing the required
packages, another option is to use Docker container that already has all the required dependencies
installed. In this case we run the Jupyter server inside the Docker container and connect
to it using a browser running in the host.

## 1.1 Installing Nvidia's Container Toolkit

Before creating the docker image, you need to install Nvidia's Container Toolkit. Instructions can be found here:

* [https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

Once you have installed everything, verify that Nvidia's Container Toolkit is working by executing:

```bash
sudo docker run --rm --gpus all nvidia/cuda:11.6.2-base-ubuntu20.04 nvidia-smi
```

You should see output following (or similar) output:

```bash
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.60.13    Driver Version: 525.60.13    CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  On   | 00000000:09:00.0  On |                  N/A |
| 32%   38C    P0    34W / 151W |    735MiB /  8192MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
+-----------------------------------------------------------------------------+
```

## 1.2 Docker Containers

Following Docker containers are available:

* [Dockerfile.pytorch2.9.0](./Dockerfile.pytorch2.9.0)
  * Dockerfile with PyTorch 2.9.0, cuda12.8 and cudnn9
  * Use with [requirements-pytorch.txt](./requirements-pytorch.txt)
* [Dockerfile.tensorflow2.2.0](./Dockerfile.tensorflow2.2.0)
  * Dockerfile with TensorFlow 2.2.0 (GPU)
  * Use with [requirements-tensorflow.txt](./requirements-tensorflow.txt)

## 1.3 Create the Docker Image

After this you can create the docker image used in the examples.

```bash
cd deep-learning-examples/docker
docker build -t <NAME> -f <DOCKERFILE> --build-arg requirements=<REQUIREMENTS-FILE> .
```

, where `<NAME>` is the name you want to give the container, `<DOCKERFILE>` is the Dockerfile used for
creating the container and `<REQUIREMENTS-FILE>` is the requirement file given to `pip` when building the container.

## 1.4 Running Jupyter Inside a Docker Container

Execute the following, inside the directory where the Jupyter notebooks are (e.g.
`deep-learning-examples/TensorFlow`), in order to start the container:

```bash
docker run -it \
  --publish 8888:8888 \
  --volume $(pwd):/workspace/ \
  -e NVIDIA_DRIVER_CAPABILITIES=all \
  --gpus all <NAME> bash
```

Replace `<NAME>` with the name of the container. Execute the following, inside the running container, in order to
launch the Jupyter server:

```bash
jupyter lab --ip=0.0.0.0 --no-browser --allow-root
```

You should see output similar to the following:

```bash
To access the notebook, open this file in a browser:
    file:///root/.local/share/jupyter/runtime/nbserver-95-open.html
Or copy and paste one of these URLs:
    http://ba2ecabdb2f8:8888/?token=d6105755dae78e8d4c6138a7a6ff42907b2e5b3f9be17456
 or http://127.0.0.1:8888/?token=d6105755dae78e8d4c6138a7a6ff42907b2e5b3f9be17456
```

Start a web-browser in the host machine, and use any of the links, e.g.
`http://127.0.0.1:8888/?token=d6105755dae78e8d4c6138a7a6ff42907b2e5b3f9be17456` (use the actual link that was
output when starting the Jupyter server) to connect to the Jupyter server.
4
