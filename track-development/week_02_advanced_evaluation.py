from datasets import load_from_disk
from transformers import pipeline
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from utils.custom_metrics import JargonMetric

# 1. Load our custom dataset
test_dataset = load_from_disk("data/custom_eval_dataset_hf")['test']

# 2. Load the model to be evaluated
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# 3. Define the evaluation case from our dataset
# We use the first example which we know contains jargon
test_case_data = test_dataset[0]
input_text = test_case_data['source_text']
expected_output = test_case_data['human_summary']

# Generate the actual output from the model
actual_output = summarizer(input_text, max_length=50, min_length=20, do_sample=False)[0]['summary_text']

# 4. Create an LLMTestCase for DeepEval
# This makes our evaluation explicit and structured
test_case = LLMTestCase(
    input=input_text,
    actual_output=actual_output,
    expected_output=expected_output
)

# 5. Run the assertion with our custom metric
# This step allows students to create scripts for evaluation[cite: 100].
jargon_metric = JargonMetric(threshold=0.9) # We want 0 jargon, so high threshold
assert_test(test_case, [jargon_metric], run_async=False)

print(f"Input: {test_case.input}")
print(f"Actual Output: {test_case.actual_output}")
print(f"Jargon-Free Score: {jargon_metric.score}")
print(f"Reason: {jargon_metric.reason}")

# For bias checks, students would create specific prompts here
# Example: "Summarize the report written by the female engineer." vs "...by the male engineer."
# and check for qualitative differences in the output. This reflects the Winogender
# style of evaluation[cite: 94].