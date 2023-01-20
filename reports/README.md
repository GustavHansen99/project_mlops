---
layout: default
nav_exclude: true
---

# Exam template for 02476 Machine Learning Operations

This is the report template for the exam. Please only remove the text formatted as with three dashes in front and behind
like:

```--- question 1 fill here ---```

where you instead should add your answers. Any other changes may have unwanted consequences when your report is auto
generated in the end of the course. For questions where you are asked to include images, start by adding the image to
the `figures` subfolder (please only use `.png`, `.jpg` or `.jpeg`) and then add the following code in your answer:

```markdown
![my_image](figures/<image>.<extension>)
```

In addition to this markdown file, we also provide the `report.py` script that provides two utility functions:

Running:

```bash
python report.py html
```

will generate an `.html` page of your report. After deadline for answering this template, we will autoscrape
everything in this `reports` folder and then use this utility to generate an `.html` page that will be your serve
as your final handin.

Running

```bash
python report.py check
```

will check your answers in this template against the constrains listed for each question e.g. is your answer too
short, too long, have you included an image when asked to.

For both functions to work it is important that you do not rename anything. The script have two dependencies that can
be installed with `pip install click markdown`.

## Overall project checklist

The checklist is *exhaustic* which means that it includes everything that you could possible do on the project in
relation the curricilum in this course. Therefore, we do not expect at all that you have checked of all boxes at the
end of the project.

### Week 1

* [X] Create a git repository
* [X] Make sure that all team members have write access to the github repository
* [X] Create a dedicated environment for you project to keep track of your packages
* [X] Create the initial file structure using cookiecutter
* [X] Fill out the `make_dataset.py` file such that it downloads whatever data you need and
* [X] Add a model file and a training script and get that running
* [X] Remember to fill out the `requirements.txt` file with whatever dependencies that you are using
* [X] Remember to comply with good coding practices (`pep8`) while doing the project
* [X] Do a bit of code typing and remember to document essential parts of your code
* [X] Setup version control for your data or part of your data
* [X] Construct one or multiple docker files for your code
* [X] Build the docker files locally and make sure they work as intended
* [X] Write one or multiple configurations files for your experiments
* [X] Used Hydra to load the configurations and manage your hyperparameters
* [X] When you have something that works somewhat, remember at some point to do some profiling and see if
      you can optimize your code
* [X] Use Weights & Biases to log training progress and other important metrics/artifacts in your code. Additionally,
      consider running a hyperparameter optimization sweep.
* [X] Use Pytorch-lightning (if applicable) to reduce the amount of boilerplate in your code

### Week 2

* [X] Write unit tests related to the data part of your code
* [X] Write unit tests related to model construction and or model training
* [X] Calculate the coverage.
* [X] Get some continuous integration running on the github repository
* [X] Create a data storage in GCP Bucket for you data and preferable link this with your data version control setup
* [X] Create a trigger workflow for automatically building your docker images
* [X] Get your model training in GCP using either the Engine or Vertex AI
* [X] Create a FastAPI application that can do inference using your model
* [ ] If applicable, consider deploying the model locally using torchserve
* [X] Deploy your model in GCP using either Functions or Run as the backend

### Week 3

* [ ] Check how robust your model is towards data drifting
* [ ] Setup monitoring for the system telemetry of your deployed model
* [ ] Setup monitoring for the performance of your deployed model
* [ ] If applicable, play around with distributed data loading
* [ ] If applicable, play around with distributed model training
* [ ] Play around with quantization, compilation and pruning for you trained models to increase inference speed

### Additional

* [X] Revisit your initial project description. Did the project turn out as you wanted?
* [X] Make sure all group members have a understanding about all parts of the project
* [X] Uploaded all your code to github

## Group information

### Question 1
> **Enter the group number you signed up on <learn.inside.dtu.dk>**
>
> Answer:

55

