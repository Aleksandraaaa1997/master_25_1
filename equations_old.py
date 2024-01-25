import random
import math
from math import gcd


class Easy:
    pass

class Medium:
    pass

class Hard:
    pass

class Task_e1(Easy):
    def __init__(self):
        self.id = 'equations_e1'
    def generate_variants(self):
        while True:
            first_addend = random.randint(1, 15)
            result = random.randint(10, 20)
            solution = result - first_addend

            if first_addend < result and solution > 2:
                break

            incorrect1_solution = solution+5
            incorrect2_solution = solution+1

        self.text = f"Reši jednačinu {first_addend} + x = {result}."
        self.helps = ["Rešenje jednačine je broj koji zamenjen u jednačinu prevodi jednačinu u tačnu jednakost.<br>Razmisli koji bi broj bio nepoznati sabirak.",
                      "Primeni pravilo za nepoznati sabirak koje nam govori da se nepoznati sabirak izračunava tako što se od zbira oduzme poznati sabirak."]

        self.solution = "U datoj jednačini nepoznat je sabirak.<br>" \
                        "Primenićemo pravilo za pronalaženje nepoznatog sabirka koje nam govori da se nepoznati sabirak izračunava tako što se od zbira oduzme poznati sabirak.<br><br>" \
                        f"U datoj jednačini poznati sabirak je {first_addend}, dok je zbir {result}.<br><br>" \
                        "Primenjujući pravilo za nepoznati sabirak dobijamo:<br>" \
                        f"x = {result} - {first_addend} = {solution}.<br><br>" \
                        f"Ako zamenimo nepoznati sabirak u datu jednačinu, saberemo ga sa poznatim sabirkom i dobijemo zbir {result} dobijeno rešenje je tačno.<br><br>" \
                        "Kako je:<br>" \
                        f"{first_addend} + {solution} = {result},<br>" \
                        "zaključujemo da je dobijeno rešenje tačno."


        self.options = [{solution},
                        {incorrect1_solution},
                        {incorrect2_solution}]
        random.shuffle(self.options)
        self.correct_answer = solution

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

class Task_m1(Medium):
    def __init__(self):
        self.id = 'equations_m1'
    def generate_variants(self):
        first_addend = random.randint(20, 45)
        result = random.randint(50, 100)
        solution = result - first_addend

        incorrect1_solution = solution+5
        incorrect2_solution = solution+1
        self.text = f"Reši jednačinu {first_addend} + x = {result}."
        self.helps = ["Rešenje jednačine je broj koji zamenjen u jednačinu prevodi jednačinu u tačnu jednakost.<br>Razmisli koji bi broj bio nepoznati sabirak.",
                      "Primeni pravilo za nepoznati sabirak koje nam govori da se nepoznati sabirak izračunava tako što se od zbira oduzme poznati sabirak."]

        self.solution = "U datoj jednačini nepoznat je sabirak.<br>" \
                        "Primenićemo pravilo za pronalaženje nepoznatog sabirka koje nam govori da se nepoznati sabirak izračunava tako što se od zbira oduzme poznati sabirak.<br><br>" \
                        f"U datoj jednačini poznati sabirak je {first_addend}, dok je zbir {result}.<br><br>" \
                        "Primenjujući pravilo za nepoznati sabirak dobijamo:<br>" \
                        f"x = {result} - {first_addend} = {solution}.<br><br>" \
                        f"Ako zamenimo nepoznati sabirak u datu jednačinu, saberemo ga sa poznatim sabirkom i dobijemo zbir {result} dobijeno rešenje je tačno.<br><br>" \
                        "Kako je:<br>" \
                        f"{first_addend} + {solution} = {result},<br>" \
                        "zaključujemo da je dobijeno rešenje tačno."


        self.options = [{solution},
                        {incorrect1_solution},
                        {incorrect2_solution}]
        random.shuffle(self.options)
        self.correct_answer = solution

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

