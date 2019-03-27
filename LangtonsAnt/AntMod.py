import pygame as pg
import Images

Images = Images.Images()

class Ant:   
    def __init__(self, startpos = {'x' : 0, 'y' : 0}, startframe = Images.Ant[0]):
        self.frame = startframe
        self.curpos = startpos
        self.curdir = self.frame
        self.prevdir = self.curdir
        self.prevpos = self.curpos
        self.turns = 0

    def move(self, direction):
        self.prevpos = self.curpos.copy()
        self.prevdir = self.curdir
        
        # Direction Fixing WORKS.
                
        if direction == 'l':
            print('turn left')
            if self.prevdir == Images.Ant[3]:
                self.curdir = Images.Ant[0]
            elif self.prevdir == Images.Ant[2]:
                self.curdir = Images.Ant[3]
            elif self.prevdir == Images.Ant[1]:
                self.curdir = Images.Ant[2]
            elif self.prevdir == Images.Ant[0]:
                self.curdir = Images.Ant[1]
        elif direction == 'r':
            print('turn right')
            if self.prevdir == Images.Ant[3]:
                self.curdir = Images.Ant[2]
            elif self.prevdir == Images.Ant[2]:
                self.curdir = Images.Ant[1]
            elif self.prevdir == Images.Ant[1]:
                self.curdir = Images.Ant[0]
            elif self.prevdir == Images.Ant[0]:
                self.curdir = Images.Ant[3]
        self.frame = self.curdir

        # Move The Ant ISSUE SOMEWHERE.
        if self.curdir == Images.Ant[0]:
            print('up')
            if self.curpos['y'] != 448:
                self.curpos['y'] += 64
            else:
                self.curpos['y'] = 0
        elif self.curdir == Images.Ant[1]:
            print('left')
            if self.curpos['x'] != 0:
                self.curpos['x'] -= 64
            else:
                self.curpos['x'] = 448
        elif self.curdir == Images.Ant[2]:
            print('down')
            if self.curpos['y'] != 0:
                self.curpos['y'] -= 64
            else:
                self.curpos['y'] = 448
        elif self.curdir == Images.Ant[3]:
            print('right')
            if self.curpos['x'] != 448:
                self.curpos['x'] += 64
            else:
                self.curpos['x'] = 0
        print(self.curpos['x'], 'x', self.curpos['y'])

    def load(self, game, image):
        game.blit(self.frame, (self.curpos['x'], self.curpos['y']))
        if self.turns > 0:
            game.blit(image, (self.prevpos['x'], self.prevpos['y']))
        self.turns += 1
        print(self.turns)
