# Building a Cloud-Native Platform: From IaaS to PaaS

**Meta-Track: Infrastructure → Platform → Product**

This track is about **owning the full stack**. You will get your hands on building a complete cloud platform stack end-to-end: starting from raw infrastructure, moving through Kubernetes, and ending with a production-grade PaaS product with APIs, UI, automation, and observability.

Every phase results in something tangible. By the end, you will have built and operated a real platform that reflects how modern cloud providers actually work.

**Outcome:** A fully working PaaS on Kubernetes, running on OpenStack and SKE, with automation, observability, and developer tooling.

![image](./image.png)

## Week 1 – IaaS Foundations with OpenStack

You start at the bottom.

### Goal

Understand and operate Infrastructure-as-a-Service by setting up and validating an OpenStack environment.

### Scope

1. **Understanding the OpenStack Architecture**  
   - How OpenStack is structured  
   - Responsibilities of core components:  
     - Virtual Machines  
     - Networks  
     - Storage and related services  
2. **Installation and Basic Configuration** of a Single-node OpenStack cluster using DevStack  
3. **Validation of the installation** by**:**  
   - Checking system logs  
   - Checking service status and health  
4. **Deployment** of a virtual machine via OpenStack  
5. **Architecture Analysis:**  
   - Analyze the current installation  
   - Create a technically correct architecture diagram of the setup

## Week 2 – Provisioning a Kubernetes Cluster on OpenStack

Now you automate. Manual infrastructure does not scale.

### Goal

Provision a Kubernetes cluster on OpenStack using Terraform \- Infrastructure-as-Code (IaC)

### Scope

1. **Understanding Terraform** and Infrastructure as Code:  
   - What Infrastructure as Code is and what are its advantages  
   - Terraform basics:  
     - Providers  
     - Resources  
     - State  
   - Terraform workflow  
2. **Provisioning a Kubernetes Cluster** with Terraform using OpenStack APIs  
3. **Installation and Configuration** of Kubernetes  
4. **Core Kubernetes Concepts**  
   - Infrastructure Components: Control Plane and Worker Nodes  
   - Pods, Deployments, Services, Namespaces

## Week 3 – Developing a Platform-as-a-Service (PaaS) Product (on SKE)

Infrastructure is useless without a product. Now you build one.

### Goal

Design and implement a Platform-as-a-Service offering on top of Kubernetes.

### Scope

1. **SKE Cluster Creation:** Using the STACKIT Terraform Provider to provision an SKE (STACKIT Kubernetes Engine) Cluster  
2. **PaaS Product Implementation (e.g., Managed Database)**: Design and technical implementation of a simple PaaS service.  
   - **Operator deployment**: Provisioning of an Operator  
   - **Product Component Management**:  Utilization of Custom Kubernetes Resources (CRs) for the provisioning and management of product components  
   - **Connectivity**: Documentation and demonstration of connecting to and using the PaaS product  
3. **Understanding Kubernetes Concepts:** Deepening knowledge of Custom Resource Definitions (CRDs) and the functioning of Operators (Reconciler Pattern)

### Bonus

**Automating the Deployment:** Introduction of a GitOps approach and CI/CD integration for automated provisioning of the SKE and the PaaS service

## Week 4 – Provisioning and Interaction via RESTful API

APIs are the front door to your platform. Make them robust, secure, and developer-friendly.

### Goal

Expose the PaaS product through a clean, production-ready RESTful API to enable automated provisioning and seamless integration.

### Scope

1. **API Development for Product Instances**: Development of a RESTful API that provides the following functions: creation, deletion, and listing of PaaS product instances, as well as retrieval of the associated connection and access data.  
* API Specification: The functionality of the API must be documented in the form of OpenAPI specifications  
2. **Unit Tests:** Implementation of simple Unit Tests for each endpoint of the developed API  
3. **Docker Container Image** for the API creation, upload to the STACKIT Container Registry, and provisioning of the API via SKE  
4. **Understanding the Creation Process (Create Flow):**  
* **Flowchart for the creation of a product instance:** Visualization of the individual steps  
* **Basic understanding of how a RESTful API works**

### Bonus

1. **Automated API Deployment**: Integration of the deployment of the RESTful API into the existing GitOps infrastructure  
2. **Auto-Scaling and Performance Tests**:  
* **Horizontal Pod Autoscaler (HPA):** Configuration of the Kubernetes HPA for automatic scaling of the Control Plane RESTful API  
* **Performance Tests**: Implementation of performance tests for the RESTful API to verify the functionality of the HPA  
3. **Update Functionality**: Implementation and testing of an API endpoint that allows the updating of access data and details of the product instance

## Week 5 – Extending the Platform with Advanced Features

Your platform isn’t complete until users can securely access and interact with it.

### Goal

Build a user-facing interface and expose the PaaS product securely via the web, ensuring a smooth and accessible developer experience.

### Scope

1. **Development of a user-friendly Web UI** with Vue.js or similar for interaction with the PaaS product, covering all relevant functions of the API  
2. **Implementation of secure communication** between UI and backend APIs using JWT (JSON Web Tokens) or similar  
3. **Deployment of Ingress controller** on SKE cluster  
4. **Publication of the API and Web UI** on SKE cluster with SSL and free STACKIT subdomain URL  
5. **Adaptation of the architecture diagram** to illustrate the traffic flow with API, Web UI, and Ingress

### Bonus

6. **Automated Deployment** of the Web UI on the existing SKE via GitOps integration  
7. **Implementation of E2E tests** (e.g., with Cypress or Playwright) for the Web UI and the RESTful API

## Week 6 –  Implementation of Observability and Audit Logging

If you can’t see it or audit it, you can’t run it at scale.

### Goal

Enable production-grade operations through observability and audit logging.

### Scope

1. **Internal Monitoring**: Persistent telemetry data that the product operator can use for monitoring  
* Integration of Prometheus and Grafana for monitoring the health of Kubernetes clusters and application performance  
* Setup of Loki for collecting and analyzing application logs  
    
2. **User-Centric Monitoring:** Persistently stored logs that users can retrieve for their instances via the UI (or API)  
* Implementation of an Audit Logging system for recording user actions (creation/modification/deletion of an instance or access data or similar)  
* Implementation of Service Logs with relevant information for the user for security and compliance (asynchronous status changes or similar information that might be of interest to the user)

### Bonus

**Development of a Golang SDK for the PaaS Product**

* Creation of a Golang SDK that simplifies interaction with the PaaS product's API  
* Implementation of authentication and authorization mechanisms within the SDK  
* Provision of clear documentation and examples for using the SDK

## Final Result

By the end of this track, you will have:

* **Designed and operated a complete infrastructure stack** — from raw IaaS with OpenStack to a functional PaaS running on Kubernetes  
* **Provisioned and managed Kubernetes clusters** using Infrastructure as Code with Terraform  
* **Built and deployed a Kubernetes-native PaaS product**, including CRDs and Operators  
* **Exposed the platform through a production-ready RESTful API** for product lifecycle management  
* **Developed a secure, user-facing Web UI** that interfaces with the API and runs on Kubernetes with proper ingress and SSL  
* **Implemented observability and audit logging**, enabling platform-level monitoring, logging, and traceability for both operators and users

This is how real-world platforms are designed, built, and operated from the ground up.
