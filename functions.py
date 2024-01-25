import random
from math import gcd
import matplotlib.pyplot as plt
import numpy as np
import os

class Easy:
    def __init__(self):
        self.points = 4

class Medium:
    def __init__(self):
        self.points = 8

class Hard:
    def __init__(self):
        self.points = 12

class Task_e1(Easy):
    def __init__(self):
        super().__init__()
        self.id = 'functions_e1'
    def generate_variants(self):
        c = random.randint(1, 10)
        self.text = f"Data je linearna funkcija u implicitnom obliku x + y + {c} = 0. Zapiši datu funkciju u eksplicitnom obliku."
        self.helps = ["Za linearnu funkciju y = kx + n kažemo da je zadata u eksplicitnom obliku.<br>"
                      f"Zapiši datu funkciju x + y + {c} = 0 u obliku y = kx + n.",
                      f"Kako bi datu funkciju x + y + {c} = 0 zapisali u eksplicitnom obliku y = kx + n potrebno je ostaviti samo y sa leve strane.<br>"
                      f"Oduzmi x i {c} od obe strane jednakosti x + y + {c} = 0."]

        self.solution = "Za linearnu funkciju y = kx + n kažemo da je zadataka u eksplicitnom obliku.<br>" \
                        f"Kako bi datu funkciju x + y + {c} = 0 zapisali u eksplicitnom obliku y = kx + n potrebno je ostaviti samo y sa leve strane." \
                        f"Oduzećemo x i {c} od obe strane jednakosti x + y + {c} = 0 i dobijamo:<br>" \
                        f"x + y + {c} = 0 / - x - {c}<br>" \
                        f"x + y + {c} - x - {c} = 0 - x - {c}<br>" \
                        f"y = - x - {c}<br>" \
                        f"Primeti da smo datu funkciju x + y + {c} = 0 zapisali u eksplicitnom obliku y = kx + n, gde je k = -1 i n = -{c}."
        self.options = [f"y = - x - {c}",
                        f"x = - y - {c}",
                        f"0 = x + y + {c}"]
        random.shuffle(self.options)
        self.correct_answer = f"y = - x - {c}"

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution, 'points':self.points}

class Task_m1(Medium):
    def __init__(self):
        super().__init__()
        self.id = 'functions_m1'
    def generate_variants(self):
        while True:
            a = random.randint(3, 20)
            b = random.randint(20, 31)
            c = random.randint(3, 20)
            if gcd(a, b) == 1 and gcd(c, b):
                break

        self.text = f"Data je linearna funkcija u implicitnom obliku {a}x + {b}y + {c} = 0. Zapiši datu funkciju u eksplicitnom obliku."
        self.helps = [
            "Za linearnu funkciju y = kx + n kažemo da je zadataka u eksplicitnom obliku.<br>"
            f"Zapiši datu funkciju {a}x + {b}y + {c} = 0 u obliku y = kx + n.",
            f"Kako bi datu funkciju {a}x + {b}y + {c} = 0 zapisali u eksplicitnom obliku y = kx + n potrebno je ostaviti samo y sa leve strane.<br>"
            f"Oduzmi {a}x i {c} od obe strane jednakosti {a}x + {b}y - {c} = 0. Zatim podeli obe srane jednakosti sa {b}."]

        self.solution = "Za linearnu funkciju y = kx + n kažemo da je zadataka u eksplicitnom obliku.<br>" \
                        f"Kako bi datu funkciju {a}x + {b}y + {c} = 0 zapisali u eksplicitnom obliku y = kx + n potrebno je ostaviti samo y sa leve strane." \
                        f"Oduzećemo {a}x i {c} od obe strane jednakosti {a}x + {b}y + {c} = 0 i dobijamo:<br>" \
                        f"{a}x + {b}y + {c} = 0 / - {a}x - {c}<br>" \
                        f"{a}x + {b}y + {c} - {a}x - {c} = 0 - {a}x - {c}<br>" \
                        f"{b}y = - {a}x - {c}<br>" \
                        f"Podelićemo obe srane jednakosti {b}y = - {a}x - {c} sa {b}, kako bi sa leve strane ostao samo y.<br>" \
                        f"{b}y = - {a}x - {c} / :{b}<br>" \
                        f"<math> <mfrac> <mrow> <mn>{b}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>y = " \
                        f"<math> <mo>-</mo> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>x - " \
                        f"<math> <mfrac> <mrow> <mn>{c}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math><br>" \
                        f"y = <math> <mo>-</mo> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>x - " \
                        f"<math> <mfrac> <mrow> <mn>{c}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math><br>" \
                        f"Primeti da smo datu funkciju {a}x + {b}y + {c} = 0 zapisali u eksplicitnom obliku y = kx + n, gde je k = " \
                        f"<math> <mo>-</mo> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math> i n = " \
                        f"<math> <mo>-</mo> <mfrac> <mrow> <mn>{c}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>."
        self.options = [
            f"y = <math> <mo>-</mo> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>x - " \
                        f"<math> <mfrac> <mrow> <mn>{c}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math><br>",
            f"x = <math> <mo>-</mo> <mfrac> <mrow> <mn>{b}</mn> </mrow> <mrow> <mn>{a}</mn> </mrow> </mfrac> </math>x - {c}",
            f"y = <math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>x + " \
                        f"<math> <mfrac> <mrow> <mn>{c}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math><br>"]
        random.shuffle(self.options)
        self.correct_answer = f"y = <math> <mo>-</mo> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>x - " \
                        f"<math> <mfrac> <mrow> <mn>{c}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math><br>"

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution, 'points':self.points}

