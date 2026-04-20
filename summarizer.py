from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_text(text):

    prompt = f"""
    You are an expert research analyst.

    Analyze the following research paper and provide a structured output.

    IMPORTANT:
    - Always include numerical data and percentages wherever possible.
    - Highlight key statistics clearly.

    Provide:

    1. 📌 Title of the Paper  
    2. 📖 Short Summary (5-6 lines)  
    3. 🎯 Research Objective  
    4. 🔬 Methodology Used  
    5. 📊 Key Findings (include numbers, percentages, data)  
    6. 💡 Key Contributions  
    7. ⚠️ Limitations of the Study  
    8. 🌍 Real-World Impact / Applications  
    9. 📈 Important Data Insights (clearly highlight statistics)

    Paper:
    {text[:4000]}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content