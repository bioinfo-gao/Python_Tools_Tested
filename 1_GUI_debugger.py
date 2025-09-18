# debug_example.py
# this is the best debugger tutorial I ever see
import pdb
# https://www.bilibili.com/video/BV1Vc6vYhEX3/?spm_id_from=333.788.player.switch&vd_source=9a4bc8c6c4b3f65118a7338473c15077&p=96

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