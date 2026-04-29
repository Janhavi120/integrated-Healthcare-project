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
Generate a professional medical report.

Age: {age}
Gender: {gender}
Symptoms: {symptoms}

Include:
- Possible Condition
- Basic Advice
- Lifestyle Suggestions
- When to Visit Doctor
""")

chain = prompt | llm | StrOutputParser()


def generate_report(age, gender, symptoms):

    for attempt in range(3):
        try:
            print(f"[GenAI] Attempt {attempt+1}")

            result = chain.invoke({
                "age": age,
                "gender": gender,
                "symptoms": symptoms
            })

            print("[GenAI] Success")
            return result

        except Exception as e:
            print("[GenAI] Failed:", e)
            time.sleep(3)

    # DEFAULT REPORT IF GEMINI FAILS
    return f"""
# Medical Report

## Patient Details
- Age: {age}
- Gender: {gender}
- Symptoms: {symptoms}

## Preliminary Observation

Based on the entered symptoms, the patient may be experiencing a common viral infection, seasonal fever, weakness, dehydration, or stress-related condition. Exact diagnosis requires physical examination and medical testing.

## Recommended Advice

1. Take complete rest.
2. Drink enough water and fluids.
3. Eat light and healthy food.
4. Monitor body temperature regularly.
5. Avoid cold food and outside food.
6. Maintain hygiene and proper sleep.

## Lifestyle Suggestions

- Sleep for 7-8 hours.
- Reduce stress.
- Avoid excessive screen time.
- Take fresh fruits and vegetables.

## Visit Doctor If

- Fever continues for more than 2 days
- Breathing issue starts
- Severe headache occurs
- Vomiting or weakness increases

## Disclaimer

This is an AI-generated backup medical report. Please consult a nearby doctor for proper diagnosis.
"""