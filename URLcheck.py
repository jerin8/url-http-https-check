#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 10:35:33 2020

@author: jerincharly
"""


    
 
from urllib.request import Request, urlopen
from urllib.error import URLError
f = open("weblist.txt","r")
prefix = "https://"
for x in f:
    z = "%s%s" % (prefix,x)
    print (z)
    req = Request(z)
    try:
        response = urlopen(req)
    except URLError as e:
        print(z,'is not an https:// site.')
    else:
        print (z,'Is a https:// site')

    
    
