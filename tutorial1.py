# exec(f"{name} = None"): This line uses the exec function to execute a dynamically generated string
# as Python code. 
# Here, it tries to assign the value None to a variable named by the string name.
def is_valid_identifier(name):
    try:
       #exec(f"{name} = None")
        exec(f"{name} = 123" )
        print(name)#orce an exception to avoid actually creating the variable
        return True
    except:
        return False

# print(is_valid_identifier("2var"))  # False
# print(is_valid_identifier("var2"))  # True
# print(is_valid_identifier(".var"))  # False
# print(is_valid_identifier("&ar2"))  # True

import Runoo
print(f"The imported module name is {Runoo.__name__}")
print(Runoo.quick_sort([3,6,8,10,1,2,1]))



