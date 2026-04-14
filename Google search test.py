from googlesearch import search  # pip install googlesearch-python

def googlesearch(texte):
    """
    Fonction de recherche Google
    Entrée : requête
    Sortie : URL du premier résultat
    """
    try:
        # search() renvoie un itérable de liens
        search_results = search(texte, 1)  # récupère 1 seul résultat
        first_result = next(search_results)  # prend le premier lien
        return first_result  # on renvoie le lien au lieu de juste print
    except Exception as e:
        print("Une erreur s'est produite lors de la recherche sur Google :", e)
        return None

requete = input("Recherche Google : ")
url = googlesearch(requete)
if url:
    print("Premier résultat :", url)