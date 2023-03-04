import pygame
from pygame.locals import *

# Initialize the Pygame display
pygame.init()
screen = pygame.display.set_mode((400, 400), DOUBLEBUF|OPENGL)

# Define the vertices of the square
vertices = (
    (1, 1, 0),
    (-1, 1, 0),
    (-1, -1, 0),
    (1, -1, 0)
)

# Define the edges of the square
edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0)
)

# Draw the square
glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
glBegin(GL_LINES)
for edge in edges:
    for vertex in edge:
        glVertex3fv(vertices[vertex])
glEnd()
pygame.display.flip()

# Run the Pygame loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