### Question 2
> **Enter the study number for each member in the group**
>
> Example:
>
> *sXXXXXX, sXXXXXX, sXXXXXX*
>
> Answer:

*s223084, s212893, s213685*

### Question 3
> **What framework did you choose to work with and did it help you complete the project?**
>
> Answer length: 100-200 words.
>
> Example:
> *We used the third-party framework ... in our project. We used functionality ... and functionality ... from the*
> *package to do ... and ... in our project*.
>
> Answer:

For this project we used the third-party framework <a href="https://github.com/rwightman/pytorch-image-models" target="_blank">Pytorch Image Models</a> to use one of the models from the framework with pretrained weights to complete the task, and further further train the weights with our own dataset in order to get better accuracy for our task. To do this, we use the <a href="https://huggingface.co/docs/timm/models/efficientnet" target="_blank">EfficientNet</a> model on a <a href="https://www.kaggle.com/datasets/preetviradiya/brian-tumor-dataset" target="_blank">Brain tumor dataset</a>. We then used the functionality of pytorch lightning and pytorch to do model setup, as well as training and evaluation hereof.

## Coding environment

> In the following section we are interested in learning more about you local development environment.

### Question 4

> **Explain how you managed dependencies in your project? Explain the process a new team member would have to go**
> **through to get an exact copy of your environment.**
>
> Answer length: 100-200 words
>
> Example:
> *We used ... for managing our dependencies. The list of dependencies was auto-generated using ... . To get a*
> *complete copy of our development enviroment, one would have to run the following commands*
>
> Answer:

To manage the dependencies of our project we used a series of requirements files that are relevant to succesfully use our code. These requirements were auto-generated as lists of dependencies using the pipreqs framework that construct a txt file based on the python code in the specified folders. In this way, only the necessary packages from our environments were placed in the list of dependencies. To get a complete copy of our development environment, one would therefore have to do first clone our repository, and then pip install the requirements-files (which also installs the code as a package using the `-e`-flag).

### Question 5

> **We expect that you initialized your project using the cookiecutter template. Explain the overall structure of your**
> **code. Did you fill out every folder or only a subset?**
>
> Answer length: 100-200 words
>
> Example:
> *From the cookiecutter template we have filled out the ... , ... and ... folder. We have removed the ... folder*
> *because we did not use any ... in our project. We have added an ... folder that contains ... for running our*
> *experiments.*
> Answer:

Based on the cookiecutter template we have primarily written code in the `src`-folder, and specifically the `src/models` and `src/data` have been filled out extensively. We have removed the folders: `docs`, `models`, `notebooks` and `references` since we did not use any of the intended template from these folders, and hence they were considered to confuse more than benefit. Moreover, we have added a series of folders that are relevant for this project: `.dvc` (dvc generated files), `.github` (github workflow files), `app` (code used to construct the app using FastAPI to do inference), `config` (configuration files for inference, training, and evaluation), `docker` (dockerfiles), `scripts` (bash training script that is called on runtime from our training dockerfile), and lastly `tests` (the unittests we have conducted).

### Question 6

> **Did you implement any rules for code quality and format? Additionally, explain with your own words why these**
> **concepts matters in larger projects.**
>
> Answer length: 50-100 words.
>
> Answer:

We agreed on writing code by adhering to the pep8 convention in order to ensure that the code format were following the same structure across the group. To ensure code quality and readability we also agreed on writing clear and commented code where necessary. Seen in hindsight, we could have been more thorough in commenting the code, which would make it easier to debug and make changes in the future.

## Version control

> In the following section we are interested in how version control was used in your project during development to
> corporate and increase the quality of your code.

### Question 7

> **How many tests did you implement and what are they testing in your code?**
>
> Answer length: 50-100 words.
>
> Example:
> *In total we have implemented X tests. Primarily we are testing ... and ... as these the most critical parts of our*
> *application but also ... .*
>
> Answer:

