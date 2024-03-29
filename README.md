## End-to-End-Kidney-Disease-Classification-Using-MLflow-DVC

MLflow for experiment tracking and DVC for ML Pipeline tracking, Data versioning and experiment tracking too. I'm using mlflow for experiment tracking.

Tasks

- Project template creation
- Project setup and requirements installation
- Logging, Utils and exception module
- Project Workflows
- All components notebook experiment
- All components modular code implementation
- training pipeline
- MLflow (MLOps tool for experiments tracking and model registration)
- DVC (MLOps tool for pipeline tracking and implementation)
- Prediction pipeline and user app creation
- Docker
- Final CI/CD Deployment on AWS

## Workflows

- Update config.yaml
- Update secrets.yaml [Optional]
- Update params.yaml
- Update the entity
- Update the configuration manager in src config
- Update the components
- Update the pipeline
- Update the main.py
- Upddate the dvc.yaml
- Update app.py

## How to install

Clone the repository

```bash
git clone https://github.com/MartinKalema/Kidney-Disease-Classification-MLflow-DVC.git
```

Create a conda environment after opening the repository and activate it

```bash
conda create -n kidney python=3.8 -y
```

```bash
conda activate kidney
```

Install the requirements

```bash
pip install -r requirements.txt
```

This Project is connected to Dagshub so all my experiments are sent to dagshub and can be viewed on dagshub itself or on the mlflow platform integrated there. MLflow is a production grade experiments tracker for managing end-to-end machine learning lifecycle. It helps with experiments tracking, packaging code into reproducible runs and sharing and deploying models.

## View experiments locally.

Do not set the tracking uri using,

```python
mlflow.set_tracking_uri()
```

All experiments will be stored inside an auto generated folder called **mlruns**. Use the command below to view them in the mlflow web interface

```
mlflow ui
```

## For remote views & collaboration.

Connect your github account to DagsHub @ https://dagshub.com

Whenever you close your editor and open it again, the mlflow uri configs are erased and you must run the commands below in your bash terminal again, otherwise the experiments will be saved on your local machine in a folder called **mlruns**

```
export MLFLOW_TRACKING_URI=https://dagshub.com/kalema3502/Kidney-Disease-Classification-MLflow-DVC.mlflow
```

```
export MLFLOW_TRACKING_USERNAME=kalema3502
```

```
export MLFLOW_TRACKING_PASSWORD=fb3845efcc3b2e46a4157b1d2c977a21e02dd16e
```

## DVC setup

DVC (Data Version Control) is a light weight experiments tracker and it can perform orchestration (creating pipelines)

```
dvc init
```

Add the project pipelines to the dvc.yaml file, then run the command below.

```
dvc repro
```

To the pipeline structure, use the command below

```
dvc dag
```

## AWS CI/CD Deployment with Github Actions

- Login to the AWS console
- Create an IAM user for deployment
- The user should have EC2 & ECR access. The deployment steps are mentioned below,

  1. Build the docker image of the source code
  2. Push your docker image to the ECR
  3. Launch your EC2
  4. Pull your image from the ECR to the EC2
  5. Launch your docker image in the EC2

- Policy

  1. Amazon EC2 Container Registry Access
  2. Amazon EC2 Full Access

- Create EC2 repo to save docker image
  ```
  save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken
  ```
- Create Ubuntu EC2 VM
- Install Docker on the EC2 Machine

  ```
      #optional

      sudo apt-get update -y

      sudo apt-get upgrade

      #required

      curl -fsSL https://get.docker.com -o get-docker.sh

      sudo sh get-docker.sh

      sudo usermod -aG docker ubuntu

      newgrp docker
  ```

- Configure EC2 as self-hosted runner
  ```
  setting > actions > runner > new self hosted runner > choose os >
  ```
- Setup github secrets

  ```
      AWS_ACCESS_KEY_ID=

      AWS_SECRET_ACCESS_KEY=

      AWS_REGION = us-east-1

      AWS_ECR_LOGIN_URI = demo >>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

      ECR_REPOSITORY_NAME = kidney
  ```
