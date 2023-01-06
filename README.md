# Final Project MLOps
==============================
## Project desctiption - Image Classification for Brain Tumors

### Overall goal of the project
The goal of this project is to use image classification model to solve a binary classification task to predict whether a brain scan depicts a brain with a tumor or no. 

### What framework are you going to use (Kornia, Transformer, Pytorch-Geometrics)
Since we chose animage classification problem, we plan to use the to use <a href="https://github.com/rwightman/pytorch-image-models" target="_blank">Pytorch Image Models</a>.

### How to you intend to include the framework into your project
We will use one of the models from the framework with pretrained weights to complete the task. 

### What data are you going to run on (initially, may change)
We are going to use a <a href="https://www.kaggle.com/datasets/preetviradiya/brian-tumor-dataset" target="_blank">Brain tumor dataset</a> obtained from kaggle. The dataset is comprised of brain scans, split into healthy brains (0) and brains with tumors (1). The dataset we chose is quite simple since the objective of the project is to employ the techniques shown in the course and not the project itself. 

### What deep learning models do you expect to use
The intention is to use a model with pretrained weights and train it on the dataset above. As a first approach we will use the <a href="https://huggingface.co/docs/timm/models/efficientnet" target="_blank">EfficientNet</a>. If 

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
