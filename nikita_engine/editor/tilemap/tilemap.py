from .tile import Tile, TilesOnMap
from ..editor_state import EditorState
from ..config import SCALE, TILE_SIZE
from ..enums import EditMode
import pygame

class TileMap:
    def __init__(self, images : list[str], column : int, spaces : int, pos : tuple[int, int]):
        self.tiles : list[Tile] = []
        self.column = column
        self.spaces = spaces
        self.show = True
        for i in range(len(images)):
            x = i % self.column * self.spaces + pos[0]
            y = i // self.column * self.spaces + pos[1]
            self.tiles.append(Tile(images[i], x, y))

    
    def draw(self, screen):
        if self.show:
            for tile in self.tiles:
                tile.draw(screen)
    
    def update(self, event, mouse_pos, editor_state : EditorState, tiles_on_map):
        if editor_state.edit_mode == EditMode(1) and self.show:
            for tile in self.tiles:
                tile.check_hover(mouse_pos)
                tile.handle_event(event, editor_state)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and editor_state.edit_mode == EditMode(2):
            self.set_tile(tiles_on_map, mouse_pos, editor_state.current_id)
    
    def set_tile(self,tiles_on_map : TilesOnMap, mouse_pos, tile_id):
        pos = mouse_pos[0] // (TILE_SIZE * SCALE) * (SCALE * TILE_SIZE), mouse_pos[1] // (TILE_SIZE * SCALE) * (SCALE * TILE_SIZE)
        print(pos)
        print(mouse_pos)
        tiles_on_map.append(pos, tile_id)
