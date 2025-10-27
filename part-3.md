# Part 3: From Notebook to MLOps Pipeline

Welcome to Part 3 of the Machine Learning module. So far, you have built regression and classification models using Jupyter notebooks. You've learned how to preprocess data, train models, and evaluate their performance using established machine learning workflows.

In this part, we move from the world of exploratory notebooks into production-grade MLOps. You’ll take the machine learning workflow you've already developed and convert it into an automated pipeline using modern tools and practices that reflect how machine learning is done in industry.

## Objective

Your goal is to convert your existing model training notebook (from either Part 1 or Part 2) into a fully automated machine learning pipeline. You will use **Dagster** to build the pipeline, **LakeFS** for versioning data, and apply professional software engineering practices to ensure your project is well-structured, reproducible, and robust.

## Tools

* **Dagster:** A modern orchestration platform for data workflows. You’ll use Dagster to define assets, resources, IO managers and sensors.
* **LakeFS:** A data versioning system that works like Git for data. You’ll use it to track data changes and trigger pipeline runs when new data arrives.
* **lakefs-spec:** A Python library that helps interact with LakeFS in Python.
* **Ruff and Pyright (via Pylance in VSCode):** For formatting, linting, and type-checking your code.
* **GitHub:** For version control.

## Task Overview


### 1. Structure your project

Create a Python package and structure it clearly:

```
ml_pipeline/
├── __init__.py
├── assets/
├── resources/
├── io_managers/
├── config/
└── utils/
```

* Use type hints throughout your code.
* Document functions and modules using a consistent standard (e.g., NumPy or Google docstrings).

### 2. Rebuild your pipeline with Dagster

* Define Dagster assets for each step (e.g., load data, preprocess, train, evaluate).
* Create custom Resources for accessing external services (e.g., MLflow)
* Build custom IOManagers to load and store data (for now, use local disk; later replace with remote service).
* Make your pipeline configurable.

### 3. Integrate LakeFS for Data Versioning

* Deploy a local LakeFS instance using Docker.
* Use `lakefs-spec` to define how your pipeline interacts with versioned datasets.
* Design and implement a strategy for versioning you data assets in LakeFS.

### 4. Trigger your pipeline with Sensors

* Instead of running your pipeline manually, use a Dagster Sensor that watches LakeFS.
* The sensor should detect when new data arrives.
* Automatically materialize downstream assets when the data changes.

> Hint. You can simulate data changes by splitting the data set per year (Bike Sharing dataset), or by splitting the dataset in multiple parts (Spotify Tracks dataset)

### 5. Testing and Best practices

* Write tests for you core functions and logic. **Pytest** is a common framework for unit testing in Python.
* Configure Ruff and Pyright for linting and static type checking.
* Ensure your code is commited (regularly) to a Github Repository with a clear README.

By the end of this exercise, you'll have taken your ML model into the world of MLOps, where pipelines are automated, data is versioned, and code is written and tested like professional software. This sets the stage for scalable, reproducible, and collaborative machine learning.

Let’s get building!
