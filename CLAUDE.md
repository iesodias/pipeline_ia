# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Development
- **Run the troubleshooting script locally**: `python3 scripts/chatgpt_troubleshoot.py`
- **Install Python dependencies**: `pip install requests openai` or `pip install requests pandas numpy`
- **Test script functionality**: Set environment variables and run the Python script directly

### Pipeline Testing
- **Trigger pipeline manually**: Use workflow_dispatch event in GitHub Actions
- **View pipeline results**: Check Actions tab for workflow runs and artifacts
- **Download troubleshooting reports**: Access artifacts from completed pipeline runs

## Architecture

This is a CI/CD troubleshooting automation project that uses ChatGPT to analyze pipeline failures and provide automated troubleshooting suggestions.

### Core Components

**GitHub Actions Workflow (`.github/workflows/cd.yml`)**
- **failing-step job**: Intentionally simulates common deployment failures (database timeouts, missing env vars, Docker build failures, permission errors)
- **chatgpt-troubleshooting job**: Runs only on failure, analyzes the error using OpenAI GPT-4, and generates troubleshooting reports

**Python Troubleshooting Script (`scripts/chatgpt_troubleshoot.py`)**
- Integrates with OpenAI GPT-4 API for intelligent error analysis
- Captures GitHub Actions context (workflow, repository, branch, commit, error type)
- Generates structured troubleshooting reports in Markdown format
- Handles API errors and timeouts gracefully

### Pipeline Flow
1. **Intentional Failure**: Randomly selects and simulates one of four error types
2. **Error Capture**: Collects detailed context about the failure
3. **ChatGPT Analysis**: Sends error context to GPT-4 for analysis
4. **Report Generation**: Creates structured troubleshooting report
5. **Artifact Upload**: Saves report as pipeline artifact
6. **PR Comments**: Automatically comments on pull requests with troubleshooting suggestions

### Environment Variables
- `OPENAI_API_KEY`: Required secret for OpenAI API authentication
- `ERROR_TYPE`: Captured from failing step output
- `WORKFLOW_NAME`, `REPOSITORY`, `BRANCH`, `COMMIT`: GitHub context variables

### Error Types Simulated
- `database_connection_timeout`: Database connectivity failures
- `missing_environment_variable`: Missing required configuration
- `docker_build_failure`: Docker image build errors
- `permission_denied`: Authentication and authorization failures

## Key Features

**Intelligent Error Analysis**: Uses GPT-4 to provide contextual troubleshooting advice with diagnosis, solutions, implementation commands, prevention strategies, and verification checklists.

**Automated Reporting**: Generates detailed Markdown reports with timestamp, error context, and ChatGPT analysis that are uploaded as pipeline artifacts.

**PR Integration**: Automatically comments on pull requests with troubleshooting suggestions when pipelines fail.

**Educational Purpose**: Designed for learning DevOps troubleshooting and CI/CD automation patterns.