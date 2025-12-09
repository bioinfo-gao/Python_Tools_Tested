# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 23:06:29 2024

@author: zhen-
"""
#f = open(r"C:\Users\zhen-\Documents\Python Scripts\Series.py")

# #f = open( r"C:\Users\zhen-\Documents\Python Scripts\S1.txt" )
# f = open( "S1.txt" )

# f
# cNames =  #_io.TextIOWrapper' object has no attribute 'readLines'
# #print(cNames)
# print(f)

# f.close()


# f = read('goodlines.txt')
# mylist = f.readlines()


# #with open('goodlines.txt') as f:
# with open(r"C:\Users\zhen-\Documents\Python Scripts\.txt") as f:
#     mylist = list(f)


import os
print( os.getcwd() ) # Prints the current working directory

path="/Users/zhen-/Documents/Python Scripts"
os.chdir(path)
    
L = ["Geeks\n", "for\n", "Geeks\n"]
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()

# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    
    
    