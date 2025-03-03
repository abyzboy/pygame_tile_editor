from engine_components.transform import Transform

class Shape:
    def dot_on_shape(self, other_pos) -> bool:
        pass


class SquareCollider(Shape):
    def __init__(self, x : int, y : int, width : int, height : int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.width

    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y + self.height

    def dot_on_collider(self, other_pos) -> bool:
        """Проверяет лежит ли точка на коллайдере."""
        return (
            self.left <= other_pos[0] <= self.right and
            self.top <= other_pos[1] <= self.bottom
        )
    
    def collides_with_rect(self, other):
        """Проверяет столкновение с другим прямоугольником."""
        return not (
            self.right < other.left or
            self.left > other.right or
            self.bottom < other.top or
            self.top > other.bottom
        )