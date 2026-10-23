# Data Science - demand forecasting with real-world retail data

## Overview

This track focuses on building an end-to-end data science pipeline using real-world Kaufland data from the Czech Republic. You will predict demand for fruit and vegetable articles, moving from market research and exploratory analysis through clustering and forecasting to deployment and model monitoring.

Rather than treating each technique in isolation, this track approaches data science as a connected workflow: cleaning and understanding operational retail data, discovering product and store archetypes, training demand models that mirror distribution-center and store lead times, and keeping those models reliable in production.

By the end of the track, you will have built a production-style demand forecasting system that connects raw sales data to actionable, monitored predictions.

![image](./image.png)

## What You Will Build

- A unified cleaned `.parquet` dataset with market-informed exploratory analysis
- Article and store clustering (K-Means and an alternative algorithm) with Streamlit exploration
- Aggregated univariate demand forecasts for T+2 and T+7 horizons with MLflow and retail metrics
- Store-article multivariate forecasts with feature selection and SHAP explainability
- A live prediction dashboard with drift detection and a documented retraining strategy

This project mirrors how retail organizations operationalize data science to support inventory and availability decisions.

## Learning Path

- [Week 1: Data Understanding & EDA](Tasks%20Week%201.ipynb) · [Acceptance criteria](week-1-acceptance-criteria.md)

- [Week 2: Clustering & Streamlit Exploration](Tasks%20Week%202.ipynb) · [Acceptance criteria](week-2-acceptance-criteria.md)

- [Week 3: Aggregated Demand Forecasting](Tasks%20Week%203.ipynb) · [Acceptance criteria](week-3-acceptance-criteria.md)

- [Week 4: Local Multivariate Forecasting](Tasks%20Week%204.ipynb) · [Acceptance criteria](week-4-acceptance-criteria.md)

- [Week 5: Deployment & Model Monitoring](Tasks%20Week%205.ipynb) · [Acceptance criteria](week-5-acceptance-criteria.md)
