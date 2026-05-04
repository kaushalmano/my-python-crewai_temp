# creaw_ai_1

A small CrewAI-based project that runs a two-agent workflow to generate and format QA test cases.

## Overview

This project uses the `crewai` framework to define:
- a research agent that generates QA test cases
- a writer/formatter agent that rewrites the generated content into clean bullet points
- a sequential crew process that executes both tasks in order

The workflow is defined in `main.py`, and the LLM configuration is stored in `config.py`.

## Files

- `main.py` - orchestrates the crew, agents, and tasks, then runs the workflow.
- `agent.py` - defines the `get_research_agent()` and `get_writer_agent()` functions.
- `task.py` - defines the `get_research_task()` and `get_writing_task()` functions.
- `config.py` - stores the LLM configuration used by both agents.

## Requirements

- Python 3.8+
- `crewai` Python package
- Access to the `ollama/phi3` model or any supported LLM backend configured in `config.py`

## Usage

1. Install dependencies (example):

```bash
pip install crewai
```

2. Run the project:

```bash
python main.py
```

3. The script prints the final output after executing the crew workflow.

## Behavior

- `get_research_task()` prompts the research agent to generate one QA test case for Samsung Galaxy AI in strict bullet-point format.
- `get_writing_task()` prompts the writer agent to rewrite the research output into clean bullet points.
- The crew executes tasks sequentially with verbose logging enabled.

## Customization

- Change `LLM_CONFIG` in `config.py` to point to a different model.
- Update the agent `role`, `goal`, and `backstory` in `agent.py` for different behavior.
- Modify task descriptions in `task.py` to generate other structured outputs.
