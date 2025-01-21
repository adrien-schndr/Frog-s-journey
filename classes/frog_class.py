from constantes import *

class Frog(pygame.sprite.Sprite):
    def __init__(self, chosen_skin):
        super().__init__()
        skin_frog = pygame.image.load("images/skin_menu/frogs/" + chosen_skin + ".png").convert_alpha()
        skin_frog = pygame.transform.scale(skin_frog, (100, 100))
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)
        self.image.blit(skin_frog, (self.rect.x, self.rect.y))
        self.rect.x = 900

    def move(self, event, direction=""):
        vitesse = 100

        if (event.type == KEYDOWN and event.key == K_LEFT) or direction == "left":
            direction = "left"
            if 0 <= self.rect.x - vitesse <= window_length - 100:
                self.rect.x -= vitesse
                return direction
        if (event.type == KEYDOWN and event.key == K_RIGHT) or direction == "right":
            direction = "right"
            if 0 <= self.rect.x + vitesse <= window_length - 100:
                self.rect.x += vitesse
                return direction
        if (event.type == KEYDOWN and event.key == K_UP) or direction == "up":
            direction = "up"
            if 0 <= self.rect.y - vitesse <= window_height - 100:
                self.rect.y -= vitesse
                return direction
        if (event.type == KEYDOWN and event.key == K_DOWN) or direction == "down":
            direction = "down"
            if 0 <= self.rect.y + vitesse <= window_height - 100:
                self.rect.y += vitesse
                return direction