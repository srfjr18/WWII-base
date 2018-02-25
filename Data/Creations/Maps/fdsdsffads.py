import pygame
from Resources.scripts.Menus import screen #so if display (full/windowed) stays the same
spawnarea_x = (-300, -299)
spawnarea_y = (-300, -299)
background_color = (0, 67, 0)
def blit_map(imagesx, imagesy):
    pygame.draw.rect(screen, (0, 0, 0), (0 - imagesx, 0 - imagesy, 0, 0))
    pygame.draw.rect(screen, (0, 0, 0), (0 - imagesx, 0 - imagesy, 0, 0), 3)
    enemy_pos = [(121, 254),def collision(imagesx, imagesy):
    return]