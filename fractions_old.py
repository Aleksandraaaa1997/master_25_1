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
        self.text = f"Razlomak <math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>" \
                    f"proširiti sa {c}."
        self.helps = ["Proširivanje razlomka treba da te asocira na množenje ralomka sa određenim brojem.",
                      "Prilikom proširivanja razlomka sa određenim brojem, potrebno je pomnožiti imenilac i "
                      "brojilac razlomka sa tim brojem. <br>Primeni to na proširivanje razlomka "
                      f"<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math> sa brojem {c}"]

        self.solution = "Prilikom proširivanja razlomka sa određenim brojem, potrebno je pomnožiti imenilac i " \
                        "brojilac razlomka sa tim brojem.<br>Kako bi proširili razlomak " \
                        f"<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math> sa brojem {c}" \
                        f"potrebno je da pomnožimo brojilac i imenilac razlomka sa {c}.<br>Dobijamo :<br>" \
                        f"<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> <mo>*</mo>" \
                        f"<mfrac> <mrow> <mn>{c}</mn> </mrow> <mrow> <mn>{c}</mn> </mrow> </mfrac> </math> = " \
                        f"<math> <mfrac> <mrow> <mn>{a}</mn> <mo>*</mo><mn>{c}</mn> </mrow> <mrow> <mn>{b}</mn> <mo>*</mo><mn>{c}</mn> </mrow> </mfrac> </math>" \
                        f"= <math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math><br>" \
                        f"Razlomak <math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math> " \
                        f"proširen sa {c} je <math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math>"
        self.options = [f"<math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math>",
                        f"<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math>",
                        f"<math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>"]
        random.shuffle(self.options)
        self.correct_answer = f"<math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math>"

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

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
        self.text = f"Razlomak <math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>" \
                    f"proširiti sa {c}."
        self.helps = ["Proširivanje razlomka treba da te asocira na množenje ralomka sa određenim brojem.",
                      "Prilikom proširivanja razlomka sa određenim brojem, potrebno je pomnožiti imenilac i "
                      "brojilac razlomka sa tim brojem. <br>Primeni to na proširivanje razlomka "
                      f"<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math> sa brojem {c}"]

        self.solution = "Prilikom proširivanja razlomka sa određenim brojem, potrebno je pomnožiti imenilac i " \
                        "brojilac razlomka sa tim brojem.<br>Kako bi proširili razlomak " \
                        f"<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math> sa brojem {c}" \
                        f"potrebno je da pomnožimo brojilac i imenilac razlomka sa {c}.<br>Dobijamo :<br>" \
                        f"<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> <mo>*</mo>" \
                        f"<mfrac> <mrow> <mn>{c}</mn> </mrow> <mrow> <mn>{c}</mn> </mrow> </mfrac> </math> = " \
                        f"<math> <mfrac> <mrow> <mn>{a}</mn> <mo>*</mo><mn>{c}</mn> </mrow> <mrow> <mn>{b}</mn> <mo>*</mo><mn>{c}</mn> </mrow> </mfrac> </math>" \
                        f"= <math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math><br>" \
                        f"Razlomak <math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math> " \
                        f"proširen sa {c} je <math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math>"
        self.options = [f"<math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math>",
                        f"<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math>",
                        f"<math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>"]
        random.shuffle(self.options)
        self.correct_answer = f"<math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math>"

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

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
        fraction_ab = f'<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>'
        fraction_acbc = f'<math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math>'
        fraction_cc = f'<math> <mfrac> <mrow> <mn>{c}</mn> </mrow> <mrow> <mn>{c}</mn> </mrow> </mfrac> </math>'
        fraction_ac_bc = f'<math> <mfrac> <mrow> <mn>{a}</mn> <mo>*</mo> <mn>{c}</mn> </mrow> <mrow> <mn>{b}</mn> <mo>*</mo> <mn>{c}</mn> </mrow> </mfrac> </math>'
        self.text = f"Sa kojim brojem treba proširiti razlomak {fraction_ab}" \
                    f"tako da prošireni razlomak bude {fraction_acbc}"
        self.helps = ["Proširivanje razlomka treba da te asocira na množenje ralomka sa određenim brojem.",
                      "Prilikom proširivanja razlomka sa određenim brojem, potrebno je pomnožiti imenilac i "
                      "brojilac razlomka sa tim brojem. <br>Kako bi pronašao broj koji treba pomnožiti sa "
                      f"{fraction_ab} razmisli"
                      f"o deljenju proširenog imenioca sa neproširenim imeniocem odnosno deljenjem brojioca sa "
                      f"neproširenim brojiocem"]

        self.solution = "Prilikom proširivanja razlomka sa određenim brojem, potrebno je pomnožiti imenilac i brojilac razlomka sa tim brojem. <br>" \
                        f"Kako bi pronašali vrednost koju treba pomnožiti sa {fraction_ab}" \
                        f" kako bi dobili {fraction_acbc} jedan od načina" \
                        " je da podelimo prošireni imenilac sa neproširenim imeniocem, odnosno da podelimo prošireni brojilac sa neproširenim brojiocem.<br><br>" \
                        f"Kako je {a*c}/{a} = {c}, kao i {b*c}/{b} = {c}, dobijemo da je razlomak {fraction_ab} potrebno da proširimo sa {c}" \
                        f" kako bi dobili razlomak {fraction_acbc}.<br><br>Proverićemo da je razlomak {fraction_ab} proširen sa {c}" \
                        f" jednak razlomku {fraction_acbc}.<br>" \
                        f"{fraction_ab}*{fraction_cc}={fraction_ac_bc}={fraction_acbc}"
        self.options = [f"{c}",
                        f"{a*c-a}",
                        f"{c+1}"]
        random.shuffle(self.options)
        self.correct_answer = f"{c}"

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

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
        fraction_ab = f'<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>'
        fraction_acbc = f'<math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math>'
        self.text = f"Skratiti razlomak {fraction_acbc}."
        self.helps = ["Skraćivanje razlomka treba da te asocira na deljenje imenioca i brojioca nekim brojem. Razmisli koji bi to broj bio.",
                      f"Razlomak možes skratiti samo brojem koji deli i brojilac i imenilac.<br>"
                      f"Razmisli o pronalaženju najvećeg zajedničkog delioca za brojeve {a*c} i {b*c}."]

        self.solution = "Razlomak možeš skratiti samo brojem koji deli i brojilac i imenilac.<br>" \
                        f"Kako je najveći zajednički delilac za brojeve {a*c} i {b*c} broj {c}," \
                        f" zaključujemo da razlomak {fraction_acbc} možemo da skratimo sa {c}.<br><br>" \
                        f"Podelićemo imenilac i brojilac brojem {c}:<br>" \
                        f"{fraction_acbc} = <math> <mfrac> <mrow> <mn>{a*c}</mn> <mo>/</mo> <mn>{c}</mn>" \
                        f" </mrow> <mrow> <mn>{b*c}</mn> <mo>/</mo> <mn>{c}</mn> </mrow> </mfrac> </math> = {fraction_ab}." \
                        f"<br><br>Nakon skraćivanja razlomka {fraction_acbc} dobijamo razlomak {fraction_ab}."
        self.options = [f"{fraction_ab}",
                        f"<math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>",
                        f"<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math>"]
        random.shuffle(self.options)
        self.correct_answer = f"{fraction_ab}"

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

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
        fraction_ab = f'<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>'
        fraction_acbc = f'<math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math>'
        self.text = f"Skratiti razlomak {fraction_acbc}."
        self.helps = ["Skraćivanje razlomka treba da te asocira na deljenje imenioca i brojioca nekim brojem. Razmisli koji bi to broj bio.",
                      f"Razlomak možes skratiti samo brojem koji deli i brojilac i imenilac.<br>"
                      f"Razmisli o pronalaženju najvećeg zajedničkog delioca za brojeve {a*c} i {b*c}."]

        self.solution = "Razlomak možeš skratiti samo brojem koji deli i brojilac i imenilac.<br>" \
                        f"Kako je najveći zajednički delilac za brojeve {a*c} i {b*c} broj {c}," \
                        f" zaključujemo da razlomak {fraction_acbc} možemo da skratimo sa {c}.<br><br>" \
                        f"Podelićemo imenilac i brojilac brojem {c}:<br>" \
                        f"{fraction_acbc} = <math> <mfrac> <mrow> <mn>{a*c}</mn> <mo>/</mo> <mn>{c}</mn>" \
                        f" </mrow> <mrow> <mn>{b*c}</mn> <mo>/</mo> <mn>{c}</mn> </mrow> </mfrac> </math> = {fraction_ab}." \
                        f"<br><br>Nakon skraćivanja razlomka {fraction_acbc} dobijamo razlomak {fraction_ab}."
        self.options = [f"{fraction_ab}",
                        f"<math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>",
                        f"<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math>"]
        random.shuffle(self.options)
        self.correct_answer = f"{fraction_ab}"

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

