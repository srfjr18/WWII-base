import pygame
from Resources.scripts.Menus import screen #so if display (full/windowed) stays the same
spawnarea_x = (-300, -299)
spawnarea_y = (-300, -299)
background_color = (0, 75, 0)
def blit_map(imagesx, imagesy):
    pygame.draw.rect(screen, (0, 0, 0), (0 - imagesx, 0 - imagesy, 0, 0))
    pygame.draw.rect(screen, (0, 0, 0), (0 - imagesx, 0 - imagesy, 0, 0), 3)
    enemy_pos = [(552, -1456),(832, -1438),(1116, -1430),(1382, -1455),(1388, -1656),(1392, -1819),(1401, -1969),(1396, -2100),(1405, -2233),(1390, -2342),(1397, -2510),(1423, -2645),(1618, -2712),(1916, -2710),(2193, -2686),(2439, -2723),(2697, -2727),(2982, -2729),(3256, -2688),(3508, -2744),(3707, -2746),(3977, -2744),(4216, -2736),(4544, -2732),(4896, -2724),(5145, -2727),(5434, -2734),(5827, -2735),(6197, -2711),def collision(imagesx, imagesy):
    return]