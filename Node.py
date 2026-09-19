import pygame

WHITE = (255,255,255)
BLACK = (000,000,000)
RED = (255,000,000)
GREEN = (000,255,000)
BLUE = (000,000,255)
YELLOW = (255,255,000)
PURPLE = (128, 0, 128)

class create_node:
    def __init__(self, row, col, width, all_rows):
        self.row = row
        self.col = col

        self.x = row * width
        self.y = col * width

        self.width = width
        self.all_rows = all_rows

        self.color = WHITE
        self.neighbor = []
    
    def get_position(self):
        return self.row, self.col

    def draw(self, screen):
        #draw a cube in screen
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    #chack color
    def is_empty(self):
        return self.color == WHITE
    def is_wall(self):
        return self.color == BLACK
    def is_start(self):
        return self.color == YELLOW
    def is_end(self):
        return self.color == PURPLE
    def is_path(self):
        return self.color == BLUE
    def is_currenly_visit(self):
        return self.color == GREEN
    def is_visited(self):
        return self.color == RED

    #Set color
    def set_visited(self):
        self.color = RED
    def set_empty(self):
        self.color = WHITE
    def set_wall(self):
        self.color = BLACK
    def set_start(self):
        self.color = YELLOW
    def set_end(self):
        self.color = PURPLE
    def set_path(self):
        self.color = BLUE
    def set_currenly_visit(self):
        self.color = GREEN

    def __lt__(self, other_node): # function for compare Node
        pass