class Task_h1(Hard):
    def __init__(self):
        self.id = 'equations_h1'
    def generate_variants(self):
        while True:
            first_addend_numerator = random.randint(1, 4)
            first_addend_denominator = random.randint(7, 12)

            result_numerator = random.randint(9, 13)
            result_denominator = first_addend_denominator*2

            solution_numerator = result_numerator - first_addend_numerator*2
            solution_denominator = result_denominator

            if (result_numerator-first_addend_numerator)!=(result_denominator-first_addend_denominator) and gcd(first_addend_numerator, first_addend_denominator) == 1 and gcd(result_numerator, result_denominator) == 1 and gcd(solution_numerator, solution_denominator) == 1:
                break

            fraction_first_addend = f"<math> <mfrac> <mrow> <mn>{first_addend_numerator}</mn> </mrow> <mrow> <mn>{first_addend_denominator}</mn> </mrow> </mfrac> </math>"
            fraction_result = f"<math> <mfrac> <mrow> <mn>{result_numerator}</mn> </mrow> <mrow> <mn>{result_denominator}</mn> </mrow> </mfrac> </math>"
            fraction_2_2 = "<math> <mfrac> <mrow> <mn>2</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </math>"
            fraction_first_addend_times_two = f"<math> <mfrac> <mrow> <mn>{first_addend_numerator*2}</mn> </mrow> <mrow> <mn>{first_addend_denominator*2}</mn> </mrow> </mfrac> </math>"
            fraction_solution = f"<math> <mfrac> <mrow> <mn>{solution_numerator}</mn> </mrow> <mrow> <mn>{solution_denominator}</mn> </mrow> </mfrac> </math>"
            incorrect_solution = result_numerator - first_addend_numerator
            fraction_incorrect_solution = f"<math> <mfrac> <mrow> <mn>{result_numerator-first_addend_numerator}</mn> </mrow> <mrow> <mn>{result_denominator-first_addend_denominator}</mn> </mrow> </mfrac> </math>"

        self.text = f"Reši jednačinu {fraction_first_addend} + x = {fraction_result}."
        self.helps = ["Rešenje jednačine je broj koji zamenjen u jednačinu prevodi jednačinu u tačnu jednakost.<br>Razmisli koji bi broj bio nepoznati sabirak.",
                      "Primeni pravilo za nepoznati sabirak koje nam govori da se nepoznati sabirak izračunava tako što se od zbira oduzme poznati sabirak."]

        self.solution = "U datoj jednačini nepoznat je sabirak.<br>" \
                        "Primenićemo pravilo za pronalaženje nepoznatog sabirka koje nam govori da se nepoznati sabirak izračunava tako što se od zbira oduzme poznati sabirak.<br><br>" \
                        f"U datoj jednačini poznati sabirak je {fraction_first_addend}, dok je zbir {fraction_result}.<br><br>" \
                        "Primenjujući pravilo za nepoznati sabirak dobijamo:<br>" \
                        f"x = {fraction_first_addend} - {fraction_result}.<br><br>" \
                        f"Da bi se razlomci oduzeli potrebno je svesti ih na isti imenilac.<br>" \
                        f" Kako je imenilac zbira duplo veći od imenioca poznatog sabirka, proširićemo poznati sabirak sa 2 kako bi razlomci imali iste imenioce. <br>" \
                        f"Kako bi proširili poznati sabirak sa 2 potrebno je brojilac i imenilac razlomka da pomnožimo sa 2. <br><br>" \
                        f"Nakon proširivanja dobijamo da je poznati sabirak: <br>" \
                        f"{fraction_first_addend} = {fraction_first_addend} * {fraction_2_2} = {fraction_first_addend_times_two} <br><br>" \
                        f"Primenjujući pravilo za nepoznati sabirak dobijamo:<br>" \
                        f"x = {fraction_result} - {fraction_first_addend_times_two} = {fraction_solution}.<br><br>" \
                        f"Ako zamenimo nepoznati sabirak u datu jednačinu, saberemo ga sa poznatim sabirkom i dobijemo zbir {fraction_result} dobijeno rešenje je tačno.<br><br>" \
                        "Kako je:<br>" \
                        f"{fraction_first_addend_times_two} + {fraction_solution} = {fraction_result},<br>" \
                        "zaključujemo da je dobijeno rešenje tačno."


        self.options = [{fraction_solution},
                        {incorrect_solution},
                        {fraction_incorrect_solution}]
        random.shuffle(self.options)
        self.correct_answer = fraction_solution

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

