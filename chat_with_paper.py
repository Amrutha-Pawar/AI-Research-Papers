import ollama

def ask_question(context, question):

    prompt = f"""
    Use the following research paper to answer the question.

    Paper:
    {context[:4000]}

    Question:
    {question}
    """

    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    return response["message"]["content"]