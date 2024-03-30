import pygame 
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# define the vertices of the square
vertices = ( ( 1, 1 ),
            ( 1, -1 ),
            ( -1, -1 ),
            ( -1, 1 ) )

# define the edges of the square
edge = ( ( 0, 1 ),
        ( 1, 2 ),
        ( 2, 3 ),
        ( 3, 0 ) )

def square() :
    glBegin( GL_LINES )
    for e in edge:
        for vertex in e:
            glVertex2iv( vertices[ vertex ] )
    glEnd()

# Create a pygame window 
def main() :
    pygame.init()
    
    # display size
    display = ( 500, 500 )
    
    pygame.display.set_mode( display, DOUBLEBUF | OPENGL )

    gluPerspective( 40, ( display[ 0 ] / display[ 1 ] ), 1, 10 )

    glTranslatef( 0.0, 0.0, -5 )

    # main loop
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        square()
        
        # update the display
        pygame.display.flip()

main()