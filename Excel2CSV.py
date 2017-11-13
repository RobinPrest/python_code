#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Attention, si la première ligne ne commence pas en haut à gauche,
# seules les colonnes après sont prises en compte

# Code pour convertir un répertoire de fichiers Excels
# en fichiers CSV délimités par des ;

import os, sys, fnmatch
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

import_dir = input(u'Répertoire source :')
export_dir = input(u'Répertoire cible (ex : X:\Data\):')
count_read = 0

#Fonction pour créer un fichier CSV à partir d'un fichier Excel
def read_excel(excel_file, export_dir):
    sheet_to_df_map = {}

    #Lecture de tous les noms de feuilles
    xls = pd.ExcelFile(excel_file)
    shn = xls.sheet_names

    #Boucle sur les noms de feuilles
    for sheet_name in shn:
        df = pd.read_excel(excel_file,sheet_name)
        #-->Possibilité ici de créer des modules de controle, modif ou autre

        #export en csv vers le répertoire spécifié
        df.to_csv(export_dir+'_'+sheet_name+'.csv', sep=';', encoding='utf-8', index=False)

# Fonction pour chercher les fichier dans des repertoires et sous-repertoires
def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

#Lancement du process
try:
    print('Traitement en cours')
    exceptions = []
    try:
        for f in find_files(import_dir, '*.xls*'):
            f_path = os.path.dirname(f)
            f_basename = os.path.basename(f).split('.')[0]
            read_excel(f,export_dir+f_basename)
            print(f+' lu')
            count_read = count_read+1
    except Exception, e:
       exceptions.append((f,e.message))
       print(exceptions)

    print(str(count_read)+u' fichiers lus')

except:
    print "Unexpected error:", sys.exc_info()[0]
    raise