class Task_e2(Easy):
    def __init__(self):
        self.id = 'equations_e2'
    def generate_variants(self):
        subtrahend = random.randint(6, 10)
        result = random.randint(2, 5)
        ''' result = minuend - subtrahend, task: x - subtrahend = result'''

        solution = subtrahend + result
        incorrect1_solution = subtrahend - result
        incorrect2_solution = subtrahend + result + 1

        self.text = f"Reši jednačinu x - {subtrahend} = {result}."
        self.helps = ["Rešenje jednačine je broj koji zamenjen u jednačinu prevodi jednačinu u tačnu jednakost.<br>Razmisli koji bi broj bio nepoznati umanjenik.",
                      "Primeni pravilo za pronalaženje nepoznatog umanjenika koje nam govori da se nepoznati umanjenik izračunava tako što se sabere razlika i umanjilac."]

        self.solution = "U datoj jednačini nepoznat je umanjenik.<br>" \
                        "Primenićemo pravilo za pronalaženje nepoznatog umanjenika koje nam govori da se nepoznati umanjenik izračunava tako što se sabere razlika i umanjilac.<br><br>" \
                        f"U datoj jednačini umanjilac je {subtrahend}, dok je razlika {result}.<br><br>" \
                        "Primenjujući pravilo za nepoznati umanjenik dobijamo:<br>" \
                        f"x = {subtrahend} + {result} = {solution}.<br><br>" \
                        f"Ako zamenimo nepoznati umanjenik u datu jednačinu, od njega oduzmemo umanjilac i dobijemo razliku {result} dobijeno rešenje je tačno.<br><br>" \
                        "Kako je:<br>" \
                        f"{solution} - {subtrahend} = {result},<br>" \
                        "zaključujemo da je dobijeno rešenje tačno."


        self.options = [{solution},
                        {incorrect1_solution},
                        {incorrect2_solution}]
        random.shuffle(self.options)
        self.correct_answer = solution

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

class Task_m2(Medium):
    def __init__(self):
        self.id = 'equations_m2'
    def generate_variants(self):
        subtrahend = random.randint(30, 50)
        result = random.randint(20, 30)
        ''' result = minuend - subtrahend, task: x - subtrahend = result'''

        solution = subtrahend + result
        incorrect1_solution = subtrahend - result
        incorrect2_solution = subtrahend + result + 1

        self.text = f"Reši jednačinu x - {subtrahend} = {result}."
        self.helps = ["Rešenje jednačine je broj koji zamenjen u jednačinu prevodi jednačinu u tačnu jednakost.<br>Razmisli koji bi broj bio nepoznati umanjenik.",
                      "Primeni pravilo za pronalaženje nepoznatog umanjenika koje nam govori da se nepoznati umanjenik izračunava tako što se sabere razlika i umanjilac."]

        self.solution = "U datoj jednačini nepoznat je umanjenik.<br>" \
                        "Primenićemo pravilo za pronalaženje nepoznatog umanjenika koje nam govori da se nepoznati umanjenik izračunava tako što se sabere razlika i umanjilac.<br><br>" \
                        f"U datoj jednačini umanjilac je {subtrahend}, dok je razlika {result}.<br><br>" \
                        "Primenjujući pravilo za nepoznati umanjenik dobijamo:<br>" \
                        f"x = {subtrahend} + {result} = {solution}.<br><br>" \
                        f"Ako zamenimo nepoznati umanjenik u datu jednačinu, od njega oduzmemo umanjilac i dobijemo razliku {result} dobijeno rešenje je tačno.<br><br>" \
                        "Kako je:<br>" \
                        f"{solution} - {subtrahend} = {result},<br>" \
                        "zaključujemo da je dobijeno rešenje tačno."


        self.options = [{solution},
                        {incorrect1_solution},
                        {incorrect2_solution}]
        random.shuffle(self.options)
        self.correct_answer = solution

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

