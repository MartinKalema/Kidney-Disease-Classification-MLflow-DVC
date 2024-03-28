## End-to-End-Kidney-Disease-Classification-Using-MLflow-DVC
MLflow for experiment tracking and DVC for ML Pipeline tracking.

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

This Project is connected to Dagshub so all my experiments are sent to dagshub and can be viewed on dagshub itself or on the mlflow platform integrated there.

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
Utilise **Dagshub**

Before running an experiment add the mlflow uri configs as shown below.
```
export MLFLOW_TRACKING_URI=https://dagshub.com/kalema3502/Kidney-Disease-Classification-MLflow-DVC.mlflow
```
```
export MLFLOW_TRACKING_USERNAME=kalema3502
```
```
export MLFLOW_TRACKING_PASSWORD=fb3845efcc3b2e46a4157b1d2c977a21e02dd16e 
```



