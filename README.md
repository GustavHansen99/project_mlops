# Final Project MLOps

==============================

## Project description - Image Classification for Brain Tumors

### Overall goal of the project

The goal of this project is to use image classification model to solve a binary classification task to predict whether a brain scan depicts a brain with a tumor or no.

### What framework are you going to use (Pytorch Image Models, Transformer, Pytorch-Geometrics)

Since we chose an image classification problem, we plan to use the to use <a href="https://github.com/rwightman/pytorch-image-models" target="_blank">Pytorch Image Models</a>. This framework provides 70 different image models for various computer vision tasks (classification, segmentation, etc).

### How to you intend to include the framework into your project

We will use one of the models from the framework with pretrained weights to complete the task. We will further train the weights with our own dataset in order to get better accuracy for our task.

### What data are you going to run on (initially, may change)

We are going to use a <a href="https://www.kaggle.com/datasets/preetviradiya/brian-tumor-dataset" target="_blank">Brain tumor dataset</a> obtained from kaggle. The dataset is comprised of brain scans, split into healthy brains (0) and brains with tumors (1). The dataset we chose is quite simple since the objective of the project is to employ the techniques shown in the course and not the project itself.

### What deep learning models do you expect to use

The intention is to use a model with pretrained weights and train it on the dataset above. As a first approach we will use the <a href="https://huggingface.co/docs/timm/models/efficientnet" target="_blank">EfficientNet</a>.

## Start docker container

```
docker run --rm -it --shm-size=8G --gpus all --device /dev/nvidiactl --device /dev/nvidia0 -e WANDB_API_KEY=$WANDB_API_KEY -v secrets:secrets gcr.io/dtumlops-project-group-55/trainer:latest
```

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