class Task_h2(Hard):
    def __init__(self):
        self.id = 'fractions_h2'
    def generate_variants(self):
        while True:
            a = random.randint(11, 30)
            b = random.randint(11, 30)
            d = random.randint(a+1, a+10)
            if a < b and gcd(a, b) == 1 and d < b and gcd(d, b) == 1:
                break
        c = random.choice([2, 3, 5])
        fraction_ab = f'<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>'
        fraction_acbc = f'<math> <mfrac> <mrow> <mn>{a*c}</mn> </mrow> <mrow> <mn>{b*c}</mn> </mrow> </mfrac> </math>'
        frction_db = f'<math> <mfrac> <mrow> <mn>{d}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>'
        self.text = f"Skratiti razlomak {fraction_acbc} i uporediti ga sa {frction_db}."
        self.helps = ["Skraćivanje razlomka treba da te asocira na deljenje imenioca i brojioca nekim brojem. Razmisli koji bi to broj bio.<br>"
                      "Upoređivanje 2 razlomka treba da te asocira na analiziranje vrednosti razlomaka radi utvrđivanja njihovog odnosa.",
                      f"Razlomak možes skratiti samo brojem koji deli i brojilac i imenilac.<br>"
                      f"Razmisli o pronalaženju najvećeg zajedničkog delioca za brojeve {a*c} i {b*c}.<br>"
                      f"S' obzirom da razlomci imaju iste imenioce dovoljno je uporediti brojioce i zaključiti u kakvom su odnosu."]

        self.solution = "Razlomak možeš skratiti samo brojem koji deli i brojilac i imenilac.<br>" \
                        f"Kako je najveći zajednički delilac za brojeve {a*c} i {b*c} broj {c}," \
                        f" zaključujemo da razlomak {fraction_acbc} možemo da skratimo sa {c}.<br><br>" \
                        f"Podelićemo imenilac i brojilac brojem {c}:<br>" \
                        f"{fraction_acbc} = <math> <mfrac> <mrow> <mn>{a*c}</mn> <mo>/</mo> <mn>{c}</mn>" \
                        f" </mrow> <mrow> <mn>{b*c}</mn> <mo>/</mo> <mn>{c}</mn> </mrow> </mfrac> </math> = {fraction_ab}." \
                        f"<br><br>Nakon skraćivanja razlomka {fraction_acbc} dobijamo razlomak {fraction_ab}.<br><br>" \
                        f"Ako uporedimo skraćeni razlomak {fraction_ab} i {frction_db}, s' obzirom da imaju isti imenilac, " \
                        f"zaključujemo da je {frction_db} veće od skraćenog razlomka jer je {d} veće od {a}."
        self.options = [f"{fraction_ab} i {fraction_acbc} < {frction_db}",
                        f"{fraction_ab} i {fraction_acbc} > {frction_db}",
                        f"{frction_db} i {fraction_acbc} = {frction_db}"]
        random.shuffle(self.options)
        self.correct_answer = f"{fraction_ab} i {fraction_acbc} < {frction_db}"

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

