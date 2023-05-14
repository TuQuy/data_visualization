import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Một lớp học để quản lý con tàu."""
    def __init__(self, ai_game):
        """Khởi tạo con tàu và thiết lập vị trí bắt đầu của nó."""
        super().__init__()
        self.screen = ai_game.screen #1
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() #2 truy cập thuộc tính hình chữ nhậkt của màn hình bằng phương thức get_rect()
        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp') #3
        self.rect = self.image.get_rect()
        # Bắt đầu mỗi con tàu mới ở giữa dưới cùng của màn hình
        self.rect.midbottom = self.screen_rect.midbottom #4
        self.x = float(self.rect.x)
        #Movement flag
        self.moving_right = False #1
        self.moving_left = False

    def update(self): #2
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Việc sử dụng 2 if thay vì elif cho phép con tàu sẽ đứng yên thay vì nó sẽ tự ưu tiên di chuyển sang phải nếu nhấn 2 phím cùng lúc

        self.rect.x = self.x

    def blitme(self): #5
        """Vẽ con tàu tại vị trí hiện tại của nó."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)