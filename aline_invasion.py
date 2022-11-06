# 创建游戏窗口
import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import *


class AlineInvasion(object):
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        # 调用Settings类
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_wight = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode((self.settings.screen_wight, self.settings.screen_height))

        # 设置屏幕尺寸
        self.screen = pygame.display.set_mode((1200, 800))

        # 设置背景颜色

        self.bg_color = (150, 240, 240)

        # 设置游戏标题
        pygame.display.set_caption("外星人入侵")

        self.ship = Ship(self)

        # 创建一个sprite 精灵组
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()

            self.bullets.update()

            # 删除消失的子弹
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

            self._update_screen()

    def _check_events(self):

        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.k_q:
           sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应松开"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入到编组bullets中"""
        if len(self.bullets) < self.settings.bullets_allowed:
            n_bullets = Bullet(self)
            self.bullets.add(n_bullets)

    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()

    def _update_screen(self):
        # 每次循环都更新屏幕
        self.screen.fill(self.settings.bg_color)

        # 调用Ship类中的blit me方法
        self.ship.blitme()

        # 在精灵族中循环绘制子弹
        for bullet in self.bullets.sprites():
            # DOTO 绘制子弹有大问题

            # bullet.draw_bullet()

        # 让绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建AlineInvasion对象a_i
    a_i = AlineInvasion()
    # 对象a_i调用主循环，创建游戏窗口
    a_i.run_game()
