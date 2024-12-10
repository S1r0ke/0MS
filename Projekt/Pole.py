import random
from Otazky import QuestionManager # Importujeme naši novou třídu
import tkinter as tk

class Board:
    def __init__(self, size, num_tasks):
        # Inicializace velikosti hrací plochy a počtu úkolových políček
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.tasks = {}
        self.question_manager = QuestionManager() # Inicializujeme třídu QuestionManager
        self.place_tasks(num_tasks)
        self.root = tk.Tk()
        self.m = 50
        canvas_size = self.size * self.m  
        self.canvas = tk.Canvas(self.root, width=canvas_size, height=canvas_size, bg="white")


    def place_tasks(self, num_tasks):
        # Umístění úkolových políček na hrací plochu
        for _ in range(num_tasks):
            while True: 
                x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1) 
                if (x, y) not in self.tasks: 
                    self.tasks[(x, y)] = self.question_manager.get_random_question() # Použijeme QuestionManager k získání otázky
                    break

    def is_task(self, position):
        # Kontrola, zda je na pozici úkolové políčko
        return position in self.tasks

    def get_question(self, position):
        # Získání otázky na dané pozici
        return self.tasks[position]

    #kod zobrazí okno s polem 𝑛×𝑛 čtverců, kde každý čtverec má velikost 𝑚×𝑚.
    def vytvor_pole_ctvercu_gui(self, posx0 , posy0, posx1 , posy1):
        # hlavní okno aplikace
        
        self.root.title("Pole nxn čtverců") # titulek okna

        #velikost pole
        self.canvas.pack() #zobrazení

        # vykreslení jednotlivých čtverců
        for i in range(self.size): #řádky
            for j in range(self.size): #sloupce
                x0 = j * self.m
                y0 = i * self.m
                x1 = x0 + self.m
                y1 = y0 + self.m
                if (posx0, posy0) == (j, i):
                    self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="blue")
                elif (posx1, posy1) == (j, i):
                    self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="green")
                elif (j, i) in self.tasks.keys():
                    self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="red")
                else:
                    self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="white")
        self.root.mainloop()




