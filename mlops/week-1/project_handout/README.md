# Week 1 - Classification model

## Summary

_In this assignment, you will build your first supervised machine learning model
using the Titanic passenger dataset. You will first use scikit-learn to train
and evaluate a logistic regression classifier, and then implement logistic
regression yourself using NumPy. By combining library-based modeling with a
from-scratch implementation, you will learn both how to apply machine learning
tools and how the underlying algorithm works._

## Introduction

This is the first assignment in the Machine Learning and MLOps track. It is your
first practical step into machine leaning: you will train a model that learns
from data and uses this information to make predictions.

Machine Learning is a field of computer science in which programs improve their
performance on a task by learning patterns from data. In supervised learning,
the model is training on samples where both the input data (i.e., features) and
correct output labels are known.

In this assignment, you will be training a classification model. Classification
models are machine learning models that learn to assign inputs to predefined
categories or classes based on patterns found in labeled training data.

## Goal

The goal of this assignment is to introduce you to the core ideas of supervised
learning. You will work with the Titanic passenger dataset, an open dataset that
is commonly used for educational purposes in machine learning.

The assignment is divided into two parts. In the first part, you will explore
the dataset, and train a classification model using a machine learning library.
In the second part, you will go one level deeper and implement a machine
learning model from scratch. Instead of relying on libraries with pre-build
abstractions, you will reconstruct the components of the algorithm in Python
code. This will help you understand how predictions are generated, how model
parameters are learned, and what role the optimization plays in the training
process.


## How to approach this assignment

### Part 1: Classification model using scikit-learn

**Dataset:** In this assignment, you will work with the Titanic passenger
dataset. This dataset contains information about the individual passengers,
including age, sex, ticket class, and whether they survived the disaster. The
task is to build a model that can predict whether a passenger survived based on
these features.

**Exploration:** Before you start with modeling, it is important to become
familiar with the structure and content of the dataset. Inspect the dataset and
create summaries, identify data types, check for any data quality issues, and
create visualizations that help you to explore the dataset.

**Model training:** Using the prepared dataset, train a classification model
(logistic regression) using the scikit-learn library.

**Evaluation:** Finally, evaluate the performance of your model. Explore
multiple evaluation metrics and reflect on what each of them reveals about the
model.


### Part 2: Logistic regression from scratch

In this part, you will go one step further and implement logistic
regression yourself using only NumPy.

The goal of this part of the exercise is not to build a production-ready model,
but to develop an intuition for how machine learning models work internally. In
applied machine learning, you will almost always rely on optimized libraries
such as Scikit-learn.

Training a model means adjusting its parameters so that its predictions better
match the observed data. In logistic regression, the parameters are the weights
and the bias. The weights determine how strongly each input feature influences
the prediction, while the bias acts as an offset that shifts the prediction up
or down independently of the features.

A logistic regression model is built from a sequence of components: a linear
model to compute a score, a sigmoid function to convert that score into a
probability, a loss function to measure error, and gradients to determine how
the parameters should be updated. These components are combined in a training
loop that iteratively adjusts the weights and bias to improve the model’s
predictions.

**Note:** use the provided notebook as starting point for implementing the model
from scratch. The notebook also contains the mathematical basis.


## Acceptance criteria

* The implementations are provided as a Jupyter notebooks.
* The notebooks execute from start to finish without errors.
* The code cells are logically structured and are documented with a short
  description using markdown cells.
* **Part 1:**
    * Summaries and visualizations of the dataset are created.
    * A logistic regression model is trained using scikit-learn.
    * Model performance is evaluated using multiple metrics.
* **Part 2:**
    * The model components are implemented as separate functions.
    * The training loop tracks the loss over time.
    * The loss decreases during training.
    * The logistic regression implementation is applied to the same dataset as
      in part 1.


## Tools

Here are suggestions for tools and Python libraries to complete your assignment:

* **uv:** The project uses uv for dependency management. This tool can be used
  to install the required packages from the provided project specification and
  to create and manage a virtual environment for the assignment. Working in a
  virtual environment helps keep the project dependencies isolated from other
  Python installations on your system, which makes the development setup cleaner
  and more reproducible.
* **Jupyter Notebooks:** A Jupyter notebook is an interactive environment for
  writing and running Python code in small parts, often called cells. Instead of
  writing a full script and running it from beginning to end, a notebook allows
  you to execute individual pieces of code, inspect intermediate results, and
  gradually build up your analysis. Jupyter notebooks are typically started as a
  local web server and then accessed through a browser, but they can also be
  created and run directly inside and IDEs like Visual Studio Code.
* **Pandas:** pandas is one of the standard libraries in the Python data
  ecosystem and has become a central tool for working with tabular data. It was
  developed to make data analysis and data manipulation in Python more practical
  and expressive, and it is now widely used in both industry and education.
* **Scikit learn:** scikit-learn is a widely used Python library for machine
  learning. It provides implementations of many common algorithms for tasks such
  as classification, regression, clustering, dimensionality reduction, and model
  evaluation. The library is designed to work well with NumPy and pandas, making
  it practical for building complete data analysis and machine learning
  workflows.
* **Seaborn:** seaborn is a Python visualization library built on top of
  matplotlib. It is especially useful for creating clear and informative
  statistical graphics, such as scatter plots, box plots, histograms, heatmaps,
  and pair plots. Seaborn works well with pandas DataFrames and is often used to
  explore patterns, relationships, and distributions in datasets.
* **NumPy:** NumPy is a foundational Python library for numerical computing. It
  provides efficient array and matrix data structures, along with many functions
  for mathematical operations, linear algebra, random number generation, and
  data manipulation. Many other Python data science libraries, including pandas,
  scikit-learn, and seaborn, rely on NumPy internally.


## Tips

Implementing a machine learning model from scratch requires the individual parts
to correctly work together. Here are some tips for implementing Part 2 of this
assignment:

* Implement the functions in order and test each step before moving on.
* Always use the probabilities that the model predicts, not the final
  classification values.
* Use small datasets first to verify correctness.
* Play close attention to the array shapes when using NumPy operations.
* Use np.clip in the loss function to avoid numerical issues with logarithms.
* Print the loss values to debug the training. If the loss does not decrease,
  check the gradient calculation and learning rate.
* Keep your implementation simple!
