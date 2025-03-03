import pygame
from engine_components.collider import SquareCollider
from ..editor_state import EditorState
from ..config import SCALE

class Tile:
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
                print(self.tile_id)


class TilesOnMap:
    def __init__(self):
        self.d = {}

    def append(self, pos, tile_id):
        if pos in self.d:
            self.d[pos] = tile_id
        else:
            self.d[pos] = tile_id
    
    def draw(self, screen : pygame.Surface):
        for pos, tile_info in self.d.items():
            img = find_img(tile_info)
            screen.blit(img, pos)
            
def find_img(id):
    image = pygame.image.load(f'res/tiles/img_{id}.png')
    return pygame.transform.scale(image, (image.get_width() * SCALE,image.get_height() * SCALE))