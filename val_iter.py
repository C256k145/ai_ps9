import math  
from random import random

def worldBuilder():
    x = -.04
    world = [[x,x,x], [x,x,x], [x,x,x], [x,-1,1]]
    return world

def main():
    world = worldBuilder()
    start_pos = [1,1]
    pos = update(start_pos, world)

    

main()