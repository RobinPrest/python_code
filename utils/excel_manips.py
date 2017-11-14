# !/usr/bin/python2.7
# -*- coding: utf-8 -*-

import pandas as pd

# Fonction pour créer un fichier CSV à partir d'un fichier Excel
def excel2csv(excel_file, export_xls_dir):
    # Lecture de tous les noms de feuilles
    xls = pd.ExcelFile(excel_file)
    shn = xls.sheet_names

    # Boucle sur les noms de feuilles
    for sheet_name in shn:
        df = pd.read_excel(excel_file, sheet_name)
        # -->Possibilité ici de créer des modules de controle, modif ou autre

        # export en csv vers le répertoire spécifié
        df.to_csv(export_xls_dir + '_' + sheet_name + '.csv', sep=';', encoding='utf-8', index=False)
