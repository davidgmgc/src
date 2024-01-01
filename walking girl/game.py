import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Walking Girl")

# Cargar imágenes y configurar animaciones
walking_animation = pygame.image.load("walking_animation.png")
walking_frames_right = [walking_animation.subsurface((i * 64, 0, 64, 128)) for i in range(8)]
walking_frames_left =  [walking_animation.subsurface((i * 64, 128, 64, 128)) for i in range(8)]

# Otros parámetros
clock = pygame.time.Clock()
girl_x = 0
girl_speed = 5
direction = 1  # 1 para derecha, -1 para izquierda

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar posición de la chica
    girl_x += girl_speed * direction

    # Verificar si la chica ha llegado al borde derecho o izquierdo
    if girl_x > width:
        girl_x = width - 64  # Reposicionar al borde derecho
        direction = -1  # Cambiar dirección a izquierda
    elif girl_x < -64:
        girl_x = -1  # Reposicionar al borde izquierdo
        direction = 1  # Cambiar dirección a derecha

    # Dibujar en la pantalla
    screen.fill((255, 255, 255))  # Fondo blanco
    
    if direction == 1:
        screen.blit(walking_frames_right[int(pygame.time.get_ticks() / 100) % 8], (girl_x, height-256))
    elif direction ==-1:
        screen.blit(walking_frames_left[int(pygame.time.get_ticks() / 100) % 8], (girl_x, height-256))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(60)
