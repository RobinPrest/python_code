#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Attention, si la première ligne ne commence pas en haut à gauche,
# seules les colonnes après sont prises en compte

# Le code find_files va trouver des fichiers correspondant à un pattern de type *.xls*
# Le code excel2csv va convertir chaque fichier excel et ses feuilles en csv dans un répertoire cible

from utils.file_manips import find_files, excel2csv, path_separator

# Input
import_dir = input(u'Répertoire source :') or r'\\geosrv\Temporaire\RP'
export_dir = input(u'Répertoire cible :') or r'\\geosrv\Temporaire\RP'

if import_dir and export_dir:

    # Init compteur
    count_read = 0

    # Lancement du process
    try:
        print('Traitement en cours')

        for f in find_files(import_dir, '*.xls*'):
            try:
                f_repertoire = path_separator(f)['rep']
                excel2csv(f, export_dir)
                print(f + ' lu')
                count_read = count_read + 1
            except Exception as e:
                raise

        print(str(count_read) + u' fichiers lus')

    except Exception as e:
        raise
else:
    print("Il manque un répertoire - Traitement annulé")
