from crewai import Task
def get_research_task(agent):
    return Task(
        description="""
Create QA test cases for Samsung Galaxy AI.

STRICT RULES:
- ONLY bullet points
- NO explanations

Format:
- Feature:
  - Test Case:
  - Steps:
    1.
    2.
  - Expected Result:

Generate 1 test cases.
""",
        expected_output="Bullet test cases",
        agent=agent
    )

def get_writing_task(agent, context):
    return Task(
        description="""
Rewrite content into clean bullet points.

STRICT RULES:
- ONLY bullet points
- DO NOT refuse
""",
        expected_output="Clean formatted bullets",
        agent=agent,
        context=[context]
    )