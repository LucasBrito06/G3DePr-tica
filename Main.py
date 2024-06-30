import pygame
import sys
from pygame.locals import QUIT
import Classes

# Constants
WIDTH, HEIGHT = 800, 600
WORLD_WIDTH, WORLD_HEIGHT = 1100, 1300

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Box Camera Example")

# Camera setup
camera = pygame.Rect(0, 0, WIDTH, HEIGHT)
offset_x, offset_y = 0, 0

# Load assets (assuming these files are in the same directory)
tileset = pygame.image.load("Tiles/t.png")
tileProp = pygame.image.load("Tiles/props.png")
colliders = []

clock = pygame.time.Clock()

pygame.init()
some_other_rect = pygame.Rect(WIDTH // 2 + 20, HEIGHT // 2 + 20, 50, 50)

def read(file_path):
    with open(file_path, 'r') as file:
        pattern = [line.strip().split() for line in file]
    return pattern

def draw_tiles(screen):
    g = tileset.subsurface(pygame.Rect(0, 0, 32, 32))
    f = tileset.subsurface(pygame.Rect(32 * 7, 0, 32, 32))
    r = tileset.subsurface(pygame.Rect(32, 32 * 5, 32, 32))
    box = tileProp.subsurface(pygame.Rect(32 * 3, 32, 32, 32))

    tile_images = {
        'G': pygame.transform.scale(g, (g.get_width() * 2, g.get_height() * 2)),
        'F': pygame.transform.scale(f, (f.get_width() * 2, f.get_height() * 2)),
        'R': pygame.transform.scale(r, (r.get_width() * 2, r.get_height() * 2)),
        'B': pygame.transform.scale(box, (box.get_width() * 2, box.get_height() * 2)),
    }

    colliders.clear()
    for y, row in enumerate(tile_map):
        for x, tile in enumerate(row):
            if tile in tile_images:
                screen.blit(tile_images[tile], (x * 64 - offset_x, y * 64 - offset_y))
    
    for y, row in enumerate(prop_map):
        for x, tile in enumerate(row):
            if tile in tile_images:
                if tile == 'B':
                    screen.blit(tile_images[tile], (x * 64 - offset_x, y * 64 - offset_y))
                    colliders.append(pygame.Rect(x * 64 - offset_x, y * 64 - offset_y, 64, 64))

def cameraUpdate(player):
    global camera
    camera.center = (player.x, player.y)
    camera.clamp_ip(pygame.Rect(0, 0, WORLD_WIDTH, WORLD_HEIGHT))

def load(events):
    global PlayerX, tile_map, prop_map

    PlayerX = Classes.Player(100, 100, 32, 32, WORLD_WIDTH, WORLD_HEIGHT, colliders)  # Initialize player with proper size and position

    tile_map = read('map.txt')
    prop_map = read('propMap.txt')

def update(dt):
    PlayerX.handle(dt, offset_x, offset_y)
    cameraUpdate(PlayerX)
    draw(screen)

def draw(screen):
    global offset_x, offset_y
    offset_x = camera.left
    offset_y = camera.top

    screen.fill((152, 209, 250))

    draw_tiles(screen)
    PlayerX.show(screen, offset_x, offset_y)

    pygame.display.flip()

load(pygame.event.get())
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()
    update(dt)
    pygame.display.update()