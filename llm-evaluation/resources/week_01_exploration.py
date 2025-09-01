import pandas as pd
from transformers import pipeline

# 1. Load a pre-trained model for initial probing
# We use a standard summarization model to see how it performs "out-of-the-box"
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# 2. Load our raw, domain-specific data
df = pd.read_csv("data/raw_data.csv")

# Loop through all rows in the DataFrame
for idx, row in df.iterrows():
    source_text = row['source_text']
    human_summary = row['human_summary']
    generic_summary = summarizer(source_text, max_length=50, min_length=25, do_sample=False)[0]['summary_text']

    print(f"\n=== ROW {idx} ===")
    print("--- DOMAIN-SPECIFIC TEXT ---")
    print(source_text)
    print("\n--- GENERIC MODEL SUMMARY ---")
    print(generic_summary)
    print("\n--- HUMAN-WRITTEN (TARGET) SUMMARY ---")
    print(human_summary)

# 4. Analysis & Observations (Markdown cells in the notebook)
# Think about the following observations:
# - **Observation 1: Metric-Goal Misalignment.** The generic summary is factually correct but misses the target audience. It's still too technical. This highlights the "Metric-Goal Misalignment" issue from our planning[cite: 20].
# - **Observation 2: Omission of Real-World Scenarios.** The model wasn't trained on "technical-to-business" translation, so it omits the key context of who the summary is for[cite: 18].
# - **Observation 3: Unresolved Limitations.** Even a powerful model like BART has limitations when applied to a new domain without fine-tuning[cite: 16, 17].