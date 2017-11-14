#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from utils.file_manips import find_files, csv_first_line_export

# Choix du répertoire
start_dir = input(u'Répertoire à traiter :')
# start_dir = os.getcwd()

# Choix du filtre
pattern = input(u'Extension ou filtre de fichier texte (ex : *.txt): ')

# Reset du compteur de fichiers
count = 0

if start_dir and pattern:
    print('Traitement de ' + start_dir)
    # nom du fichier d'export
    out_log = start_dir + '\export.log'

    # Lancement du process
    try:
        for f in find_files(start_dir, pattern):
            # print 'Found text files:', f
            csv_first_line_export(f,out_log)
            count = count + 1
    except Exception as e:
        print('Unexpected error:', sys.exc_info()[0])
        raise

    print(str(count) + u' fichiers lus')
    print(u'Fichier produit : ' + start_dir + '\export.log')

else:
    print(u"Il manque un argument - traitement annulé")

