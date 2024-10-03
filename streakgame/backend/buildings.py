import pygame
from pygame import Vector2
import time
import datetime
import pytmx
import pyscroll
import os
from scripts.utils import convert_float_to_int_if_possible, scale_down_surface
import xml.etree.ElementTree as ET
from streakgame.backend import objects
from streakgame.backend.inventory import Inventory
from streakgame.backend.items import Item
from streakgame.boring import config
from streakgame.boring import imgs, utils, colors
from typing import Optional
from streakgame.boring.config import ratio
cwd = os.path.dirname(os.path.dirname(__file__))

class Building(Item):
    def __init__(self, object, img=pygame.Surface((32,32)), size=None):
        img = img.copy()
        if size:
            img.blit(img ,(0,0),img.get_bounding_rect())
            # img = scale_down_surface(img, *size)
            img = pygame.transform.scale(img, size)
        super().__init__(object.name, img)
        self.id = object.id
        self.name = object.name
        self.gid = object.gid
        self.object = object
        self.img_gray_scale = utils.grayscale(img)

        self.cache = {}

    def update_camera(self, camera_rect):
        super().update_camera(camera_rect)
        zoom = self.zoom_buffer.get_width() / self.img.get_width()
        if zoom not in self.cache:
            self.img_gray_scale = utils.grayscale(self.zoom_buffer)
            self.cache[zoom] = self.img_gray_scale
        else:
            self.img_gray_scale = self.cache[zoom]

class BuildingsMenu(objects.GameObjectNoImg):
    def __init__(self, game, size, buildings, pytmx, obj, maxratio=1.8):
        x_menu = game.win.get_width()/2
        y_menu = game.win.get_height()/2
        self.game = game
        self.buildings: list[Building] = buildings
        mratio = 0
        for building in self.buildings:
            mratio = max(mratio, building.img.get_height()/building.img.get_width())
        
        pos = (x_menu-size[0]/2, y_menu-(size[1]*min(mratio, maxratio))/2)
        super().__init__(Vector2(pos), (size[0], size[1]*min(mratio, maxratio)))
        self.is_open = False
        self.pytmx = pytmx
        self.hovered = False
        self.hovered_item_index = -1
        self.obj = obj

        self.item_size = -1  # will be calculated in update_buildings_rect
        self.item_padding = 10
        self.finished = False

        self.buildings_rects: list[pygame.Rect] = []
        self.selected_building = None
        self.rows = 1
        self.inventory = None

        self.update_buildings_rect()

    def link_inventory(self, inventory):
        self.inventory = inventory

    def update_buildings_rect(self):
        self.buildings_rects = []
        self.item_size = (self.rect.width - (len(self.buildings) + 1) * self.item_padding) // len(self.buildings), (self.rect.height*0.9)/self.rows
        y = self.rect.y + (self.rect.height - self.item_size[1]) // 2

        for i, item in enumerate(self.buildings):
            self.buildings_rects.append(
                pygame.Rect((self.rect.x + self.item_padding + i * (self.item_size[0] + self.item_padding), y),(self.item_size[0], self.item_size[1])))
                
            self.buildings[i] = Building(item.object, item.img, size=self.item_size)

    def add_item(self, item):
        self.buildings.append(item)

    def update_camera(self, camera_rect):
        objects.GameObjectNoImg.update_camera(self, camera_rect)
        for i, item in enumerate(self.buildings):
            item.update_camera(camera_rect)
        self.update_buildings_rect()

    def replace_buildings(self):
        for obj_layer in self.pytmx.data_tmx:
            if obj_layer.name == "Objects":
                for obj in obj_layer.copy():
                    self.path = os.path.join(cwd, "assets", "map", "map_with_objects.tmx")
                    tree = ET.parse(self.path)
                    self.root = tree.getroot()
                    for objectgroup in self.root.findall('objectgroup'):
                        for obj in objectgroup.findall('object'):
                            if 'gid' in obj.attrib and 'type' in obj.attrib and obj.attrib['type'] != 'Farm':
                                obj_dict = {'id' :str(self.obj.id), 'name':self.obj.name, 'type':self.obj.type, 'gid':str(self.obj.gid), 'width':str(convert_float_to_int_if_possible(self.obj.width)), 'height':str(convert_float_to_int_if_possible(self.obj.height))}
                                attrib = obj.attrib.copy()
                                del attrib['x']
                                del attrib['y']
                                diff = {key:(attrib[key], obj_dict[key])  for key in attrib if attrib[key] != obj_dict[key]}
                                if 'building'.lower() in attrib['type'].lower():
                                    print(attrib)
                                if len(list(diff.keys())) < 2:
                                    for object in objectgroup.findall('object'):
                                        if object.attrib['name'] == self.selected_building.name:gid=object.attrib['gid']
                                    print(obj.attrib)
                                    obj.attrib['name'] = self.selected_building.name
                                    obj.attrib['gid'] = str(gid)
                                    obj.attrib['width'] = str(self.selected_building.object.width)
                                    obj.attrib['height'] = str(self.selected_building.object.height)
                                    # obj.attrib['gid'] = str(self.selected_building.gid)
                                        
        tree.write(self.pytmx.path)
        # for obj_layer in self.pytmx.data_tmx:
        #     if obj_layer.name == "Objects":
        #         for obj in obj_layer:
        #             if obj.type == "Farm":
        #                 pass
        #             else:
        #                 obj.id = self.selected_building.id
        # self.data_tmx = pytmx.load_pygame(self.pytmx.path)
        # pyscroll_data = pyscroll.data.TiledMapData(self.pytmx.data_tmx)
        # self.pytmx.map_layer = pyscroll.BufferedRenderer(pyscroll_data, self.pytmx.win.get_size(), clamp_camera=True, zoom=self.pytmx.zoom_target)
        # self.pytmx.update(0)
        # self.pytmx.handle_events([])
        self.game.building_names[self.game.building_names.index(self.selected_building.name)] = self.obj.name

        
                        

    def handle_events(self, events):
        for event in events:
            for i, item in enumerate(self.buildings):
                if self.buildings_rects[i].collidepoint(pygame.mouse.get_pos()):
                    self.hovered_item_index = i
                    break
                else:
                    self.hovered_item_index = -1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.is_open = not self.is_open
                else:
                    self.is_open = False
                # Check if an item is clicked
                for i, item in enumerate(self.buildings):
                    if self.buildings_rects[i].collidepoint(event.pos):
                        self.selected_building = item
                        return
        selected_building= self.selected_building
        # objects.Clickable.handle_events(self, events)
        was_open = self.is_open
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos
                if self.hovered_item_index >= 0:
                    self.is_open = True
        if self.is_open and was_open:
            if pygame.mouse.get_pressed(3)[0]:
                if selected_building is not None:
                    pos = list(pygame.mouse.get_pos())
                    pos[0] *= ratio
                    pos[1] *= ratio
                    self.finished = True
                    self.replace_buildings()

    def draw(self, win):
        # draw inventoryUI background slightly transparent black with white border
        utils.draw_menu_rect(win, self.rect, colors.MENU_BACKGROUND)
        for i, item in enumerate(self.buildings):
            if self.hovered_item_index == i:
                pygame.draw.rect(win, colors.MENU_SELECTED, self.buildings_rects[i].inflate(10, 10), border_radius=10)
            img = item.zoom_buffer
            win.blit(img, (self.buildings_rects[i].centerx-(img.get_width()-img.get_bounding_rect()[0])/2,self.buildings_rects[i].centery-(img.get_height()-img.get_bounding_rect()[1])/2))
