import wikipedia #pip install wikipedia
import difflib

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
        print("Le terme ", e.title, " est ambigu.")

        #afficher les choix
        for option in e.options :
            print(option)
        
        #prends le choix le plus proche de l'entré utilisateur
        choix = difflib.get_close_matches(input("Choisis la bonne page : "), e.options)
        choixnumber = e.options.index(choix[0])

        result = wikipedia.page(e.options[choixnumber])

    #retourner le premier paragraphe
    content = result.content
    first_paragraph = content.split("\n\n")[0]
    return first_paragraph

def wikisearch2(text):
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

print(wikisearch2("Linux"))