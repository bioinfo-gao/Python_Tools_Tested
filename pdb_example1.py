# debug_example.py

import pdb

def calculate(a, b):
    result = a + b
    #pdb.set_trace()  # ⬅️ 在这里设置断点 pdf, GUI debugger is much better
    result = result * 2
    return result

def main():
    x = 10
    y = 20
    total = calculate(x, y)
    print("最终结果:", total)

if __name__ == "__main__":
    main()