class Task_e3(Easy):
    def __init__(self):
        self.id = 'fractions_e3'
    def generate_variants(self):
        while True:
            a = random.randint(2, 9)
            b = random.randint(2, 13)
            c = random.randint(2, 9)
            d = b
            if a < b and gcd(a, b) == 1 and c < d and gcd(c, d) == 1 and gcd(a+c, d) == 1 and (a+c) < d and gcd(a+c, d+b) == 1:
                break
        fraction_ab = f'<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>'
        fraction_cd = f'<math> <mfrac> <mrow> <mn>{c}</mn> </mrow> <mrow> <mn>{d}</mn> </mrow> </mfrac> </math>'
        fraction_ac_d = f'<math> <mfrac> <mrow> <mn>{a}</mn> <mo>+</mo> <mn>{c}</mn> </mrow> <mrow> <mn>{d}</mn> </mrow> </mfrac> </math>'
        fraction_sum = f'<math> <mfrac> <mrow> <mn>{a+c}</mn> </mrow> <mrow> <mn>{d}</mn> </mrow> </mfrac> </math>'
        fraction_incorrect = f'<math> <mfrac> <mrow> <mn>{a + c}</mn> </mrow> <mrow> <mn>{d+b}</mn> </mrow> </mfrac> </math>'
        self.text = f"Saberi razlomke {fraction_ab} i {fraction_cd}."
        self.helps = ["Primeti da razlomci imaju iste imenioce. Razmisli kako se sabiraju razlomci koji imaju iste imenioce.",
                      "Razlomci koji imaju iste imenioce sabiraju se tako što se brojioci saberu, a imenilac prepiše."]

        self.solution = "Razlomci koji imaju iste imenioce sabiraju se tako što se brojioci saberu, a imenilac prepiše. Nakon primene pravila dobijamo:" \
                        f"{fraction_ab} + {fraction_cd} = {fraction_ac_d} = {fraction_sum}."
        self.options = [f"{fraction_sum}",
                        f"{fraction_incorrect}",
                        1]
        random.shuffle(self.options)
        self.correct_answer = f"{fraction_sum}"

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

