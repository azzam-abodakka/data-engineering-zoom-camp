# Data Engineering Zoomcamp - My Learning Journey 🚀

This repository tracks my progress through the Data Engineering Zoomcamp. My goal is to build a solid foundation in data infrastructure, containerization, and cloud engineering.

## 📁 Week 1: Infrastructure & Environment Setup

In the first week, I focused on setting up a professional development environment and learning the "Standard Pipeline" for data ingestion.

### 🏗️ Projects in this Directory

#### 1. Data Pipeline (`/first-week/pipeline`)
I practiced containerizing a data ingestion workflow. This setup allows for a reproducible environment regardless of the local machine's configuration.
* **Docker & Postgres:** Running a local PostgreSQL database alongside pgAdmin for data exploration.
* **Data Ingestion:** Using Python and Pandas to stream large datasets into a structured database.
* **Network Isolation:** Connecting multiple containers via a dedicated Docker network.

#### 2. Infrastructure as Code (`/first-week/terraform`)
I moved away from manual cloud configuration and learned to manage resources using **Terraform**.
* **GCP Provider:** Authenticating and connecting to Google Cloud Platform.
* **Cloud Storage:** Provisioning Google Cloud Storage (GCS) buckets for raw data.
* **BigQuery:** Setting up a data warehouse schema automatically.

---

### 🧠 Skills Mastered
* **Containerization:** Writing Dockerfiles and managing multi-container apps with Docker Compose.
* **SQL Logic:** Complex data filtering, date casting, and multi-table joins for analytical queries.
* **IaC (Infrastructure as Code):** Understanding the `init` -> `plan` -> `apply` workflow to maintain cloud state.
* **Version Control:** Organizing code into a clean, professional GitHub directory structure.


---
*Follow my journey as I move into Week 2: Workflow Orchestration!*