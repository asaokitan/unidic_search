#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import json
import unidic_search

# メイン
if __name__ == "__main__":

	print "Content-type: application/json;charset=utf-8\n"
	form = cgi.FieldStorage()
	
	if form.getvalue('keyword'):

		string = form.getvalue('keyword').decode('utf-8')
		#dots = form.getvalue('dots')

		result = list(unidic_search.search(string))
	else:
		result = []
	
	#print cgi.escape(result).encode('utf-8')
	
	# JSONとかで返そうよ！！ JSON で渡す！ jQueryがそれを料理する！
	print json.dumps(result)