import google.genai as genai #pip install google-genai

def get_api_key():
    with open('api_key.txt') as f:
        return f.read().strip() # retire les retours à la ligne

def gemini_answer(answer):
    client = genai.Client(api_key=get_api_key())
    preset = "explique le moi rapidement et simplement"
    response = client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=answer + preset
    )
    
    result = response.text
    result = result.replace("**", "")
    return(result)
