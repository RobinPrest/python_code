# !/usr/bin/python2.7
# -*- coding: utf-8 -*-

import fnmatch


# Fonction pour chercher les fichiers dans des repertoires et sous-repertoires
def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename
