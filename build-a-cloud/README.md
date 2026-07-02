<!--
Copyright 2026 STACKIT GmbH
Licensed under the Apache License, Version 2.0. See LICENSE file.
-->
# Building a Cloud-Native Platform: From IaaS to PaaS

**Meta-Track: Infrastructure → Platform → Product**

This track is about **owning the full stack**. You will get your hands on building a complete cloud platform stack end-to-end—starting from raw infrastructure, moving through Kubernetes, and ending with a production-grade PaaS product featuring APIs, UI, automation, and observability.

Every phase results in something tangible. By the end, you will have built and operated a real platform that reflects how modern cloud providers actually work.

**Outcome**: A fully functional PaaS on Kubernetes, running on OpenStack and SKE, complete with automation, observability, and developer tooling.

![image](./image.png)

---

## Week 1 – IaaS Foundations & Provisioning a Kubernetes Cluster on OpenStack

You start at the bottom, no shortcuts.

### Goal
Understand and operate Infrastructure-as-a-Service (IaaS) by setting up and validating an OpenStack environment.

### Scope
1. **Understanding the OpenStack Architecture**
   - How OpenStack is structured
   - Responsibilities of core components: Virtual Machines, Networks, Storage, and related services
2. **Installation and Basic Configuration** of a single-node OpenStack cluster using DevStack
3. **Validation of the Installation** by:
   - Checking system logs
   - Checking service status and health
4. **Deployment** of a virtual machine via OpenStack
5. **Architecture Analysis:**
   - Analyze the current installation
   - Create a technically correct architecture diagram of the setup
6. **Understanding Terraform and Infrastructure as Code (IaC):**
   - What Infrastructure as Code is and its core advantages
   - Terraform basics: Providers, Resources, State
   - The core Terraform workflow
7. **Provision a Virtual Machine** with Terraform using the OpenStack APIs
8. **Installation and Configuration of Kubernetes** with a tool of your choice

### Bonus
* **Fully Automated Installation:** Implement a single command to automatically provision the OpenStack virtual machine and install the Kubernetes cluster.
* **Two-Node Kubernetes Cluster Setup:** Expand the installation script to provision two virtual machines and configure them to form a two-node Kubernetes cluster.

---

## Week 2 – Developing a Platform-as-a-Service (PaaS) Product on STACKIT Kubernetes Engine (SKE)

Infrastructure is useless without a product. Now you build one.


### Goal
Design and implement a Platform-as-a-Service offering on top of Kubernetes.

### Scope
1. **Understanding Kubernetes Concepts**
   - Infrastructure Components: Control Plane and Worker Nodes
2. **SKE Cluster Creation:** Using the STACKIT Terraform Provider to provision an SKE cluster
3. **PaaS Product Implementation (e.g., Managed Database):** Design and technical implementation of a simple PaaS service
   - **Operator Deployment:** Provisioning of a Kubernetes Operator
   - **Product Component Management:** Utilization of Custom Resources (CRs) for provisioning and managing product components
   - **Connectivity:** Documentation and demonstration of connecting to and using the PaaS product
4. **Deepening Kubernetes Knowledge:** Deepening knowledge of Custom Resource Definitions (CRDs) and the functioning of Operators (Reconciler Pattern)

### Bonus
* **Automating the Deployment:** Introduction of a GitOps approach and CI/CD integration for automated provisioning of both SKE and the PaaS service.

---

## Week 3 – Developing a Platform-as-a-Service (PaaS) Product: API Layer

APIs are the front door to your platform. Make them robust, secure, and developer-friendly.


### Goal
Expose the PaaS product through a clean, production-ready RESTful API to enable automated provisioning and seamless integration.


### Scope
1. **API Development for Product Instances:** Development of a RESTful API that provides operations for creating, deleting, and listing PaaS product instances, as well as retrieving associated connection and access data.
   - **API Specification:** The functionality of the API must be fully documented using the OpenAPI specification.
