import pygame
from Resources.scripts.Menus import screen #so if display (full/windowed) stays the same
shotgun=True
def gun():
    return 10, "full-auto", 29, 6, 160, 20
def blit_gun(angle, mainx=295, mainy=215):
    bg = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
    pygame.draw.rect(bg, (0, 0, 0), (71, 5, 8, 24))
    pygame.draw.rect(bg, (0, 0, 0), (71, 15, 16, 19))
    pygame.draw.rect(bg, (0, 0, 0), (71, 26, 9, 16))
    pygame.draw.rect(bg, (0, 0, 0), (68, 38, 15, 8))
    bg = pygame.transform.rotate(bg, angle)
    screen.blit(bg, (mainx - 25, mainy - 25))
    return [(None, (0, 0, 0), (71, 5, 8, 24)), (None, (0, 0, 0), (71, 15, 16, 19)), (None, (0, 0, 0), (71, 26, 9, 16)), (None, (0, 0, 0), (68, 38, 15, 8))]