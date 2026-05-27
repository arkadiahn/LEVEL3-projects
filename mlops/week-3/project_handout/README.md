# Week 3 - Bike rental predictions


## Summary

_In this assignment, you will return to the dataset produced in week 2 and take
the next step: understanding the data through exploration and using it to train
regression models. You will analyze patterns, establish a baseline model, and
iteratively improve performance. Finally, you will integrate your modeling work
into the existing pipeline to create a reproducible end-to-end workflow._


## Introduction

At this stage of the project, the focus shifts from data preparation to learning
from the data. Before building effective machine learning models, it is
essential to understand the structure, distributions, and relationships within
the dataset.

You will begin by exploring the prepared dataset to uncover patterns in bike
rental demand. This includes generating summaries and visualizations that help
explain how different variables relate to the target variable.

Next, you will train regression models to predict bike demand. Unlike the
classification task in week 1, this problem involves predicting a continuous
value, which requires different evaluation metrics and modeling approaches.

The final step is to take what you learned in the notebook and incorporate it
into your pipeline, extending it to include model training and output.


## Goal

The goal of this assignment is to extend your existing pipeline with a machine
learning component:

* Explore and visualize the prepared dataset from Week 2
* Train and evaluate regression models
* Improve model performance through feature engineering and model selection
* Integrate model training into the pipeline as a reproducible step


## How to approach this assignment


* **Exploratory data analysis (EDA):**  
    Inspect the dataset structure and data types. Generate summary statistics
    and analyze distributions. Create visualizations to explore relationships
    between features and target.

* **Base regression model:**  
    Train an initial regression model to establish baseline performance. Use the
    fastest and simplest model available. Evaluate the performance using
    appropriate regression metrics.

* **Model improvement:**  
    Iteratively improve the model performance (i.e., experiment!). Perform
    feature engineering and/or try more advanced models available in
    Scikit-learn and XGBoost. Time-box your experiments to leave enough time for
    the pipeline integration.

* **Pipeline integration:**  
    Extend the key data processing and modeling steps from the notebook and
    extend your pipeline from Week 2.


## Acceptance criteria

* A notebook (or multiple notebooks) containing the data exploration, base model
  training and evaluation, and the modeling experiments.
* The extended Dagster pipeline that includes preprocessing and model training
  steps. The pipeline saves trained models as serialized Python objects.
* Both notebook and pipeline run successfully and produce the expected outputs.
* The codebase remains well-structured and readable. If you add additional
  features, work them into your upstream pipeline by either adapting the
  existing assets, or creating new assets, depending on what is appropriate.


## Tips

* Keep the exploration focused. What are you trying to answer with a
  visualization?  
  Describe your intentions using Markdown blocks in your notebook.
* Start simple, then iterate. Only move to more complex models and optimizations
  if you can justify it with results.
* Track your intentions and document your results.