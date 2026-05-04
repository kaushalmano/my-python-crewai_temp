from crewai import Crew, Process
from agent import get_research_agent, get_writer_agent
from task import get_research_task, get_writing_task

def run():
    # Agents
    researcher = get_research_agent()
    writer = get_writer_agent()

    # Tasks
    research_task = get_research_task(researcher)
    writing_task = get_writing_task(writer, research_task)

    # Crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=True
    )

    print("Starting Crew execution...")
    result = crew.kickoff()
    print("Execution done")
    print("\nFINAL OUTPUT:\n")
    print(result)


if __name__ == "__main__":
    run()