#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Attention, si la première ligne ne commence pas en haut à gauche,
# seules les colonnes après sont prises en compte

# Code pour convertir un répertoire de fichiers Excels
# en fichiers CSV délimités par des ;

import os
import sys
from utils.excel_manips import excel2csv
from utils.file_manips import find_files

import_dir = input(u'Répertoire source :')
export_dir = input(u'Répertoire cible (ex : X:\Data\):')
count_read = 0

# Lancement du process
try:
    print('Traitement en cours')
    exceptions = []
    for f in find_files(import_dir, '*.xls*'):
        try:
            f_path = os.path.dirname(f)
            f_basename = os.path.basename(f).split('.')[0]
            excel2csv(str(f), export_dir + str(f_basename))
            print(f + ' lu')
            count_read = count_read + 1
        except Exception as e:
            exceptions.append((str(f), e))
            print(exceptions)

    print(str(count_read) + u' fichiers lus')

except Exception as e:
    print("Unexpected error:", sys.exc_info()[0])
    raise