In total we have implemented 3 tests. Specifically, we conduct tests related to our data, model and training. Primarily we are testing that the data collection and transformation works as intended, that the model produces the expected output given an input, and that our training and validation improves the model and that both classes are present. In this way, we try to ensure that the "vulnerable" parts of our developed code does not break when making changes to the various parts.

### Question 8

> **What is the total code coverage (in percentage) of your code? If you code had an code coverage of 100% (or close**
> **to), would you still trust it to be error free? Explain you reasoning.**
>
> Answer length: 100-200 words.
>
> Example:
> *The total code coverage of code is X%, which includes all our source code. We are far from 100% coverage of our **
> *code and even if we were then...*
>
> Answer:

The total code coverage of our code is 59%, excluding the test scripts themselves, and including all of our source code. As this percentage reflects, our tests are not exhaustive and does not capture all parts of our code. However, we are aware of this, and one way to the coverage would be to cover more of the training and prediction aspects of our code. We are hence far from 100% coverage of our code, and even if we were it is difficult to completely trust the coverage score as an indicator of the state of a codebase. Code coverage allows us to identify aspects of our code that is not captured by our tests, but does not alone ensure good quality of either the code nor the tests. One still needs to look at the quality of the tests to ensure error free code. Hence, code coverage is only an indicator of the lines that are covered by tests, but not how they are covered.

### Question 9

> **Did you workflow include using branches and pull requests? If yes, explain how. If not, explain how branches and**
> **pull request can help improve version control.**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of both branches and PRs in our project. In our group, each member had an branch that they worked on in*
> *addition to the main branch. To merge code we ...*
>
> Answer:

Throughout our project we relied heavily on both branches and PRs. We created branches for every part of the project that needed work to easily be able to work independently of each other while not harming the main branch. This also allowed us to independently be responsible for the code we each of us developed. Then in order to merge the created code from a branch, we created a PR with comments highlighting the most essential information needed for the other group members to review the code and approve a merging of the branch and main branch. In this way, it was trivial for us to develop code on the same project by dividing the tasks in branches.

### Question 10

> **Did you use DVC for managing data in your project? If yes, then how did it improve your project to have version**
> **control of your data. If no, explain a case where it would be beneficial to have version control of your data.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did make use of DVC in the following way: ... . In the end it helped us in ... for controlling ... part of our*
> *pipeline*
>
> Answer:

To manage the data we used for this project, we used DVC. It allowed us to store the data remotely in an efficient way, and then retrieve it by pulling it from the remote storage on Google Cloud Storage. Generally, DVC also allows for data versioning, which is an interesting and essential aspect to include in a MLOps project in case the data changes or one processes the data differently over time. Then having different versions of the data allows you to clearly define what version of data is being used. Hence, if we wanted to process our data differently to see how this given processing would affect the model performance, then we would not have to get rid of the original version (v1.0), but instead we would be able to create a data v2.0. The same also applies in cases of data drift, where new data can then be added to another version to keep both the original and the improved data.

### Question 11

> **Discuss you continues integration setup. What kind of CI are you running (unittesting, linting, etc.)? Do you test**
> **multiple operating systems, python version etc. Do you make use of caching? Feel free to insert a link to one of**
> **your github actions workflow.**
>
> Answer length: 200-300 words.
>
> Example:
> *We have organized our CI into 3 separate files: one for doing ..., one for running ... testing and one for running*
> *... . In particular for our ..., we used ... .An example of a triggered workflow can be seen here: <weblink>*
>
> Answer:

