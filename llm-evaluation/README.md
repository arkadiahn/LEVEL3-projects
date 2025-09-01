<!--
Copyright 2025 Aleph Alpha GmbH and Aleph Alpha Research GmbH
Licensed under the Apache License, Version 2.0. See LICENSE file.
-->
# **LLM-Evaluation Track**

### **What is LLM-Evaluation?**

LLM-Evaluation is a research area in artificial intelligence that focuses on **assessing large language models (LLMs)** by measuring their accuracy, reasoning, fairness, and safety. The goal is to identify strengths, weaknesses, and risks in order to deploy models responsibly.

### **Why LLM-Evaluation?**

AI often looks strong on benchmarks but fails in the real world. This track gives students the tools to close that gap by building their own tests that measure what really matters \- **skills relevant for jobs and for emerging laws like the AI Act**.

By the end, you will:

* **Build an automated evaluation suite** for a language model, complete with custom metrics, a domain-specific dataset, and tests for bias and robustness.  
* Gain practical experience with the full cycle: finding a real-world problem, running evaluations, and presenting a nuanced analysis beyond accuracy scores.
* Best case, we, Aleph Alpha, will publish the results, benchmarks, and best practices on Hugging Face. If the results prove even more impressive, we are happy to collaborate with the corresponding team on a research paper and submit it to a major AI conference.
* Be able to confidently say:  
  *“I’m well-prepared for the real-world challenges of building and deploying responsible and effective AI systems. I have a gut feeling for AI’s limitations and possible solutions because I’ve built a system that uncovers core Challenges in LLM Evaluation everyone faces but most don’t solve”*

### **Core Challenges in LLM Evaluation**

* Evaluate Results  
  * Unresolved limitations after fine-tuning: Metrics are optimized, but the model continues to hallucinate, underperform, show random validation loss, and struggle with context understanding.  
* Review Process  
  * Synthetic-only testing: Reliance on artificial data misses real-world failures.  
  * Lack of user-centered validation: Results don’t reflect practical needs.  
  * Omission of real-world testing: Models appear strong in labs but weak in practice.  
* Reasonable Next Steps  
  * Domain-specific metrics: Existing metrics fail to capture outcomes stakeholders care about.  
  * Avoid surface-level metrics: Misaligned metrics lead to poor insights.  
  * Integrate real-world testing: Combine robustness, fairness, and custom measures into the evaluation pipeline.
 


## **Week 1: The Foundations of Evaluation and Identifying a Real-World Problem**

This week, we'll move beyond the simplistic view of "good" and "bad" models. We'll start by deconstructing the limitations of popular benchmarks.

* **Goal**: Understand the pitfalls of standard benchmarks and define a specific, real-world problem to evaluate.  
* **Topics**:  
  * The "overfitting on public benchmarks" problem.  
  * The difference between generative MMLU and "Lock-Props".  
  * The importance of domain-specific evaluation.  
* **Challenge**:  
  1. **Select a domain**: Choose a specific, real-world scenario (e.g., a customer support chatbot for a specific industry, a tool for summarizing legal documents, a generator of "simple language" text for public services).  
  2. **Initial Exploration**: Use a pre-trained LLM for your chosen domain.  
  3. **Identify "Failure" Modes**: Manually probe the model to find examples of where it fails. This could be factual inaccuracies, stylistic issues, or biases.  
