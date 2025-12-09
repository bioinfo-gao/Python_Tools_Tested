import random
import my_calulator
from my_calulator import my_adder

def mutate(a_list):
    b_list = []
    new_item =0
    for item in a_list:
        new_item = item *2
        new_item += random.randint(1,3)
        new_item = my_calulator.my_adder(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,4,5, 8,13])
