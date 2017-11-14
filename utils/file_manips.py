# !/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import fnmatch
import pandas as pd


def find_files(directory, pattern):

    """
        Cherche des fichiers selon un motif avec joker dans un répertoire
        et ses sous-répertoires
        Source
        Un répertoire en entrée : X:\REP
        Un pattern avec joker * : *.txt
    """

    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                assert isinstance(filename, object)
                yield filename


def is_non_zero_file(file_path):
    """
        Vérifie si un fichier est vide
    """
    return True if os.path.isfile(file_path) and os.path.getsize(file_path) > 0 else False


def csv_first_line_export(file_csv, write_csv):
    """
        lit la première ligne d'un fichier csv
        Un fichier csv en entrée
        Un fichier csv en sortie
        :type file_csv: basestring
        :type write_csv : basestring
    """

    try:
        if is_non_zero_file(file_csv):
            # write_csv = file_csv + '.log'
            df = pd.read_csv(file_csv)
            df_header = df[:0]
            df_header.to_csv(write_csv, sep=';', mode='a', header=True)
        else:
            print('Fichier vide : ' + file_csv)

    except:
        raise


def excel2csv(excel_file, export_csv_dir):
    """
        Crée un ou des fichiers CSV à partir d'un fichier Excel
        Source
        Un fichier excel en entrée
        Un répertoire en sortie
        :type excel_file: basestring
        :type export_csv_dir : basestring
    """

    # Lecture de tous les noms de feuilles
    xls = pd.ExcelFile(excel_file)
    shn = xls.sheet_names

    # Boucle sur les noms de feuilles
    for sheet_name in shn:
        df = pd.read_excel(excel_file, sheet_name)
        # -->Possibilité ici de créer des modules de controle, modif ou autre

        # export en csv vers le répertoire spécifié
        df.to_csv(export_csv_dir + '_' + sheet_name + '.csv', sep=';', encoding='utf-8', index=False)
