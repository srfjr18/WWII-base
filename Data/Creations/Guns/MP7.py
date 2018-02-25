import pygame
from Resources.scripts.Menus import screen #so if display (full/windowed) stays the same
def gun():
    return 3, "full-auto", 42, 25, 240, 15
def blit_gun(angle, mainx=295, mainy=215):
    bg = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
    pygame.draw.rect(bg, (28, 26, 22), (69, 13, 12, 20))
    pygame.draw.rect(bg, (28, 26, 22), (72, 8, 6, 9))
    pygame.draw.rect(bg, (28, 26, 22), (72, 25, 7, 19))
    pygame.draw.rect(bg, (28, 26, 22), (69, 39, 13, 6))
    bg = pygame.transform.rotate(bg, angle)
    screen.blit(bg, (mainx - 25, mainy - 25))
    return [(None, (28, 26, 22), (69, 13, 12, 20)), (None, (28, 26, 22), (72, 8, 6, 9)), (None, (28, 26, 22), (72, 25, 7, 19)), (None, (28, 26, 22), (69, 39, 13, 6))]