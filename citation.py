import ollama

def generate_citation(text):

    prompt = f"""
    Extract citation for this research paper.

    Provide APA citation.

    Paper:
    {text[:2000]}
    """

    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    return response["message"]["content"]