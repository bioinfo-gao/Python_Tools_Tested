#print("Runoob")


# 按下 Tab 键接受所有补全建议：按下 Ctrl+→ 键(mac系统为Command+→)接收单个词补全建议：
# left bar Fitten Code – 开始对话或者使用快捷键Ctrl+Alt+C(mac系统为Control+Option+C)打开对话窗口进行对话：
# 当用户选中代码段再进行对话时，Fitten Code 会自动引用用户所选中的代码段，此时可直接针对该代码段进行问询等操作：

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Example usage:
# arr = [3, 6, 8, 10, 1, 2, 1]
# sorted_arr = quick_sort(arr)
# print("Sorted array:", sorted_arr)

