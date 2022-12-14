import pygame
import game_config as gc

from pygame import display, event, image
from time import sleep
from pygame import display, event, image
from time import sleep
from alash import alash
def find_index_from_xy(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return row, col, index
