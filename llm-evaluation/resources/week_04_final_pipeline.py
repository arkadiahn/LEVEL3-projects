import pandas as pd
from datasets import load_from_disk
from transformers import pipeline
from evaluate import load
from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from utils.custom_metrics import JargonMetric
import matplotlib.pyplot as plt

def run_full_evaluation_pipeline():
    """
    This script automates the full evaluation and generates a results report.
    This gives students exposure to code bases that implement benchmarks[cite: 102].
    """
    # --- 1. SETUP ---
    dataset = load_from_disk("data/custom_eval_dataset_hf")['test']
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    rouge_metric = load('rouge')
    jargon_metric = JargonMetric()
    
    test_cases = []
    results = []

    # --- 2. GENERATE & EVALUATE ---
    for item in dataset:
        actual_output = summarizer(item['source_text'], max_length=50, min_length=20, do_sample=False)[0]['summary_text']
        test_case = LLMTestCase(
            input=item['source_text'],
            actual_output=actual_output,
            expected_output=item['human_summary']
        )
        test_cases.append(test_case)

    # Run DeepEval for custom metrics
    deepeval_results = evaluate(test_cases, [jargon_metric])

    # Run standard metrics
    predictions = [tc.actual_output for tc in test_cases]
    references = [tc.expected_output for tc in test_cases]
    rouge_scores = rouge_metric.compute(predictions=predictions, references=references)

    # --- 3. REPORTING ---
    print("--- EVALUATION REPORT ---")
    print(f"Average ROUGE-L Score: {rouge_scores['rougeL']:.4f}")

    # Extracting custom metric scores
    avg_jargon_score = sum(result.metrics_data[0].score for result in deepeval_results.test_results) / len(deepeval_results.test_results)
    print(f"Average Jargon-Free Score: {avg_jargon_score:.4f}")

    # --- 4. VISUALIZATION ---
    # This addresses the need for proper illustration/presentation[cite: 101].
    fig, ax = plt.subplots()
    metrics = ['ROUGE-L', 'Jargon-Free']
    scores = [rouge_scores['rougeL'], avg_jargon_score]
    ax.bar(metrics, scores, color=['skyblue', 'lightgreen'])
    ax.set_ylabel('Scores')
    ax.set_title('LLM Summarization Evaluation Results')
    ax.set_ylim(0, 1)
    plt.savefig('track-development/evaluation_results.png')
    print("\nResults chart saved to 'evaluation_results.png'")


if __name__ == "__main__":
    run_full_evaluation_pipeline()