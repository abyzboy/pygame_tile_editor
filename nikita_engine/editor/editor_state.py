import pygame
from .enums import EditMode
class EditorState:
    def __init__(self):
        self.current_surface : pygame.Surface = None
        self.current_id = 0
        self.edit_mode = EditMode(1)
        self.layer = 1
        self.is_clear = False