class Task_h1(Hard):
    def __init__(self):
        super().__init__()
        self.id = 'functions_h1'
    def generate_variants(self):
        b = random.randint(3, 15)
        a = 2*b
        # Generate x values
        x_values = np.linspace(-20, 20, 100)

        x_axis = np.linspace(-20, 20, 100)
        y_axis = np.linspace(-10, 10, 100)

        # Calculate y values
        y_values = (-1/2)*x_values-1
        y_values_2 = (1/2)*x_values-1

        plt.plot(x_values, y_values_2)
        plt.plot(x_axis, [0]*100, color='black')
        plt.plot([0]*100, y_axis, color='black')
        # Add grid with step 1 on both axes
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.xticks(np.arange(np.floor(min(x_values)), np.ceil(max(x_values)) + 1, step=1))
        plt.yticks(np.arange(np.floor(min(y_values_2)), np.ceil(max(y_values_2)) + 1, step=1))
        plt.gca().set_aspect('equal')
        plt.tick_params(labelbottom=False, labelleft=False)
        images_path = f"./static/images/{self.id}"
        plt.xlim(-10,10)
        plt.ylim(-10,10)
        plt.tight_layout()
        plt.text(0, 9.8, 'V', fontsize=12, rotation=180, ha='center', va='center')
        plt.text(9.82, -0.06, '>', fontsize=12, ha='center', va='center')
        for x in range(-9, 10):
            if x != 0:
                plt.text(x, -0.3, str(x), ha='center', va='top', fontsize=8, color='black')

        for y in range(-9, 10):
            if y != 0:
                plt.text(0.3, y, str(y), ha='center', va='top', fontsize=8, color='black')
        plt.savefig(f'{images_path}/incorrect_answer.png')

        plt.clf()

        plt.plot(x_values, y_values)
        plt.plot(x_axis, [0]*100, color='black')
        plt.plot([0]*100, np.linspace(-10, 10, 100), color='black')
        # Add grid with step 1 on both axes
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.xticks(np.arange(np.floor(min(x_values)), np.ceil(max(x_values)) + 1, step=1))
        plt.yticks(np.arange(np.floor(min(y_values_2)), np.ceil(max(y_values_2)) + 1, step=1))
        plt.gca().set_aspect('equal')
        plt.tick_params(labelbottom=False, labelleft=False)
        plt.xlim(-10,10)
        plt.ylim(-10,10)
        plt.tight_layout()
        plt.text(0, 9.8, 'V', fontsize=12, rotation=180, ha='center', va='center')
        plt.text(9.82, -0.06, '>', fontsize=12, ha='center', va='center')
        for x in range(-9, 10):
            if x != 0:
                plt.text(x, -0.3, str(x), ha='center', va='top', fontsize=8, color='black')

        for y in range(-9, 10):
            if y != 0:
                plt.text(0.3, y, str(y), ha='center', va='top', fontsize=8, color='black')

        plt.savefig(f'{images_path}/correct_answer.png')
        plt.clf()

        self.text = f"Data je linearna funkcija u implicitnom obliku {a}x + {b}y + {b} = 0. Zapiši datu funkciju u eksplicitnom obliku i odredi koji grafik odgovara grafiku date funkcije."
        self.helps = [
            "Za linearnu funkciju y = kx + n kažemo da je zadataka u eksplicitnom obliku.<br>"
            f"Zapiši datu funkciju {a}x + {b}y + {b} = 0 u obliku y = kx + n.<br>"
            f"Kako bi pronašao dobar grafik date funkcije odredi nule funkcije, odnosno gde data funkcija seče x i y osu.<br>"
            f"Funckija seče x osu kada je y = 0, dok seče y osu kada je x = 0.",
            f"Kako bi datu funkciju {a}x + {b}y + {b} = 0 zapisali u eksplicitnom obliku y = kx + n potrebno je ostaviti samo y sa leve strane.<br>"
            f"Oduzmi {a}x i {b} od obe strane jednakosti {a}x + {b}y - {b} = 0. Zatim podeli obe srane jednakosti sa {b}.<br>"
            f"Funkcija seče x osu u tački (<math> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </math>,0), dok seče y osu u tački (0,-1)."]

        self.solution = "Za linearnu funkciju y = kx + n kažemo da je zadataka u eksplicitnom obliku.<br>" \
                        f"Kako bi datu funkciju {a}x + {b}y + {b} = 0 zapisali u eksplicitnom obliku y = kx + n potrebno je ostaviti samo y sa leve strane." \
                        f"Oduzećemo {a}x i {b} od obe strane jednakosti {a}x + {b}y + {b} = 0 i dobijamo:<br>" \
                        f"{a}x + {b}y + {b} = 0 / - {a}x - {b}<br>" \
                        f"{a}x + {b}y + {b} - {a}x - {b} = 0 - {a}x - {b}<br>" \
                        f"{b}y = - {a}x - {b}<br>" \
                        f"Podelićemo obe srane jednakosti {b}y = - {a}x - {b} sa {b}, kako bi sa leve strane ostao samo y.<br>" \
                        f"{b}y = - {a}x - {b} / :{b}<br>" \
                        f"<math> <mfrac> <mrow> <mn>{b}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>y = " \
                        f"<math> <mo>-</mo> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>x - " \
                        f"<math> <mfrac> <mrow> <mn>{b}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math><br><br>" \
                        f"y = -2x - 1 <br>" \
                        f"Primeti da smo datu funkciju {a}x + {b}y + {b} = 0 zapisali u eksplicitnom obliku y = kx + n, gde je k = -2 i n = -1<br>" \
                        f"Kako bi pronašli dobar grafik date funkcije treba odrediti nule date funkcije, odnosno gde data funkcija seče x i y osu.<br>" \
                        f"Funckija seče x osu kada je y = 0, dok seče y osu kada je x = 0.<br><br>" \
                        f"Funkcija seče x osu kada je y = 0. Zamenićemo y = 0 u jednačinu {a}x + {b}y + {b} = 0. Dobijamo:<br>" \
                        f"{a}x + {b}*0 + {b} = 0<br>" \
                        f"{a}x + 0 + {b} = 0<br>" \
                        f"{a}x + {b} = 0 / -{b}<br>" \
                        f"{a}x = -{b}<br>" \
                        f"x = <math> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </math><br><br>" \
                        f"Znači funkcija seče x osu u tački <math> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </math>.<br><br>" \
                        f"Funkcija seče y osu kada je x = 0. Zamenićemo x = 0 u jednačinu {a}x + {b}y + {b} = 0. Dobijamo:<br>" \
                        f"{a}*0 + {b}y + {b} = 0<br>" \
                        f"0 + {b}y + {b} = 0<br>" \
                        f"{b}y + {b} = 0 / -{b}<br>" \
                        f"{b}y = -{b}<br>" \
                        f"y = <math> <mo>-</mo> <mfrac> <mrow> <mn>{b}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math><br>" \
                        f"y = -1<br><br>" \
                        f"Znači funkcija seče y osu u tački -1.<br>" \
                        f"Grafik date funkcije mora prolaziti kroz tačke (0,-1) i (<math> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </math>,0).<br><br>" \
                        f"Zaključujemo da je grafik date funkcije:<br><br>" \
                        f"<img src='../static/images/functions_h1/correct_answer.png'>"
        self.options = [f"y = -2x - 1 i ovo je grafik koji predstavlja funkciju:<br><img class='option_image' src='../static/images/functions_h1/correct_answer.png'>",
                        f"y = 2x + 1 i ovo je grafik koji predstavlja funkciju:<br><img class='option_image' src='../static/images/functions_h1/correct_answer.png'>",
                        f"y = -2x - 1 i ovo je grafik koji predstavlja funkciju:<br><img class='option_image' src='../static/images/functions_h1/incorrect_answer.png'>"]
        self.pdf_options = [f"y = -2x - 1 i ovo je grafik koji predstavlja funkciju:<br><img class='option_image' src='{os.path.join(os.getcwd(), 'static', 'images', 'functions_h1','correct_answer.png')}'>",
                        f"y = 2x + 1 i ovo je grafik koji predstavlja funkciju:<br><img class='option_image' src='{os.path.join(os.getcwd(), 'static', 'images', 'functions_h1','correct_answer.png')}'>",
                        f"y = -2x - 1 i ovo je grafik koji predstavlja funkciju:<br><img class='option_image' src='{os.path.join(os.getcwd(), 'static', 'images', 'functions_h1','incorrect_answer.png')}'>"]


        random.shuffle(self.options)
        self.correct_answer = f"y = -2x - 1 i ovo je grafik koji predstavlja funkciju:<br><img class='option_image' src='../static/images/functions_h1/correct_answer.png'>"

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution, 'points': self.points, 'pdf_options': self.pdf_options}

def generate_functions_questions(number_of_questions,level):
    if level == "Lak":
        easy_subclasses = Easy.__subclasses__()
        objects = [cls() for cls in easy_subclasses]
        chosen_objects = random.sample(objects,number_of_questions)
        questions = [o.generate_variants() for o in chosen_objects]
        return questions
    elif level == "Srednji":
        medium_subclasses = Medium.__subclasses__()
        objects = [cls() for cls in medium_subclasses]
        chosen_objects = random.sample(objects, number_of_questions)
        questions = [o.generate_variants() for o in chosen_objects]
        return questions
    else:
        hard_subclasses = Hard.__subclasses__()
        objects = [cls() for cls in hard_subclasses]
        chosen_objects = random.sample(objects, number_of_questions)
        questions = [o.generate_variants() for o in chosen_objects]
        return questions
