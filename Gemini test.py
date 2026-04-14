import google.genai as genai #pip install google-genai

def get_api_key():
    with open('API key.txt') as f:
        return f.read().strip() # retire les retours à la ligne

def gemini_answer(answer) :
    client = genai.Client(api_key=get_api_key())

    response = client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=answer
    )
    
    result = response.text
    result = result.replace("**", "")
    return(result)

print(gemini_answer("Quelle est la taille de la tour Eiffel ?"))