<!--
Copyright 2026 Arkadia Heilbronn gGmbH
Licensed under the Apache License, Version 2.0. See LICENSE file.
-->
# AI Engineering

**August 31 – October 2, 2026 · 5 weeks, full-time**
Mentored by **appliedAI** in collaboration with **TUM Venture Lab**

## About the Track

In AI Engineering, teams designed and built their own agentic AI application from their own idea, going *beyond a standard chatbot*: systems where AI agents do the essential work by calling tools, retrieving information, and completing multi-step tasks.

- **Weeks 1–4:** Build an MVP, with mentor sessions on architecture, technical decisions, implementation challenges, and pitching the business case.
- **Week 5:** Final pitch preparation and team demos.

Teams chose their own stack. Common building blocks included tool-calling agents, multi-agent coordination, RAG and vector databases, structured outputs, agent memory and state, human-in-the-loop workflows, and evaluation. Arkadia provided API credits for LLM access, and all MVPs are open source.

## Projects

| Project | Repository | In one line |
|---------|------------|-------------|
| MIA | [frankgeorge/mia-dpp](https://github.com/frankgeorge/mia-dpp) | Turns product datasheets into EU-compliant Digital Product Passports |
| Content-Bridge | [vishnudevramachandra/Content-Bridge](https://github.com/vishnudevramachandra/Content-Bridge) | Connects content across CMS platforms without migrating them |
| GoalCoach | [Psyche0920/GoalCoach](https://github.com/Psyche0920/GoalCoach) | Adaptive, state-driven coach for learning Chinese |
| Quotation Bot (Friday Afternoon) | [Shuyin-bot/Friday_Afternoon](https://github.com/Shuyin-bot/Friday_Afternoon) | Turns incoming request emails into quotation drafts |

### MIA: Digital Product Passport Platform

Under the EU ESPR regulation, manufacturers will need Digital Product Passports (DPPs). MIA generates them in minutes. A manufacturer uploads a product datasheet (PDF, Excel, CSV or DOCX), and an AI agent extracts the product data and maps it to the official IDTA Asset Administration Shell submodels (Digital Nameplate, Technical Data, Carbon Footprint, Handover Documentation). The agent flags missing required fields and can ask suppliers for them through an emailed portal link. MIA then compiles and validates a standards-compliant AAS JSON and publishes a public passport page with a QR code.

*Stack:* PydanticAI, OpenRouter, FastAPI, aas-core3.0, Next.js, Supabase, deployed on Vercel. Live at [mia-dpp.vercel.app](https://mia-dpp.vercel.app).

### Content-Bridge

Many organizations run content across several CMS platforms and keep them in sync by hand. Content-Bridge connects them with a shared semantic mapping layer instead of a full migration. An orchestrator agent coordinates three specialist sub-agents:

- A **Discovery** agent reads each system (Strapi, WordPress) and describes its schema as an OWL ontology.
- A **Mapping** agent links the two ontologies in an SSSOM mapping table.
- A **Sync** agent uses that mapping to push Strapi content to WordPress.

The same mapping also catches compliance drift. For example, when a WordPress post cites an outdated certification that no longer matches the system of record, it flags the post for human review. The approach is deterministic where the data allows it, uses LLM judgment where it doesn't, and keeps a human in the loop when even that isn't enough.

*Stack:* PydanticAI multi-agent orchestration, Strapi, WordPress, React/Vite frontend, Docker Compose.

### GoalCoach

Most AI language tutors are stateless chatbots. They forget what the learner has mastered, they don't pace a curriculum, and they can't schedule spaced repetition. GoalCoach is an adaptive coach for Chinese as a second language (HSK 1) built around a closed, state-driven loop: *Goal → Plan → Teach → Grade → Update State → Adapt → Re-plan*. Deterministic Python handles mastery scoring, retention decay, and prerequisite graphs. PydanticAI agents (Planning, Teaching, and a Grader) are used only where teaching judgment is needed, so the same goal with different learner state produces a different plan. A hosted model is the primary engine, with automatic fallback to a local Ollama model.

*Stack:* PydanticAI, FastAPI, SQLite (curriculum + learner-state databases), React 18/Vite web app, interactive CLI.

### Quotation Bot (Friday Afternoon)

Built for a packaging manufacturer, Quotation Bot automates the repetitive work of answering quotation requests. It reads incoming emails from an IMAP mailbox and classifies which ones are quotation requests. A tool-using core agent then extracts the request, researches the customer, searches the product catalog (SQL and a Chroma vector store), calculates prices from inventory and price lists, and drafts a reply. When information is missing, the agent pauses to ask a human and resumes from its saved session. Every draft is approved, edited, rejected, or sent back for revision in a review dashboard before it goes out.

*Stack:* PydanticAI, SQLAlchemy/Alembic + SQLite, Chroma, FastAPI, React + Material UI dashboard ([friday_afternoon_fe](https://github.com/Shuyin-bot/friday_afternoon_fe)).
