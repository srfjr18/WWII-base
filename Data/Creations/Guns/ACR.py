import pygame
from Resources.scripts.Menus import screen #so if display (full/windowed) stays the same
def gun():
    return 6, "full-auto", 29, 20, 220, 17
def blit_gun(angle, mainx=295, mainy=215):
    bg = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
    pygame.draw.rect(bg, (97, 67, 0), (70, 13, 11, 23))
    pygame.draw.rect(bg, (97, 67, 0), (72, 30, 7, 13))
    pygame.draw.rect(bg, (97, 67, 0), (70, 40, 11, 7))
    pygame.draw.rect(bg, (97, 67, 0), (72, 9, 7, 17))
    pygame.draw.rect(bg, (0, 2, 0), (74, 1, 3, 9))
    pygame.draw.rect(bg, (0, 2, 0), (70, 16, 10, 1))
    pygame.draw.rect(bg, (0, 2, 0), (70, 22, 11, 1))
    pygame.draw.rect(bg, (0, 2, 0), (71, 29, 10, 1))
    bg = pygame.transform.rotate(bg, angle)
    screen.blit(bg, (mainx - 25, mainy - 25))
    return [(None, (97, 67, 0), (70, 13, 11, 23)), (None, (97, 67, 0), (72, 30, 7, 13)), (None, (97, 67, 0), (70, 40, 11, 7)), (None, (97, 67, 0), (72, 9, 7, 17)), (None, (0, 2, 0), (74, 1, 3, 9)), (None, (0, 2, 0), (70, 16, 10, 1)), (None, (0, 2, 0), (70, 22, 11, 1)), (None, (0, 2, 0), (71, 29, 10, 1))]