#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from utils.file_manips import find_files, csv_first_line_export,path_separator

# Choix du répertoire
start_dir = input(r'Répertoire à traiter (ex : X:\rep\:')
# start_dir = os.getcwd()

if start_dir:

    # Choix du filtre
    pattern = input(u'Extension ou filtre de fichier texte (ex : *.txt): ')

    # Reset du compteur de fichiers
    count = 0

    if pattern:
        print('Traitement du répertoire ' + start_dir)

        # Lancement du process
        try:
            for f in find_files(start_dir, pattern):

                # nom du fichier d'export
                out_log = path_separator(f)[0] + '\export.log'

                print('Found text files:', f)

                csv_first_line_export(f, out_log)
                count = count + 1
                print(u'Fichier produit : ' + path_separator(f)[0] + '\export.log')

        except Exception as e:
            print('Unexpected error:', sys.exc_info()[0])
            raise

        print(str(count) + u' fichiers lus')

    else:
        print(u"Il manque le motif (ex : *.txt) - traitement annulé")

else:
    "Pas de fichier à traiter"
