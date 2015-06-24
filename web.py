#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import json
import unidic_search

def wildcard2re(string):
	
	if not string:
		return string

	string = string.replace('?','.')
	string = string.replace(u'？','.')
	string = string.replace('*','.+')
	string = string.replace(u'＊','.+')

	string = '^' + string + '$'
	
	return string


# メイン
if __name__ == "__main__":

	print "Content-type: application/json;charset=utf-8\n"
	form = cgi.FieldStorage()
	
	if form.getvalue('surface') or form.getvalue('lForm'):

		surface = form.getvalue('surface', '').decode('utf-8')
		re_surface = wildcard2re(surface)
		lForm = form.getvalue('lForm', '').decode('utf-8')
		re_lForm = wildcard2re(lForm)

		result = list(unidic_search.search(surface=re_surface, lForm=re_lForm))
	else:
		result = []
	
	#print cgi.escape(result).encode('utf-8')
	
	# JSONとかで返そうよ！！ JSON で渡す！ jQueryがそれを料理する！
	print json.dumps(result)
