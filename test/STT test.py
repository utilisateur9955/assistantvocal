import speech_recognition as sr #pip install SpeechRecognition

def recognition():
    '''
    Fonction de reconaissance
    Entrée : voix de l'utilisateur
    Sortie : Retour du texte issu de la voix par STT
    '''

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("En écoute")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        texte = recognizer.recognize_google(audio, language='fr-FR') #utilisation du STT de Google
        if texte is None: #Gestion de l'erreur 'aucune voix reconnue'
            print("Je n'ai rien entendu")
        print("phrase reconnue : ", texte)
        return(texte) #CQFD
    
    #gestion des erreurs
    except sr.UnknownValueError:
        print("Je n'ai pas compris")
    except sr.RequestError as e:
        print("Erreur lors de la requête vers le service de reconnaissance vocale ; {0}".format(e))

print(recognition())