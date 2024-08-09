import pygame
import random
import math
from enum import Enum


class Colors(Enum):
    FIRE = [[255, 0, 0], (255, 150, 0), (50, 50, 50)]
    WATER = ((15,94,156), (28,163,236), (116,204,244))
    ICE = ((63,208,212), (185,232,234), (255,255,255))

class Particle:
    def __init__(self, x, y, radius, start, colors):
        self.x = x
        self.y = y
        self.radius = radius
        self.start = start
        self.colors = colors
        self.yvel = random.random() * 1.8
        self.burn_rate = 0.02
        
        self.layers = 2
        self.glow = 2.5
        
        surf_size = 2 * self.radius * self.layers * self.layers * self.glow
        self.surf = pygame.Surface((surf_size, surf_size), pygame.SRCALPHA)
        
    def update(self, win, pos):
        xvel = random.random() - 0.5
        self.x += xvel
        self.y -= self.yvel
        
        self.radius -= self.burn_rate
        if self.radius <= 0:
            self.radius = 0.01
        
        surf_size = 2 * self.radius * self.layers * self.layers * self.glow
        self.surf = pygame.Surface((surf_size, surf_size), pygame.SRCALPHA)
        
        for i in range(self.layers, -1, -1):
            alpha = 255 - i * (255 // self.layers - 5)
            if alpha <= 0:
                alpha = 0.01
            radius = int(self.radius * self.glow * i * i)
             
            if self.radius >1.6:
                color = self.colors[0]
            elif self.radius > 1.1:
                color = self.colors[1]
            else:
                color = self.colors[2]
            color = (*color, alpha)
        
            pygame.draw.circle(self.surf, color, (self.surf.get_width() // 2, self.surf.get_height() // 2), radius)
        win.blit(self.surf, self.surf.get_rect(center=(self.x-(self.start[0]-pos[0]), self.y-(self.start[1]-pos[1]))))



class EffectManager:
    def __init__(self, screen, map=None) -> None:
        self.particles: list[Particle] = []  
        self.screen = screen      
        self.map = map
        self.update()
            
    def update(self):
        for particle in self.particles:
            if self.map:
                particle.update(self.screen, (self.map.x_start, self.map.y_start))
            else:
                particle.update(self.screen, (0,0))
            if particle.radius <= 0.3:
                self.particles.remove(particle)

    def add_particle(self, pos, color):
        for i in range(2):
            x, y = pos
            r = random.random()*2
            if self.map:
                f = Particle(x, y, r, (self.map.x_start, self.map.y_start), color)
            else:
                f = Particle(x, y, r, (0,0), color)
            self.particles.append(f)        
def throw(p1, p2, ratio, heigth):
    x_dist = p2[0] - p1[0]
    y_dist = p1[1] - p2[1]
    offsets = []
    offsets.append(x_dist*ratio)
    
    offsets.append(y_dist*ratio+math.sin(ratio*math.pi)*heigth)
    return offsets

if __name__ == '__main__':
    pygame.init()
    SCREEN = WIDTH, HEIGHT = 288, 512
    win = pygame.display.set_mode(SCREEN)
    pygame.mouse.set_pos((WIDTH//2, HEIGHT//2))

    show_torch = True

    running = True
    clock = pygame.time.Clock()
    FPS = 60
    p1, p2 = [50,220], [250,150]
    p = 0
    pcopy = p1.copy()
    height = 80
    manager = EffectManager(win)
    while running:
        win.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False
        offsets = throw(p1, p2, p, height)
        p += 0.01
        p%= 1
        
        pygame.draw.circle(win, (0,0,255), p1, 5)
        pygame.draw.circle(win, (255,0,0), (p1[0] + offsets[0], (p1[1] - offsets[1])), 5)
        
        pygame.draw.circle(win, (0,255,0), p2, 5)
        pos = pygame.mouse.get_pos()
        manager.add_particle((p1[0] + offsets[0], p1[1] - offsets[1]), color=Colors.FIRE.value)
        manager.update()
        # manager.update()
        # manager.add_particle(pos, ((15,94,156), (28,163,236), (116,204,244)))
        
        clock.tick(FPS)
        print(clock.get_fps())
        pygame.display.update()    