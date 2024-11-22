import os 
import pytmx
import pygame
cwd = os.path.dirname(os.path.dirname(__file__))


class Pytmx:
    def __init__(self, win):
        self.win = win
        self.data_tmx = pytmx.load_pygame(os.path.join(cwd, "assets", "map", "map.tmx"))
        self.zoom = 3
        self.x_start, self.y_start = 500, -500

        self.zoomed_tile_width = self.data_tmx.tilewidth * self.zoom
        self.zoomed_tile_height = self.data_tmx.tileheight * self.zoom

        self.free_places: list[tuple[int, int]] = []

        for k, v in enumerate(self.data_tmx.images):
            if not v:
                continue
            self.data_tmx.images[k] = pygame.transform.scale(v, (
                int(v.get_width() * self.zoom), int(v.get_height() * self.zoom)))

        self.load_free_places()

    def load_free_places(self):
        for layer in self.data_tmx.visible_layers:
            for j, i, gid in layer:
                if gid == 2:
                    self.free_places.append((j + 1, i))  # Fix to make it look better
        

    def ortho_to_iso(self, j: int, i: int) -> tuple[float, float]:
        return ((j - i) * self.zoomed_tile_width / 2 + self.x_start,
                (j + i) * self.zoomed_tile_height / 2 + self.y_start)

    def iso_to_ortho(self, x, y) -> tuple[int, int]:
        j = int((x - self.x_start) / self.zoomed_tile_width + (y - self.y_start) / self.zoomed_tile_height)
        i = int((y - self.y_start) / self.zoomed_tile_height - (x - self.x_start) / self.zoomed_tile_width)
        return j, i

    def draw(self, win):
        for layer in self.data_tmx.visible_layers:
            for j, i, gid in layer:
                tile = self.data_tmx.get_tile_image_by_gid(gid)
                if tile:
                    win.blit(tile, self.ortho_to_iso(j, i))
