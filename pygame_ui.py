import pygame,sys
from pygame.locals import *

# 使用pygame之前必须初始化
pygame.init()

# 设置主屏窗口
screen = pygame.display.set_mode((600,600))

# 设置窗口的标题，即游戏名称
pygame.display.set_caption('Texas')

font = pygame.font.SysFont("arial", 16);
font_height = font.get_linesize()
event_text = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()




