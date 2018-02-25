import pygame
from Resources.scripts.Menus import screen #so if display (full/windowed) stays the same
shotgun=False
def gun():
    return 6, "semi-auto", 11, 35, 160, 10
def blit_gun(angle, mainx=295, mainy=215):
    bg = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
    pygame.draw.rect(bg, (0, 0, 0), (60, 11, 5, 27))
    pygame.draw.rect(bg, (0, 0, 0), (62, 19, 23, 7))
    pygame.draw.rect(bg, (0, 34, 0), (81, 10, 6, 27))
    bg = pygame.transform.rotate(bg, angle)
    screen.blit(bg, (mainx - 25, mainy - 25))
    return [(None, (0, 0, 0), (60, 11, 5, 27)), (None, (0, 0, 0), (62, 19, 23, 7)), (None, (0, 34, 0), (81, 10, 6, 27))]