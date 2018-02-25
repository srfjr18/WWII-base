import pygame
from Resources.scripts.Menus import screen #so if display (full/windowed) stays the same
spawnarea_x = (-302, 433)
spawnarea_y = (-415, 145)
background_color = (0, 75, 0)
def blit_map(self.imagesx, self.imagesy):
        pygame.draw.rect(screen, (0, 0, 0), (-2 - self.imagesx, 445 - self.imagesy, 670, 36))
        pygame.draw.rect(screen, (0, 0, 0), (-2 - self.imagesx, 445 - self.imagesy, 670, 36), 3)
        pygame.draw.rect(screen, (0, 0, 0), (-2 - self.imagesx, -115 - self.imagesy, 65, 562))
        pygame.draw.rect(screen, (0, 0, 0), (-2 - self.imagesx, -115 - self.imagesy, 65, 562), 3)
        pygame.draw.rect(screen, (0, 0, 0), (46 - self.imagesx, -114 - self.imagesy, 754, 49))
        pygame.draw.rect(screen, (0, 0, 0), (46 - self.imagesx, -114 - self.imagesy, 754, 49), 3)
        pygame.draw.rect(screen, (0, 0, 0), (733 - self.imagesx, -81 - self.imagesy, 62, 573))
        pygame.draw.rect(screen, (0, 0, 0), (733 - self.imagesx, -81 - self.imagesy, 62, 573), 3)
        pygame.draw.rect(screen, (1, 0, 0), (597 - self.imagesx, 445 - self.imagesy, 153, 36))
        pygame.draw.rect(screen, (0, 0, 0), (597 - self.imagesx, 445 - self.imagesy, 153, 36), 3)
        screen.blit(pygame.transform.rotate(self.character,180) (117 - self.imagesx, 163 - self.imagesy)
        if 175 - 5 <= self.mainx - self.self.imagesx <= 175 + 10: campaign.text("sir hello")
def collision(self.imagesx, self.imagesy):
    return [pygame.Rect((-2 - self.imagesx, 445 - self.imagesy), (670, 36)), pygame.Rect((-2 - self.imagesx, -115 - self.imagesy), (65, 562)), pygame.Rect((46 - self.imagesx, -114 - self.imagesy), (754, 49)), pygame.Rect((733 - self.imagesx, -81 - self.imagesy), (62, 573)), pygame.Rect((597 - self.imagesx, 445 - self.imagesy), (153, 36))]
