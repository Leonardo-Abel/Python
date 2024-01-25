import pygame

# inicializando o mixer PyGame
pygame.mixer.init()
# Inicianlizando o PyGame
pygame.init()
pygame.mixer.music.load('ex.mp3')
pygame.mixer.music.play()
pygame.event.wait()
