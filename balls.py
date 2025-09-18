import pygame
import random
import math
import sys

# 初始化pygame
pygame.init()

# 窗口设置
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("双球碰撞模拟")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)

# 圆的参数
CIRCLE_CENTER = (WIDTH // 2, HEIGHT // 2)
CIRCLE_RADIUS = 250


# 小球类
class Ball:
    def __init__(self, x, y, radius, color, is_black=False):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-3, 3)
        self.is_black = is_black
        self.growth_rate = 0.1  # 黑色球碰到白球时的增长率

    def update(self):
        # 更新位置
        self.x += self.vx
        self.y += self.vy

        # 计算到圆心的距离
        distance_to_center = math.sqrt((self.x - CIRCLE_CENTER[0]) ** 2 + (self.y - CIRCLE_CENTER[1]) ** 2)

        # 边界反弹（碰到大圆边界）
        if distance_to_center + self.radius > CIRCLE_RADIUS:
            # 计算法线方向
            nx = (self.x - CIRCLE_CENTER[0]) / distance_to_center
            ny = (self.y - CIRCLE_CENTER[1]) / distance_to_center

            # 反射速度
            dot_product = self.vx * nx + self.vy * ny
            self.vx -= 2 * dot_product * nx
            self.vy -= 2 * dot_product * ny

            # 调整位置，防止穿出边界
            overlap = distance_to_center + self.radius - CIRCLE_RADIUS
            self.x -= nx * overlap
            self.y -= ny * overlap

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))

    def check_collision_with_white_ball(self, white_ball):
        if not self.is_black:
            return False

        # 计算两球距离
        distance = math.sqrt((self.x - white_ball.x) ** 2 + (self.y - white_ball.y) ** 2)

        # 如果碰撞，黑色球变大
        if distance < self.radius + white_ball.radius:
            self.radius += self.growth_rate
            return True
        return False


# 创建初始小球
black_ball = Ball(WIDTH // 2, HEIGHT // 2, 15, BLACK, True)
white_balls = [Ball(random.randint(CIRCLE_CENTER[0] - CIRCLE_RADIUS + 20, CIRCLE_CENTER[0] + CIRCLE_RADIUS - 20),
                    random.randint(CIRCLE_CENTER[1] - CIRCLE_RADIUS + 20, CIRCLE_CENTER[1] + CIRCLE_RADIUS - 20),
                    10, WHITE)]

# 游戏循环
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 按空格键添加新的白球
                new_white_ball = Ball(
                    random.randint(CIRCLE_CENTER[0] - CIRCLE_RADIUS + 20, CIRCLE_CENTER[0] + CIRCLE_RADIUS - 20),
                    random.randint(CIRCLE_CENTER[1] - CIRCLE_RADIUS + 20, CIRCLE_CENTER[1] + CIRCLE_RADIUS - 20),
                    10, WHITE
                )
                white_balls.append(new_white_ball)

    # 更新
    black_ball.update()

    # 检查白球碰撞并更新
    new_white_balls = []
    for white_ball in white_balls[:]:
        white_ball.update()

        # 检查黑色球是否碰到白色球
        if black_ball.check_collision_with_white_ball(white_ball):
            # 生成新的随机位置的白色小球
            new_white_ball = Ball(
                random.randint(CIRCLE_CENTER[0] - CIRCLE_RADIUS + 20, CIRCLE_CENTER[0] + CIRCLE_RADIUS - 20),
                random.randint(CIRCLE_CENTER[1] - CIRCLE_RADIUS + 20, CIRCLE_CENTER[1] + CIRCLE_RADIUS - 20),
                10, WHITE
            )
            new_white_balls.append(new_white_ball)

    # 添加新生成的白球
    white_balls.extend(new_white_balls)

    # 绘制
    screen.fill(GRAY)

    # 绘制大圆
    pygame.draw.circle(screen, RED, CIRCLE_CENTER, CIRCLE_RADIUS, 3)

    # 绘制小球
    black_ball.draw(screen)
    for white_ball in white_balls:
        white_ball.draw(screen)

    # 显示信息
    info_text = f"白球数量: {len(white_balls)} | 黑球大小: {black_ball.radius:.1f}"
    text_surface = font.render(info_text, True, WHITE)
    screen.blit(text_surface, (10, 10))

    info_text2 = "按空格键手动添加白球"
    text_surface2 = font.render(info_text2, True, WHITE)
    screen.blit(text_surface2, (10, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
