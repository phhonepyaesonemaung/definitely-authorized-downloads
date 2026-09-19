name: GDrive to Telegram Sync

on:
  workflow_dispatch:

jobs:
  migrate:
    name: Upload Course
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 1
      fail-fast: false
      matrix:
        course_name:
          - "12 Factor App"
          - "AB-900_ Microsoft 365 Copilot and Agent Administration Fundamentals"
          - "AI Agents"
          - "AI Agents Fundamentals"
          - "AI Agents for Beginners_ OpenClaw Case Study"
          - "AI Assisted Ansible"
          - "AI Infrastructure_ LLM-D, vLLM and GPUs"
          - "AI-102_ Microsoft Certified Azure AI Engineer Associate"
          - "AI-900_ Microsoft Certified Azure AI Fundamentals"
          - "AI-Assisted Development"
          - "AWS - IAM"
          - "AWS Certified AI Practitioner"
          - "AWS Certified CloudOps Engineer – Associate"
          - "AWS Certified Developer - Associate"
          - "AWS Certified Machine Learning Engineer - Associate"
          - "AWS Cloud Practitioner (CLF-C02)"
          - "AWS CloudFormation"
          - "AWS CloudWatch"
          - "AWS CodePipeline (CI_CD Pipeline)"
          - "AWS EKS"
          - "AWS Lambda"
          - "AWS Networking Fundamentals"
          - "AWS RDS"
          - "AWS Solutions Architect Associate Certification"
          - "AZ-204_ Developing Solutions for Microsoft Azure"
          - "AZ-305_ Microsoft Azure Solutions Architect Expert"
          - "AZ-400_ Designing and Implementing Microsoft DevOps Solutions"
          - "AZ-700_ Designing and Implementing Microsoft Azure Networking Solutions"
          - "AZ900_ Microsoft Azure Fundamentals"
          - "Advanced Bash Scripting"
          - "Advanced Golang"
          - "Advanced Jenkins"
          - "Amazon Elastic Compute Cloud (EC2)"
          - "Amazon Elastic Container Service (AWS ECS)"
          - "Amazon Simple Storage Service (Amazon S3)"
          - "Ansible Advanced Course"
          - "Azure Kubernetes Service"
          - "CDK for Terraform with TypeScript"
          - "Certified Jenkins Engineer"
          - "Certified Kubernetes Administrator (CKA)"
          - "Certified Kubernetes Application Developer (CKAD)"
          - "Certified Kubernetes Security Specialist (CKS)"
          - "Chaos Engineering"
          - "Claude Code for Beginners"
          - "Cline"
          - "Cloud Computing Fundamentals"
          - "Cloud Native Buildpacks"
          - "CompTIA Security+ Certification"
          - "Crash Course_ Docker For Absolute Beginners"
          - "Crash Course_ Kubernetes For Absolute Beginners"
          - "Cursor AI"
          - "DP-900_ Microsoft Azure Data Fundamentals"
          - "Data Engineering Fundamentals"
          - "Database Fundamentals"
          - "Demystifying DNS"
          - "DevOps Interview Preparation Course"
          - "DevOps Pre-Requisite Course"
          - "DevSecOps - Kubernetes DevOps & Security"
          - "Docker - SWARM _ SERVICES _ STACKS - Hands-on"
          - "Docker Certified Associate Exam Course"
          - "Enhancing Soft Skills for DevOps Engineers_ Essential Non-Technical Skills to Th"
          - "Event Streaming with Kafka"
          - "Exploring WebAssembly (WASM)"
          - "Fundamentals of DevOps"
          - "Fundamentals of RAG"
          - "GCP Cloud Digital Leader Certification"
          - "GCP DevOps Project"
          - "GIT for Beginners"
          - "GKE - Google Kubernetes Engine"
          - "Gateway API with NGINX Fabric Gateway"
          - "Generative AI in Practice_ Advanced Insights and Operations"
          - "GitHub Actions"
          - "GitHub Actions Certification"
          - "GitHub Copilot Certification"
          - "GitHub Copilot in Action"
          - "GitHub Foundations Certification"
          - "GitLab CI_CD_ Architecting, Deploying, and Optimizing Pipelines"
          - "GitOps with ArgoCD"
          - "GitOps with FluxCD"
          - "Golang"
          - "Google ADK"
          - "Google Cloud Professional Data Engineer Certification"
          - "Grafana Loki"
          - "Hands-On AWS Project_ Deploy Your First Crypto App"
          - "HashiCorp Certified_ Consul Associate Certification"
          - "HashiCorp Certified_ Terraform Associate 004"
          - "HashiCorp Certified_ Vault Associate Certification"
          - "HashiCorp Certified_ Vault Operations Professional 2022"
          - "HashiCorp Packer"
          - "HashiCorp _ Terraform Cloud"
          - "Helm for Beginners"
          - "Introduction to AWS Databases"
          - "Introduction to K8sGPT and AI-Driven Kubernetes Engineering"
          - "Introduction to OpenAI"
          - "Introduction to Sealed Secrets in Kubernetes"
          - "Istio Service Mesh"
          - "JSON Path Test - Free Course"
          - "Jenkins"
          - "Jenkins For Beginners"
          - "Jenkins Pipelines"
          - "Jenkins Project_ Building CI_CD Pipeline for Scalable Web Applications"
          - "Jinja2 Basics (Mini Course)"
          - "KServe Fundamentals_ Serving ML Models on Kubernetes"
          - "Kubeflow"
          - "Kubernetes Autoscaling"
          - "Kubernetes Networking Deep Dive"
          - "Kubernetes Operators"
          - "Kubernetes Troubleshooting for Application Developers"
          - "Kubernetes and Cloud Native Security Associate (KCSA)"
          - "Kubernetes and Cloud-Native Associate (KCNA)"
          - "Kubernetes for the Absolute Beginners - Hands-on Tutorial"
          - "Kustomize"
          - "LangChain"
          - "LangGraph"
          - "Learn Ansible Basics - Beginners Course"
          - "Learn By Doing - MariaDB"
          - "Learn By Doing_ AWS Workshop with Terraform"
          - "Learn By Doing_ Beginner's Guide to Apache Kafka - Foundations and Development"
          - "Learn By Doing_ Building AI Agents with Claude Agent SDK"
          - "Learn By Doing_ Crossplane"
          - "Learn By Doing_ Deploying and Managing the EFK Stack on Kubernetes"
          - "Learn By Doing_ Kubernetes Policies with Kyverno"
          - "Learn By Doing_ Taskfile"
          - "Learn-By-Doing Kubernetes Network Policies"
          - "Learning Linux Basics Course & Labs"
          - "Linode _ Kubernetes Engine"
          - "Linux Professional Institute LPIC-1 Exam 101"
          - "Loop Engineering"
          - "MCP For Beginners"
          - "Mastering Generative AI with OpenAI"
          - "Microsoft Azure Security Technologies (AZ-500)"
          - "Migrating Jenkins Pipelines to GitHub Actions"
          - "Migrating to Datadog"
          - "NVIDIA Generative AI LLMs Associate Certification"
          - "Nginx for Beginners"
          - "Open Source for Beginners"
          - "OpenShift 4"
          - "OpenTofu_ A Beginners Guide to a Terraform Fork Including Migration From Terrafo"
          - "PCAP - Python Certification Course"
          - "Postman Essentials"
          - "Prep Course - Certified Argo Project Associate (CAPA)"
          - "Prep Course - Certified Backstage Associate (CBA) Certification"
          - "Prep Course - Certified Cloud Native Platform Engineer (CNPE)"
          - "Prep Course - Certified Cloud Native Platform Engineering Associate (CNPA)"
          - "Prep Course - Cilium Certified Associate (CCA) Certification"
          - "Prep Course - FinOps Certified Practitioner"
          - "Prep Course - GitOps Certified Associate (CGOA)"
          - "Prep Course - Istio Certified Associate (ICA) Certification"
          - "Prep Course - Kyverno Certified Associate (KCA) Certification"
          - "Prep Course - Linux Foundation Certified System Administrator (LFCS) Certificati"
          - "Prep Course - OpenTelemetry Certified Associate (OTCA) Certification"
          - "Prep Course - Prometheus Certified Associate (PCA) Certification"
          - "Prep Course - Red Hat Certified System Administrator (RHCSA)"
          - "Prep Course - Red Hat Certified System Administrator(RHCSA)"
          - "Programming Fundamentals"
          - "Pulumi Essentials"
          - "PyTorch"
          - "Python Basics"
          - "Running Local LLMs With Ollama"
          - "Rust Programming"
          - "Shell Scripts for Beginners"
          - "Spacelift_ Elevate Your Infrastructure Deployment"
          - "Telepresence For Kubernetes"
          - "Terraform Basics Training Course"
          - "Terraform On Azure"
          - "Terragrunt for Beginners"
          - "Ultimate Certified Kubernetes Administrator (CKA) Mock Exam Series"
          - "Ultimate Certified Kubernetes Application Developer (CKAD) Mock Exam Series"
          - "Ultimate Certified Kubernetes Security Specialist (CKS) Mock Exam Series"
          - "Vector Database for GenAI"
          - "[Updated] AZ-104_ Microsoft Azure Administrator"
          - "n8n_ Zero to Hero"

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install Dependencies
        run: pip install --upgrade telethon cryptg

      - name: Install Rclone
        run: sudo curl https://rclone.org/install.sh | sudo bash

      - name: Configure Rclone
        run: |
          mkdir -p ~/.config/rclone
          cat << 'EOF' > ~/.config/rclone/rclone.conf
          ${{ secrets.RCLONE_CONFIG }}
          EOF

      - name: Download Course to Runner
        run: |
          mkdir -p "./payload"
          rclone copy "CloudDriveRemote:KodeKloud/KodeKloud/${{ matrix.course_name }}" "./payload" --progress

      - name: Upload to Telegram Group Topic
        env:
          TELEGRAM_API_ID: ${{ secrets.TELEGRAM_API_ID }}
          TELEGRAM_API_HASH: ${{ secrets.TELEGRAM_API_HASH }}
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
          TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
        run: python telegram_upload.py "./payload" "${{ matrix.course_name }}"
