#!/usr/bin/python3

# a, b = "abc", 'bc'
# a, b = -9, 1
a, b = 9, 1
if a < b:
    print('a ({}) is less than b ({})'.format(a, b))
else:
    print('a ({}) is not less than b ({})'.format(a, b))

print("foo" if a< b else "bar")