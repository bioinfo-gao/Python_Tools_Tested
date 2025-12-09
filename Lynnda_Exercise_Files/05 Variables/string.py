#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s1='this is single quote string'
    print("This is the string! .", s1)

    s2="this is double quote string"
    print("This is the string! .", s2)
    s21=r"this is double \nquote string"
    print("This is the string! .", s21)

    s3='''this is 
    triple 
    quote string'''
    print("This is the string! .", s3)

    s4='this is single \n quote string'
    print("This is the single quote string! with escape.", s4)

    s5="this is double quote \n string"
    print("This is the double string with escape! .", s5)

if __name__ == "__main__": main()
