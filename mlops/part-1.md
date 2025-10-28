# Part 1: Machine Learning - Introduction

Welcome to the first part of the **Artificial Intelligence and Machine Learning** module.  
In this section, you'll begin your journey into machine learning and train your first models.

Don’t just follow the subject blindly—strive to **understand** the tools you're using.  
Read the documentation, and be prepared to explain:

- What each step does
- Why it’s important
- The advantages and limitations of each tool

---

## What is Machine Learning?

Machine learning is a branch of computer science focused on building systems that **learn from data**.  
Rather than following fixed rules like traditional programs, ML models uncover hidden patterns in datasets to make predictions or decisions.

### Research Topics

Before getting started do your research on machine learning and be able to **at least** answer the following questions:

- What is the difference between supervised and unsupervised learning?
- What are types of supervised learning?
- What’s the difference between **classification** and **regression**? What output does each produce?
- How do you determine whether a problem is classification or regression?
- Are there ML problems that fall outside classification and regression?
- What is skewed data and how to mitigate it's effect?

---

## Predicting Bike Sharing Demand

Explore the dataset to understand distributions, correlations, and feature relationships.  
Use appropriate plots and explain your choices—why you chose that graph, and what alternatives exist.

### Prepare:

1. Gain insights from the data through exploration.
2. Clean and adjust the data as necessary.
3. Build a **preprocessing pipeline** using `scikit-learn`.
   - Wrap the pipeline creation into a **reusable function** that accepts any estimator.

### Model Training

Train models to predict hourly bike rentals using:

- `LinearRegression`
- `RandomForestRegressor`
- `XGBRegressor`
- `GridSearchCV` for hyperparameter tuning

Evaluate your models using **multiple performance metrics**.

### Dataset

Download the dataset from the UCI Machine Learning Repository:

👉 [Bike Sharing Dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset)

---

## Requirements

You are required to use the following tools:

- `uv` – Dependency management
- `jupyter` – Interactive notebook environment
- `pandas` – Data manipulation
- `seaborn` – Visualization
- `scikit-learn` – ML toolkit
- `mlflow` – Experiment tracking and logging
