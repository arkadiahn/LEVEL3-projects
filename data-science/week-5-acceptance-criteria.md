# Week 5 Acceptance Criteria

#### Code & Structure

- The notebook executes sequentially from top to bottom without errors.
- Code cells include meaningful comments.
- Markdown headers separate each phase and Markdown cells are used to document code and insights.
- MLflow experiments are saved with clean, descriptive names making them easily identifiable for external reviewers.
- The delivery includes both a Jupyter Notebook (for Parts 2, 3, and Bonus) and a separate `.py` script for the Streamlit dashboard.

#### Part 1
- The existing Streamlit app is expanded with a new view or tab to load the serialized models and generate predictions on-the-fly.
- The UI allows the user to select specific store-article combinations and visualizes Actuals vs. Predictions.
- WMAPE and BIAS are dynamically calculated and displayed for the selected combination.
- A download button exports the currently selected forecast data as a `.csv` file.

#### Part 2
- A drift detection strategy was implemented and is functional in the notebook with comments describing the approach and justifying the decision.
- A drift detection indicator or visual alert is added to the dashboard.

#### Part 3
- Historical backtesting is successfully implemented, simulating a production timeline.
- Different retraining strategies were explored, tracked in MLflow, and documented.
- A documented business recommendation specifies the optimal retraining strategy, frequency and time window, justified by metrics.

#### Bonus
- The new dataset is explored and the drift is programmatically quantified.
- A mitigation strategy is explained, implemented, and proven to recover model performance on the new data.
