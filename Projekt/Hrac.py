import random
import sympy as sp

class Player:
    def __init__(self, player_id, board):
        # Inicializace hráče, jeho pozice, skóre a počtu nalezených úkolů
        self.id = player_id
        self.board = board
        self.position = (random.randint(1, 4), random.randint(1, 4))
        self.score = 0
        self.tasks_found = 0

    def move(self, direction):
        # Pohyb hráče podle zvoleného směru
        (x, y) = self.position
        
        if direction == 'nahoru' and y > 0:  
            y -= 1
        elif direction == 'dolu' and y < 4: 
            y += 1
        elif direction == 'vlevo' and x > 0:  
            x -= 1
        elif direction == 'vpravo' and x < 4:  
            x += 1
        
        new_position = (x, y) 
        # Aktualizace pozice hráče
        if new_position != self.position: # Kontrola, zda se postava skutečně pohnula 
            self.position = new_position 
            print(f"Hráč {self.id} se pohnul do pozice {self.position}") 
        else: 
            print(f"Hráč {self.id} se nemohl pohnout z pozice {self.position}")
    
    def answer_question(self, question):
        # Logika pro hráčovu odpověď na otázku, zde generujeme odpověď na základě typu otázky 
        if "derivace" in question: 
            x = sp.symbols('x') 
            expr = sp.sympify(question.split(' ')[-1]) 
            return str(sp.diff(expr, x)) 
        elif "rovnice" in question: 
            x = sp.symbols('x') 
            eq = sp.Eq(sp.sympify(question.split('=')[0]), int(question.split('=')[1])) 
            return sp.solve(eq, x) 
        elif "determinant" in question: 
            matrix = sp.Matrix([[1, 2], [3, 4]]) 
            return matrix.det() 
        elif "soustava" in question: 
            x, y = sp.symbols('x y') 
            eq1 = sp.Eq(2*x + 3*y, 6) 
            eq2 = sp.Eq(x - y, 2) 
            return sp.solve((eq1, eq2), (x, y)) 
        else: 
            # Pro jednoduché otázky vracíme náhodné hodnoty 
            return random.choice([4, 9, "2x"])




