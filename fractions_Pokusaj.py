import random
from math import gcd


class Easy:
    pass

class Medium:
    pass

class Hard:
    pass

class Task_e1(Easy):
    def __init__(self):
        self.id = 'fractions_e1'

    def generate_variants(self):
        while True:
            a = random.randint(1, 9)
            b = random.randint(2, 9)

            if a < b and gcd(a, b) == 1:
                break
        c = random.randint(2, 9)

        fraction = f'\( \\frac{{{a}}}{{{b}}} \)'
        fraction_expanded = f'\( \\frac{{{a * c}}}{{{b * c}}} \)'

        self.text = f"Razlomak {fraction} proširiti sa {c}."

        self.helps = [
            f"Prilikom proširivanja razlomka sa određenim brojem, pomnoži imenilac i brojilac razlomka sa tim brojem.",
            f"Kako bi proširili razlomak {fraction} sa brojem {c}, pomnoži brojilac i imenilac razlomka sa {c}."
        ]
        self.solution = f"Prilikom proširivanja razlomka sa određenim brojem, potrebno je pomnožiti imenilac i " \
                        f"brojilac razlomka sa tim brojem.<br>Kako bi proširili razlomak {fraction} sa brojem {c}" \
                        f", potrebno je pomnožiti brojilac i imenilac razlomka sa {c}.<br>Dobijamo :<br>" \
                        f"{fraction} * \( \\frac{{{c}}}{{{c}}} \) = {fraction_expanded}"

        self.options = [
            f"{fraction_expanded}",
            f"\( \\frac{{{a * c}}}{{{b * c}}} \)",
            f"\( \\frac{{{a}}}{{{b * c}}} \)"
        ]
        random.shuffle(self.options)
        self.correct_answer = f"{fraction_expanded}"

        return {
            'text': self.text,
            'id': self.id,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'helps': list(enumerate(self.helps)),
            'solution': self.solution
        }



class Task_m1(Medium):
    def __init__(self):
        self.id = 'fractions_m1'

    def generate_variants(self):
        while True:
            a = random.randint(15, 30)
            b = random.randint(20, 30)

            if a < b and gcd(a, b) == 1:
                break
        c = random.randint(11, 15)

        fraction = f'\( \\frac{{{a}}}{{{b}}} \)'
        fraction_expanded = f'\( \\frac{{{a * c}}}{{{b * c}}} \)'

        self.text = f"Razlomak {fraction} proširiti sa {c}."
        self.helps = [
            "Prilikom proširivanja razlomka sa određenim brojem, potrebno je pomnožiti razlomak sa tim brojem.",
            f"Kako bi pomoću razlomka {fraction} sa brojem {c} pomogli, pomnožite imenilac i brojilac razlomka sa brojem {c}."
        ]

        self.solution = f"Prilikom proširivanja razlomka sa određenim brojem, potrebno je pomnožiti imenilac i " \
                        f"brojilac razlomka sa tim brojem.<br>Kako bi proširili razlomak {fraction} sa brojem {c}" \
                        f", potrebno je pomnožiti brojilac i imenilac razlomka sa {c}.<br>Dobijamo :<br>" \
                        f"{fraction} \\cdot \\( \\frac{{{c}}}{{{c}}} \\) = {fraction_expanded}"

        self.options = [
            f"{fraction_expanded}",
            f"\( \\frac{{{a * c}}}{{{b * c}}} \)",
            f"\( \\frac{{{a}}}{{{b * c}}} \)"
        ]
        random.shuffle(self.options)
        self.correct_answer = f"{fraction_expanded}"

        return {
            'text': self.text,
            'id': self.id,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'helps': list(enumerate(self.helps)),
            'solution': self.solution
        }


