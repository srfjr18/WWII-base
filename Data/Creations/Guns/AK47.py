import pygame
from Resources.scripts.Menus import screen #so if display (full/windowed) stays the same
def gun():
    return 8, "full-auto", 29, 25, 200, 18
def blit_gun(angle, mainx=295, mainy=215):
    bg = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
    pygame.draw.rect(bg, (50, 20, 0), (71, 10, 9, 28))
    pygame.draw.rect(bg, (50, 20, 0), (72, 28, 7, 15))
    pygame.draw.rect(bg, (50, 20, 0), (70, 43, 11, 7))
    pygame.draw.rect(bg, (0, 20, 0), (73, 1, 4, 9))
    bg = pygame.transform.rotate(bg, angle)
    screen.blit(bg, (mainx - 25, mainy - 25))
    return [(None, (50, 20, 0), (71, 10, 9, 28)), (None, (50, 20, 0), (72, 28, 7, 15)), (None, (50, 20, 0), (70, 43, 11, 7)), (None, (0, 20, 0), (73, 1, 4, 9))]