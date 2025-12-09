#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

try: 
    fh = open('xlines.txt') 
    for line in fh.readlines():
        #print(line)
        print(line, end='') # print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

except IOError as e:
    print(" Eror happended as {}".format(e))