class Task_h1(Hard):
    def __init__(self):
        self.id = 'fractions_h1'

    def generate_variants(self):
        while True:
            a = random.randint(15, 30)
            b = random.randint(20, 30)

            if a < b and gcd(a, b) == 1:
                break
        c = random.randint(11, 15)

        fraction_ab = f'\( \\frac{{{a}}}{{{b}}} \)'
        fraction_acbc = f'\( \\frac{{{a * c}}}{{{b * c}}} \)'
        fraction_cc = f'\( \\frac{{{c}}}{{{c}}} \)'
        fraction_ac_bc = f'\( \\frac{{{a * c}}}{{{b * c}}} \)'

        self.text = f"Sa kojim brojem treba proširiti razlomak {fraction_ab}" \
                    f"tako da prošireni razlomak bude {fraction_acbc}"
        self.helps = [
            "Prilikom proširivanja razlomka sa određenim brojem, potrebno je pomnožiti imenilac i "
            "brojilac razlomka sa tim brojem.",
            f"Kako bi pronašao broj koji treba pomnožiti sa {fraction_ab}, razmisli"
            f"o deljenju proširenog imenioca sa neproširenim imeniocem, odnosno deljenju brojioca sa "
            f"neproširenim brojiocem"
        ]

        self.solution = f"Prilikom proširivanja razlomka sa određenim brojem, potrebno je pomnožiti imenilac i brojilac razlomka sa tim brojem. <br>" \
                        f"Kako bi pronašali vrednost koju treba pomnožiti sa {fraction_ab}" \
                        f" kako bi dobili {fraction_acbc}, jedan od načina" \
                        " je da podelimo prošireni imenilac sa neproširenim imeniocem, odnosno da podelimo prošireni brojilac sa neproširenim brojiocem.<br><br>" \
                        f"Kako je \( \\frac{{{a * c}}}{{{a}}} = {c} \), kao i \( \\frac{{{b * c}}}{{{b}}} = {c} \), dobijemo da je razlomak {fraction_ab} potrebno da proširimo sa {c}" \
                        f" kako bi dobili razlomak {fraction_acbc}.<br><br>Proverićemo da je razlomak {fraction_ab} proširen sa {c}" \
                        f" jednak razlomku {fraction_acbc}.<br>" \
                        f"\( {fraction_ab} * {fraction_cc} = {fraction_ac_bc} = {fraction_acbc} \)"
        self.options = [f"{c}", f"{a * c - a}", f"{c + 1}"]
        random.shuffle(self.options)
        self.correct_answer = f"{c}"

        return {
            'text': self.text,
            'id': self.id,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'helps': list(enumerate(self.helps)),
            'solution': self.solution
        }


class Task_e2(Easy):
    def __init__(self):
        self.id = 'fractions_e2'

    def generate_variants(self):
        while True:
            a = random.randint(1, 9)
            b = random.randint(2, 10)

            if a < b and gcd(a, b) == 1:
                break
        c = random.choice([2, 3])

        fraction_ab = f'\( \\frac{{{a}}}{{{b}}} \)'
        fraction_acbc = f'\( \\frac{{{a * c}}}{{{b * c}}} \)'

        self.text = f"Skratiti razlomak {fraction_acbc}."
        self.helps = [
            "Razlomak može da se skrati samo brojem koji deli i brojilac i imenilac.<br>"
            f"Pronađi najveći zajednički delilac za brojeve {a * c} i {b * c}.",
            f"Najveći zajednički delilac za brojeve {a * c} i {b * c} je {c}."
        ]

        self.solution = f"Razlomak može da se skrati samo brojem koji deli i brojilac i imenilac.<br>" \
                        f"Kako je najveći zajednički delilac za brojeve {a * c} i {b * c} broj {c}," \
                        f" zaključujemo da razlomak {fraction_acbc} možemo da skratimo sa {c}.<br><br>" \
                        f"Podelićemo imenilac i brojilac brojem {c}:<br>" \
                        f"{fraction_acbc} = \( \\frac{{{a * c}}}{{{c}}} \\div \\frac{{{b * c}}}{{{c}}} = {fraction_ab} \)." \
                        f"<br><br>Nakon skraćivanja razlomka {fraction_acbc} dobijamo razlomak {fraction_ab}."
        self.options = [
            f"{fraction_ab}",
            f'\( \\frac{{{a * c}}}{{{b}}} \)',
            f'\( \\frac{{{a}}}{{{b * c}}} \)'
        ]
        random.shuffle(self.options)
        self.correct_answer = f"{fraction_ab}"

        return {
            'text': self.text,
            'id': self.id,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'helps': list(enumerate(self.helps)),
            'solution': self.solution
        }



