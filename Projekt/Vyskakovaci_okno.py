import tkinter as tk
from tkinter import simpledialog, messagebox
from Otazky import QuestionManager  # Importujeme naši novou třídu

class OtazkaDialog:
    def __init__(self, root, otazky):
        self.root = root
        self.otazky = otazky
        self.ask_question() # Zavolá metodu pro zobrazení otázky

    def ask_question(self):
        # Zobrazení otázky a zpracování odpovědi
        # Získání náhodné otázky a její správné odpovědi
        question, correct_answer = self.otazky.get_random_question()
        # Zobrazení dialogového okna pro zadání odpovědi
        answer = simpledialog.askstring("Otázka", question, parent=self.root)
        
        if answer is not None:
            if str(answer) == str(correct_answer):
                messagebox.showinfo("Výsledek", "Správně!")
            else:
                messagebox.showinfo("Výsledek", "Špatně! Správná odpověď je: " + str(correct_answer))
        else:
            messagebox.showinfo("Výsledek", "Odpověď byla zrušena.")

if __name__ == "__main__":
    # Inicializace hlavního okna aplikace
    root = tk.Tk()
    root.withdraw()  # Skrýt hlavní okno

    # Vytvoření instance třídy QuestionManager
    otazky = QuestionManager()
    # Vytvoření a zobrazení dialogu s otázkou
    OtazkaDialog(root, otazky)

    # Spuštění hlavní smyčky aplikace
    root.mainloop()



