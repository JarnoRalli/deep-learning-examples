#FROM nvcr.io/nvidia/tensorrt:22.03-py3
FROM tensorflow/tensorflow:latest-gpu

# To get video driver libraries at runtime (libnvidia-encode.so/libnvcuvid.so)
ENV NVIDIA_DRIVER_CAPABILITIES $NVIDIA_DRIVER_CAPABILITIES,video,compute,graphics,utility

# Ignore sudo warning for pip
ENV PIP_ROOT_USER_ACTION=ignore
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install required packages. 
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    wget python3 python3-pip python3.8-venv python-is-python3 python3-dev \
    gcc \
    make \
    libglvnd0 \
    libgl1 \
    libglx0 \
    libegl1 \
    glmark2 \
    mesa-utils \
    git && \
    python3 -m pip install --upgrade build && \
    rm -rf /var/lib/apt/lists/* && \
    python -m pip install --upgrade pip && \
    apt-get autoremove -y

ARG requirements
ADD $requirements ./

RUN pip install -r $requirements

# Set up "home" directory for Jupyter user
RUN useradd -ms /bin/bash jupyter
ENV JUPYTER_RUNTIME_DIR=/home/jupyter
ENV JUPYTER_DATA_DIR=/home/jupyter

# Set the workdir
WORKDIR /workspace

