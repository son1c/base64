#!/usr/bin/env python3
# encoding: utf-8

import os
import base64
import sys


try :
	
	mode = sys.argv[1]
	wert = sys.argv[2]
	
	
	if mode == "encode":
	
		encoded_str = str(base64.b64encode(wert.encode()))
		tmp = encoded_str[2:]
		lgtmp2 = len(tmp)
		final = tmp[:lgtmp2-1]
		print (final)
	
	if mode == "decode":
		bwert = bytes(wert, 'utf-8')
		decoded_str = base64.b64decode(bwert).decode()
		print (decoded_str)
		
except :
	print ("b64.py [encode/decode] [String]")