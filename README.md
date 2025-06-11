# GMAIL-AI-ASSISTANT

*Empower Your Inbox with Intelligent AI Assistance*


**Built with the tools and technologies:**

![Flask](https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=flask)
![Gunicorn](https://img.shields.io/badge/Gunicorn-green?style=for-the-badge&logo=gunicorn)
![Python](https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python)

## Table of Contents

• [Overview](#overview)

• [Getting Started](#getting-started)

  • [Prerequisites](#prerequisites)
  
  • [Installation](#installation)

## Overview

**gmail-ai-assistant** is a robust developer tool that simplifies the integration of OpenAI's API into your applications through MCP server  Flask-based web service.

![image](https://github.com/user-attachments/assets/37aff85a-5a2b-48a3-a66e-e7f24711a4df)


### Why gmail-ai-assistant?
This project empowers developers to build AI-powered email management applications using natural language interfaces. It streamlines communication between users and Gmail through a simple and extensible backend architecture.

## Key Features:


- **AI-powered email management** – Enables users to interact with Gmail using natural language commands for intuitive control.  
- **Comprehensive Gmail operations** – Supports sending, drafting, searching, labeling, archiving, and deleting emails.  
- **Zapier MCP integration** – Utilizes Zapier’s Managed Connected Platform to connect seamlessly with Gmail and other tools.  
- **Unified API endpoint** – A single `/query` endpoint handles all user interactions, reducing complexity.  
- **Clean, minimal responses** – Returns only the AI’s reply, removing unnecessary technical metadata.  


## Prerequisites

This project requires the following dependencies:

• **Programming Language**: Python

• **Package Manager**: Pip

## Installation

Build gmail-ai-assistant from the source and install dependencies:

### 1. Clone the repository:

```bash
git clone https://github.com/priyaladesara/gmail-ai-assistant
```

### 2. Navigate to the project directory:

```bash
cd gmail-ai-assistant
```

### 3. Install the dependencies:

**Using pip:**

```bash
pip install -r openai-flask-wrapper/requirements.txt
```

## Usage

Run the project with:

```bash
python app.py
