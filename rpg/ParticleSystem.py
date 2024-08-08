import pygame
import random


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
    def __init__(self, screen, map) -> None:
        self.particles: list[Particle] = []  
        self.screen = screen      
        self.map = map
        self.update()
            
    def update(self):
        for particle in self.particles:
            particle.update(self.screen, (self.map.x_start, self.map.y_start))
            if particle.radius <= 0.3:
                self.particles.remove(particle)

    def add_particle(self, pos, color):
        for i in range(2):
            x, y = pos
            r = random.random()*2
            f = Particle(x, y, r, (self.map.x_start, self.map.y_start), color)
            self.particles.append(f)        

if __name__ == '__main__':
    pygame.init()
    SCREEN = WIDTH, HEIGHT = 288, 512
    win = pygame.display.set_mode(SCREEN)
    pygame.mouse.set_pos((WIDTH//2, HEIGHT//2))

    show_torch = True

    running = True
    clock = pygame.time.Clock()
    FPS = 60

    manager = EffectManager(win)
    while running:
        win.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False
                
        pos = pygame.mouse.get_pos()
        manager.update()
        manager.add_particle(pos, ((15,94,156), (28,163,236), (116,204,244)))
        
        clock.tick(FPS)
        pygame.display.update()    