class Task_h2(Hard):
    def __init__(self):
        self.id = 'equations_h2'
    def generate_variants(self):
        while True:
            subtrahend = round(random.uniform(30.00, 50.99), 2)
            result = round(random.uniform(20.00, 30.99), 2)

            solution = round(subtrahend + result, 2)
            incorrect1_solution = round(subtrahend - result, 2)
            incorrect2_solution = round(subtrahend + result + 5, 2)


            if math.isclose(subtrahend, round(subtrahend, 2)) or math.isclose(result, round(result, 2)):
                break

        self.text = f"Reši jednačinu x - {subtrahend} = {result}."
        self.helps = ["Rešenje jednačine je broj koji zamenjen u jednačinu prevodi jednačinu u tačnu jednakost.<br>Razmisli koji bi broj bio nepoznati umanjenik.",
                      "Primeni pravilo za pronalaženje nepoznatog umanjenika koje nam govori da se nepoznati umanjenik izračunava tako što se sabere razlika i umanjilac."]

        self.solution = "U datoj jednačini nepoznat je umanjenik.<br>" \
                        "Primenićemo pravilo za pronalaženje nepoznatog umanjenika koje nam govori da se nepoznati umanjenik izračunava tako što se sabere razlika i umanjilac.<br><br>" \
                        f"U datoj jednačini umanjilac je {subtrahend}, dok je razlika {result}.<br><br>" \
                        "Primenjujući pravilo za nepoznati umanjenik dobijamo:<br>" \
                        f"x = {subtrahend} + {result} = {solution}.<br><br>" \
                        f"Ako zamenimo nepoznati umanjenik u datu jednačinu, od njega oduzmemo umanjilac i dobijemo razliku {result} dobijeno rešenje je tačno.<br><br>" \
                        "Kako je:<br>" \
                        f"{solution} - {subtrahend} = {result},<br>" \
                        "zaključujemo da je dobijeno rešenje tačno."


        self.options = [{solution},
                        {incorrect1_solution},
                        {incorrect2_solution}]
        random.shuffle(self.options)
        self.correct_answer = solution

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

class Task_e3(Easy):
    def __init__(self):
        self.id = 'equations_e3'
    def generate_variants(self):
        minuend = random.randint(9, 15)
        result = random.randint(2, 6)
        ''' result = minuend - subtrahend, task: minuend - x = result'''

        solution = minuend - result
        incorrect1_solution = minuend + result
        incorrect2_solution = result - minuend

        self.text = f"Reši jednačinu {minuend} - x = {result}."
        self.helps = ["Rešenje jednačine je broj koji zamenjen u jednačinu prevodi jednačinu u tačnu jednakost.<br>Razmisli koji bi broj bio nepoznati umanjilac.",
                      "Primeni pravilo za pronalaženje nepoznatog umanjioca, koje nam govori da se nepoznati umanjilac izračunava tako što se od umanjenika oduzme razlika."]

        self.solution = "U datoj jednačini nepoznat je umanjilac.<br>" \
                        "Primenićemo pravilo za pronalaženje nepoznatog umanjioca, koje nam govori da se nepoznati umanjilac izračunava tako što se od umanjenika oduzme razlika.<br><br>" \
                        f"U datoj jednačini umanjenik je {minuend}, dok je razlika {result}.<br><br>" \
                        "Primenjujući pravilo za nepoznati umanjilac dobijamo:<br>" \
                        f"x = {minuend} + {result} = {solution}.<br><br>" \
                        f"Ako zamenimo nepoznati umanjilac u datu jednačinu, od umanjika oduzmemo dobijeni umanjilac i dobijemo razliku {result} dobijeno rešenje je tačno.<br><br>" \
                        "Kako je:<br>" \
                        f"{minuend} - {solution} = {result},<br>" \
                        "zaključujemo da je dobijeno rešenje tačno."


        self.options = [{solution},
                        {incorrect1_solution},
                        {incorrect2_solution}]
        random.shuffle(self.options)
        self.correct_answer = solution

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

