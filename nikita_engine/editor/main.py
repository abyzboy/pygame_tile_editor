# Example file showing a basic pygame "game loop"
import pygame
from .config import SCALE
from .tilemap.tilemap import TileMap
from .tilemap.tile import TilesOnMap
from .editor_state import EditorState
from .enums import EditMode
import os

layer = 1
tiles = [f'res/tiles/{pth}' for pth in os.listdir('res/tiles/')]
tile_map = TileMap(tiles, 6, 16 * SCALE, (300, 300))
tiles_on_map_layer_1 = TilesOnMap()
tiles_on_map_layer_2 = TilesOnMap()
editor_state = EditorState()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    screen.fill("green")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if editor_state.edit_mode == EditMode(1): editor_state.edit_mode = EditMode(2)
                elif editor_state.edit_mode == EditMode(2): editor_state.edit_mode = EditMode(1)
                print(editor_state.edit_mode)

            if event.key == pygame.K_2:
                tile_map.show = not tile_map.show
            
            if event.key == pygame.K_3:
                if layer == 1: layer = 2
                elif layer == 2: layer = 1
                print(f'Layer : {layer}')

        if layer == 1: tile_map.update(event, mouse_pos, editor_state, tiles_on_map_layer_1)
        if layer == 2: tile_map.update(event, mouse_pos, editor_state, tiles_on_map_layer_2)

    tiles_on_map_layer_1.draw(screen)
    tiles_on_map_layer_2.draw(screen)

    tile_map.draw(screen)

    if editor_state.current_surface:
        screen.blit(editor_state.current_surface, (mouse_pos[0] - editor_state.current_surface.get_size()[0] // 2, 
                                                   mouse_pos[1] - editor_state.current_surface.get_size()[1] // 2))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()