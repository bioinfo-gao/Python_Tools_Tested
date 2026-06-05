#!/usr/bin/python3
# iterators.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# any container object is iterable

# cd "/home/gao/Python_Tools_Tested/Lynnda_Exercise_Files/07 Loops/"
# 相对路径依赖工作目录：当代码使用 'lines.txt' 这样的相对路径时，Python 会在当前工作目录中查找文件，而不是在脚本所在的目录中查找。
def main():
    #fh = open('lines.txt')
    fh = open('/home/gao/Python_Tools_Tested/Lynnda_Exercise_Files/07 Loops/lines.txt')
    for line in fh.readlines():
        print(line)

if __name__ == "__main__": main()


import os

os.getcwd() # 获取当前工作目录

# def main():
#     # Get the directory where this script is located
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     print(script_dir)
#     file_path = os.path.join(script_dir, 'lines.txt')
#     fh = open(file_path)
#     for line in fh.readlines():
#         print(line)

# if __name__ == "__main__": main()