# !/usr/bin/python2.7
# -*- coding: utf-8 -*-


def find_files(directory, pattern):

    """
        Cherche des fichiers selon un motif avec joker dans un répertoire
        et ses sous-répertoires
        Source
        Un répertoire en entrée : X:\REP
        Un pattern avec joker * : *.txt
    """

    import fnmatch
    import os

    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                assert isinstance(filename, object)
                yield filename