class Task_m2(Medium):
    def __init__(self):
        self.id = 'fractions_m2'

    def generate_variants(self):
        while True:
            a = random.randint(11, 30)
            b = random.randint(11, 30)

            if a < b and gcd(a, b) == 1:
                break
        c = random.choice([2, 3, 5])

        fraction_ab = f'\( \\frac{{{a}}}{{{b}}} \)'
        fraction_acbc = f'\( \\frac{{{a * c}}}{{{b * c}}} \)'

        self.text = f"Skratiti razlomak {fraction_acbc}."
        self.helps = [
            "Razlomak može da se skrati samo brojem koji deli i brojilac i imenilac.<br>"
            f"Pronađi najveći zajednički delilac za brojeve {a * c} i {b * c}.",
            f"Najveći zajednički delilac za brojeve {a * c} i {b * c} je {c}."
        ]

        self.solution = f"Razlomak može da se skrati samo brojem koji deli i brojilac i imenilac.<br>" \
                        f"Kako je najveći zajednički delilac za brojeve {a * c} i {b * c} broj {c}," \
                        f" zaključujemo da razlomak {fraction_acbc} možemo da skratimo sa {c}.<br><br>" \
                        f"Podelićemo imenilac i brojilac brojem {c}:<br>" \
                        f"{fraction_acbc} = \( \\frac{{{a * c}}}{{{c}}} \\div \\frac{{{b * c}}}{{{c}}} = {fraction_ab} \)." \
                        f"<br><br>Nakon skraćivanja razlomka {fraction_acbc} dobijamo razlomak {fraction_ab}."
        self.options = [
            f"{fraction_ab}",
            f'\( \\frac{{{a * c}}}{{{b}}} \)',
            f'\( \\frac{{{a}}}{{{b * c}}} \)'
        ]
        random.shuffle(self.options)
        self.correct_answer = f"{fraction_ab}"

        return {
            'text': self.text,
            'id': self.id,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'helps': list(enumerate(self.helps)),
            'solution': self.solution
        }



class Task_h2(Hard):
    def __init__(self):
        self.id = 'fractions_h2'

    def generate_variants(self):
        while True:
            a = random.randint(11, 30)
            b = random.randint(11, 30)
            d = random.randint(a + 1, a + 10)
            if a < b and gcd(a, b) == 1 and d < b and gcd(d, b) == 1:
                break
        c = random.choice([2, 3, 5])

        fraction_ab = f'\( \\frac{{{a}}}{{{b}}} \)'
        fraction_acbc = f'\( \\frac{{{a * c}}}{{{b * c}}} \)'
        fraction_db = f'\( \\frac{{{d}}}{{{b}}} \)'

        self.text = f"Skratiti razlomak {fraction_acbc} i uporediti ga sa {fraction_db}."

        self.helps = [
            f"Razlomak može da se skrati samo brojem koji deli i brojilac i imenilac.<br>Pronađi najveći zajednički delilac za brojeve {a * c} i {b * c}."
            "Upoređivanje 2 razlomka je analiziranje vrednosti razlomaka radi utvrđivanja njihovog odnosa.",
            f"Najveći zajednički delilac za brojeve {a * c} i {b * c} je {c}."
            f"S' obzirom da razlomci imaju iste imenioce dovoljno je uporediti brojioce i zaključiti u kakvom su odnosu."
        ]

        self.solution = f"Razlomak može da se skrati samo brojem koji deli i brojilac i imenilac.<br>" \
                        f"Kako je najveći zajednički delilac za brojeve {a * c} i {b * c} broj {c}," \
                        f" zaključujemo da razlomak {fraction_acbc} možemo da skratimo sa {c}.<br><br>" \
                        f"Podelićemo imenilac i brojilac brojem {c}:<br>" \
                        f"{fraction_acbc} = \( \\frac{{{a * c}}}{{{c}}} \\div \\frac{{{b * c}}}{{{c}}} = {fraction_ab} \)." \
                        f"<br><br>Nakon skraćivanja razlomka {fraction_acbc} dobijamo razlomak {fraction_ab}.<br><br>" \
                        f"Ako uporedimo skraćeni razlomak {fraction_ab} i {fraction_db}, s' obzirom da imaju isti imenilac, " \
                        f"zaključujemo da je {fraction_db} veće od skraćenog razlomka jer je {d} veće od {a}."
        self.options = [f"{fraction_ab} i {fraction_acbc} < {fraction_db}",
                        f"{fraction_ab} i {fraction_acbc} > {fraction_db}",
                        f"{fraction_db} i {fraction_acbc} = {fraction_db}"]
        random.shuffle(self.options)
        self.correct_answer = f"{fraction_ab} i {fraction_acbc} < {fraction_db}"

        return {
            'text': self.text,
            'id': self.id,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'helps': list(enumerate(self.helps)),
            'solution': self.solution
        }



