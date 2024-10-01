# programa que abra e reproduza um árquivo mp3

import pygame

pygame.init()
pygame.mixer.music.load('ex020.mp3')
pygame.mixer.music.play()
pygame.event.wait()
