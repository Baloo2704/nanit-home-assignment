# Nanit Home Assignment

## Overview
This repository contains the automation infrastructure for:
1.  **Stage 1:** API Validation of the Mock Streaming Server.
2.  **Stage 2:** Mock Mobile Session implementation.

## Setup
1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Start the Mock Server:**
    Open a separate terminal and run:
    ```bash
    python mock_services/mock_streaming_server.py
    ```
    *Server will listen on http://localhost:8082*

## Running Tests

### Default Execution
Run all tests using the default configuration (`config.json`):
```bash
pytest
```

Run tests with specific marker
```bash
pytest -m api
```

Run tests with environment variable
```bash
pytest --env=dev.json
```