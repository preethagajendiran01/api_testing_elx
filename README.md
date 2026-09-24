# API Framework ELX

This is a  API automation framework for testing the JSONPlaceholder `/posts` APIs using Python, Pytest, Requests, and Pydantic.
 
## Structure
 
- `api/api_handler.py` - Reusable GET/POST/PUT/DELETE methods
- `schemas/post_schema.py` - Response schema validation using Pydantic
- `testdata/post_payloads.py` - Request test data
- `tests/test_posts.py` - API test cases
- `conftest.py` - Shared `api_handler` fixture
- `config/config.py` - Reads environment configuration
- `.env.example` - Example configuration for local execution
- `azure-pipelines.yml` - Azure DevOps pipeline configuration
 
## Local Configuration
 
For local execution, environment-specific values and API credentials are stored in a `.env` file instead of hardcoding them in the Python code.
 
The actual `.env` file is intentionally not committed to Git.
 
After cloning the repository, use `.env.example` as a reference and create a new `.env` file in the project root.
 
Example:
 
```text
BASE_URL=https://jsonplaceholder.typicode.com
API_TOKEN=
TIMEOUT=10
```
 
JSONPlaceholder does not require authentication, so `API_TOKEN` can remain empty.
 
For APIs that require authentication, provide the required token in your local `.env` file.
 
> Do not commit the `.env` file or real API tokens to Git.
 
## Setup and Run Locally
 
Create a virtual environment:
 
```bash
python -m venv .venv
```
 
Activate the virtual environment.
 
Windows:
 
```bash
.venv\Scripts\activate
```
 
macOS/Linux:
 
```bash
source .venv/bin/activate
```
 
Install the required packages:
 
```bash
pip install -r requirements.txt
```
 
Run all tests:
 
```bash
pytest
```
 
Run P1 tests:
 
```bash
pytest -m p1
```
 
Run P2 tests:
 
```bash
pytest -m p2
```
 
## Azure DevOps Integration
 
The framework is also integrated with Azure DevOps Pipelines for CI test execution.

Repo - https://dev.azure.com/preethagajendiran01/_git/Elxproject
Pipeline - https://dev.azure.com/preethagajendiran01/Elxproject/_build?definitionId=3
 
For Azure DevOps runs, the `.env` file is not uploaded to the repository.
 
Instead, the same environment values are configured using Azure DevOps Pipeline Variables
 
When creating a new Azure DevOps pipeline for this framework, the same variables should be configured in the pipeline before executing the tests.
 
This allows the same test framework to run locally and in Azure DevOps without hardcoding environment-specific values or credentials.
 
## Azure Pipeline Execution
 
The Azure DevOps pipeline performs the following steps:
 
```text
Checkout Repository
↓
Setup Python
↓
Install requirements.txt
↓
Run Pytest
↓
Publish Test Results
↓
Publish HTML Test Report
```
 
The pipeline is currently configured for manual execution, so tests can be started from:
 
```text
Azure DevOps
→ Pipelines
→ Select Pipeline
→ Run Pipeline
```
  ##Below is sample Pipeline run result

  <img width="1918" height="1062" alt="image" src="https://github.com/user-attachments/assets/5bbdcba7-b610-4bcf-80bf-e364b5fffa95" />
