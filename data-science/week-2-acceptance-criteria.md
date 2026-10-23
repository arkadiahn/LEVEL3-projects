# Week 2 Acceptance Criteria

#### Code & Structure
- The notebook executes sequentially from top to bottom without errors.
- Code cells include meaningful comments.
- Markdown headers separate each phase and Markdown cells are used to document code and insights.

#### Part 1
- The sales data is aggregated to the article level and a second custom level.
- Your process is documented in Markdown and your choices explained.

#### Part 2
- K-Means is trained across a range of _k_ for both aggregation levels.
- The choice of optimal _k_ is justified using visual or mathematical metrics.
- A visualization clearly displays the resulting clusters.
- The methodology used to create the visualization is documented and explained.

#### Part 3
- An alternative clustering algorithm was successfully used on the dataset.
- Markdown documentation explains how the algorithm works, supported cluster shapes or capabilities, parameter tuning choices and how its performance compares to K-Means.
- Includes business-oriented interpretations of the identified clusters.

#### Part 4
- A Streamlit app is created and runs without errors.
- The UI allows the user to switch between the clustering algorithms and aggregation levels.
- Interactive visualizations dynamically update based on the selected algorithm and level.
- The UI allows the user to hide or highlight specific clusters and dynamically displays the Cluster Profile.
- A download button exports the currently selected cluster data as a `.csv` file.

#### Bonus
- A working K-Means function is built strictly using NumPy/Python.
- An execution speed comparison against `sklearn.cluster.KMeans` is included.