class Task_m3(Medium):
    def __init__(self):
        self.id = 'fractions_m3'
    def generate_variants(self):
        while True:
            d = random.randint(4, 12)
            b = 2*d
            a = random.randint(1, b-1)
            c = random.randint(1, d - 1)
            if gcd(a, b) == 1 and gcd(c, d) == 1 and gcd(a+2*c, b) == 1:
                break
        fraction_ab = f'<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>'
        fraction_cd = f'<math> <mfrac> <mrow> <mn>{c}</mn> </mrow> <mrow> <mn>{d}</mn> </mrow> </mfrac> </math>'
        fraction_22 = '<math> <mfrac> <mrow> <mn>2</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </math>'
        fraction_c2d2 = f'<math> <mfrac> <mrow> <mn>{c}</mn> <mo>*</mo> 2 </mrow> <mrow> <mn>{d}</mn> <mo>*</mo> 2 </mrow> </mfrac> </math>'
        fraction_c2_d2 = f'<math> <mfrac> <mrow> <mn>{c*2}</mn> </mrow> <mrow> <mn>{d*2}</mn> </mrow> </mfrac> </math>'
        fraction_sum = f'<math> <mfrac> <mrow> <mn>{a + c * 2}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>'
        fraction_incorrect1 = f'<math> <mfrac> <mrow> <mn>{a + c}</mn> </mrow> <mrow> <mn>{b+d}</mn> </mrow> </mfrac> </math>'
        fraction_incorrect2 = f'<math> <mfrac> <mrow> <mn>{b}</mn> </mrow> <mrow> <mn>{a + c * 2}</mn> </mrow> </mfrac> </math>'
        self.text = f"Saberi razlomke {fraction_ab} i {fraction_cd}."
        self.helps = ["Primeti da razlomci nemaju iste imenioce. Razmisli kako se sabiraju razlomci koji nemaju iste imenioce.",
                      "Razlomci koji nemaju iste imenioce sabiraju se tako što se svedu na iste imenioce."]

        self.solution = "Razlomci koji nemaju iste imenioce sabiraju se tako što se svedu na iste imenioce. <br>" \
                        "Kako je imenilac prvog razlomka duplo veći od imenioca drugog razlomka, proširićemo drugi razlomak sa 2:<br>" \
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

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

