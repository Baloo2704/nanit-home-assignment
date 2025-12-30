```markdown
# Nanit Home Assignment - Automation Infrastructure

> A comprehensive automation framework designed to validate streaming servers, mock mobile sessions, and perform integration testing.

## 📚 Overview

This repository contains the automation logic for three distinct stages:

1.  **Stage 1: API Validation**
    Validates the integrity and response correctness of the Mock Streaming Server endpoints.
2.  **Stage 2: Mock Mobile Session**
    Implements a client-side simulation to mimic mobile device behavior and session management.
3.  **Stage 3: Integration Testing**
    End-to-end flows validating the interaction between the Mobile Session and the Streaming Server.

## 🛠️ Tech Stack

* **Language:** Python 3.8+
* **Validation:** Pydantic
* **Testing Framework:** Pytest
* **HTTP Requests:** Requests Library
* **Mock Server:** Flask & Flask-CORS

## 📂 Project Structure

```text
.
├── infra/                   # Infrastructure and core utilities
├── mock_services/           # Source code for the mock server
│   └── mock_streaming_server.py
├── config/                  # Configuration files
│   └── config.json          # Default configuration
├── tests/                   # Test suites (API, Mobile, Integration)
├── pytest.ini               # Pytest configuration settings
├── requirements.txt         # Project dependencies
└── README.md

```

## ⚙️ Setup & Installation

### 1. Prerequisites

Ensure you have **Python 3.8** or higher installed. It is recommended to use a virtual environment.

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

### 3. Start the Mock Server

The automation requires the mock server to be running in the background. Open a **separate terminal** and run:

```bash
python mock_services/mock_streaming_server.py

```

> **Note:** The server will start listening on `http://localhost:8082`. Keep this terminal open while running tests.

## 🧪 Running Tests

This framework uses `pytest` for test execution. The default configuration is located at `config/config.json`.

| Action | Command | Description |
| --- | --- | --- |
| **Run All Tests** | `pytest` | Executes all tests using defaults (configured in `pytest.ini` or defaults to `config/config.json`). |
| **Run API Tests** | `pytest -m api` | Runs only tests marked as `api` (Stage 1). |
| **Run Mobile Tests** | `pytest -m mobile` | Runs only tests marked as `mobile` (Stage 2). |
| **Run Integration Tests** | `pytest -m integration` | Runs only tests marked as `integration` (Stage 3). |
| **Custom Configuration** | `pytest --env=config/custom_config.json` | Runs tests using a different configuration file (if created). |

## 📝 Configuration

The framework supports multiple environments via JSON configuration files located in the `config/` directory.

* **`config/config.json`**: The default configuration used for test execution.
* **`--env` flag**: Use this to inject a specific configuration file at runtime.
