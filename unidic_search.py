#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import csv

data_path = 'src/unidic-mecab_kana-accent-2.1.2_src/lex.csv'
colnames = ["sForm", "lID", "rID", "cost",
        'pos1', 'pos2', 'pos3', 'pos4',
        'cType', 'cForm', 'lForm', 'lemma',
        'orth', 'pron', 'orthBase', 'pronBase',
        'goshu', 'iType', 'iForm', 'fType', 'fForm',
        'kana', 'kanaBase', 'form', 'formBase',
        'iConType', 'fConType', 'aType', 'aConType', 'aModType']
source_file = 'src/unidic_kana-accent-2.1.2_src/lex.csv'

# def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
#     # csv.py doesn't do Unicode; encode temporarily as UTF-8:
#     csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
#                             dialect=dialect, **kwargs)
#     for row in csv_reader:
#         # decode UTF-8 back to Unicode, cell by cell:
#         yield [unicode(cell, 'utf-8') for cell in row]
# 
# def utf_8_encoder(unicode_csv_data):
#     for line in unicode_csv_data:
#         yield line.encode('utf-8')


def search(string):
	
	data = open(data_path, 'r')
	for line in data:
		word = line.decode('utf-8').rstrip().split(',')
		if string in word[0]:
			yield [word[0],word[4],word[5],word[6],word[7],word[8],word[9],word[10],word[11]]

if __name__ == '__main__':
	
	pass
