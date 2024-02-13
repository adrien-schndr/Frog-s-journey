import pygame
from pygame.locals import *

# Fenêtre
window_length = 1920
window_height = 1080
screen = pygame.display.set_mode((window_length, window_height), pygame.SCALED | pygame.FULLSCREEN)


# Textures
wooden_log_textures = []
for image in range(0, 18):
    texture = pygame.image.load("images/wood/wood_log_" + str(image) + ".png")
    texture = pygame.transform.scale(texture, (100, 100))
    wooden_log_textures.append(texture)

menu_background = "images/menu_background.png"

story = "Ah voyageur intrépide, ribbit bienvenue dans ces contrées sylvestres. Je suis Layton, Chef de la Guilde, gardien de ces marais ancestraux. J’entrevois dans vos yeux une lueur de détermination et de bravoure ribbit. Je vous confie une quête d’une importance capitale, même si vous ne l’avez peut être pas encore souhaitée. Vous êtes désigné pour récupérer les dix épées légendaires, symbole de pouvoir et de savoir ancien. Je vous servirais de guide n’ayez crainte ribbit. Il est maintenant l’heure pour vous d’accomplir votre destinée. Je vous souhaite bonne chance voyageur ribbit."