class Task_e3(Easy):
    def __init__(self):
        self.id = 'fractions_e3'

    def generate_variants(self):
        while True:
            a = random.randint(2, 9)
            b = random.randint(2, 13)
            c = random.randint(2, 9)
            d = b
            if a < b and gcd(a, b) == 1 and c < d and gcd(c, d) == 1 and gcd(a + c, d) == 1 and (a + c) < d and gcd(
                    a + c, d + b) == 1:
                break
        fraction_ab = f'\( \\frac{{{a}}}{{{b}}} \)'
        fraction_cd = f'\( \\frac{{{c}}}{{{d}}} \)'
        fraction_ac_d = f'\( \\frac{{{a}}}{{1}} + \\frac{{{c}}}{{1}} \)'
        fraction_sum = f'\( \\frac{{{a + c}}}{{{d}}} \)'
        fraction_incorrect = f'\( \\frac{{{a + c}}}{{{d + b}}} \)'

        self.text = f"Saberi razlomke {fraction_ab} i {fraction_cd}."
        self.helps = [
            "Razlomci koje je potrebno sabrati imaju iste imenioce. Razlomci koji imaju iste imenioce sabiraju se tako što se brojioci saberu, a imenilac prepiše.",
            "Razlomci koji imaju iste imenioce sabiraju se tako što se brojioci saberu, a imenilac prepiše."
        ]

        self.solution = f"Razlomci koji imaju iste imenioce sabiraju se tako što se brojioci saberu, a imenilac prepiše. Nakon primene pravila dobijamo:<br>" \
                        f"{fraction_ab} + {fraction_cd} = {fraction_ac_d} = {fraction_sum}."
        self.options = [f"{fraction_sum}",
                        f"{fraction_incorrect}",
                        1]
        random.shuffle(self.options)
        self.correct_answer = f"{fraction_sum}"

        return {
            'text': self.text,
            'id': self.id,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'helps': list(enumerate(self.helps)),
            'solution': self.solution
        }



class Task_m3(Medium):
    def __init__(self):
        self.id = 'fractions_m3'

    def generate_variants(self):
        while True:
            d = random.randint(4, 12)
            b = 2 * d
            a = random.randint(1, b - 1)
            c = random.randint(1, d - 1)
            if gcd(a, b) == 1 and gcd(c, d) == 1 and gcd(a + 2 * c, b) == 1:
                break
        fraction_ab = f'\( \\frac{{{a}}}{{{b}}} \)'
        fraction_cd = f'\( \\frac{{{c}}}{{{d}}} \)'
        fraction_22 = '\( \\frac{{2}}{{2}} \)'
        fraction_c2d2 = f'\( \\frac{{{c * 2}}}{{{d * 2}}} \)'
        fraction_c2_d2 = f'\( \\frac{{{c * 2}}}{{{d * 2}}} \)'
        fraction_sum = f'\( \\frac{{{a + c * 2}}}{{{b}}} \)'
        fraction_incorrect1 = f'\( \\frac{{{a + c}}}{{{b + d}}} \)'
        fraction_incorrect2 = f'\( \\frac{{{b}}}{{{a + c * 2}}} \)'

        self.text = f"Saberi razlomke {fraction_ab} i {fraction_cd}."
        self.helps = [
            "Kako bi se sabrali razlomci koji nemaju iste imenioce potrebno je svesti ih na razlomke sa istim imeniocima.",
            "Primeti da je imenilac prvog razlomka duplo veći od imenioca drugog razlomka."
            "Kako bi se razlomci sveli na iste imenioce potrebno je da se drugi razlomak proširi sa 2."
        ]

        self.solution = f"Kako bi se sabrali razlomci koji nemaju iste imenioce potrebno je svesti ih na razlomke sa istim imeniocima. <br>" \
                        "Primeti da je imenilac prvog razlomka duplo veći od imenioca drugog razlomka, proširićemo drugi razlomak sa 2:<br>" \
                        f"{fraction_cd} * {fraction_22} = {fraction_c2d2} = {fraction_c2_d2}.<br>" \
                        f"Sada razlomci {fraction_ab} i {fraction_cd} imaju iste imenioce. <br>" \
                        f"Sabraćemo ih tako što ćemo im sabrati brojioce i prepisati imenilac.<br>" \
                        f"Dobijamo:<br>" \
                        f"{fraction_ab} + {fraction_c2_d2} = {fraction_sum}"
        self.options = [f"{fraction_sum}",
                        f"{fraction_incorrect1}",
                        f"{fraction_incorrect2}"]
        random.shuffle(self.options)
        self.correct_answer = f"{fraction_sum}"

        return {
            'text': self.text,
            'id': self.id,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'helps': list(enumerate(self.helps)),
            'solution': self.solution
        }




