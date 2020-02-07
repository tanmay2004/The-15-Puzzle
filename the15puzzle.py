# Created by Tanmay Garg

import pygame
from pygame.locals import *
import random
import time
import math

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((598,598))
screen.fill((0,0,0))
pygame.display.set_caption("Arrange the Numbers!")
font = pygame.font.Font('fonts/Adca.ttf', 35)
clock = pygame.time.Clock()
victory = pygame.mixer.Sound("sounds/TaDa.ogg")

RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)

class Tile(object):
    def __init__(self, num, x, y):
        self.number = num
        self.x = x
        self.y = y
        self.width = 99
        self.height = 99
        
    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height), 0)
        text = font.render(str(self.number), True, WHITE)
        textRect = text.get_rect(center=((2*self.x+self.width)/2, (2*self.y+self.height)/2))
        screen.blit(text, textRect)
        
    def moveIt(self, dist):
        final_x = self.x + dist[0]
        final_y = self.y + dist[1]
        
        while self.x != final_x or self.y != final_y:
            screen.fill(WHITE, [self.x, self.y, 99, 99])
            self.x += int(dist[0]/50)
            self.y += int(dist[1]/50)
            self.draw()
            pygame.display.update()

        clock.tick(60)

def count_inversions(num_order):
  inversions = 0
  for i in range(len(num_order)-1):
    for k in range(i+1, len(num_order)):
      if num_order[i] > num_order[k]:
        inversions += 1
  return inversions

def moves_display(mytext):
    txt = font.render(mytext, True, WHITE)
    textRect = txt.get_rect(center=(299, 550))
    screen.blit(txt, textRect)

def show_congrats():
    txt = font.render("Congratulations! You did it!", True, GREEN)
    textRect = txt.get_rect(center=(299, 49))
    screen.blit(txt, textRect)
    finalTile = Tile(16, empty_x, empty_y)
    finalTile.draw()
    pygame.display.update()
    print("\nYou solved it! Game window closing in 10 seconds....")

corret_matches = [[100, 100, 1], [200, 100, 2], [300, 100, 3], [400, 100, 4], [100, 200, 5], [200, 200, 6], [300, 200, 7], [400, 200, 8], [100, 300, 9], [200, 300, 10], [300, 300, 11], [400, 300, 12], [100, 400, 13], [200, 400, 14], [300, 400, 15]]

def detectWin():
    for tile in listOfTiles:
        curr_arrangement = [tile.x, tile.y, tile.number]
        if curr_arrangement not in corret_matches:
            return False        
    return True

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
random.shuffle(nums)

while count_inversions(nums) % 2 != 0:
  random.shuffle(nums)

listOfTiles = []
move_counter = 0
index = 0

pygame.draw.rect(screen, WHITE, (98, 98, 403, 403))
for y in range(100, 500, 100):
    for x in range(100, 500, 100):
        if index < 15:
            da_num = nums[index]
            newTile = Tile(da_num, x, y)
            listOfTiles.append(newTile)
            newTile.draw()
            index += 1
            
empty_x = 400
empty_y = 400

pygame.display.update()

running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        elif event.type == MOUSEBUTTONDOWN:
            this_pos = pygame.mouse.get_pos()
            
            x = int(math.floor(this_pos[0] / 100.0)) * 100
            y = int(math.floor(this_pos[1] / 100.0)) * 100
            
            li = [(empty_x - x), (empty_y - y)]
            if 0 in li and (100 in li or -100 in li):
                for tile in listOfTiles:
                    if tile.x == x and tile.y == y:
                        move_counter += 1
                        empty_x = tile.x
                        empty_y = tile.y
                        tile.moveIt(li)
    
        elif event.type == KEYDOWN:
            arrows = [K_LEFT, K_RIGHT, K_UP, K_DOWN]
            
            if event.key == K_ESCAPE:
                running = False
            
            elif event.key in arrows:
                xy_dist = [None, None]
                
                if event.key == K_LEFT:
                    xy_dist = [-100, 0]
                if event.key == K_RIGHT:
                    xy_dist = [100, 0]
                if event.key == K_UP:
                    xy_dist = [0, -100]
                if event.key == K_DOWN:
                    xy_dist = [0, 100]

                for tile in listOfTiles:
                    if tile.x + xy_dist[0] == empty_x and tile.y + xy_dist[1] == empty_y:
                        move_counter += 1
                        empty_x = tile.x
                        empty_y = tile.y
                        tile.moveIt(xy_dist)
                        break

    screen.fill(BLACK, [200, 515, 200, 85])
    moves_display("Moves: " + str(move_counter))
    pygame.display.update()
    clock.tick(60)
    
    if detectWin() == True:
        show_congrats()
        victory.play()
        running = False
        time.sleep(10)

pygame.quit()

# https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html
# https://www.instructables.com/id/How-To-Solve-The-15-Puzzle/
# https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/
# https://www.pygame.org/docs/ref/key.html
# http://jamie-wong.com/2011/10/16/fifteen-puzzle-algorithm/