#!/usr/bin/env python
import pygame
from src.JumpingFish import JumpingFish

if __name__ == '__main__':
    fish = JumpingFish()
    fish.fly()
    pygame.quit()
    quit()
