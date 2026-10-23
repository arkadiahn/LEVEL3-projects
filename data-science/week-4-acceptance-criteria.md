# Week 4 Acceptance Criteria

#### Code & Structure
- The notebook executes sequentially from top to bottom without errors.
- Code cells include meaningful comments.
- Markdown headers separate each phase and Markdown cells are used to document code and insights.
- MLflow experiments are saved with clean, descriptive names making them easily identifiable for external reviewers.

#### Part 1
- Engineered features contain no data leakage and are available at prediction time.
- Categorical features are encoded appropriately.
- Feature selection is implemented, with dropped and retained features documented.

#### Part 2
- A justification for choosing the model is provided.
- Local forecasting models for the `T+3` horizon are trained for the specified article-store combinations as well as 5 combinations (1 additional article * 5 stores) of your choice.
- Baselines are established, and the trained models successfully outperform them.
- All model runs are logged in MLflow.

#### Part 3
- SHAP values for an article-store combination are calculated and visualized. 
- A business summary translates the feature importance results into insights.

### Part 4
- The existing Streamlit app is successfully expanded with a new store-article level forecasting view.
- The UI provides controls to easily select both an Article and a Store and view a suitable visualization of Actuals vs. Predictions.
- A visualization of the Feature Importance is successfully integrated.
- A download button exports the currently selected forecast data as a `.csv` file.

#### Bonus
- A global model is trained using a clustering from Week 2.
- A comparative analysis highlights the performance and operational trade-offs between the global and local modeling approaches.
- The Streamlit app is updated with a visualization to allow comparison between the default and global models.
