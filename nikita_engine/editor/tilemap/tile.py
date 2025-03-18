import pygame
from engine_components.collider import SquareCollider
from ..editor_state import EditorState
from ..config import SCALE, HEIGHT, WIDTH

class Tile:
    def __init__(self, id):
        self.id = id
        img = pygame.image.load(f'res/tiles/img_{id}.png')
        self.image =  pygame.transform.scale(img, (img.get_width() * SCALE,img.get_height() * SCALE))
    
    def draw(self, screen : pygame.Surface, pos):
        screen.blit(self.image, (pos))


class TileOnPlatte:
    def __init__(self, image : str, x , y):
        self.tile_id = image.split('.')[0][-2:]
        self.surface = pygame.transform.scale(pygame.image.load(image), (
            pygame.image.load(image).get_width() * SCALE,
            pygame.image.load(image).get_height() * SCALE))
        width, height = self.surface.get_size()
        self.rect = SquareCollider(x, y, width, height)
        self.is_hovered = False

    
    def draw(self, screen : pygame.Surface):
        screen.blit(self.surface, (self.rect.x, self.rect.y))

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.dot_on_collider(mouse_pos)
    
    def handle_event(self, event, editor_state : EditorState):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered:
                editor_state.current_surface = self.surface.copy()
                editor_state.current_id = self.tile_id


class TilesOnMap:
    def __init__(self):
        self.layer_1 = {}
        self.layer_2 = {}

    def layer_to_json_format(self, layer: dict):
        lr = {}
        for key, value in layer.items():
            lr[key] = value.id
        return lr
    
    def layer_to_normal_format(self, layer:dict):
        lr = {}
        for key, value in layer.items():
            lr[key] = Tile(value)
        return lr

    def get_layers_to_json_format(self):
        self.layer_to_json_format(self.layer_1)
        return [self.layer_to_json_format(self.layer_1), self.layer_to_json_format(self.layer_2)]
    
    def load_layers_to_normal_format(self, layers):
        if layers:
            self.layer_1 = self.layer_to_normal_format(layers[0])
            self.layer_2 = self.layer_to_normal_format(layers[1])

    def add_tile(self, pos, tile_id, layer):
        if layer == 1:
            self.__add_tile_on_layer(pos, tile_id, self.layer_1)
        elif layer == 2:
            self.__add_tile_on_layer(pos, tile_id, self.layer_2)
    
    def del_tile(self, pos, layer):
        if layer == 1:
            self.__del_tile_on_layer(pos, self.layer_1)
        elif layer == 2:
            self.__del_tile_on_layer(pos, self.layer_2)
    

    def draw(self, screen : pygame.Surface, global_pos):
        self.__draw_tiles(screen, self.layer_1, global_pos)
        self.__draw_tiles(screen, self.layer_2, global_pos)
    
    def __draw_tiles(self, screen : pygame.Surface ,layer : dict, global_pos):
        for pos, tile in layer.items():
            if tile and global_pos[0] - 20 * SCALE  <= pos[0] <= WIDTH + global_pos[0] + 10 * SCALE and global_pos[1] - 20 * SCALE  <= pos[1] <= HEIGHT + global_pos[1] + 10 * SCALE:
                tile.draw(screen, (pos[0] - global_pos[0], pos[1] - global_pos[1]))

    def __add_tile_on_layer(self, pos, tile_id, layer : dict):
        if pos in layer:
            layer[pos] = Tile(tile_id)
        else:
            layer[pos] = Tile(tile_id)
    
    def __del_tile_on_layer(self, pos, layer : dict):
        if pos in layer:
            layer.pop(pos)