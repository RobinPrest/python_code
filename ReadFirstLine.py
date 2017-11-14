#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import io
import sys
from utils.file_manips import find_files

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
    open(start_dir + '\export.log', 'w').close()

    # Ouverture du fichier d'export
    export_file = io.open(start_dir + '\export.log', mode="a", encoding='utf-8')

    # Lancement du process
    try:

        for f in find_files(start_dir, pattern):
            # print 'Found text files:', f
            first_line = io.open(f, mode='r').readline()
            file_basename = os.path.basename(f)
            first_line = first_line.rstrip() + '@' + file_basename + '\r\n'
            export_file.write(first_line)
            count = count + 1

    except Exception as e:
        print('Unexpected error:', sys.exc_info()[0])
        raise

    export_file.close()
    print(str(count) + u' fichiers lus')
    print(u'Fichier produit : ' + start_dir + '\export.log')
else:
    print(u"Il manque un argument - traitement annulé")