class Task_h3(Hard):
    def __init__(self):
        self.id = 'fractions_h3'

    def generate_variants(self):
        while True:
            b = random.randint(2, 8)
            a = random.randint(1, b - 1)
            c = random.randint(2, 9)
            if gcd(a, b) == 1 and gcd(a + c * b, b) == 1 and gcd(a + c, b) == 1:
                break
        fraction_ab = f'\( \\frac{{{a}}}{{{b}}} \)'
        fraction_cb_1b = f'\( \\frac{{ {c} \\cdot {b} }}{{ 1 \\cdot {b} }} \)'
        fraction_cb_b = f'\( \\frac{{ {c * b} }}{{ {b} }} \)'
        fraction_c_1 = f'\( \\frac{{ {c} }}{{ 1 }} \)'
        fraction_b_b = f'\( \\frac{{ {b} }}{{ {b} }} \)'
        fraction_acb_b = f'\( \\frac{{ {a} + {c * b} }}{{ {b} }} \)'
        fraction_sum = f'\( \\frac{{ {a + c * b} }}{{ {b} }} \)'
        fraction_incorrect1 = f'\( \\frac{{ {a + c} }}{{ {b} }} \)'
        fraction_incorrect2 = f'{a + c}'

        self.text = f"Saberi razlomak {fraction_ab} i broj {c}."
        self.helps = [
            "Kako bi se razlomak sabrao sa celim brojem, potrebno je da se ceo broj predstavi u obliku razlomka koji ima isti imenilac kao dati razlomak.",
            f"Ceo broj {c} predstavljen u obliku razlomka koji ima isti imenilac kao dati razlomak je {fraction_cb_b}. Sada je potrebno sabrati razlomke."
        ]

        self.solution = f"Kako bi se razlomak sabrao sa celim brojem, potrebno je da se ceo broj predstavi u obliku razlomka koji ima isti imenilac kao dati razlomak. <br>" \
                        "Zatim je potrebno sabrati ih kao dva razlomka sa istim imeniocem. <br>" \
                        f"Predstavićemo broj u obliku razlomka koji ima isti imenilac kao dati razlomak, odnosno da mu je imenilac broj {b}:<br>" \
                        f"Broj {c} možemo da predstavimo kao razlomak {fraction_c_1}, i zatim da ga proširimo sa {b}. " \
                        f"Dobijamo: <br>" \
                        f"{fraction_c_1} * {fraction_b_b} = {fraction_cb_1b} = {fraction_cb_b}. <br>" \
                        f"Kako sada razlomci {fraction_ab} i {fraction_cb_b} imaju iste imenioce, sabraćemo ih primenjujući pravilo o sabiranju razlomaka koji imaju iste imenioce," \
                        f"koje kaže da je potrebno sabrati brojioce i prepisati imenilac. Dobijamo: <br>" \
                        f"{fraction_ab} + {fraction_cb_b} = {fraction_acb_b} = {fraction_sum}." \

        self.options = [f"{fraction_sum}",
                        f"{fraction_incorrect1}",
                        f"{fraction_incorrect2}"]
        random.shuffle(self.options)
        self.correct_answer = f"{fraction_sum}"

        return {
            'text': self.text,
            'id': self.id,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'helps': list(enumerate(self.helps)),
            'solution': self.solution
        }




def generate_fractions_questions(number_of_questions,level):
    if level == "Lakši":
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

print(generate_fractions_questions(2,'Srednji'))
