import random

#Otázky a dopovědi
class QuestionManager:
    def __init__(self):
        self.questions = [
            ("Kolik je 2 + 2?", 4),
            # Další otázky...
        ]

    def get_random_question(self):
        # Návrat náhodné otázky ze seznamu otázek
        if not self.questions:
            raise ValueError("Seznam otázek je prázdný.")
        return random.choice(self.questions)



