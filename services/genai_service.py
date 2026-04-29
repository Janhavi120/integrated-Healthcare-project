from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import GEMINI_API_KEY
import time

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.5
)

prompt = ChatPromptTemplate.from_template("""
Generate a short medical report.

Age: {age}
Gender: {gender}
Symptoms: {symptoms}

Give:
- Possible condition
- Basic advice
""")

chain = prompt | llm | StrOutputParser()

def generate_report(age, gender, symptoms):
    print("[GenAI] Calling Gemini API...")

    for attempt in range(3):
        try:
            result = chain.invoke({
                "age": age,
                "gender": gender,
                "symptoms": symptoms
            })

            print("[GenAI] Response received")
            return result

        except Exception as e:
            print(f"[GenAI] Attempt {attempt+1} failed: {e}")

            if attempt < 2:
                print("[GenAI] Retrying...")
                time.sleep(2)
            else:
                return "AI service is busy right now. Please try again in a few moments."