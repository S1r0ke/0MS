import random
from Pole import Board
from Hrac import Player
from Otazky import QuestionManager 
import tkinter as tk 
from tkinter import simpledialog, messagebox

class Game:
    def __init__(self, num_players, board_size, num_tasks, num_moves):
        # Inicializace hry, vytvoření hrací plochy a hráčů
        self.num_players = num_players
        self.board_size = board_size
        self.num_tasks = num_tasks
        self.num_moves = num_moves
        self.board = Board(board_size, num_tasks)
        self.players = [Player(0, self.board), Player(1, self.board)]
        self.current_move = 0
        self.init_gui()


    def init_gui(self): 
        # Inicializace grafického uživatelského rozhraní
        self.root = tk.Tk() 
        self.root.title("Matematická hra") 
        self.lbl_info = tk.Label(self.root, text="Klikněte na tlačítko pro tah hráče") 
        self.lbl_info.pack() 
        self.btn_move = tk.Button(self.root, text="Další tah", command=self.play_turn) 
        self.btn_move.pack() 
        self.txt_log = tk.Text(self.root, state=tk.DISABLED, width=50, height=20) 
        self.txt_log.pack()

    def play_turn(self):
        # Hlavní smyčka hry pro zpracování tahů
        if self.current_move < self.num_moves:
            for player in self.players:
                # Pohyb hráče v náhodně vybraném směru
                direction = random.choice(['nahoru', 'dolu', 'vlevo', 'vpravo'])
                player.getOpponentCoords(self.players[1]) if self.players[0] == player else player.getOpponentCoords(self.players[0])
                player.move(direction)
                if self.board.is_task(player.position):
                    # Zpracování úkolu na poli
                    player.tasks_found += 1
                    question, correct_answer = self.board.get_question(player.position)
                    self.log_message(f"Hráč {player.id}, otázka: {question}") 
                    answer = self.ask_question(question)
                    if str(answer) == str(correct_answer): 
                        self.log_message("Správně!") 
                        player.score += 1 
                        self.board.tasks[player.position] = None
                    else: self.log_message(f"Špatně! Správná odpověď je: {correct_answer}")
            self.current_move += 1
            self.board.vytvor_pole_ctvercu_gui(self.players[0].position[0], self.players[0].position[1], self.players[1].position[0], self.players[1].position[1])
            return
        if self.current_move == self.num_moves:
            self.show_results()
            return


    def ask_question(self, question): 
        # Zobrazení otázky a získání odpovědi od hráče
        answer = simpledialog.askstring("Otázka", question, parent=self.root) 
        if answer is not None: 
            return answer
        else: 
            messagebox.showinfo("Výsledek", "Odpověď byla zrušena.") 
        return None 
    
    def log_message(self, message): 
        # Zobrazení zpráv v textovém poli
        self.txt_log.config(state=tk.NORMAL) 
        self.txt_log.insert(tk.END, message + "\n") 
        self.txt_log.config(state=tk.DISABLED)

    def show_results(self):
        # Zobrazení výsledků hry po dokončení všech tahů
        results = "\nVýsledky:\n" 
        max_score = 0 
        winner_id = -1

        for player in self.players:
            success_rate = (player.score / player.tasks_found) * 100 if player.tasks_found > 0 else 0
            results += f"Hráč {player.id} našel {player.tasks_found} úkolů a získal {player.score} bodů.\n" 
            results += f"Úspěšnost: {success_rate:.2f}%\n"
            if player.score > max_score: 
                max_score = player.score 
                winner_id = player.id 
        if winner_id != -1: 
            results += f"\nVítěz je hráč {winner_id} s {max_score} body!\n" 
            messagebox.showinfo("Výsledky hry", results)
        if winner_id == -1: 
            results += f"\nVe hře došlo k remíze, hráči skončili s {max_score} body!\n" 
            messagebox.showinfo("Výsledky hry", results)

    def start(self): 
        self.board.vytvor_pole_ctvercu_gui(self.players[0].position[0], self.players[0].position[1], self.players[1].position[0], self.players[0].position[1])
        self.root.mainloop()
        self.play_turn()
        self.play_turn()

if __name__ == "__main__":
    game = Game(num_players=2, board_size=10, num_tasks=20, num_moves=60)
    game.start()