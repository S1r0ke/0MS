import random
import sympy as sp

class Player:
    def __init__(self, player_id, board):
        # Inicializace hráče, jeho pozice, skóre a počtu nalezených úkolů
        self.id = player_id
        self.board = board
        self.position = (random.randint(0, self.board.size-1), random.randint(0, self.board.size-1))
        self.score = 0
        self.tasks_found = 0

    def getOpponentCoords(self, player):
        self.opponentCoords = player.position

    def move(self, direction):
        # Pohyb hráče podle zvoleného směru
        (x, y) = self.position
        
        if direction == 'nahoru' and y > 0:  
            y -= 1
        elif direction == 'dolu' and y < self.board.size-1: 
            y += 1
        elif direction == 'vlevo' and x > 0:  
            x -= 1
        elif direction == 'vpravo' and x < self.board.size-1: 
            x += 1
        new_position = (x, y)

        if new_position == self.opponentCoords:
            new_position = self.position
        # Aktualizace pozice hráče
        if new_position != self.position: # Kontrola, zda se postava skutečně pohnula 
            self.position = new_position 
            print(f"Hráč {self.id} se pohnul do pozice {self.position}") 
        else: 
            print(f"Hráč {self.id} se nemohl pohnout z pozice {self.position}")
    