* **Hints & Constraints:**  
  1. **Tools:** Python 3.8+, Hugging Face *transformers*, *datasets*, and *evaluate*.  
  2. **Readings:**   
     * [On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?](https://faculty.washington.edu/ebender//papers/Bender-NE-ExpAI.pdf) by Bender et al.  
     * [The Ultimate Guide to LLM Evaluation](https://www.confident-ai.com/blog/how-to-evaluate-llm-applications#:~:text=In%20this%20article%2C%20as%20the%20founder%20of%20Confident,when%20building%20RAG%20applications%20that%20evaluation%20can%20solve.) by Confident AI.  
     * [Chatbot Arena](https://lmsys.org/blog/2023-05-03-arena/)  
  3. **Pitfalls to Avoid:** Don’t chase a single number. Don’t forget the “why.”

## **Week 2: Evaluation \- Bias, Fairness, and Adversarial Testing**

Now we move into the really interesting and challenging aspects of evaluation. We'll actively try to break our model.

* **Goal**: Implement tests for bias, fairness, and robustness to adversarial attacks.  
* **Topics**:  
  * The impact of orthography on languages like German.  
  * Gender bias (Winogender).  
  * "Jailbreaking" and adversarial prompting.  
* **Challenge**:  
  1. **Bias Testing**: Create a set of prompts designed to reveal biases in your model. For example, if you're evaluating a hiring assistant, test for gender or racial bias in its recommendations.  
  2. **Adversarial Attacks**: Try to "jailbreak" your model. Can you get it to produce harmful or nonsensical content?  
  3. **Implement a Custom Metric**: Go beyond standard metrics and create your own evaluation metric using a tool like DeepEval. This could be a metric for "simplicity of language" or "adherence to a specific format."  
* **Hints & Constraints:**  
  1. **Tools:** DeepEval for custom metrics.  
  2. **Readings:**   
     * Latest papers from Aleph Alpha’s *DEITY* group.  
     * [https://github.com/rudinger/winogender-schemas](https://github.com/rudinger/winogender-schemas)  
     * [https://deepeval.com/docs/getting-started](https://deepeval.com/docs/getting-started)  
  3. **Pitfalls to Avoid:** Don’t use surface-level or irrelevant metrics.

## **Week 3: Building a Custom Evaluation Dataset**

This week is all about getting your hands dirty with data. As Samu says, "Nobody reads through eval datasets", but we will. Ask yourself: what do I want to prove?

* **Goal**: Create a high-quality, domain-specific evaluation dataset.  
* **Topics**:  
  * The problem of "not enough samples".  
  * Techniques for creating "golden" datasets.  
  * Understanding that even famous datasets like MNIST have labeling errors.  
* **Challenge**:  
  1. **Data Collection**: Gather a small (50-100 examples) but diverse set of data for your chosen domain.  
  2. **Manual Annotation**: Write "golden" outputs for your collected data. This will be your ground truth.  
  3. **Augmentation**: Use an LLM to generate variations of your collected data to increase the size and diversity of your dataset.  
* **Hints & Constraints:**  
  1. **Tools:** Hugging Face Hub for dataset/model sharing.  
  2. **Readings:**   
     * [https://huggingface.co/docs/datasets/create\_dataset](https://huggingface.co/docs/datasets/create_dataset)  
     * [https://aclanthology.org/2021.emnlp-main.255/](https://aclanthology.org/2021.emnlp-main.255/)  
     * [https://neptune.ai/blog/data-augmentation-nlp](https://neptune.ai/blog/data-augmentation-nlp)  
  3. **Pitfalls to Avoid:** Don’t underestimate annotation difficulty \- start small and iterate.

## **Week 4: Automation, Reporting, and a Final Solution**

In the final week, we'll bring everything together into a professional, automated pipeline. We open-sourced our eval framework which can be found on [github](https://github.com/Aleph-Alpha-Research/eval-framework). Get familiar with it, then use it to your means.

* **Goal**: Automate the entire evaluation process and present the results in a clear, insightful way.  
* **Topics**:  
  * Using APIs for evaluation.  
  * Creating effective visualizations and presentations.  
  * The importance of a "proper quality standard".  
* **Challenge**:  
  1. **Build an Evaluation Script**: Write a script that takes a model and your custom dataset, runs all your evaluation metrics (standard, custom, bias, adversarial), and saves the results.  
  2. **Visualize the Results**: Create charts and graphs to visualize your findings.  
  3. **Write a Final Report**: Summarize your findings in a report. This report should not just present the numbers, but also offer a nuanced analysis of the model's performance in your chosen domain.  
* **Hints & Constraints:**  
  1. **Tools:** Aleph Alpha’s Pharia Studio; Weights & Biases for experiment tracking.  
  2. **Readings:**   
     * [https://dagshub.com/blog/ci-cd-for-machine-learning-test-and-and-deploy-your-ml-model-with-github-actions/](https://dagshub.com/blog/ci-cd-for-machine-learning-test-and-and-deploy-your-ml-model-with-github-actions/)  
     * [https://matplotlib.org/stable/gallery/index.html](https://matplotlib.org/stable/gallery/index.html)  
     * [https://www.dataquest.io/blog/data-science-portfolio-project/](https://www.dataquest.io/blog/data-science-portfolio-project/)  
     * [https://wandb.ai/site/reports](https://wandb.ai/site/reports)  
  3. **Pitfalls to Avoid:** Don’t rely only on synthetic validation \- real-world results matter most.
