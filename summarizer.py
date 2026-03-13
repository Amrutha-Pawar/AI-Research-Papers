import ollama

def summarize_text(text):

    print("Sending text to AI model...")

    prompt = f"""
    Summarize the following research paper.

    Provide:
    1. Short summary
    2. Key contributions
    3. Important concepts

    Paper:
    {text[:3000]}
    """

    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print("AI response received")

    return response["message"]["content"]