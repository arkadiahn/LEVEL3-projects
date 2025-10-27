# Part 2: Machine Learning - Classification

Welcome to Part 2 of the Machine Learning module. In Part 1, you tackled a regression problem where the goal was to predict a continuous value - the number of bike rentals on a given day. You explored data preprocessing, built pipelines, trained models, and evaluated their performance.

In this part, we are shifting focus to another type of machine learning task: classification.

A classification problem involves predicting discrete categories or class labels rather than continuous values. For example, instead of predicting how many people will rent bikes, you might predict whether bike rentals will be high or low on a given day, or whether a user will click on an ad or not. Classification is used in many real-world applications, such as email spam detection, fraud detection, and disease diagnosis.

Let's dive in!

## Spotify Track Popularity

In this part of the exercise, you will work on a classification problem based on data from Spotify tracks. The goal is to predict whether a given track is popular or not using features such as danceability, energy, tempo, acousticity, and more.

This kind of model has practical applications in the music industry, where streaming platforms like Spotify aim to understand and anticipate user preferences. A popularity prediction model can be used to personalize recommendations by promoting popular songs, support playlist creation, or assist artist and producers in analyzing which musical attributes contribute to popularity.

## Data set

The dataset for this exercise comes from Kaggle, a popular online platform for data science competitions, datasets, and community-based learning. Kaggle hosts a wide variety of real-world datasets and allows users to share notebooks, solutions, and experiments.

To access and download the Spotify dataset, you’ll first need to create a free Kaggle account if you haven’t already.

Once you're signed in, follow the instructions to download your Kaggle API key (`kaggle.json`) from your account settings. You can find the step-by-step guide [here](https://www.kaggle.com/docs/api).

The dataset that we are using for this exercise is `amitanshjoshi/spotify-1million-tracks`.

## Model training

Following a similar process as for part-1, train a machine learning model that can predict if a song is popular or not. Note that the evaluation metrics for classification problems are different!

Log the model parameters, metrics, and the model (i.e., the fitted pipeline) to MLflow.

## MLflow as Model Registry

MLflow is more than an experiment tracker. It also includes a model registry, a central place where you can store all (or specific versions of) your models.

MLflow allows you to register models from you training runs in the registry. Assign stage aliases like "production", or "staging", or "test-1003" to manage the lifecycle and experimentation with different models.

Explore the MLflow UI, specifically the Model registry. Register your trained models and set the best-performing model as "production" model.

## Prediction API end-point

Develop a simple REST API for predictions. The API server:

- Loads the model directly from MLflow by alias (e.g., "production"),
- Accepts POST requests with track features in JSON format,
- Returns a classification `{"popular": 0}` or `{"popular": 1}`.

The API server program should be configurable to switch between model versions available in MLflow.

> Hint: You can use a lightweight web framework like FastAPI or Flask, or a framework of your choice.

## Frontend

As a final touch, create a frontend application where music producers can adjust features like danceability, energy, and tempo using e.g. sliders. See real-time predictions from the deployed model called via the API.

> Hint: Streamlit is ideal for creating such a prototype. It allows you to build interactive UIs with minimal code, using pure Python.
