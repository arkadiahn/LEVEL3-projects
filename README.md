# Aleph Alpha LEVEL3 Projects

## 1. Define the Topic
The core of this track is to address a critical gap in the current AI landscape: the disconnect between performance on public benchmarks and real-world utility. As your notes rightly point out, "Average benchmarks don't cut it". We see this in the news, with controversies around major companies allegedly "cheating" on benchmarks or models being overfit to popular tests. This track will empower students to build their own domain-specific evaluation pipelines, a skill that is not only highly relevant for jobs but also increasingly necessary under regulations like the AI Act.

By the end of the four weeks, each participant will have:

Built a comprehensive, automated evaluation suite for a large language model. This will include custom metrics, a domain-specific dataset, and tests for bias and adversarial robustness.

Accomplished a full cycle of model evaluation, from identifying a real-world problem to presenting a nuanced analysis of a model's strengths and weaknesses that goes far beyond a single accuracy score.

This is immediately useful in a job context because it mirrors the work of a conscientious machine learning engineer. Companies are grappling with "unresolved limitations after fine-tuning" and "metric-goal misalignment". A graduate who can say, "I've built a system to identify these issues," is a far more impressive candidate. They will have a "gut feeling' for AI" and know "the possible solution space for evals".

## 2. Structure the Track
The project is broken down into four weekly modules. Each week builds on the last, culminating in a complete, working project.

### Week 1: The Foundations of Evaluation and Identifying a Real-World Problem
This week, we'll move beyond the simplistic view of "good" and "bad" models. We'll start by deconstructing the limitations of popular benchmarks.

Goal: Understand the pitfalls of standard benchmarks and define a specific, real-world problem to evaluate.

Topics:

The "overfitting on public benchmarks" problem.

The difference between generative MMLU and "Lock-Props".

The importance of domain-specific evaluation.

Challenge:

Select a domain: Choose a specific, real-world scenario (e.g., a customer support chatbot for a specific industry, a tool for summarizing legal documents, a generator of "simple language" text for public services).

Initial Exploration: Use a pre-trained LLM for your chosen domain.

Identify "Failure" Modes: Manually probe the model to find examples of where it fails. This could be factual inaccuracies, stylistic issues, or biases.

### Week 2: Building a Custom Evaluation Dataset
This week is all about getting your hands dirty with data. As Samu says, "Keiner liest sich Evaldatensätze durch" ("Nobody reads through eval datasets"), but we will.

Goal: Create a high-quality, domain-specific evaluation dataset.

Topics:

The problem of "not enough samples".

Techniques for creating "golden" datasets.

Understanding that even famous datasets like MNIST have labeling errors.

Challenge:

Data Collection: Gather a small (50-100 examples) but diverse set of data for your chosen domain.

Manual Annotation: Write "golden" outputs for your collected data. This will be your ground truth.

Augmentation: Use an LLM to generate variations of your collected data to increase the size and diversity of your dataset.


### Week 3: Advanced Evaluation - Bias, Fairness, and Adversarial Testing
Now we move into the really interesting and challenging aspects of evaluation. We'll actively try to break our model.

Goal: Implement tests for bias, fairness, and robustness to adversarial attacks.

Topics:

The impact of orthography on languages like German.

Gender bias (Winogender).

"Jailbreaking" and adversarial prompting.

Challenge:

Bias Testing: Create a set of prompts designed to reveal biases in your model. For example, if you're evaluating a hiring assistant, test for gender or racial bias in its recommendations.

Adversarial Attacks: Try to "jailbreak" your model. Can you get it to produce harmful or nonsensical content?

Implement a Custom Metric: Go beyond standard metrics and create your own evaluation metric using a tool like DeepEval. This could be a metric for "simplicity of language" or "adherence to a specific format."


### Week 4: Automation, Reporting, and a Final Solution
In the final week, we'll bring everything together into a professional, automated pipeline.

Goal: Automate the entire evaluation process and present the results in a clear, insightful way.

Topics:

Using APIs for evaluation.

Creating effective visualizations and presentations.

The importance of a "proper quality standard".

Challenge:

Build an Evaluation Script: Write a script that takes a model and your custom dataset, runs all your evaluation metrics (standard, custom, bias, adversarial), and saves the results.

Visualize the Results: Create charts and graphs to visualize your findings.

Write a Final Report: Summarize your findings in a report. This report should not just present the numbers, but also offer a nuanced analysis of the model's performance in your chosen domain.


![logo](./level3.png)

## Project List

| Name                                               | Description                         |
| -------------------------------------------------- | ----------------------------------- |
| [Track Development](./track-development/README.md) | A meta-track for developing a track |


