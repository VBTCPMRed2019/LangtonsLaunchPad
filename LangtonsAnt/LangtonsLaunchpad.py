import pygame as pg
import AntMod
import Images
from time import sleep as wait
from random import randint as random
import LaunchPad

# Initializes Window
pg.init()
display = (512, 512)
game = pg.display.set_mode(display)
pg.display.set_caption("Langton's Ant")

# Grid Variables
TilesPos = {}


# Initialize Ant
Ant = AntMod.Ant()


# Initialize Images
Images = Images.Images()


# Grid Functions
def load_grid():
    for i in range(8):
        for j in range(8):
            x = (i * 64)
            y = (j * 64)
            game.blit(Images.Tile[0], (x, y))
            TilesPos[x,"x",y] = Images.Tile[0]
    pg.display.update()
    
# Loading Functions
load_grid()
Ant.load(game, Images.Tile[0])

# The main loop where all the other modules are executed. 
while True:
    AtoTpos = Ant.curpos['x'], "x", Ant.curpos['y']
    if TilesPos[AtoTpos] == Images.Tile[0] or TilesPos[AtoTpos] == Images.Tile[2]:
        Ant.move('l')
        TilesPos[AtoTpos] = Images.Tile[1]
        Ant.load(game = game, image = Images.Tile[1])
    elif TilesPos[AtoTpos] == Images.Tile[1]:
        Ant.move('r')
        TilesPos[AtoTpos] = Images.Tile[2]
        Ant.load(game = game, image = Images.Tile[2])
    #LaunchPad.writeMidi(Ant)
    LaunchPad.writeMidi2(Ant)
    pg.display.update()
    wait(0)
