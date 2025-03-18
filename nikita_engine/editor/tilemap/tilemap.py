from .tile import TileOnPlatte, TilesOnMap
from ..editor_state import EditorState
from ..config import SCALE, TILE_SIZE
from ..enums import EditMode
import pygame

class TileMap:
    def __init__(self, images : list[str], column : int, spaces : int, pos : tuple[int, int]):
        self.tiles : list[TileOnPlatte] = []
        self.column = column
        self.spaces = spaces
        self.show = True
        for i in range(len(images)):
            x = i % self.column * self.spaces + pos[0]
            y = i // self.column * self.spaces + pos[1]
            self.tiles.append(TileOnPlatte(images[i], x, y))

    
    def draw(self, screen):
        if self.show:
            for tile in self.tiles:
                tile.draw(screen)
    
    def update(self, event, mouse_pos, editor_state : EditorState, tiles_on_map, global_pos):
        left_mouse_button = pygame.mouse.get_pressed()[0]
        if editor_state.is_clear and left_mouse_button:
            self.del_tile(tiles_on_map, (mouse_pos[0] + global_pos[0], mouse_pos[1] + global_pos[1]), editor_state)
        else:
            if editor_state.edit_mode == EditMode(1) and self.show:
                for tile in self.tiles:
                    tile.check_hover(mouse_pos)
                    tile.handle_event(event, editor_state)

            if left_mouse_button and editor_state.edit_mode == EditMode(2) and editor_state.current_surface:
                self.set_tile(tiles_on_map, (mouse_pos[0] + global_pos[0], mouse_pos[1] + global_pos[1]), editor_state)
    
    def set_tile(self, tiles_on_map : TilesOnMap, mouse_pos, editor_state : EditorState):
        pos = mouse_pos[0] // (TILE_SIZE * SCALE) * (SCALE * TILE_SIZE), mouse_pos[1] // (TILE_SIZE * SCALE) * (SCALE * TILE_SIZE)
        tiles_on_map.add_tile(pos, editor_state.current_id , editor_state.layer)

    def del_tile(self, tiles_on_map : TilesOnMap, mouse_pos, editor_state : EditorState):
        pos = mouse_pos[0] // (TILE_SIZE * SCALE) * (SCALE * TILE_SIZE), mouse_pos[1] // (TILE_SIZE * SCALE) * (SCALE * TILE_SIZE)
        tiles_on_map.del_tile(pos, editor_state.layer)