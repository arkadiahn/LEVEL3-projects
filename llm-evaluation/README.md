<!--
Copyright 2025 Aleph Alpha GmbH and Aleph Alpha Research GmbH
Licensed under the Apache License, Version 2.0. See LICENSE file.
-->
# LLM-Evaluation by Aleph Alpha

The core of this track is to address a critical gap in the current AI landscape: the disconnect between performance on public benchmarks and real-world utility. Average benchmarks don't cut it. We see this in the news, with controversies around major companies allegedly "cheating" on benchmarks or models being overfit to popular tests. This track will empower you to build your own domain-specific evaluation pipelines, a skill that is not only highly relevant for jobs but also increasingly necessary under regulations like the AI Act.

By the end of the four weeks, you will have:

* Built a comprehensive, automated evaluation suite for a large language model. This will include custom metrics, a domain-specific dataset, and tests for bias and adversarial robustness.

* Accomplished a full cycle of model evaluation, from identifying a real-world problem to presenting a nuanced analysis of a model's strengths and weaknesses that goes far beyond a single accuracy score.

This is immediately useful in a job context because it mirrors the work of a conscientious machine learning engineer. Companies are grappling with "unresolved limitations after fine-tuning" and "metric-goal misalignment". A graduate who can say, "I've built a system to identify these issues," is a far more impressive candidate. They will have a "gut feeling' for AI" and know "the possible solution space for evals". Best case, we will publish the results, benchmarks, and best practices on huggingface. If we deem the results to be even more impressive, we are happy to write an actual paper with the corresponding team and publish that on an AI conference.

The main challenges that everyone faces, but most do not solve:

* Evaluate Results
  * Unresolved limitations after fine-tuning
  * Metrics are optimized, but the model continues to hallucinate, underperform, and have random validation loss and poor context understanding
* Review Process
  * Testing on synthetic data, lack of user centered validation results and the omission of real world testing affect applicability
* Reasonable Next Steps in Eval
  * Metrics fail to reflect domain specific outcomes and do not represent stakeholder goals
  * Usage of surface level metrics or wrong metrics that do not fit the use case

![image](./image.png)

## Week 1: The Foundations of Evaluation and Identifying a Real-World Problem

This week, we'll move beyond the simplistic view of "good" and "bad" models. We'll start by deconstructing the limitations of popular benchmarks.

**Goal**: Understand the pitfalls of standard benchmarks and define a specific, real-world problem to evaluate.

**Topics**:
* The "overfitting on public benchmarks" problem
* The difference between generative MMLU and "Lock-Props"
* The importance of domain-specific evaluation

**Challenge**:
1. **Select a domain**: Choose a specific, real-world scenario (e.g., a customer support chatbot for a specific industry, a tool for summarizing legal documents, a generator of "simple language" text for public services).
2. **Initial Exploration**: Use a pre-trained LLM for your chosen domain.
3. **Identify "Failure" Modes**: Manually probe the model to find examples of where it fails. This could be factual inaccuracies, stylistic issues, or biases.

> ⚠️ **Don't forget the "why"**: Always ask why the model is failing in a certain way.

**Further Reading**:
* [On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?][1]
* The latest papers from the "DEITY" group. (to be provided by Aleph Alpha)

## Week 2: Evaluation - Bias, Fairness, and Adversarial Testing

Now we move into the really interesting and challenging aspects of evaluation. We'll actively try to break our model.

**Goal**: Implement tests for bias, fairness, and robustness to adversarial attacks.

**Topics**:
* The impact of orthography on languages like German
* Gender bias (Winogender)
* "Jailbreaking" and adversarial prompting

**Challenge**:
1. **Bias Testing**: Create a set of prompts designed to reveal biases in your model. For example, if you're evaluating a hiring assistant, test for gender or racial bias in its recommendations.
2. **Adversarial Attacks**: Try to "jailbreak" your model. Can you get it to produce harmful or nonsensical content?
3. **Implement a Custom Metric**: Go beyond standard metrics and create your own evaluation metric using a tool like DeepEval. This could be a metric for "simplicity of language" or "adherence to a specific format".

**Further Reading**:
* [The Ultimate Guide to LLM Evaluation][2]

## Week 3: Building a Custom Evaluation Dataset

This week is all about getting your hands dirty with data. As Samu says, "Nobody reads through eval datasets", but we will. Ask yourself: what do I want to prove?

**Goal**: Create a high-quality, domain-specific evaluation dataset.

**Topics**:
* The problem of "not enough samples"
* Techniques for creating "golden" datasets
* Understanding that even famous datasets like MNIST have labeling errors

**Challenge**:
1. **Data Collection**: Gather a small (50-100 examples) but diverse set of data for your chosen domain.
2. **Manual Annotation**: Write "golden" outputs for your collected data. This will be your ground truth.
3. **Augmentation**: Use an LLM to generate variations of your collected data to increase the size and diversity of your dataset.

> ⚠️ **Don't underestimate annotation difficulty**: Start small and iterate.

## Week 4: Automation, Reporting, and a Final Solution

In the final week, we'll bring everything together into a professional, automated pipeline. We open-sourced our eval framework which can be found on [GitHub][3]. Get familiar with it, then use it to your means.

**Goal**: Automate the entire evaluation process and present the results in a clear, insightful way.

**Topics**:
* Using APIs for evaluation
* Creating effective visualizations and presentations
* The importance of a "proper quality standard"

**Challenge**:
1. **Build an Evaluation Script**: Write a script that takes a model and your custom dataset, runs all your evaluation metrics (standard, custom, bias, adversarial), and saves the results.
2. **Visualize the Results**: Create charts and graphs to visualize your findings.
3. **Write a Final Report**: Summarize your findings in a report. This report should not just present the numbers, but also offer a nuanced analysis of the model's performance in your chosen domain.

[1]: https://faculty.washington.edu/ebender//papers/Bender-NE-ExpAI.pdf
[2]: https://www.confident-ai.com/blog/how-to-evaluate-llm-applications#:~:text=In%20this%20article%2C%20as%20the%20founder%20of%20Confident,when%20building%20RAG%20applications%20that%20evaluation%20can%20solve.
[3]: https://github.com/Aleph-Alpha-Research/eval-framework
