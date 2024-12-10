import random
import sympy as sp
from sympy import *
from sympy.matrices import Matrix
from array import *

#Otázky a dopovědi
class QuestionManager:
    def __init__(self):
        x, y = sp.symbols('x y')
        self.questions = [
            ["d", 3*x**3 + 2*x**2 - 5*x + 1, None],
            ["d", x**3 - 1*x**2 + 2*x - 3, None],
            ["d", 4*x**3 - 2*x + 1, None],
            ["d", 2*x**3 - 3*x**2 + 1*x + 4, None],
            ["d", x**3 + 3*x**2 + 5*x - 5, None],
            ["r", x**2 - 5*x - 6, None],
            ["r", 2*x**2 - 3*x + 1, None],
            ["r", x**2 - 3*x - 4, None],
            ["r", x**2 + 4*x - 21, None],
            ["r", x**2 + 6*x + 9, None],
            ["m", [[2, 3], [1, 4]], None],
            ["m", [[1, 2], [3, 4]], None],
            ["m", [[3, 5], [2, 7]], None],
            ["m", [[6, 1], [2, 3]], None],
            ["m", [[4, 6], [1, 2]], None],
            ["s", [3*x + 4*y - 7, 2*x - y - 3] , None],
            ["s", [x - 2*y - 4, 3*x + y - 5], None],
            ["s", [4*x - y - 6, 2*x + 3*y - 11], None],
            ["s", [x + 3*y - 10, 2*x - 4*y - 8], None],
            ["s", [5*x + 2*y - 12, 3*x - 4*y - 1], None]
        ]
        self.solveQuestions()
        self.questions = self.formatQuestions()


    def get_random_question(self):
        # Návrat náhodné otázky ze seznamu otázek
        if not self.questions:
            raise ValueError("Seznam otázek je prázdný.")
        return random.choice(self.questions)

    def solveQuestions(self):
        x, y = sp.symbols('x y')
        for i in self.questions:
            match i[0]:
                case "d":
                    answer = sp.diff(i[1], x)
                case "r":
                    answer = sp.solve(i[1], x)
                case "m":
                    M = sp.Matrix(i[1])
                    answer = M.det()
                case "s":
                    answer = solve(i[1], [x, y], dict=True)
                    answer = (answer[0][x], answer[0][y])
            i[2] = answer
        return
    def formatQuestions(self):
        finalList = []
        for i in self.questions:
            match i[0]:
                case "d":
                    finalList.append(["Derivujte vzhledem k x:\n" + str(i[1]), i[2]])
                case "r":
                    finalList.append(["Řešte pro x:\n" + str(i[1]) + " = 0\nVýsledek ve tvaru x1,x2", str(i[2][0]) +","+ str(i[2][-1])])
                case "m":
                    finalList.append(["Vyřešte determinant matice:\n" + str(i[1][0]) +"\n" + str(i[1][1]), i[2]])
                case "s":
                    finalList.append(["Řešte soustavu rovnic:\n" + str(i[1][0]) + " = 0\n" + str(i[1][1]) + " = 0" + "\nVýsledek ve tvaru x1,x2", str(i[2][0]) +","+ str(i[2][1])])
        return finalList


