<!--
Copyright 2025 Arkadia Heilbronn gGmbH
Licensed under the Apache License, Version 2.0. See LICENSE file.
-->
# Track Development 
**Meta-track: Building a Track**

In this track, you’ll design and build a complete LEVEL3 track, based on something that actually matters. The goal is to turn a real-world challenge into a structured 4-week challenge that helps others learn something useful, relevant, and impressive.

You’ll go through the full process:  
- Choosing the topic
- Structuring the 4-week progression
- Collecting helpful resources and hints
- Building a working solution to test and validate the track

This "Track Development Project" will also act as a **template for what a good LEVEL3 track should look like**.

> ⚠️ **Don’t work in isolation.** Each phase should be reviewed with us to make sure you’re on track and aligned with the goals of the program.

## Submission Format
- Submit your track as a **Markdown document**.

![image](./image.jpeg)

## Track Development Process

### 1. Setup and define the Topic

1. **Fork the repository** and clone your fork locally:
   
   1.1. **Fork the repository:**
   - Go to https://github.com/arkadiahn/LEVEL3-projects
   - Click the "Fork" button as shown in the picture: ![Fork button](./fork_button.png)
   
   1.2. **Set the repository name:**
   - Set your repository name as shown in the picture: ![Repository name](./name_of_repo_name.png)
   
   1.3. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/LEVEL3-projects.git
   cd LEVEL3-projects
   ```

2. **Create a feature branch** from the `development` branch:
   
   First, add the upstream repository and fetch the latest changes:
   ```bash
   git remote add upstream https://github.com/arkadiahn/LEVEL3-projects.git
   git fetch upstream
   ```
   
   Then, checkout the `development` branch and create your feature branch:
   ```bash
   git checkout -b feature/my-track-name upstream/development
   ```
   
   Replace `my-track-name` with a descriptive name for your track (e.g., `feature/data-intelligence-track`).
   
   Push your feature branch to your fork:
   ```bash
   git push -u origin feature/my-track-name
   ```

3. **Create a new folder** for your track in your feature branch. Be sure to include a `README.md` file within it.  

4. **Update the main table:** Add your track as a new entry at the bottom of the table in the main [README](/README.md).  

5. **Choose your topic wisely:** Focus on a subject that highlights a **real-world problem or process**—something people truly care about and encounter in everyday engineering or product work.  

    Your topic should be:  
    - **Job-relevant** (it reflects real-world scenarios)
    - **Teachable in 4 weeks**
    - **Impressive** (you’d be impressed if someone brought it up in an interview)

6. **Write a short introduction** at the top of your Readme that clearly answers:  
   - What is the problem?
   - What will participants have built or accomplished by the end of the track duration to solve this problem?
   - Why is this useful or relevant in a real job context?  

### 2. Structure the Track

Break the project into **four incremental parts**, each representing one week of work. Each week should have a clear, achievable goal. All weeks need to be connected or built upon each other, and lead toward a final, working deliverable in the end of the track.
> 💡 Tip: Keep the scope realistic. If Week 1 takes 3 days in the real world, that's fine — not everything needs to be perfectly even. And the appointment for mentor review can be flexible.

1. **Week structure:** Create **4 weeks as mandatory** content, and optionally **2 additional weeks as bonus** for students who want to go deeper into the topic.

2. **For each week**, use the following structure (you can add more sections if needed):
   - **Short introduction** — Context and overview for the week
   - **Goal** — What participants should achieve
   - **Scope** — What's included in this week's work
   - **Expected Outcome** (or **Deliveries**) — What participants will have completed by the end of the week
   - **Bonus part** — Optional extensions or deeper exploration

Include helpful resources and constraints for participants:  
- **Links** to articles, repos, docs, or internal tools
- **Hints** about pitfalls to avoid
- **Restrictions**: required tools, libraries, languages, frameworks, etc.
> ⚠️ You don't need to explain the theory. The goal is to **save time and reduce frustration**, not write a textbook.

### 3. Submission

   **Create a pull request** targeting the `development` branch in the upstream repository.  
   Our team will review your track, share feedback, and may make small adjustments before merging it into `main`.  
   
   To create a pull request:
   - Go to your GitHub repository
   - Click "Compare & pull request" as shown in the picture: ![Create PR](./create_PR.png)
   - Select the `development` branch as the target branch, as shown in the picture: ![Choose development branch](./choose_development_branch.png)


### 4. Build Your Own Solution

You must build the full project yourself to ensure:  
1. It's feasible in practice  
2. You catch tricky or ambiguous areas  
3. You can provide a working reference if questions come up later

Your solution doesn’t have to be pretty or production-grade, but it should:  
- Cover all weeks
- Meet your own stated requirements
- Be shared in a **private repo** with us

> ⚠️ Your solution is **not the final product** — it’s a safety net.