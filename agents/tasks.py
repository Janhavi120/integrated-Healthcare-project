from crewai import Task
from agents.agents import disease_agent, treatment_agent

def get_tasks(user_input):
    print("[Agents] Preparing tasks...")
    task1 = Task(
        description=f"Analyze disease for: {user_input}",
        expected_output="Give disease name and short explanation",
        agent=disease_agent
    )

    task2 = Task(
        description=f"Give treatment plan for: {user_input}",
        expected_output="Give simple treatment steps and advice",
        agent=treatment_agent
    )

    return [task1, task2]