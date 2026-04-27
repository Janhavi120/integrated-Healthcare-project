from crewai import Agent

# Use model as STRING (important fix)
MODEL = "gemini/gemini-2.5-flash"

disease_agent = Agent(
    role="Disease Analyzer",
    goal="Identify disease from symptoms",
    backstory="Expert doctor",
    llm=MODEL
)

treatment_agent = Agent(
    role="Treatment Planner",
    goal="Give treatment plan",
    backstory="Medical specialist",
    llm=MODEL
)