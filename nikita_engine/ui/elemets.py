import pygame

BLACK = (0, 0, 0)



class Label:
    def __init__(self, x, y, text, size_text):
        self.pos = x, y
        self.text = text
        self.font = pygame.font.Font("res/fonts/MesloLGSNFRegular.ttf", size_text)

    def draw(self, screen : pygame.Surface):
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        #pos = text_surface.get_rect(center=self.pos)
        pos = self.pos
        screen.blit(text_surface, pos)


class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, function=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.function = function
        self.is_hovered = False
        self.font = pygame.font.Font("res/fonts/MesloLGSNFRegular.ttf", 30)

    def draw(self, screen):
        # Определяем цвет кнопки (обычный или при наведении)
        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, current_color, self.rect, border_radius=10)

        # Отрисовка текста
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event, *args):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Левая кнопка мыши
            if self.is_hovered and self.function:
                self.function(args)  # Вызов функции, если кнопка нажата

class InputBox:
    def __init__(self, x, y, width, height, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font("res/fonts/MesloLGSNFRegular.ttf", font_size)
        self.ft_size = font_size
        self.scale_modif = 1.2
        self.active = False
        self.text = '421421'
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Активация при клике
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                print("Введенный текст:", self.text)
                self.text = ''
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if self.text_surface.get_width() < self.rect.w - self.ft_size // 2:
                    self.text += event.unicode
                

    def draw(self, screen):
        r = self.rect
        rect = pygame.Rect(r.x - (self.rect.width * (self.scale_modif - 1)) // 2, r.y - (self.rect.height * (self.scale_modif - 1))// 2, int(self.rect.width * self.scale_modif), int(self.rect.height * self.scale_modif))
        pygame.draw.rect(screen, (30, 30, 30), rect, border_radius=20)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, border_radius=20)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        pos = self.rect.topleft
        screen.blit(self.text_surface, pos)


class InputBox1:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (255, 255, 255)
        self.text = text
        self.font = pygame.font.Font('res/fonts/MesloLGSNFRegular.ttf', 30)
        self.txt_surface = self.font.render(text, True, BLACK)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Активация при клике
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = ACTIVE_COLOR if self.active else GRAY
        
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                print("Введенный текст:", self.text)
                self.text = ''
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if self.txt_surface.get_width() < self.rect.w - 15:
                    self.text += event.unicode
            
            self.txt_surface = self.font.render(self.text, True, BLACK)

    def update(self):
        width = max(self.rect.w, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)