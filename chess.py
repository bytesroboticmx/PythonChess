import pygame

# Inicializamos Pygame
pygame.init()

# Definimos algunos colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Definimos el tamaño de la ventana
TAMANIO_VENTANA = (600, 600)
VENTANA = pygame.display.set_mode(TAMANIO_VENTANA)

# Definimos el título de la ventana
pygame.display.set_caption("Movimientos de Ajedrez")

# Creamos una clase para representar las piezas de ajedrez
class Pieza:
    def __init__(self, imagen, x, y):
        self.imagen = imagen
        self.rect = imagen.get_rect()
        self.rect.x = x
        self.rect.y = y

    def mover(self, x, y):
        self.rect.x = x
        self.rect.y = y

# Cargamos las imágenes de las piezas de ajedrez
peon_blanco = pygame.image.load("peon_blanco.png").convert_alpha()
peon_negro = pygame.image.load("peon_negro.png").convert_alpha()
torre_blanca = pygame.image.load("torre_blanca.png").convert_alpha()
torre_negra = pygame.image.load("torre_negra.png").convert_alpha()

# Creamos algunas piezas de ajedrez
peon1_blanco = Pieza(peon_blanco, 0, 1)
peon2_blanco = Pieza(peon_blanco, 1, 1)
peon3_blanco = Pieza(peon_blanco, 2, 1)
peon4_blanco = Pieza(peon_blanco, 3, 1)
peon5_blanco = Pieza(peon_blanco, 4, 1)
peon6_blanco = Pieza(peon_blanco, 5, 1)
peon7_blanco = Pieza(peon_blanco, 6, 1)
peon8_blanco = Pieza(peon_blanco, 7, 1)

peon1_negro = Pieza(peon_negro, 0, 6)
peon2_negro = Pieza(peon_negro, 1, 6)
peon3_negro = Pieza(peon_negro, 2, 6)
peon4_negro = Pieza(peon_negro, 3, 6)
peon5_negro = Pieza(peon_negro, 4, 6)
peon6_negro = Pieza(peon_negro, 5, 6)
peon7_negro = Pieza(peon_negro, 6, 6)
peon8_negro = Pieza(peon_negro, 7, 6)

torre1_blanca = Pieza(torre_blanca, 0, 0)
torre2_blanca = Pieza(torre_blanca, 7, 0)

torre1_negra = Pieza(torre_negra, 0, 7)
torre2_negra = Pieza(torre_negra, 7, 7)

# Creamos una lista de piezas para facilitar su gestion

piezas = [
peon1_blanco, peon2_blanco, peon3_blanco, peon4_blanco,
peon5_blanco, peon6_blanco, peon7_blanco, peon8_blanco,
peon1_negro, peon2_negro, peon3_negro, peon4_negro,
peon5_negro, peon6_negro, peon7_negro, peon8_negro,
torre1_blanca, torre2_blanca, torre1_negra, torre2_negra
]

#Definimos una función para dibujar las piezas en la pantalla

def dibujar_piezas():
    for pieza in piezas:
        VENTANA.blit(pieza.imagen, pieza.rect)

#Definimos una función para mover una pieza a una posición dada

def mover_pieza(piez, x, y):
    pieza.mover(x,y)

#Mostramos las piezas en la pantalla por primera vez
dibujar_piezas()

#Definimos la posicion actual del raton
posicion_ratón=None

#Definimos el bucle principal del juego
while True:
# Recorremos todos los eventos que se hayan producido
    for evento in pygame.event.get():
# Si se ha pulsado la tecla de salida, salimos del programa
        if evento.type == pygame.QUIT:
            pygame.quit()
quit()
