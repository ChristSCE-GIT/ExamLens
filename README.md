# ExamLens – Analyse automatique des sujets PDF de mathématiques

## Description
ExamLens est un outil Python qui permet d’analyser automatiquement des sujets PDF de mathématiques afin de détecter les notions présentes et de mesurer leur fréquence.  
Il s’appuie sur PyMuPDF pour extraire le texte et sur un fichier de référentiel (`RéférencielSjtMath.txt`) qui associe chaque notion à une liste de mots-clés.

L’outil :
- Parcourt tous les PDF d’un dossier.
- Extrait le texte et le met en minuscules.
- Compare le contenu avec les mots-clés du référentiel.
- Détecte une notion si au moins deux mots-clés sont trouvés.
- Classe les notions par fréquence et génère un Top 10 en graphique.

---

## Fonctionnalités
- Extraction de texte depuis des PDF avec PyMuPDF.  
- Détection de notions grâce à un référentiel de mots-clés.  
- Classement global des notions par fréquence.  
- Visualisation graphique des dix notions les plus fréquentes.  

---

## Organisation des fichiers
- `Sujets/` → Dossier contenant les sujets PDF.  
- `RéférencielSjtMath.txt` → Fichier texte listant les notions et leurs mots-clés.  
- `analyse_notions.py` → Script principal.  

---

## Exemple de sortie
Console :
======PDF analysé : sujet1.pdf======
Notion : Probabilités ----> 3/5 mot-clés trouvés
Notion : Fonctions ----> 2/4 mot-clés trouvés

====== CLASSEMENT DES NOTIONS ======

Notion : 1. Probabilités ----> 8/12 ----> Fréquence : 66.67%
Notion : 2. Fonctions ----> 6/12 ----> Fréquence : 50.00%

Code

Graphique : un histogramme horizontal des dix notions les plus fréquentes.

---

## Installation
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/ChristSCE-GIT/ExamLens.git
   cd ExamLens
2. Installer les dépendances
   pip install -r requirements.txt

