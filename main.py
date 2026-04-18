import speech_recognition as sr #pip install SpeechRecognition
import os #bibliothèque standard
import tldextract #pip install tldextract
import wikipedia #pip install wikipedia
import google.genai as genai #pip install google-genai
import asyncio #bibliothèque standard
import edge_tts #pip install edge-tts
import vlc #pip install python-vlc

async def parler(texte, fichier="output.mp3"):
    '''
    Fonction de lecture vocale d'un texte
    Entrée : Texte à lire
    Sortie : output.mp3 + lecture du fichier
    '''
    voix = "fr-FR-HenriNeural"
    communicate = edge_tts.Communicate(texte, voix)
    await communicate.save(fichier)

    player = vlc.MediaPlayer(fichier)
    player.play()

    # attendre la fin de lecture
    import time
    duration = 0
    while duration == 0:  # attendre que VLC charge la durée
        duration = player.get_length() / 1000
        await asyncio.sleep(0.1)
    await asyncio.sleep(duration)

def recognition():
    '''
    Fonction de reconaissance vocale
    Entrée : voix de l'utilisateur
    Sortie : Retour du texte issu de la voix par STT
    '''

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("En écoute")
        asyncio.run(parler("Je t'écoute"))
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='fr-FR') #utilisation du STT de Google
        if text is None: #Gestion de l'erreur 'aucune voix reconnue'
            print("Je n'ai rien entendu")
            asyncio.run(parler("Je n'ai rien entendu"))
        print("phrase reconnue : ", text)
        return(text) #CQFD
    
    #gestion des erreurs
    except sr.UnknownValueError:
        print("Je n'ai pas compris")
        asyncio.run(parler("Je n'ai pas compris"))
    except sr.RequestError as e:
        print("Erreur lors de la requête vers le service de reconnaissance vocale ; {0}".format(e))
        asyncio.run(parler("Erreur lors de la requête vers le service de reconnaissance vocale"))

def web(path):
    '''
    ouvre un site web
    Entrée : mot cle
    Sortie : ouverture du navigateur
    '''
    if tldextract.extract(path).suffix:
        url = "https://" + path
        os.startfile(url)
    else :
        googlesearch = "https://www.google.com/search?q=" + path
        os.startfile(googlesearch)

def wikisearch(text):
    '''
    Fonction de recherche sur wikipedia
    Entrée : Mot-clé de recherche
    Sortie : premier paragraphe de la page wikipedia
    '''

    wikipedia.set_lang("fr") #demande l'accès au wikipedia français

    pages = wikipedia.search(text) #recherche la page sur wikipedia
    try : #essaie d'afficher la page si il n'y en a qu'une seule de disponible
        result = wikipedia.page(pages[0])
    
    except wikipedia.exceptions.DisambiguationError as e : #si plusieurs pages ont le même nom

        result = wikipedia.page(e.options[0])

    #retourner le premier paragraphe
    content = result.content
    first_paragraph = content.split("\n\n")[0]
    return first_paragraph

def get_api_key():
    '''
    Récupère la clé d'API de Gemini

    Entrée : aucune
    Sortie : clé d'API
    '''
    with open('api_key.txt') as f:
        api_key = f.read().strip()
        return api_key

def gemini_answer(answer) : 
    '''
    Poser une question à gemini 
    Entrée : Question 
    Sortie : Réponse de Gemini 
    '''
    client = genai.Client(api_key=get_api_key()) 

    response = client.models.generate_content( 
        model='gemini-3-flash-preview', 
        contents=answer 
    ) 
    result = response.text 
    result = result.replace("**", "") 
    return(result) 

question = recognition()

if question :
    if "qui" in question or "quoi" in question or "que" in question :
        question = question.replace("qui", "")
        question = question.replace("quoi", "")
        question = question.replace("que", "")
        question = question.replace("qu'", "")
        question = question.replace("ce", "")
        question = question.replace("c'", "")
        question = question.replace("est", "")
        reponse = wikisearch(question)
    elif "ouvre" in question : 
        question = question.replace("ouvre", "")
        reponse = ("Voici")
        web(question)
    else :
        reponse = gemini_answer(question)
    
    asyncio.run(parler(reponse))
    