# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.mixer.init() # inicia o mixer
pygame.mixer.music.load('candeia.mp3') # carrega o áudio
pygame.mixer.music.play() # tocará a música
input("Candeia - Gamação/Peixeiro Granfino/Ouço uma Voz/Vem Amenizar | Para encerrar, digite aqui: ")


