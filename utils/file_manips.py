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
        Un fichier csv en sortie en mode append
        :type file_csv: basestring
        :type write_csv : basestring
    """

    try:
        if is_non_zero_file(file_csv):
            file_name = os.path.basename(file_csv)
            df = pd.read_csv(file_csv)
            df.drop(df.columns[0], axis=1)
            df.insert(1, "source", file_name)
            df_header = df[:1]
            df_header.to_csv(write_csv, sep=';', mode='a', header=True)
        else:
            print('Fichier vide : ' + file_csv)

    except:
        raise


def path_separator(input_path):
    """
        Extrait des morceaux d'un path
        Un string path en entrée
        En sortie un dictionnaire [arborescence, dossier, nom.extension,extension]
        Valeurs possibles : dir, rep, nom_ext, ext, nom

    """

    # Extraction de l'arborescence et création du dictionnaire
    file_dir = str(os.path.dirname(input_path))

    # Extraction du repertoire au-dessous
    file_rep = str(os.path.basename(file_dir))

    # Extraction de nom.extension
    file_nom_ext = str(os.path.basename(input_path))

    # Extraction de l'extension
    list_ext = input_path.split('.')[1:]
    file_ext = ".".join(list_ext)

    # Extraction du nom de fichier sans extension
    file_nom = str(file_nom_ext[:-len(file_ext) - 1])

    parties = {'dir': file_dir, 'rep': file_rep, 'nom_ext': file_nom_ext, 'ext': file_ext, 'nom': file_nom}
    return parties


def excel2csv(excel_file, export_csv_dir):
    """
        Crée un ou des fichiers CSV à partir d'un fichier Excel
        vers un répertoir donné
        Source
        Un fichier excel en entrée
        Un fichier csv en sortie
        :type excel_file: basestring
        :type export_csv_dir : basestring
    """

    # Lecture de tous les noms de feuilles
    xls = pd.ExcelFile(excel_file)

    # Boucle sur les noms de feuilles
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(excel_file, sheet_name)
        export_name = path_separator(excel_file)['rep']+'_'+path_separator(excel_file)['nom']+'_'+sheet_name+'.csv'
        # -->Possibilité ici de créer des modules de controle, modif ou autre

        # export en csv vers le répertoire spécifié
        df.to_csv(export_csv_dir + '\\' + export_name, sep=';', encoding='utf-8', index=False)


def csv2csv(csv_file, export_csv_dir):
    """
        Crée un ou des fichiers CSV à partir d'un fichier CSV
        vers un répertoir donné
        Source
        Un fichier excel en entrée
        Un fichier csv en sortie
        :type csv_file: basestring
        :type export_csv_dir : basestring
    """

    df = pd.read_csv(csv_file)
    # -->Possibilité ici de créer des modules de controle, modif ou autre

    # export en csv vers le répertoire spécifié
    export_name = path_separator(csv_file)['rep'] + '_' + path_separator(csv_file)['nom'] + '.csv'
    df.to_csv(export_csv_dir + '\\' + export_name, sep=';', encoding='utf-8', index=False)