2. **Unit Tests:** Implementation of unit tests for each endpoint of the developed API.
3. **Docker Container Image:** Creating a Docker image for the API, uploading it to the STACKIT Container Registry, and deploying the API via SKE.
4. **Understanding the Lifecycle Process (Create Flow):**
   - **Flowchart:** Visualization of the individual steps required to create a product instance.
   - **REST Fundamentals:** Solidifying basic understanding of how a RESTful API operates.

### Bonus
* **Automated API Deployment:** Integration of the RESTful API deployment into the existing GitOps infrastructure.
* **Auto-Scaling and Performance Tests:**
   - **Horizontal Pod Autoscaler (HPA):** Configuration of a Kubernetes HPA for automatic scaling of the control plane RESTful API.
   - **Performance Tests:** Execution of performance tests for the RESTful API to verify the functionality of the HPA.
* **Update Functionality:** Implementation and testing of an API endpoint that allows updating access data and instance details.

---

## Week 4 – Extending the Platform with Advanced Features

Your platform isn’t complete until users can securely access and interact with it.

### Goal
Build a user-facing interface and expose the PaaS product securely via the web, ensuring a smooth and accessible developer experience.

### Scope
1. **Web UI Development:** Building a user-friendly web interface (using Vue.js or a similar framework) to interact with the PaaS product, covering all relevant API functions.
2. **Secure Communication:** Implementing secure communication between the UI and backend APIs using JWT (JSON Web Tokens) or a similar standard.
3. **Ingress Controller Deployment:** Provisioning an Ingress controller on the SKE cluster.
4. **Production Publication:** Exposing the API and Web UI on the SKE cluster with SSL/TLS encryption and a free STACKIT subdomain URL.
5. **Architecture Diagram Update:** Adapting the architecture diagram to illustrate the exact traffic flow between the Web UI, Ingress, and backend APIs.

### Bonus
* **Automated UI Deployment:** Automating the Web UI deployment on the existing SKE via GitOps integration.
* **End-to-End (E2E) Testing:** Implementation of E2E tests (e.g., via Cypress or Playwright) for both the Web UI and the RESTful API.

---

## Week 5 – Extending the Platform with Advanced Features

If you can’t see it or audit it, you can’t run it at scale.

### Goal
Enable production-grade operations through observability and audit logging.

### Scope
1. **Internal Monitoring:** Gathering persistent telemetry data that the platform operator can use for real-time health and performance evaluation.
   - Integration of Prometheus and Grafana for monitoring the health of Kubernetes clusters and application performance.
   - Setup of Loki for collecting and analyzing application logs.
2. **User-Centric Monitoring & Logging:** Persistently stored logs that users can retrieve for their specific instances via the UI or API.
   - Implementation of an Audit Logging system for recording user actions (creation, modification, or deletion of instances, access credentials, etc.).

### Bonus
* **Development of a Golang SDK for the PaaS Product:**
   - Creation of a native Go SDK to simplify developer interaction with the PaaS product's API.
   - Implementation of built-in authentication and authorization mechanisms within the SDK.
   - Provision of clear usage documentation and examples.

---

## Final Result

By the end of this track, you will have:

* **Designed and operated a complete infrastructure stack** — from raw IaaS with OpenStack to a functional PaaS running on Kubernetes.
* **Provisioned and managed Kubernetes clusters** using Infrastructure as Code (IaC) with Terraform.
* **Built and deployed a Kubernetes-native PaaS product**, including Custom Resource Definitions (CRDs) and custom Operators.
* **Exposed the platform through a production-ready RESTful API** for end-to-end product lifecycle management.
* **Developed a secure, user-facing Web UI** that interfaces seamlessly with the API and runs on Kubernetes with proper Ingress and SSL.
* **Implemented observability and audit logging**, enabling platform-level monitoring, centralized logging, and absolute traceability for both operators and end users.

This is how real-world cloud platforms are designed, built, and operated from the ground up.