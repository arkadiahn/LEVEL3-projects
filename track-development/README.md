<!--
Copyright 2025 Aleph Alpha GmbH and Aleph Alpha Research GmbH
Licensed under the Apache License, Version 2.0. See LICENSE file.
-->
# Track Development - Additional Hints and Ideas
**Meta-track: Building a Track**

In this track, you’ll design and build a complete LEVEL3 track, based on something that actually matters. The goal is to turn a real-world challenge into a structured 4-week challenge that helps others learn something useful, relevant, and impressive.

You’ll go through the full process:  
- Choosing the topic  
- Structuring the 4-week progression  
- Collecting helpful resources and hints  
- Building a working solution to test and validate the track  

## 1. Week 1: The Foundations of Evaluation and Identifying a Real-World Problem
This week, we'll move beyond the simplistic view of "good" and "bad" models. We'll start by deconstructing the limitations of popular benchmarks.

* Goal: Understand the pitfalls of standard benchmarks and define a specific, real-world problem to evaluate.

* Challenge:
  * Select a specific, real-world scenario.
  * Use a pre-trained LLM for your chosen domain.
  * Identify "failure" modes by manually probing the model.
 
* Further Reading
  * https://dl.acm.org/doi/10.1145/3442188.3445922
  * https://www.google.com/search?q=https://www.infoq.com/articles/leaderboard-trust-cv-nlp-ml/
  * https://www.google.com/search?q=https://www.promptfoo.dev/docs/guides/evaluation/
  * https://lmsys.org/blog/2023-05-03-arena/ 


## 2. Week 2: Building a Custom Evaluation Dataset
This week is all about getting your hands dirty with data. As Samu says, "Keiner liest sich Evaldatensätze durch" ("Nobody reads through eval datasets"), but we will.

* Goal: Create a high-quality, domain-specific evaluation dataset.

* Challenge:
  * Gather a small but diverse set of data for your chosen domain.
  * Write "golden" outputs for your collected data.
  * Use an LLM to generate variations of your data to increase the dataset's size.
 
* Further Reading
  * https://huggingface.co/docs/datasets/create_dataset
  * https://aclanthology.org/2021.emnlp-main.255/
  * https://www.google.com/search?q=https://www.scale.com/guides/data-annotation-guide
  * https://www.google.com/search?q=https://neptune.ai/blog/data-augmentation-in-nlp



## 3. Week 3: Advanced Evaluation - Bias, Fairness, and Adversarial Testing
Now we move into the really interesting and challenging aspects of evaluation. We'll actively try to break our model.

* Goal: Implement tests for bias, fairness, and robustness to adversarial attacks.

* Challenge:
  * Create a set of prompts designed to reveal biases in your model.
  * Try to "jailbreak" your model.
  * Implement a custom metric using a tool like DeepEval.
 
* Further Reading
  * https://github.com/rudinger/winogender-schemas
  * https://www.google.com/search?q=https://www.anthropic.com/news/red-teaming-language-models
  * https://www.jailbreakchat.com/
  * https://www.google.com/search?q=https://docs.confident-ai.com/docs/getting-started


## 4. Week 4: Automation, Reporting, and a Final Solution
In the final week, we'll bring everything together into a professional, automated pipeline.

* Goal: Automate the entire evaluation process and present the results in a clear, insightful way.

* Challenge:
  * Write a script that automates the entire evaluation process.
  * Create charts and graphs to visualize your findings.
  * Write a final report summarizing your findings.
 
* Further Reading
  * https://www.google.com/search?q=https://docs.github.com/en/actions/deployment/deploying-machine-learning-models/building-and-deploying-a-model-with-github-actions
  * https://matplotlib.org/stable/gallery/index.html
  * https://www.dataquest.io/blog/data-science-portfolio-project/
  * https://wandb.ai/site/reports
 
  
