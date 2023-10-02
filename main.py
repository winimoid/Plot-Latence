import csv
from datetime import datetime
from itertools import islice

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Initialisez des listes pour stocker les données
dates = []
latences = []

# Remplacez 'votre_fichier.csv' par le chemin de votre fichier CSV
fichier_csv = 'assets/192.168.27.69.csv'

# Ouvrez le fichier CSV en mode lecture
with open(fichier_csv, 'r') as csvfile:
    # Créez un lecteur CSV
    csvreader = csv.reader(csvfile)

    # Sautez les trois premières lignes
    for _ in range(4):
        next(csvreader)

    # Parcourez chaque ligne du fichier CSV
    for ligne in csvreader:
        # Vérifiez si la ligne contient au moins deux éléments
        if len(ligne) >= 2:
            # La première colonne est la date et l'heure
            date_heure_str = ligne[0].replace('Z', '')  # Supprimez le 'Z'  # date_heure_str = ligne[0]

            latence_str = ligne[1]

            # Gérez les valeurs non numériques (comme "*") en les remplaçant par une valeur de latence par défaut (
            # par exemple, 0)
            if latence_str == "*" or latence_str == "N/A":
                latence = 0
            else:
                # Convertissez la latence en nombre à virgule flottante
                latence = float(latence_str)

            # Convertissez la date et l'heure en objet datetime
            date_heure = datetime.strptime(date_heure_str, "%Y-%m-%d %H:%M:%S")

            # Ajoutez la date et l'heure à la liste des dates
            dates.append(date_heure)

            # Ajoutez la latence à la liste des latences
            latences.append(latence)

    # Créez un graphique
    plt.figure(figsize=(12, 6))
    plt.plot(dates, latences, marker='o', linestyle='-')
    plt.title('Latence en fonction du temps')
    plt.xlabel('Date et Heure')
    plt.ylabel('Latence (ms)')

    # Formatez les étiquettes de l'axe x avec des pas de 1 seconde
    # ax = plt.gca()
    # ax.xaxis.set_major_locator(mdates.SecondLocator(interval=1))
    # ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))

    # Formatez les étiquettes de l'axe x avec des pas de 30 minutes
    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=10))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))

    # Formatez les étiquettes de l'axe x pour qu'elles soient plus lisibles
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Affichez le graphique
    plt.show()
