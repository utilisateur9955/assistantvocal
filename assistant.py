import speech_recognition as sr
from googlesearch import search
import pyttsx3
from bs4 import BeautifulSoup
import requests
engine = pyttsx3.init()
def googlesearch(texte):
    try:
        query = texte
        search_results = search(query)
        first_result = next(search_results)
        response = requests.get(first_result)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraph = soup.find('p')
        if paragraph:
            answer = paragraph.get_text()
            print(answer)
            engine.say(answer)
            engine.runAndWait()
        else:
            print("Aucun résultat trouvé sur la page.")
    except Exception as e:
        print("Une erreur s'est produite lors de la recherche sur Google : {0}".format(e))
def recognition():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Je t'écoute")
        engine.say("Je t'écoute")
        engine.runAndWait()
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        texte = recognizer.recognize_google(audio, language='fr-FR')
        if texte is None:
            print("Je n'ai rien entendu")
            engine.say("Je n'ai rien entendu")
        print("phrase reconnue : ", texte)
        googlesearch(texte)
    except sr.UnknownValueError:
        print("Je n'ai pas compris")
    except sr.RequestError as e:
        print("Erreur lors de la requête vers le service de reconnaissance vocale ; {0}".format(e))
recognition()






