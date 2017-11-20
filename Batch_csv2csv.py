# !/usr/bin/python2.7
# -*- coding: utf-8 -*-

from utils.file_manips import find_files, path_separator, csv2csv

# Input
import_dir = input(u'Répertoire source :')
export_dir = input(u'Répertoire cible :')

if import_dir and export_dir:

    # Init compteur
    count_read = 0

    # Lancement du process
    try:
        print('Traitement en cours')

        for f in find_files(import_dir, '*.csv'):
            try:
                f_repertoire = path_separator(f)['rep']
                print('Traitement de ' + path_separator(f)['nom_ext'])
                csv2csv(f, export_dir)
                print(f + ' lu')
                count_read = count_read + 1
            except Exception as e:
                raise

        print(str(count_read) + u' fichiers lus')

    except Exception as e:
        raise
else:
    print("Il manque un répertoire - Traitement annulé")

