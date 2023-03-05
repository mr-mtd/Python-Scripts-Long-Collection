import pygame


def playMyShit():
    # initialize Pygame
    pygame.init()

    # load OGG file

    fileName = 'C:\Users\mason\Documents\\someConversionTextToSpeegOGG.ogg'

    # "C:\Users\mason\Desktop\\file_example_OOG_1MG.ogg" #"C:\Users\mason\Desktop\\response.ogg"
    sound = pygame.mixer.Sound(fileName)
    # play OGG file
    sound.play()

    # wait for sound to finish playing
    while pygame.mixer.get_busy():
        pygame.time.wait(100)
