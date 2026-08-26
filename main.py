import pymupdf
from pathlib import Path
from collections import defaultdict
import matplotlib.pyplot as plt



# Initialisation


compteur_global = defaultdict(int)


dossier = Path("Sujets")

notions=[]

frequences= []

#Liste des fichiers  

fichiers = list(dossier.glob("*.pdf"))

#Nombre total de sujets

nb_sujt_total= len(fichiers)


## Analyse des sujets PDF


for fichier in dossier.glob("*.pdf"):

    file = pymupdf.open(fichier)

    texte_cmplt= ""


    #Extraire le texte de toutes les pages
    for page in file:

        texte_cmplt += page.get_text()


    # Mettre tout en miniscule
    texte_cmplt= texte_cmplt.lower()

    print(f"\n======PDF analysé : {fichier.name}====== ")
    

    #Ouvrir et lire le fichier des référenciels

    with open("RéférencielSjtMath.txt", "r", encoding="UTF-8") as fileR:

        ligneRef= [ 
                ligne.strip("\t")                    
                for ligne in fileR
                ]


    #Chercher les notions
    for ligne in ligneRef:

        #
        #
        if "\t" not in ligne :

            continue

        # Séparer la notion du mot clé 

        notion, mot_clé= ligne.split("\t")

        # Nettoyer la donnée notion

        notion = notion.strip()

        # Transformer les notions en listes

        mot_clé=[mot.strip().lower()
                for mot in mot_clé.split(",")]

        # Compter le nombre de mot clé différent trouvé

        nombre_trouve = 0

        for mot in mot_clé:

            if mot in texte_cmplt :
                nombre_trouve += 1
            # print(f"Mot clé : {mot} ")    
        
        ### Détecter la notion, si il y a au moin 2 mots clé détectée

        if nombre_trouve >=2:  

            compteur_global[notion] += 1   

            print(f"Notion : {notion} "  
                  f"----> "
                  f"{nombre_trouve}/{len(mot_clé)} mot-clés trouvés" 
            )

    #Fermer le fichier
    file.close()  

#### Classement des notions

classement = sorted(
    compteur_global.items(),
    key=lambda element: element[1],
    reverse=True
)

##### Résumer global


print("\n\n====== CLASSEMENT DES NOTIONS ======\n\n")

for rang, (notion, nb_sujt) in enumerate(classement, start=1) :

    
    frq= (nb_sujt / nb_sujt_total )* 100

    #La méthode .sort() permet de classer dans l'ordre des éléments

    print(f"\nNotion : {rang}.{ notion}"
          f" ----> {nb_sujt}/{nb_sujt_total}"
          f" ----> Fréquence : {frq:.2f}%")

    
    #    print(repr(ligne))  
    #    print(repr(ligne))      
    #    print("probabilité" in texte_cmplt)
    #    print("Probabilité" in texte_cmplt)

top10= classement[:10]##Ajouter que les 10 premiers du classement

for notion, nb_sujt in top10:
    notions.append(notion)

    #récalculer pour chaque notions
    frq= (nb_sujt / nb_sujt_total )* 100

    frequences.append(frq)

####### Le graphique

plt.barh(notions, frequences)

plt.xlabel("Fréquence (%)")
plt.ylabel("Notions")

#Inverser et mettre la fréquence la plus haute en haut
plt.gca().invert_yaxis()

plt.show()