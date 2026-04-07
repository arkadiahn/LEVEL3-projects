# Building Digital Twins with AAS: From Concepts to Secure Infrastructure

**Duration:** 2 Weeks (Full-Time)  
**Level:** Intermediate (Programming experience required, no prior AAS knowledge needed)  
**Track Focus:** Digital Twins → AAS Infrastructure → Secure Data Exchange  

---

## Overview

This course provides a comprehensive, hands-on introduction to **Digital Twins** and the **Asset Administration Shell (AAS)** key technologies driving Industry 4.0 and the digital transformation of industrial systems.

Participants will move beyond theory and build a **fully functional AAS infrastructure** using **Eclipse BaSyx**, learning how to model digital assets, manage structured data, and enable secure communication between distributed systems.

By the end of the course, participants will have designed and operated a real-world AAS environment, reflecting how modern industrial platforms are built and used.


![AAS Digital Twin Infrastructure](https://gitlab-test.cloud.schunk.com/technology-factory/42-students-ipai/LEVEL3-projects/-/raw/main/aas-digital-twin-infrastructure/aas.png)

---

## Learning Objectives

Participants will:

- Understand the concept of **Digital Twins** and their role in modern industry  
- Gain in-depth knowledge of the **Asset Administration Shell (AAS)** architecture  
- Build and operate a **complete AAS infrastructure** using Docker and BaSyx  
- Design and implement **AAS shells and submodels**, including Technical Nameplates  
- Generate and manage **AASX files** programmatically  
- Store and retrieve AAS data using **MongoDB**  
- Enable **communication between distributed AAS systems**  
- Implement **authentication and authorization** for secure data access  
- Interact with AAS systems through **REST APIs and automation scripts**  

---

## Course Structure

---

## Phase 1 – Introduction to Digital Twins & AAS

Participants begin by understanding the fundamental concepts behind Digital Twins and the AAS standard.

**Topics include:**

- What is a Digital Twin and how it represents real-world assets  
- The role of AAS in enabling interoperability across systems  
- Structure of an AAS:
  - Asset  
  - AAS Shell  
  - Submodels  
  - Submodel Elements  
- Introduction to common industrial use cases:
  - Digital Product Passport  
  - Technical Nameplate  
  - Lifecycle tracking  

Participants will explore existing AAS examples and understand how structured data is represented in practice.

### Q&A Session

---

### Phase 2 – Building Your Own AAS Infrastructure

Participants move from theory to implementation by designing and deploying their own AAS system.

#### AAS Infrastructure Setup

- Understanding the architecture of Eclipse BaSyx:
  - AAS Server  
  - AAS Registry  
  - Submodel Repository  
- Building the system manually using **Docker Compose**  
- Integrating **MongoDB** as a persistence layer  


#### System Validation

- Verifying service health and logs  
- Accessing and interacting with the AAS system through the web UI and APIs  


#### AAS Modeling and Creation

- Choose a product from your company and find its nameplate data.
- Search the specification for the submodel **Digital Nameplate** on https://smt-repo.admin-shell-io.com/
- Map your product data to the Digital Nameplate Submodel.

#### AASX File Generation

- Creating structured JSON representations of submodels  
- Converting JSON into **AASX files**  

#### AAS Registry Usage (Core Industry Concept)

- Registering AAS instances in the **AAS Registry**  
- Discovering AAS dynamically via the Registry  
- Querying the Registry to locate AAS services instead of using fixed endpoints  

This introduces a key real-world concept: **service discovery in distributed systems**.

#### Data Persistence

- Storing and retrieving AAS data in MongoDB  
- Understanding how AAS data is managed at the storage level  

#### Bonus: BaSyx SDK

- Create your AASX file using the BaSyx SDK

#### Phase 2 Review


## Phase 3 – Secure AAS Communication & Data Exchange

In this phase, participants extend their systems into distributed environments.

Each team operates its own AAS infrastructure and enables communication between systems.

---

#### Distributed AAS Systems

- Running independent AAS servers per team  
- Establishing communication between systems via REST APIs  


#### AAS Data Exchange

- Sending and receiving AAS and Submodels between servers  
- Implementing workflows for:
  - Fetching remote AAS data  
  - Sharing submodels across systems  


#### Authentication & Authorization

Participants implement security mechanisms to protect their systems.

- Securing API endpoints using token-based authentication (e.g., JWT or API keys)  
- Defining access rules:
  - Read-only access  
  - Write permissions  
- Enforcing secure communication between teams  

#### System Design & Architecture

- Creating a complete architecture diagram of the system  
- Visualizing:
  - Data flow  
  - Component interaction  
  - Security boundaries  


#### Bonus: Automation with Python

- Developing scripts to interact with AAS systems via REST APIs  
- Automating operations such as:
  - Uploading AASX files  
  - Modifying submodels  
  - Retrieving AAS data  

### Phase 3 Review


## Final Deliverables

By the end of the course, participants will present:

- A **live demonstration** of their working AAS infrastructure  
- A **Git repository** containing:
  - Docker setup  
  - AAS models  
  - Automation scripts  
- A **technical architecture diagram**  
- A **README documentation** explaining system setup and usage  

---

## Outcome

Participants will finish the course with:

- A solid understanding of **Digital Twins and AAS standards**  
- Practical experience in building and operating **AAS-based systems**  
- The ability to model, store, and exchange **structured industrial data**  
- Hands-on experience with **BaSyx, Docker, REST APIs, and MongoDB**  
- Knowledge of **secure system design and distributed communication**  
