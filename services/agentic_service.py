from crewai import Crew
from agents.tasks import get_tasks
import time

def generate_plan(user_input):

    try:
        print("[Agentic] Calling Gemini via CrewAI...")

        tasks = get_tasks(user_input)

        crew = Crew(
            agents=[tasks[0].agent, tasks[1].agent],
            tasks=tasks,
            verbose=True
        )

        result = crew.kickoff()

        print("[Agentic] Success")
        return str(result)

    except Exception as e:
        print("[Agentic] Failed:", e)
        print("[Agentic] Using default plan")

        return """
# Treatment Plan

## Immediate Care

1. Take proper rest  
2. Drink water regularly  
3. Use fever medicine if required  
4. Eat light homemade food

## Daily Care

- Sleep early  
- Avoid outside food  
- Maintain hygiene

## Visit Doctor If

- Fever continues
- Severe cough
- Chest pain
- Weakness increases

## Final Note

Please visit your nearby doctor or hospital.
"""