# AI Powered Healthcare Management System

A simple integrated project that combines **Generative AI**, **Agentic AI**, and **DevOps** into one healthcare application.

This project allows users to enter patient details and symptoms, then automatically generates:

- 🧾 Medical Report using GenAI  
- 📋 Treatment Plan using Agentic AI (2 agents)  
- 🐳 Dockerized Deployment  
- ⚙️ GitHub CI/CD Pipeline  

---

# 🚀 Features

## 🏥 Healthcare Form
Users can enter:

- Age
- Gender
- Symptoms

## 🧾 GenAI Report Generation
Uses LLM prompt engineering to generate:

- Possible condition
- Basic advice
- Health summary

## 🤖 Agentic AI Planning
Uses 2 simple AI agents:

### Agent 1: Disease Analyzer
Analyzes symptoms and predicts possible issue.

### Agent 2: Treatment Planner
Creates step-by-step treatment suggestions.

## 💾 Database Storage
Stores:

- Patient data
- Reports
- Treatment plans

## 🎨 Beautiful Frontend

Includes:

- Home Page
- Dashboard
- Generation Page
- Loading Animation
- Success Tick after report generation

## 🐳 Docker Support

Run complete project using Docker.

## ⚙️ CI/CD Pipeline

GitHub Actions workflow included for automatic build checks.

---

# 🛠️ Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Generative AI
- CrewAI / Agents
- Docker
- GitHub Actions
