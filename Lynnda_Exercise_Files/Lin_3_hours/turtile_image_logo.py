import turtle

# 创建画布和画笔
t = turtle.Turtle()

# 设置画笔速度（1~10，0=最快）
t.speed(3)

# 画正方形
for _ in range(4):
    t.forward(100)  # 向前移动100像素
    t.right(90)     # 向右转90度

# 点击窗口关闭
turtle.done()

