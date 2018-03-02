'''
The MIT License (MIT)

Copyright (c) 2017 Tristan Stérin pour Optimale Sup Spé

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''



import copy
import random
import time

ALIVE = '#'
DEAD = '.'

def est_valide(grille,i,j):
    return i >= 0 and i < len(grille) and j >= 0 and j < len(grille[0])

def nb_voisins_vivants(grille,i,j):
    nb_vivants = 0
    directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
    for dir_ in directions:
        v_i,v_j = i+dir_[0],j+dir_[1]
        if est_valide(grille,v_i,v_j):
            nb_vivants += (grille[v_i][v_j] == ALIVE)
    
    return nb_vivants

def one_step(grille):
    new_grille = copy.deepcopy(grille)
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            nb_vivants = nb_voisins_vivants(grille,i,j)
            if grille[i][j] == DEAD:
                if nb_vivants == 3:
                    new_grille[i][j] = ALIVE
            else:
                if nb_vivants < 2 or nb_vivants > 3:
                    new_grille[i][j] = DEAD
    return new_grille

def print_grille(grille):
    str_ = ""
    for line in grille:
        str_ += "".join(line)+"\n"
    
    print(str_)

def random_grille(n,m):
    grille = [[DEAD for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if random.randint(0,1):
                grille[i][j] = ALIVE
    return grille


grille = random_grille(23,90)
while 1:
    print_grille(grille)
    grille = one_step(grille)
    time.sleep(1)