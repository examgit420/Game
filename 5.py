import pygame

pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Pygame")

# Colors and box properties
WHITE, BLUE = (255, 255, 255), (0, 0, 255)
box_pos, box_size, box_speed = [100, 100], 50, 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    box_pos[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * box_speed
    box_pos[1] += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * box_speed

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (*box_pos, box_size, box_size))
    pygame.display.flip()

pygame.quit()
