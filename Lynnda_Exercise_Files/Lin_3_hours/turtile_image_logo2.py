import turtle



# 更多示例：画彩色螺旋
t = turtle.Turtle()
t.speed(0)  # 最快速度

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
turtle.bgcolor('black')

for x in range(360):
    t.pencolor(colors[x % 6])  # 循环换颜色
    t.width(x // 100 + 1)      # 笔触粗细变化
    t.forward(x)
    t.left(59)                 # 转59度形成螺旋

turtle.done()
