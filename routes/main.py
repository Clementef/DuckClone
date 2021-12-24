import pygame
from .pygobj import GAME

class DUCK(GAME):
    def __init__(self):
        GAME.__init__(self)
        self.num_squares = 30
        self.factor = self.size/self.num_squares
        self.board = [[0 for i in range(self.num_squares)] for j in range(self.num_squares)]

        self.player_position = [self.size/2,self.size/2]
        self.player_size = [self.factor,self.factor]
        self.player_input = [0,0]
        self.player_velocity = [0,0]
        self.player_acceleration = [0,0]
        self.player_max_speed = 20
        self.player_acceleration_rate=.5
        self.player_friction = .9
    def main(self):
        self.r = False
        self.start = True
        self.player_input = [0,0]
        keys = pygame.key.get_pressed()
        self.player_input[0] += keys[pygame.K_d]-keys[pygame.K_a]
        self.player_input[1] += keys[pygame.K_s]-keys[pygame.K_w]
        # if keys[pygame.K_w]:
        #     self.player_input[1]-=1
        # if keys[pygame.K_s]:
        #     self.player_input[1]+=1
        # if keys[pygame.K_a]:
        #     self.player_input[0]-=1
        # if keys[pygame.K_d]:
        #     self.player_input[0]+=1
        self.player_acceleration[0]=self.player_input[0]*self.player_acceleration_rate
        self.player_acceleration[1]=self.player_input[1]*self.player_acceleration_rate

        self.player_velocity[0] += self.player_acceleration[0]
        self.player_velocity[1] += self.player_acceleration[1]

        self.player_position[0]+=max(-self.player_max_speed,min(self.player_velocity[0],self.player_max_speed))
        self.player_position[1]+=max(-self.player_max_speed,min(self.player_velocity[1],self.player_max_speed))

        self.player_velocity[0]*=self.player_friction
        self.player_velocity[1]*=self.player_friction
        self.update()
        pygame.draw.rect(self.inter,[0,0,255],[self.player_position[0]-(self.player_size[0]/2),self.player_position[1]-(self.player_size[1]/2),self.player_size[0],self.player_size[1]+10])
        pygame.draw.rect(self.inter,[0,255,0],[self.player_position[0]-(self.player_size[0]/2),self.player_position[1]-(self.player_size[1]/2),self.player_size[0],self.player_size[1]])

    def reset(self):
        self.board = [[0 for i in range(self.num_squares)] for j in range(self.num_squares)]

    def update(self):
        for i in range(self.num_squares):
            pygame.draw.line(self.inter,[0,0,0], (0,self.factor*i), (self.size,self.factor*i))
        for i in range(self.num_squares):
            pygame.draw.line(self.inter,[0,0,0], (self.factor*i, 0), (self.factor*i, self.size))
        if self.r:
            self.reset()
            self.r = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP_ENTER]:
            self.r = True
        if not keys[pygame.K_LSHIFT] and not keys[pygame.K_s]:
            self.save_check = True
        press = pygame.mouse.get_pressed()
        print(self.board)
        for i, k in enumerate(self.board):
            for j, v in enumerate(k):
                if v:
                    pygame.draw.rect(self.inter, [255, 0, 0], [self.factor*i+1, self.factor*j+1, self.factor, self.factor])
        if press[0]:
            locx, locy = pygame.mouse.get_pos()
            ex = locx%self.factor
            ey = locy%self.factor
            px = locx - ex
            py = locy - ey
            pygame.draw.rect(self.inter, [255,0,0], ((px, py), (self.factor, self.factor)))
            lsx = int(px/self.factor)
            lsy = int(py/self.factor)
            self.board[lsx][lsy] = 1
        if press[2]:
            locx, locy = pygame.mouse.get_pos()
            ex = locx%self.factor
            ey = locy%self.factor
            px = locx - ex
            py = locy - ey
            pygame.draw.rect(self.inter, [0,0,0], ((px, py), (self.factor, self.factor)))
            lsx = int(px/self.factor)
            lsy = int(py/self.factor)
            self.board[lsx][lsy] = 0
