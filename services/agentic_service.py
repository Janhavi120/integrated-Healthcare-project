from crewai import Crew
from agents.tasks import get_tasks

def generate_plan(user_input):
    print("[Agentic] Creating tasks...")
    
    tasks = get_tasks(user_input)
    
    print("[Agentic] Running crew...")

    crew = Crew(
        agents=[t.agent for t in tasks],
        tasks=tasks,
        verbose=False
    )
    
    result = crew.kickoff(inputs={"input": user_input})
    
    print("[Agentic] Plan generated")
    
    return str(result)