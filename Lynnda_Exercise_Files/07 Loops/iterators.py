#!/usr/bin/python3
# iterators.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# any container object is iterable
def main():
    #fh = open('lines.txt')
    fh = open('/home/gao/Python_Tools_Tested/Lynnda_Exercise_Files/07 Loops/lines.txt')
    for line in fh.readlines():
        print(line)

if __name__ == "__main__": main()
