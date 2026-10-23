# Week 3 Acceptance Criteria

#### Code & Structure
- The notebook executes sequentially from top to bottom without errors.
- Code cells include meaningful comments.
- Markdown headers separate each phase and Markdown cells are used to document code and insights.
- MLflow experiments are saved with clean, descriptive names making them easily identifiable for external reviewers.

#### Part 1
- Daily sales are aggregated to the article level.
- Bananas, Oranges, Kopfsalat and 2 other articles ideally representing distinct Week 2 clusters are selected and analyzed.
- Lagged and window features are created without introducing temporal data leakage.
- Dataset is cleanly split with the test set defined as business year 2025 (01.03.2025 – 28.02.2026).
- Markdown explanation covers direct vs. recursive forecasting and data leakage safeguards.

#### Part 2
- Reusable functions for WMAPE and BIAS are implemented.
- A Markdown section clearly explains WMAPE and BIAS for non-technical stakeholders.
- At least two baseline models are implemented and evaluated on the test set.
- Baseline runs, parameters, and metrics are logged in MLflow.

#### Part 3
- A Linear Regression is implemented for `T+2` and `T+7` horizons and logged in MLflow, successfully outperforming the baseline models.
- An evaluation section explicitly documents model strengths/weaknesses across the different product clusters.

#### Part 4
- Another model is selected and implemented for both horizons, and logged in MLflow. The model improves upon both baselines and linear regression.
- A justification for choosing the model is provided.
- An evaluation section explicitly documents model strengths/weaknesses across the different product clusters.

#### Part 5
- The existing Streamlit app is successfully expanded with a forecasting view.
- The UI allows users to select an article and view a suitable visualization of Actuals vs. Predictions.
- WMAPE and BIAS are dynamically calculated and displayed based on the selected article.
- A download button exports the currently selected forecast data as a `.csv` file.

#### Bonus
- Automated hyperparameter tuning is implemented.
- Tuned models are logged in MLflow with a clear comparison showing performance gains over the default parameters.
- The Streamlit app is updated with a visualization to allow comparison between the default and tuned models.
