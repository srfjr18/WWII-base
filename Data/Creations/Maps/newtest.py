import pygame
from Resources.scripts.Menus import screen #so if display (full/windowed) stays the same
spawnarea_x = (-300, -299)
spawnarea_y = (-300, -299)
background_color = (88, 56, 0)
def blit_map(imagesx, imagesy):
    pygame.draw.rect(screen, (0, 0, 0), (0 - imagesx, 0 - imagesy, 0, 0))
    pygame.draw.rect(screen, (0, 0, 0), (0 - imagesx, 0 - imagesy, 0, 0), 3)
    screen.blit(pygame.transform.rotate(self.character,60), (352 - imagesx, 238 - imagesy))
    if 392 - 6 <= self.mainy - imagesy <= 392 + 6:
        self.campaign.text('hello')
        self.returner = (0, '392')
    if 95 - 6 <= self.mainx - imagesx <= 95 + 6:
        self.campaign.text('sir')
        self.returner = ('150', 0)
    enemy_pos = [def collision(imagesx, imagesy):
    return]