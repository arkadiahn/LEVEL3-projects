import pandas as pd
from datasets import Dataset, DatasetDict

def create_evaluation_dataset():
    """
    Loads raw data, converts it to a Hugging Face Dataset object,
    and saves it for later use.
    The goal is creating a dataset that actually shows results.
    """
    df = pd.read_csv("data/raw_data.csv")

    # For this reference, we'll just use the raw data.
    # In a real scenario, students would add augmented data here.
    
    # Convert pandas DataFrame to Hugging Face Dataset
    hf_dataset = Dataset.from_pandas(df)

    # We create a DatasetDict, which is best practice.
    # We'll use the same data for train and test for this example,
    # but students could be asked to create a proper split.
    dataset_dict = DatasetDict({
        'test': hf_dataset
    })

    # Save the dataset to disk
    dataset_dict.save_to_disk("data/custom_eval_dataset_hf")
    print("Custom evaluation dataset created and saved to 'data/custom_eval_dataset_hf'")

if __name__ == "__main__":
    create_evaluation_dataset()