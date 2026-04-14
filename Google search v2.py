from gsearch.googlesearch import search # pip install gsearch

resultats = search("Python langage")  # renvoie jusqu'à 5 résultats
for titre, lien in resultats:
    print(lien)
