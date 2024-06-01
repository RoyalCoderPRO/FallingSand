from itertools import repeat
import os
import time
import random

os.system('cls')

framerate = 0.1
n = 10 # Rank of square matrix
matrix = [[0 for j in repeat(None,n)] for i in repeat(None, n)] # Makes a nxn matrix filled with 0

class Particle:
    def __init__ (self, posx, posy):
        self.name = self # Just to change attributes like pos of particle externally (No use yet)
        while matrix[posy-1][posx-1] == 1: # Loop to check if position is occupied
            posx = int(random.randrange(0,n))
            posy = int(random.randrange(0,n))    
        
        self.x = int(posx)-1 # Assigns new position to particle
        self.y = int(posy)-1
        matrix[self.y][self.x] = 1 # Puts a 1 in position of particle in the matrix
        printer() # Prints a fresh output of matrix
        try:
            while matrix[self.y + 1][self.x] == 0: # Checks if position below is empty
                matrix[self.y + 1][self.x] = 1 # Replaces position below
                matrix[self.y][self.x] = 0 # Makes previous position empty
                self.y += 1 # Changes particle position attribute
                printer() # Prints change
            printer() # Prints once after no empty space below
        except:
            pass
        
            
    
def printer():
    os.system('cls') # Clears output
    print(*matrix, sep='\n')
    time.sleep(framerate) 

def rand_particle_gen(count): # Generates a particle at random position in nxn matrix
    for i in range(0, count):
        exec(f'particle_{i} = Particle({random.randrange(1,n)},{random.randrange(1,n)})')
        
        
 # Randomly spawns 45 particles
rand_particle_gen(48)
test_particle = Particle(1,1) # Spawns particle at 1,1 (If occupied, spawns in random location)
test_particle_2 = Particle(n,1) # Spawns particle at n,1 (Same as test_particle)
# Name your own particle and generate it