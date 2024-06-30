import pygame

class Player:
    def __init__(self, x, y, sizeX, sizeY, world_width, world_height, colliders):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY

        self.curr_frame = 0
        self.curr_frame_time = 0

        self.currAnim = 0

        self.spriteSheet = pygame.image.load("Sprites/Walk.png")
        self.PlayerAnimations = []

        self.speed = 1

        self.world_width = world_width
        self.world_height = world_height
        self.colliders = colliders

    def handle(self, dt, offset_x, offset_y):
        keys = pygame.key.get_pressed()

        # Animations
        self.PlayerAnimations = [
            pygame.Rect(self.curr_frame * 32, 0, 32, 32),        # DOWN
            pygame.Rect(self.curr_frame * 32, 32, 32, 32),      # UP
            pygame.Rect(self.curr_frame * 32, 64, 32, 32),  # LEFT
            pygame.Rect(self.curr_frame * 32, 96, 32, 32)   # RIGHT
        ]

        # Create a temporary position for testing collisions
        temp_x = self.x
        temp_y = self.y

        if keys[pygame.K_RIGHT] and self.x < self.world_width - 100 + 32:
            self.x = self.x + self.speed * dt
            self.currAnim = 2
        elif keys[pygame.K_LEFT] and self.x > 0:
            self.x = self.x - self.speed * dt
            self.currAnim = 3
        elif keys[pygame.K_UP] and self.y > 0:
            self.y = self.y - self.speed * dt
            self.currAnim = 1
        elif keys[pygame.K_DOWN] and self.y < self.world_height - 100 + 32:
            self.y = self.y + self.speed * dt
            self.currAnim = 0

        # Animation handling
        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            if self.curr_frame_time >= 100:
                self.curr_frame = (self.curr_frame + 1) % 4
                self.curr_frame_time = 0
            self.curr_frame_time += dt
        else:
            self.curr_frame = 3

        collider_jogador = pygame.Rect(self.x + self.sizeX/2 - offset_x, self.y + self.sizeY/2 - offset_y, self.sizeX, self.sizeY)

        if any(collider_jogador.colliderect(floor) for floor in self.colliders):
            self.x = temp_x
            self.y = temp_y

    def show(self, screen, offset_x, offset_y):
        # Scaling the player image
        current_frame = self.spriteSheet.subsurface(self.PlayerAnimations[self.currAnim])
        scaled_frame = pygame.transform.scale(current_frame, (self.PlayerAnimations[self.currAnim].width * 2, self.PlayerAnimations[self.currAnim].height * 2))

        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x + self.sizeX/2 - offset_x, self.y + self.sizeY/2 - offset_y, self.sizeX, self.sizeY))

        # Draw Player
        screen.blit(scaled_frame, (self.x - offset_x, self.y - offset_y))


class Enemy:
    def __init__(self, x, y, sizeX, sizeY, world_width, world_height, colliders):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY

        self.curr_frame = 0
        self.curr_frame_time = 0

        self.currAnim = 0

        self.spriteSheet = pygame.image.load("Sprites/Walk.png")
        self.PlayerAnimations = []

        self.speed = 1

        self.world_width = world_width
        self.world_height = world_height
        self.colliders = colliders

    def handle(self, dt, offset_x, offset_y):
        keys = pygame.key.get_pressed()

        # Animations
        self.PlayerAnimations = [
            pygame.Rect(self.curr_frame * 32, 0, 32, 32),        # DOWN
            pygame.Rect(self.curr_frame * 32, 32, 32, 32),      # UP
            pygame.Rect(self.curr_frame * 32, 64, 32, 32),  # LEFT
            pygame.Rect(self.curr_frame * 32, 96, 32, 32)   # RIGHT
        ]

        # Create a temporary position for testing collisions
        temp_x = self.x
        temp_y = self.y

        if keys[pygame.K_RIGHT] and self.x < self.world_width - 100 + 32:
            self.x = self.x + self.speed * dt
            self.currAnim = 2
        elif keys[pygame.K_LEFT] and self.x > 0:
            self.x = self.x - self.speed * dt
            self.currAnim = 3
        elif keys[pygame.K_UP] and self.y > 0:
            self.y = self.y - self.speed * dt
            self.currAnim = 1
        elif keys[pygame.K_DOWN] and self.y < self.world_height - 100 + 32:
            self.y = self.y + self.speed * dt
            self.currAnim = 0

        # Animation handling
        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            if self.curr_frame_time >= 100:
                self.curr_frame = (self.curr_frame + 1) % 4
                self.curr_frame_time = 0
            self.curr_frame_time += dt
        else:
            self.curr_frame = 3

        collider_jogador = pygame.Rect(self.x + self.sizeX/2 - offset_x, self.y + self.sizeY/2 - offset_y, self.sizeX, self.sizeY)

        if any(collider_jogador.colliderect(floor) for floor in self.colliders):
            self.x = temp_x
            self.y = temp_y

    def show(self, screen, offset_x, offset_y):
        # Scaling the player image
        current_frame = self.spriteSheet.subsurface(self.PlayerAnimations[self.currAnim])
        scaled_frame = pygame.transform.scale(current_frame, (self.PlayerAnimations[self.currAnim].width * 2, self.PlayerAnimations[self.currAnim].height * 2))

        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x + self.sizeX/2 - offset_x, self.y + self.sizeY/2 - offset_y, self.sizeX, self.sizeY))

        # Draw Player
        screen.blit(scaled_frame, (self.x - offset_x, self.y - offset_y))

