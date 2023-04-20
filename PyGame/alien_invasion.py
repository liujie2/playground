import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.width, ai_settings.height))
    # 创建一个用于存储子弹的数组
    bullets = Group()
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_events(ai_settings, screen, ship, bullets)


if __name__ == '__main__':
    run_game()
