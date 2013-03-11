#!/usr/bin/env python3
# encoding: utf-8

import os
import base64
import sys


try :
	
	mode = sys.argv[1]
	wert = sys.argv[2]
	
	
	if mode == "encode":
	
		encoded_str = str(base64.b64encode(wert.encode('ascii')))
		tmp = encoded_str[2:]
		lgtmp2 = len(tmp)
		final = tmp[:lgtmp2-1]
		print (final)
	
	if mode == "decode":
	
		decoded_str = str(base64.b64decode(wert))
		tmp = decoded_str[2:]
		lgtmp2 = len(tmp)
		final = tmp[:lgtmp2-1]
		print (final)
		
except :
	print ("b64.py [encode/decode] [String]")