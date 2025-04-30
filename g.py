import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 800, 600
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.alive = True
        self.image = pygame.image.load("pet.png")  # Add your own image
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.draw_stats(surface)

    def draw_stats(self, surface):
        # Hunger bar
        pygame.draw.rect(surface, (255,0,0), (50, 50, 200, 30))
        pygame.draw.rect(surface, (0,255,0), (50, 50, 2 * self.hunger, 30))
        
        # Happiness bar
        pygame.draw.rect(surface, (255,0,0), (50, 100, 200, 30))
        pygame.draw.rect(surface, (0,255,0), (50, 100, 2 * self.happiness, 30))
        
        # Energy bar
        pygame.draw.rect(surface, (255,0,0), (50, 150, 200, 30))
        pygame.draw.rect(surface, (0,255,0), (50, 150, 2 * self.energy, 30))

    def feed(self):
        if self.alive:
            self.hunger = min(100, self.hunger + 20)
            self.happiness = min(100, self.happiness + 5)
            self.energy = max(0, self.energy - 5)

    def play(self):
        if self.alive:
            self.happiness = min(100, self.happiness + 20)
            self.energy = max(0, self.energy - 15)
            self.hunger = max(0, self.hunger - 10)

    def rest(self):
        if self.alive:
            self.energy = min(100, self.energy + 30)
            self.hunger = max(0, self.hunger - 5)

    def time_pass(self):
        if self.alive:
            self.hunger = max(0, self.hunger - 5)
            self.happiness = max(0, self.happiness - 5)
            self.energy = max(0, self.energy - 5)
            
            if self.hunger <= 0 or self.happiness <= 0 or self.energy <= 0:
                self.alive = False

class Button:
    def __init__(self, text, x, y, width, height, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = (200, 200, 200)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

def game_loop():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Virtual Pet")
    clock = pygame.time.Clock()
    
    pet_name = "Fluffy"  # Add text input functionality
    pet = VirtualPet(pet_name)
    
    # Create buttons
    buttons = [
        Button("Feed", 50, 400, 100, 50, pet.feed),
        Button("Play", 200, 400, 100, 50, pet.play),
        Button("Rest", 350, 400, 100, 50, pet.rest),
        Button("Quit", 650, 500, 100, 50, sys.exit)
    ]

    last_update = pygame.time.get_ticks()
    
    while pet.alive:
        current_time = pygame.time.get_ticks()
        
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.rect.collidepoint(pos):
                        button.action()

        # Time-based updates every 2 seconds
        if current_time - last_update > 2000:
            pet.time_pass()
            last_update = current_time

        # Drawing
        screen.fill(WHITE)
        pet.draw(screen)
        for button in buttons:
            button.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)

    # Game over screen
    font = pygame.font.Font(None, 72)
    text = font.render("GAME OVER", True, (255, 0, 0))
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)

if __name__ == "__main__":
    game_loop()