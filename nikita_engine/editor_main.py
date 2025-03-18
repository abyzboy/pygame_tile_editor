import pygame
from editor.config import SCALE, HEIGHT, WIDTH
from editor.tilemap.tilemap import TileMap
from editor.tilemap.tile import TilesOnMap
from editor.editor_state import EditorState
from editor.enums import EditMode
from editor.editor_func import save_level, load_level
from ui.elemets import Label, Button, InputBox, InputBox1
import os

print('Instructions: KEY 1: Change editor select modes '
'\nKEY 2:show - hide tile-pallete'
'\nKEY 3: change 1 or 2 layer'
'\nKEY S: save level')

inp = int(input("Введите число уровня, если новый уровень введите -1 "))

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


tiles = [f'res/tiles/{pth}' for pth in os.listdir('res/tiles/')]
tile_map = TileMap(tiles, 6, 16 * SCALE, (0, 400))
tiles_on_map = TilesOnMap()
tiles_on_map.load_layers_to_normal_format(load_level(inp))
editor_state = EditorState()

editor_mode_label = Label(0, 0, str(editor_state.edit_mode),30)
current_layer_label = Label(0, 40, "Layer: 1", 30)

running = True

global_pos = [0, 0]

show_save_menu = False

inp = ''

is_clear = False

while running:
    mouse_pos = pygame.mouse.get_pos()
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if editor_state.edit_mode == EditMode(1): 
                    editor_state.edit_mode = EditMode(2)
                elif editor_state.edit_mode == EditMode(2): 
                    editor_state.edit_mode = EditMode(1)
                editor_mode_label.text = str(editor_state.edit_mode)

            if event.key == pygame.K_2:
                tile_map.show = not tile_map.show
            
            if event.key == pygame.K_3:
                if editor_state.layer == 1: editor_state.layer = 2
                elif editor_state.layer == 2: editor_state.layer = 1
                current_layer_label.text = f"Layer: {editor_state.layer}"

            if event.key == pygame.K_4:
                editor_state.is_clear = not editor_state.is_clear
                print('clear', editor_state.is_clear)

            if event.key == pygame.K_s:
                inp = int(input('Введите число уровня '))
                save_level(tiles_on_map.get_layers_to_json_format(), inp)
                print('level save')
        tile_map.update(event, mouse_pos, editor_state, tiles_on_map, global_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: global_pos[0] -= 5
    if keys[pygame.K_RIGHT]: global_pos[0] += 5
    if keys[pygame.K_UP]: global_pos[1] -= 5
    if keys[pygame.K_DOWN]: global_pos[1] += 5
    tiles_on_map.draw(screen, global_pos)

    tile_map.draw(screen)

    if editor_state.current_surface:
        screen.blit(editor_state.current_surface, (mouse_pos[0] - editor_state.current_surface.get_size()[0] // 2, 
                                                   mouse_pos[1] - editor_state.current_surface.get_size()[1] // 2))

    editor_mode_label.draw(screen)
    current_layer_label.draw(screen)

    pygame.display.flip()
    clock.tick(144)

pygame.quit()