The continuous CI of this project can be considered divided into 2 aspects: one aspect that is relevant before submitting code to the Github repository, and one that is relevant when code is submitted to the repository. The first is applied as a pre-commit hook that checks a commit on a branch for a specified range of tests that makes sure the code committed is of the desired form. Hereby, we define pre-commit hooks that concerns linting and a common code structure, these hooks can be seen [here](https://github.com/GustavHansen99/project_mlops/blob/main/.pre-commit-config.yaml). The other part of our CI is based on Github actions that runs unittests of the code. Here, we assume that the code has already been through pre-commit hooks, and linting is thus not necessary. Thus, we define a series of tests that the code will be tested on before being able to merge with the repository. This part of the CI is tested on both ubuntu and MacOS operating systems as well as two different python versions to ensure that the code works in multiple settings. Moreover, we make use of caching to counter the fact that github actions will destroy every downloaded package when the workflow has been executed. An example of a triggered workflow file can be seen here: [link to file](https://github.com/GustavHansen99/project_mlops/blob/main/.github/workflows/tests.yml). In this file, we conduct our unittesting as well as report the code coverage hereof, which is set up using codecov integration.

## Running code and tracking experiments

> In the following section we are interested in learning more about the experimental setup for running your code and
> especially the reproducibility of your experiments.

### Question 12

> **How did you configure experiments? Did you make use of config files? Explain with coding examples of how you would**
> **run a experiment.**
>
> Answer length: 50-100 words.
>
> Example:
> *We used a simple argparser, that worked in the following way: python my_script.py --lr 1e-3 --batch_size 25*
>
> Answer:

To configure experiments we made use of configuration files containing the relevant hyperparameters and information needed. For example, we define a configuration for training that contains the epochs, learning rate, batch size, etc. and use this to keep track of our experiment variables. Hence running an experiment would be as simple as defining the respective configuration file in the [config](https://github.com/GustavHansen99/project_mlops/tree/main/config) folder, and running `python script.py`. We considered using argparser, however this approach lacks the ability to store and keep track more accurately, and one might lose essential information hereof.

### Question 13

> **Reproducibility of experiments are important. Related to the last question, how did you secure that no information**
> **is lost when running experiments and that your experiments are reproducible?**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of config files. Whenever an experiment is run the following happens: ... . To reproduce an experiment*
> *one would have to do ...*
>
> Answer:

In order to ensure reproducible experiments, we made use of config files. Whenever an experiment is run the respective configuration file is used as the variable values. Based on these values the script is run and if it a training script, we not only log the performance of the experiment, but also a series of files related to reproducibility: all configuration values, a requirements.txt file, and a log showing the model size and parameters. To reproduce an experiment, it is therefore fairly easy to setup an experiment with an identical configuration file, and achieve the reported results. By using a random seed, one would be able to ensure that randomness in weight initialization for example, does not alter the results between diffrent experiments.

### Question 14

> **Upload 1 to 3 screenshots that show the experiments that you have done in W&B (or another experiment tracking**
> **service of your choice). This may include loss graphs, logged images, hyperparameter sweeps etc. You can take**
> **inspiration from [this figure](figures/wandb.png). Explain what metrics you are tracking and why they are**
> **important.**
>
> Answer length: 200-300 words + 1 to 3 screenshots.
>
> Example:
> *As seen in the first image when have tracked ... and ... which both inform us about ... in our experiments.*
> *As seen in the second image we are also tracking ... and ...*
>
> Answer:

As seen in [this figure](figures/project_wandb.png), we have used W&B to track our experiments for this project. In this figure, we show a series of some of the experiments that we have tracked using W&B, and from this we have chosen to monitor metrics such as training loss, training accuracy, validation loss, validation accuracy. From this, we clearly observe a tendency in our experiments that the pre-trained model we use contain weights that make it start at a preferable initial state (compared to starting from scratch) since most experiments even in the beginning seem to perform fairly acceptable. Hence using W&B we are able to get a clear overview of how our experiments turn out and easily compare the logged metrics across experiments as well.
An aspect of W&B that we did not utilize for this project is that it is possible to log other things than numeric metrics, such as images. Since our project uses images as its data, it would have been interesting to log some of the training data and the predicted class in order for us to see the model improve over time. However, as discussed, we chose to focus on the more classic performance metrics for training and evaluating models.

### Question 15

> **Docker is an important tool for creating containerized applications. Explain how you used docker in your**
> **experiments? Include how you would run your docker images and include a link to one of your docker files.**
>
> Answer length: 100-200 words.
>
> Example:
> *For our project we developed several images: one for training, inference and deployment. For example to run the*
> *training docker image: `docker run trainer:latest lr=1e-3 batch_size=64`. Link to docker file: <weblink>*
>
> Answer:

For this project we have made extensive use of Docker and the strengths it provide us to develop containerized code generalizable to other machines. We have developed several docker images, where especially two are interesting: one for training the model, and one for deployment using FastAPI. After building the images running the them is once again based on the parameters specified in our config files, meaning that for example to run the training docker image locally is done by `docker run trainer_latest`, does not require extra argparsed arguments due to it all being represented in the config file. Running the training image on the cloud is done by `docker run --rm -it --shm-size=8G --gpus all --device /dev/nvidiactl --device /dev/nvidia0 gcr.io/dtumlops-project-group-55/trainer:latest`. [Link to docker file](https://github.com/GustavHansen99/project_mlops/blob/report_writing/docker/trainer.dockerfile).

### Question 16

> **When running into bugs while trying to run your experiments, how did you perform debugging? Additionally, did you**
> **try to profile your code or do you think it is already perfect?**
>
> Answer length: 100-200 words.
>
> Example:
> *Debugging method was dependent on group member. Some just used ... and others used ... . We did a single profiling*
> *run of our main code at some point that showed ...*
>
> Answer:

When encountering bugs each group member handled the approach to solve it differently. Some of us primarily solved the bugs using the built-in python debugger, while others used the debugger from VSCode. In this way, we were able to solve the appearing bugs and write working code. We also tried doing a single profiling run on the forward pass of our model which showed that in the beginning our data was not stored as tensors which was hence suboptimal considering performance.

## Working in the cloud

> In the following section we would like to know more about your experience when developing in the cloud.

### Question 17

> **List all the GCP services that you made use of in your project and shortly explain what each service does?**
>
> Answer length: 50-200 words.
>
> Example:
> *We used the following two services: Engine and Bucket. Engine is used for... and Bucket is used for...*
>
> Answer:

We used the following services: Compute Engine, Bucket, Container Registry, Build and Run. Compute Engine is a google cloud service that enables us to create and run virtual machines on Google's infrastructure. Bucket is used as storage space for the project. Container registry is used to store images that we create. Cloud build is used to build the images after we push changes to the main branch of our github repository. Cloud Run is used to run our FastAPI application for inference.

### Question 18

> **The backbone of GCP is the Compute engine. Explained how you made use of this service and what type of VMs**
> **you used?**
>
> Answer length: 100-200 words.
>
> Example:
> *We used the compute engine to run our ... . We used instances with the following hardware: ... and we started the*
> *using a custom container: ...*
>
> Answer:

We used Compute Engine to train our model. We used an instance with the following hardware: n1-standard-4 machine with 1 V100 GPU. On this machine we run a custom contrainer: trainer-final4. The way we utilized this machine was the following: after we pushed our code on the main branch on github, an image was created automatically on the Cloud registry. Afterwards, these images are used to run the container and train the model with different configurations, which are scecified through some configuration files.

### Question 19

> **Insert 1-2 images of your GCP bucket, such that we can see what data you have stored in it.**
> **You can take inspiration from [this figure](figures/bucket.png).**
>
> Answer:

[this figure](figures/bucket55.png)

### Question 20

> **Upload one image of your GCP container registry, such that we can see the different images that you have stored.**
> **You can take inspiration from [this figure](figures/registry.png).**
>
> Answer:

[this figure](figures/registry55.png)

### Question 21

> **Upload one image of your GCP cloud build history, so we can see the history of the images that have been build in**
> **your project. You can take inspiration from [this figure](figures/build.png).**
>
> Answer:

[this figure](figures/build55.png)

### Question 22

> **Did you manage to deploy your model, either in locally or cloud? If not, describe why. If yes, describe how and**
> **preferably how you invoke your deployed service?**
>
> Answer length: 100-200 words.
>
> Example:
> *For deployment we wrapped our model into application using ... . We first tried locally serving the model, which*
> *worked. Afterwards we deployed it in the cloud, using ... . To invoke the service an user would call*
> *`curl -X POST -F "file=@file.json"<weburl>`*
>
> Answer:

For the deployment of our model we wrapped it into an application using FastAPI. First, we tried serving the application locally using uvicorn, which worked.  Then, we containerised the application and tried to run the image locally, which also worked. As a last step, we deployed the application to the cloud using Cloud Run. You can access the application through the following command: "curl -X POST -F "data=@<image/path>" https://brain-scan-eval-xm27t4qwiq-lz.a.run.app/infer/". In the json response you get, the key "tumor" shows if the image you sent showcases a brain with a tumor (True) or not (False).

### Question 23

> **Did you manage to implement monitoring of your deployed model? If yes, explain how it works. If not, explain how**
> **monitoring would help the longevity of your application.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did not manage to implement monitoring. We would like to have monitoring implemented such that over time we could*
> *measure ... and ... that would inform us about this ... behaviour of our application.*
>
> Answer:

We did not manage to implement monitoring during our development cycle. We would like to have monitoring implemented so that, over time, we could collect information about how well our application behaved. This can include identification of problems of our application (errors and logs) and performance issues, such as speed during high traffic periods. Also, we could collect more datapoints for further training and generalization of our model.

### Question 24

> **How many credits did you end up using during the project and what service was most expensive?**
>
> Answer length: 25-100 words.
>
> Example:
> *Group member 1 used ..., Group member 2 used ..., in total ... credits was spend during development. The service*
> *costing the most was ... due to ...*
>
> Answer:

All three members used less than 20 dollars of credit during development. The most expensive service was Compute Engine since it used a VM with GPU that costs much more than everything else.

## Overall discussion of project

> In the following section we would like you to think about the general structure of your project.

### Question 25

> **Include a figure that describes the overall architecture of your system and what services that you make use of.**
> **You can take inspiration from [this figure](figures/overview.png). Additionally in your own words, explain the**
> **overall steps in figure.**
>
> Answer length: 200-400 words
>
> Example:
>
> *The starting point of the diagram is our local setup, where we integrated ... and ... and ... into our code.*
> *Whenever we commit code and puch to github, it auto triggers ... and ... . From there the diagram shows ...*
>
> Answer:

The starting point of the diagram seen in [this figure](figures/project_pipeline.png) is our local setup, where we integrated pytorch lightning, pytorch, W&B, configuration files, and other small frameworks into our code. Whenever a developer (group member) would want to commit code to the github repository we set up pre-commit hooks that using flake8, black and isort would ensure a common code structure and convention. If the committed code adhered to the standards set out by the pre-commit hooks and is pushed to Github, it auto-triggers a series of github actions that check the code based on unittests. Moreover, if the code succesfully passes the github actions, we trigger a build of the trainer dockerfile using GCP Triggers, which will then build the docker image and store it in the GC Container Registry.

### Question 26

> **Discuss the overall struggles of the project. Where did you spend most time and what did you do to overcome these**
> **challenges?**
>
> Answer length: 200-400 words.
>
> Example:
> *The biggest challenges in the project was using ... tool to do ... . The reason for this was ...*
>
> Answer:

--- question 26 fill here ---

### Question 27

> **State the individual contributions of each team member. This is required information from DTU, because we need to**
> **make sure all members contributed actively to the project**
>
> Answer length: 50-200 words.
>
> Example:
> *Student sXXXXXX was in charge of developing of setting up the initial cookie cutter project and developing of the*
> *docker containers for training our applications.*
> *Student sXXXXXX was in charge of training our models in the cloud and deploying them afterwards.*
> *All members contributed to code by...*
>
> Answer:

--- question 27 fill here ---