class Task_h3(Hard):
    def __init__(self):
        self.id = 'fractions_h3'
    def generate_variants(self):
        while True:
            b = random.randint(2, 8)
            a = random.randint(1, b-1)
            c = random.randint(2, 9)
            if gcd(a, b) == 1 and gcd(a + c*b, b) == 1 and gcd(a + c, b) == 1:
                break
        fraction_ab = f'<math> <mfrac> <mrow> <mn>{a}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>'
        fraction_cb_1b = f'<math> <mfrac> <mrow> <mn>{c}</mn> <mo>*</mo> <mn>{b}</mn> </mrow> <mrow> <mn>1</mn> <mo>*</mo> <mn>{b}</mn> </mrow> </mfrac> </math>'
        fraction_cb_b = f'<math> <mfrac> <mrow> <mn>{c * b}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>'
        fraction_c_1 = f'<math> <mfrac> <mrow> <mn>{c}</mn> </mrow> <mrow> <mn>1</mn> </mrow> </mfrac> </math>'
        fraction_b_b = f'<math> <mfrac> <mrow> <mn>{b}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>'
        fraction_acb_b = f'<math> <mfrac> <mrow> <mn>{a}</mn> <mo>+</mo> <mn>{c*b}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>'
        fraction_sum = f'<math> <mfrac> <mrow> <mn>{a + c * b}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>'
        fraction_incorrect1 = f'<math> <mfrac> <mrow> <mn>{a + c}</mn> </mrow> <mrow> <mn>{b}</mn> </mrow> </mfrac> </math>'
        fraction_incorrect2 = f'{a + c}'

        self.text = f"Saberi razlomak {fraction_ab} i broj {c}."
        self.helps = ["Razmisli kako sabiraš ceo broj i razlomak. Potrebno je da ceo broj predstaviš u obliku razlomka.",
                      "Ceo broj i razlomak sabiraš tako što dati broj predstaviš u obliku razlomka koji ima isti imenilac kao dati razlomak. Zatim ih sabereš kao dva razlomka"
                      "sa istim imeniocem."]

        self.solution = "Ceo broj i razlomak sabiraš tako što dati broj predstaviš u obliku razlomka koji ima isti imenilac kao dati razlomak. <br>" \
                        "Zatim ih sabereš kao dva razlomka sa istim imeniocem. <br>" \
                        f"Predstavićemo broj u obliku razlomka koji ima isti imenilac kao dati razlomak, odnosno da mu je imenilac broj {b}:<br>" \
                        f"Broj {c} možemo da predstavimo kao razlomak {fraction_c_1}, i zatim da ga proširimo sa {b}." \
                        f"Dobijamo: <br>" \
                        f"{fraction_c_1} * {fraction_b_b} = {fraction_cb_1b} = {fraction_cb_b}. <br>" \
                        f"Kako sada razlomci {fraction_ab} i {fraction_cb_b} imaju iste imenioce sabraćemo ih primenjujući pravilo o sabiranju razlomaka koji imaju iste imenioce," \
                        f"koje kaže da je potrebno sabrati brojioce i prepisati imenilac. Dobijamo: <br>" \
                        f"{fraction_ab} + {fraction_cb_b} = {fraction_acb_b} = {fraction_sum}." \

        self.options = [f"{fraction_sum}",
                        f"{fraction_incorrect1}",
                        f"{fraction_incorrect2}"]
        random.shuffle(self.options)
        self.correct_answer = f"{fraction_sum}"

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}


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
