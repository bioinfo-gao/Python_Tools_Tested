#!/usr/bin/python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is A string'
    print(s.capitalize())
    print(s.title())
    print(s.upper())
    print(s.swapcase()) 
    print(s.find('is'))
    print(s.replace('this', 'that'))
    print(s.strip())
    # the fllowing start with "is"
    print(s.isalnum()) # space is not alphanumeric !
    print(s.isalpha())
    print(s.isdigit())
    print(s.isprintable())


# help(str.swapcase) # 使用 help() 函数：查看详细的功能描述。                                 ==> popup window  
# dir(str)           # 使用 dir() 函数：列出字符串对象的所有可用方法（当你忘记具体拼写时很有用） ==> same window

if __name__ == "__main__": 
    main()