class Task_m3(Medium):
    def __init__(self):
        self.id = 'equations_m3'
    def generate_variants(self):
        minuend = random.randint(50, 100)
        result = random.randint(10, 30)
        ''' result = minuend - subtrahend, task: minuend - x = result'''

        solution = minuend - result
        incorrect1_solution = minuend + result
        incorrect2_solution = result - minuend

        self.text = f"Reši jednačinu {minuend} - x = {result}."
        self.helps = ["Rešenje jednačine je broj koji zamenjen u jednačinu prevodi jednačinu u tačnu jednakost.<br>Razmisli koji bi broj bio nepoznati umanjilac.",
                      "Primeni pravilo za pronalaženje nepoznatog umanjioca, koje nam govori da se nepoznati umanjilac izračunava tako što se od umanjenika oduzme razlika."]

        self.solution = "U datoj jednačini nepoznat je umanjilac.<br>" \
                        "Primenićemo pravilo za pronalaženje nepoznatog umanjioca, koje nam govori da se nepoznati umanjilac izračunava tako što se od umanjenika oduzme razlika.<br><br>" \
                        f"U datoj jednačini umanjenik je {minuend}, dok je razlika {result}.<br><br>" \
                        "Primenjujući pravilo za nepoznati umanjilac dobijamo:<br>" \
                        f"x = {minuend} + {result} = {solution}.<br><br>" \
                        f"Ako zamenimo nepoznati umanjilac u datu jednačinu, od umanjika oduzmemo dobijeni umanjilac i dobijemo razliku {result} dobijeno rešenje je tačno.<br><br>" \
                        "Kako je:<br>" \
                        f"{minuend} - {solution} = {result},<br>" \
                        "zaključujemo da je dobijeno rešenje tačno."


        self.options = [{solution},
                        {incorrect1_solution},
                        {incorrect2_solution}]
        random.shuffle(self.options)
        self.correct_answer = solution

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}

class Task_h3(Hard):
    def __init__(self):
        self.id = 'equations_h3'
    def generate_variants(self):
        while True:
            ''' result = minuend - subtrahend, task: minuend - x = result'''
            minuend = round(random.uniform(50.00, 100.99), 2)
            result = round(random.uniform(10.00, 30.99), 2)

            solution = round(minuend - result, 2)
            incorrect1_solution = round(minuend + result, 2)
            incorrect2_solution = round(result - minuend + 5, 2)


            if math.isclose(minuend, round(subtrahend, 2)) or math.isclose(result, round(result, 2)):
                break

        self.text = f"Reši jednačinu {minuend} - x = {result}."
        self.helps = ["Rešenje jednačine je broj koji zamenjen u jednačinu prevodi jednačinu u tačnu jednakost.<br>Razmisli koji bi broj bio nepoznati umanjilac.",
                      "Primeni pravilo za pronalaženje nepoznatog umanjioca, koje nam govori da se nepoznati umanjilac izračunava tako što se od umanjenika oduzme razlika."]

        self.solution = "U datoj jednačini nepoznat je umanjilac.<br>" \
                        "Primenićemo pravilo za pronalaženje nepoznatog umanjioca, koje nam govori da se nepoznati umanjilac izračunava tako što se od umanjenika oduzme razlika.<br><br>" \
                        f"U datoj jednačini umanjenik je {minuend}, dok je razlika {result}.<br><br>" \
                        "Primenjujući pravilo za nepoznati umanjilac dobijamo:<br>" \
                        f"x = {minuend} + {result} = {solution}.<br><br>" \
                        f"Ako zamenimo nepoznati umanjilac u datu jednačinu, od umanjika oduzmemo dobijeni umanjilac i dobijemo razliku {result} dobijeno rešenje je tačno.<br><br>" \
                        "Kako je:<br>" \
                        f"{minuend} - {solution} = {result},<br>" \
                        "zaključujemo da je dobijeno rešenje tačno."


        self.options = [{solution},
                        {incorrect1_solution},
                        {incorrect2_solution}]
        random.shuffle(self.options)
        self.correct_answer = solution

        return {'text': self.text, 'id': self.id, 'options': self.options, 'correct_answer': self.correct_answer,
             'helps': list(enumerate(self.helps)), 'solution': self.solution}
