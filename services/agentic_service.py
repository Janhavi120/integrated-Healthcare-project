from crewai import Crew
from agents.tasks import get_tasks
import time

def generate_plan(user_input):

    for attempt in range(3):
        try:
            print(f"[Agentic] Attempt {attempt+1}")

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
            time.sleep(3)

    # DEFAULT PLAN IF GEMINI FAILS
    return """
# Treatment Plan

## Immediate Care

1. Take complete bed rest.
2. Stay hydrated with water, ORS, juice.
3. Use paracetamol for fever if needed.
4. Eat simple homemade food.

## Daily Routine

- Morning: Warm water + fruits
- Afternoon: Light lunch
- Evening: Rest
- Night: Early sleep

## Safety Measures

- Avoid crowded places
- Wear mask if coughing
- Wash hands regularly

## Doctor Consultation Required If

- High fever continues
- Severe cough
- Chest pain
- Breathing difficulty
- Body weakness increases

## Final Note

This is an automatically generated backup treatment plan. Visit your nearby doctor or hospital for proper treatment.
"""