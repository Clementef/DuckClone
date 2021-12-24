import pygame


class GAME:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.size = 800
        self.half = self.size/2
        self.fps = 60
        self.inter = pygame.surface.Surface((self.size, self.size))
        self.inpos = [0, 0]
        self.back = (255, 255, 255)
        self.states = {'main':self.main}
        self.context = 'main'

    def init(self):
        pygame.init()
        display = (self.size, self.size)
        self.screen = pygame.display.set_mode(display)
        pygame.display.set_caption("")

    def run(self):
        GAME.init(self)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.clock.tick(self.fps)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                quit()
            self.states[self.context]()
            self.screen.blit(self.inter, self.inpos)
            self.inter.fill(self.back)
            pygame.display.update()

    def text(self, msg, pos, color=[10, 136, 199], back=[255,255,255], size=16, font='freesansbold'):
        font = pygame.font.SysFont(font, size)
        tx = font.render(msg, True, color, back)
        rect = tx.get_rect()
        rect.center = pos
        self.inter.blit(tx, rect)

    def main(self):
        pass
