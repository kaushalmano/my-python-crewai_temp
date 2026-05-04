from crewai import Agent
from config import LLM_CONFIG

def get_research_agent():
    return Agent(
        role="QA Test Case Generator",
        goal="Generate simple QA test cases in bullet format",
        backstory=(
            "You are a QA engineer. You ALWAYS generate output in bullet points. "
            "You NEVER explain. You NEVER refuse."
        ),
        llm=LLM_CONFIG,
        verbose=True
    )

def get_writer_agent():
    return Agent(
        role="Formatter",
        goal="Format content into clean bullet points",
        backstory=(
            "You are a formatter. You NEVER ask questions. "
            "You ALWAYS convert content into bullet points."
        ),
        llm=LLM_CONFIG,
        verbose=True
    )