from email.mime.text import MIMEText
from datetime import datetime
import random
import os
import logging
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail, Message
from user import User, is_username_email_taken, token_verification,delete_user_by_email,user_authentication, mongo
from my_fractions import generate_fractions_questions
from equations import generate_equations_questions
from functions import generate_functions_questions
import pdfcrowd
from flask import Flask, render_template
import pdfkit

# Set the logging level to DEBUG
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Initialize Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'master.aleksandra.pmf@gmail.com'
app.config['MAIL_PASSWORD'] = 'ltdexnaravrozhvl'

mail = Mail(app)

@app.route('/home')
@app.route('/')
def home():
    """
    Prikazuje početnu stranicu u kojoj korisnik može da odabere da li
    će da koristi aplikaciju kao učenik ili kao profesor.
    :return:
               - home.html
    """
    return render_template('home.html')

@app.route('/task_descriptions')
def task_descriptions():
    """
    Prikazuje početnu stranicu u kojoj korisnik može da odabere da li
    će da koristi aplikaciju kao učenik ili kao profesor.
    :return:
               - task_descriptions.html
    """
    return render_template('task_descriptions.html')

@app.route('/fractions_info')
def fractions_info():
    """
    Prikazuje početnu stranicu u kojoj korisnik može da odabere da li
    će da koristi aplikaciju kao učenik ili kao profesor.
    :return:
               - fractions_info.html
    """
    return render_template('fractions_info.html')

@app.route('/equations_info')
def equations_info():
    """
    Prikazuje početnu stranicu u kojoj korisnik može da odabere da li
    će da koristi aplikaciju kao učenik ili kao profesor.
    :return:
               - equations_info.html
    """
    return render_template('equations_info.html')

@app.route('/graph_info')
def graph_info():
    """
    Prikazuje početnu stranicu u kojoj korisnik može da odabere da li
    će da koristi aplikaciju kao učenik ili kao profesor.
    :return:
               - graph_info.html
    """
    return render_template('graph_info.html')

@app.route('/fractions_info_easy')
def fractions_info_easy():
    """
    Prikazuje početnu stranicu u kojoj korisnik može da odabere da li
    će da koristi aplikaciju kao učenik ili kao profesor.
    :return:
               - fractions_info_easy.html
    """
    return render_template('fractions_info_easy.html')

@app.route('/fractions_info_medium')
def fractions_info_medium():
    """
    Prikazuje početnu stranicu u kojoj korisnik može da odabere da li
    će da koristi aplikaciju kao učenik ili kao profesor.
    :return:
               - fractions_info_medium.html
    """
    return render_template('fractions_info_medium.html')

@app.route('/fractions_info_hard')
def fractions_info_hard():
    """
    Prikazuje početnu stranicu u kojoj korisnik može da odabere da li
    će da koristi aplikaciju kao učenik ili kao profesor.
    :return:
               - fractions_info_hard.html
    """
    return render_template('fractions_info_hard.html')

@app.route('/equations_info_easy')
def equations_info_easy():
    """
    Prikazuje početnu stranicu u kojoj korisnik može da odabere da li
    će da koristi aplikaciju kao učenik ili kao profesor.
    :return:
               - equations_info_easy.html
    """
    return render_template('equations_info_easy.html')

@app.route('/equations_info_medium')
def equations_info_medium():
    """
    Prikazuje početnu stranicu u kojoj korisnik može da odabere da li
    će da koristi aplikaciju kao učenik ili kao profesor.
    :return:
               - equations_info_medium.html
    """
    return render_template('equations_info_medium.html')

@app.route('/equations_info_hard')
def equations_info_hard():
    """
    Prikazuje početnu stranicu u kojoj korisnik može da odabere da li
    će da koristi aplikaciju kao učenik ili kao profesor.
    :return:
               - equations_info_hard.html
    """
    return render_template('equations_info_hard.html')

@app.route('/graph_info_easy')
def graph_info_easy():
    """
    Prikazuje početnu stranicu u kojoj korisnik može da odabere da li
    će da koristi aplikaciju kao učenik ili kao profesor.
    :return:
               - graph_info_easy.html
    """
    return render_template('graph_info_easy.html')

@app.route('/graph_info_medium')
def graph_info_medium():
    """
    Prikazuje početnu stranicu u kojoj korisnik može da odabere da li
    će da koristi aplikaciju kao učenik ili kao profesor.
    :return:
               - graph_info_medium.html
    """
    return render_template('graph_info_medium.html')


@app.route('/graph_info_hard')
def graph_info_hard():
    """
    Prikazuje početnu stranicu u kojoj korisnik može da odabere da li
    će da koristi aplikaciju kao učenik ili kao profesor.
    :return:
               - graph_info_hard.html
    """
    return render_template('graph_info_hard.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    """
    Prikazuje registracionu stranicu profesore. Profesor unosi svoje
    korisničko ime, email, šifru i ponovljenu šifru. Klikom na dugme
    'Registruj se' aplikacija proveri da li postoji profesor sa već
    iskorištenim datim korisničkim imenom i emailom. Ako postoji
    aplikacija će na to upozoriti korisnika a ako ne postoji poslaće
    verifikacioni email na profesorovu email adresu da on završi registraciju.
    :return:
            - register.html
            - registration_successful.html
            - registration_failed.html
    """
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        result = is_username_email_taken(username,email)
        if result["username_taken_verified"] or result["email_taken_verified"]:
            return render_template('register.html', username_taken=result["username_taken_verified"],
                                   email_taken=result["email_taken_verified"], token_problems = False)

        if result["username_taken"]:
            return render_template('register.html', username_taken=True, email_taken=False, token_problems = False)

        if result["email_taken"]:
            delete_user_by_email(email)

        usr = User(username,email,password)

        msg = Message("Verification Email", sender='noreply@demo.com', recipients=[email])
        msg.body = f'Click the following link to verify your account for user {username}:' \
                   f' https://masteraleksandra251.azurewebsites.net/verify/{usr.token_data["token"]}'

        try:
            mail.send(msg)
            app.logger.info('Poslata poruka')
            return render_template('registration_successful.html',text='Potvrdite svoju email'
                                                                       ' adresu ulaskom na link koji vam je poslat'
                                                                       ' na nju' , heading = "Uspesna registracija")

        except Exception as e:
            app.logger.error(f"Error sending email: {e}")
            return render_template('registration_failed.html',text = 'Neuspesna registracija molim vas proverite da li'
                                                                     ' je uneti mail odgovarajuci.')

    elif request.method == 'GET':
        return render_template('register.html',username_taken = False, email_taken=False, token_problems = False)


@app.route('/login_prof', methods=['POST','GET'])
def login_prof():
    """
    Omogućava profesoru da se prijavi na svoj nalog sa svojim
    korisničkim imenom i loyinkom ili da se regisruje ako
    ne posjeduje svoj profil.
    :return:
            - login_prof.html
            - test_or_results.html
    """
    input_data = {}
    if request.method == 'GET':
        return render_template('login_prof.html',input_data = input_data)
    elif request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        result = user_authentication(username,password)

        if result['user_authentication']:
            session['username'] = username
            return redirect(url_for('test_or_results'))

        if not result['user_exist']:
            input_data['username_exist'] = True
            return render_template('login_prof.html',input_data = input_data)

        if not result['user_verified']:
            input_data['user_not_verified'] = True
            return render_template('login_prof.html',input_data = input_data)

        if not result['user_authentication']:
            input_data['user_wrong_pass'] = True
            return render_template('login_prof.html',input_data = input_data)



@app.route('/verify/<token>')
def verify_token(token):
    """
    Završava verifikaciju profesora klikom na link koji je dobio
    na svoju email adresu.
    :param token: jedinstveni generisani token
    :return:
            - login_prof.html
            - register.html
    """
    try:
        result = token_verification(token)

        if result:
            input_data = {}
            input_data['verified_token'] = True
            return render_template('login_prof.html', input_data=input_data)
    except:
        return render_template('register.html', username_taken=False, email_taken=False, token_problems=True)

@app.route('/compose_test', methods=['GET'])
def compose_test():
    """
    Omogućava profesoru da sastavi kontolni rad dozvoljavajući mu da
    odredi informacije kao što su:
        - naziv kontrolnog rada
        - potrebno vreme za rad
        - datum i vreme od kada je konrolni rad aktivan
        - datum i vreme do kada je kontrolni rad aktivan
        - oblasti iz kojih želi da su zadaci na testu, njihovu
          količinu i težinu
    :return:
            - compose_test.html
            - registration_successful.html
    """
    if request.method == 'GET':
        areas = ['Razlomci', 'Jednačine', 'Funkcije i grafici']
        difficulty = ['Lak', 'Srednji', 'Težak']
        quantity = [i for i in range(1, 4)]
        return render_template('compose_test.html', areas=areas, difficulty=difficulty, quantity=quantity)

@app.route('/verify_test', methods=['POST', 'GET'])
def verify_test():
    months = enumerate(['Januar', 'Februar', 'Mart', 'April', 'Maj', 'Jun', 'Jul', 'Avgust', 'Septembar', 'Oktobar', 'Novembar', 'Decembar'],start = 1)
    try:
        print("tetstetst")
        start_day = int(request.form.get('start_day'))
        test_name = request.form.get('testName')
        session['test_name'] = test_name
        session['start_day'] = start_day
        start_month = request.form.get('start_month')
        session['start_month'] = start_month
        start_year = request.form.get('start_year')
        session['start_year'] = start_year
        start_hours = int(request.form.get('start_hours'))
        session['start_hours'] = start_hours
        start_minutes = int(request.form.get('start_minutes'))
        session['start_minutes'] = start_minutes
        end_day = int(request.form.get('end_day'))
        session['end_day'] = end_day
        end_month = request.form.get('end_month')
        session['end_month'] = end_month
        end_year = request.form.get('end_year')
        session['end_year'] = end_year
        end_hours = int(request.form.get('end_hours'))
        session['end_hours'] = end_hours
        end_minutes = int(request.form.get('end_minutes'))
        session['end_minutes'] = end_minutes
        allowed_time = request.form.get('vremeZaRad')
        session['allowed_time'] = allowed_time
        areas = request.form.getlist('area_name')
        session['areas'] = areas
        difficultys = request.form.getlist('difficulty_name')
        session['difficultys'] = difficultys
        quantitys = request.form.getlist('quantity_name')
        session['quantitys'] = quantitys
    except:
        print("greska")
        test_name = session['test_name']
        start_day = session['start_day']
        start_month = session['start_month']
        start_year = session['start_year']
        start_hours = session['start_hours']
        start_minutes = session['start_minutes']
        end_day = session['end_day']
        end_month = session['end_month']
        end_year = session['end_year']
        end_hours = session['end_hours']
        end_minutes = session['end_minutes']
        allowed_time = session['allowed_time']
        areas = session['areas']
        difficultys = session['difficultys']
        quantitys = session['quantitys']
    for i ,m in months:
        if m == start_month:
            start_month_num = i
        if m == end_month:
            end_month_num = i

    # Convert input date and time components to a datetime object
    start_datetime_str = f"{start_year}-{start_month_num:02d}-{start_day:02d}T{start_hours:02d}:{start_minutes:02d}"
    end_datetime_str = f"{end_year}-{end_month_num:02d}-{end_day:02d}T{end_hours:02d}:{end_minutes:02d}"

    # Parse the datetime strings into datetime objects
    start_datetime = datetime.fromisoformat(start_datetime_str)
    end_datetime = datetime.fromisoformat(end_datetime_str)

    # Format the datetime objects to the desired string format
    formatted_start_datetime = start_datetime.strftime("%Y-%m-%dT%H:%M")
    session['formatted_start_datetime'] = formatted_start_datetime
    formatted_end_datetime = end_datetime.strftime("%Y-%m-%dT%H:%M")
    session['formatted_end_datetime'] = formatted_end_datetime

    # Print the obtained values
    app.logger.info(f'Ime kontrolnog: {test_name}')
    app.logger.info(f'Start Date: {formatted_start_datetime}')
    app.logger.info(f'End Date: {formatted_end_datetime}')
    app.logger.info(f'areas: {areas}')
    app.logger.info(f'Tezine: {difficultys}')
    app.logger.info(f'Kolicine: {quantitys}')
    app.logger.info(f'potrebno_vreme: {allowed_time}')

    all_questions = []
    for i in range(0,len(quantitys)):
        if areas[i] == 'Razlomci':
            all_questions = all_questions + generate_fractions_questions(int(quantitys[i]),difficultys[i])
        elif areas[i] == 'Jednačine':
            all_questions = all_questions + generate_equations_questions(int(quantitys[i]),difficultys[i])
        elif areas[i] == 'Funkcije i grafici':
            all_questions = all_questions + generate_functions_questions(int(quantitys[i]),difficultys[i])
    global questions
    random.shuffle(all_questions)
    questions = all_questions
    app.logger.info(questions)
    for i, question in enumerate(questions, start=1):
        question['redni_broj'] = f"{i}. pitanje"
    session['questions'] = questions
    return render_template('verify_test.html', questions=questions, vreme = allowed_time,
                           test_name = test_name, professor = session['username'])


@app.route('/confirm_test', methods=['POST', 'GET'])
def confirm_test():
    if request.method == 'POST':
        data = {
            'test_name': session['test_name'],
            'start_date': session['formatted_start_datetime'],
            'end_date': session['formatted_end_datetime'],
            'questions': session['questions'],
            'allowed_time': session['allowed_time'],
            'professor': session['username']
        }
        # client = pdfcrowd.HtmlToPdfClient('ana_master', '6e029203285c2197c8385d40acb14817')
        # client.setPageSize('A4')
        # with open('static/css/test_styles.css','r') as css:
        #     style = css.read()
        #     style += 'body{background-color: #fff;}.container {background-color: rgba(255, 255, 255, 1);}'
        #     client.setCustomCss(style)


        professor_mail = mongo.schoolDB.profesori.find_one({'username': session['username'], 'verified': True})['email']

        test_pdf = f"Zadaci za {session['test_name']}.pdf"
        print("EEEEEEEEEEEEEEEEE")
        print(session['questions'])
        html_content = render_template('verify_test_pdf.html', questions=session['questions'], vreme = session['allowed_time'],
                           test_name = session['test_name'], professor = session['username'])
        wkhtmltopdf_path = os.path.join(os.getcwd(), 'wkhtmltox', 'bin')
        current_path = os.environ.get('PATH', '')
        if wkhtmltopdf_path not in current_path:
            os.environ['PATH'] = f"{wkhtmltopdf_path}{os.pathsep}{current_path}"

        pdf = pdfkit.from_string(html_content, css='./static/css/verify_test_pdf.css',options={"enable-local-file-access": ""})
        # with open('example_3.pdf','wb') as p:
        #     p.write(pdf)
        # client.convertStringToFile(html_content, f'kontrolni/{test_pdf}')

        msg = Message(test_pdf[:-4],
                      sender='noreply@demo.com', recipients=[professor_mail])
        msg.attach(f'{test_pdf}', 'application/pdf', pdf)
        # with app.open_resource(f'kontrolni/{test_pdf}') as pdf_file:
        #     msg.attach(f'{test_pdf}', 'application/pdf', pdf_file.read())

        try:
            mail.send(msg)
            app.logger.info('Poslata poruka')
            # Delete the PDF file after sending

            pdf_file_path = f'rezultati/{test_pdf}'
            os.remove(pdf_file_path)
            app.logger.info(f'Deleted PDF file: {pdf_file_path}')

        except Exception as e:
            app.logger.error(f"Error sending email: {e}")



        mongo.schoolDB.kontrolni.insert_one(data)
        return render_template('registration_successful.html',text=f'Zadaci za {session["test_name"]} uspešno sastavljeni.' , heading = "Uspešno!")


@app.route('/chose_test_date', methods=['POST', 'GET'])
def chose_test_date():
    """
    Prikazuje profesoru rezultate kontrolnog rada za izabrani termin.
    :return:
            - chose_test_date.html
            - test_results.html
    """
    if request.method=='GET':
        # Aggregation pipeline to get the test_name field
        pipeline = [
            {
                "$project": {
                    "_id": 0,  # Exclude the _id field from the output
                    "test_name": "$test_name",
                }
            }
        ]

        # Execute the aggregation pipeline
        result = list(mongo.schoolDB.rezultati.aggregate(pipeline))
        appointments = []
        # Print the result
        for item in result:
            appointments.append(item["test_name"])
        return render_template('chose_test_date.html', appointments=appointments)
    if request.method == 'POST':
        appointment = request.form.get('appointment_name')
        app.logger.info(appointment)
        results = mongo.schoolDB.rezultati.find_one({'test_name': appointment})['results']
        app.logger.info(results)
        table_content = render_template('test_results.html', appointment=appointment, results = results)
        return render_template('test_results.html', appointment=appointment, results = results,
                               table_content=table_content)

@app.route('/test_or_results')
def test_or_results():
    """
    Stranica koja profesoru omogućava da izabere da li želi da vidi rezultate
    određenog termina kontrolnog rada ili da sastavi novi kontrolni.
    :return:
        - test_or_results.html
    """
    return render_template('test_or_results.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    """
    Funkcija koja omogućava profesoru da rezultate kontrolnog pošalje na svoju email adresu.
    :return:
            - registration_successful.html
            - registration_failed.html
    """
    # Retrieve the table content from the form submission
    table_content = request.form.get('table_content')
    appointment_name = request.form.get('appointment_name')
    professor_mail = mongo.schoolDB.profesori.find_one({'username': session['username'], 'verified': True})['email']
    body = MIMEText(table_content, 'html')
    msg = Message(f"Rezultati testa za termin {appointment_name}", sender='noreply@demo.com',
                  recipients=[professor_mail])
    msg.html = body.get_payload(decode=True).decode(body.get_content_charset())

    try:
        mail.send(msg)
        app.logger.info('Poslata poruka')
        return render_template('registration_successful.html',text='Proverite vašu mejl adresu kako biste videli rezultate.', heading = 'Uspešno ste poslali zadatke!')

    except Exception as e:
        app.logger.error(f"Error sending email: {e}")
        return render_template('registration_failed.html', text='Neuspešno slanje rezultata na mail.')


@app.route('/login_student')
def login_student():
    """
    Stanica koja omogućava učeniku da unese svoje podatke prije početka kontrolnog rada.
    :return:
            - login_student.html
    """
    test_list = []
    for item in mongo.schoolDB.kontrolni.find():
        test_list.append(item["test_name"])

    return render_template('login_student.html', test_list=test_list)

questions = []
total_time = 0
@app.route('/start_test', methods=['POST'])
def start_test():
    """
    Stranica na kojoj učenik ima prikazan svoj kontrolni rad sa
    svojim jedinstvenim generisanim veryijama zdataka.
    :return:
            - test.html
            - registration_failed.html
    """
    student_name = request.form.get('studentName')
    student_surname = request.form.get('studentSurname')
    chosen_test = request.form.get('area_name')
    test = mongo.schoolDB.kontrolni.find_one({'test_name': chosen_test})
    start_date = datetime.strptime(test['start_date'], "%Y-%m-%dT%H:%M")
    end_date = datetime.strptime(test['end_date'], "%Y-%m-%dT%H:%M")
    current_time = datetime.now()
    start_date_readable = start_date.strftime("%Y-%m-%d %H:%M:%S")
    end_date_readable = end_date.strftime("%Y-%m-%d %H:%M:%S")

    if start_date <= current_time <= end_date:
        all_questions = test['questions']
        for q in all_questions:
            random.shuffle(q['options'])
        global questions
        random.shuffle(all_questions)
        questions = all_questions
        app.logger.info(questions)
        for i, question in enumerate(questions, start=1):
            question['redni_broj'] = f"{i}. pitanje"

        return render_template('test.html', questions=questions, vreme = test['allowed_time'],
                               test_name = test['test_name'],student_name=student_name,
                               student_surname=student_surname, professor = test['professor'])
    else:
        return render_template('registration_failed.html', text=f'Izabrani kontrolni nije trenutno aktuelan.'
                                                                f' Aktuelan je od {start_date_readable} do {end_date_readable}')



@app.route('/solution/<questionId>')
def show_solution(questionId):
    """
    Funkcija koja prikazuje rešenje za pitanje questionId.
    :param questionId: jedinstveni identifikacioni kod pitanja
    :return:
            - solution.html
    """
    global questions
    solution = ''
    for q in questions:
        if str(q['id']) == questionId:
            solution = q['solution']
            break

    return render_template('solution.html', solution=solution)

@app.route('/record_help/<questionId>', methods=['POST'])
def record_click(questionId):
    """
    Funkcija koja beleži kada učenik koristi pomoć za pitanje questionId.
    :param questionId: jedinstveni identifikacioni kod pitanja
    :return:
    """
    global questions
    data = request.get_json()
    for q in questions:
        if str(q['id']) == questionId:
            q['help_level'] = int(data['help_level'])
            app.logger.info('Setovanja je pomoc za pitanje ' + questionId + ' na nivo ' + str(data['help_level']))
            break

    return 'recorded'

@app.route('/record_time', methods=['POST'])
def record_time():
    """
    Funkcija koja beleži preostalo vreme kada učenik završi svoj kontrolni rad.
    :return:
    """
    global total_time
    data = request.get_json()
    total_time = data['total_time']

    return 'recorded'

@app.route('/test_result', methods=['POST'])
def test_result():
    """
    Funkcija koja prikazuje učeniku rezultate njegovog kontrolnog rada.
    :return:
            - result.html
    """
    global questions
    global total_time
    points = 0
    total_points = 0
    student_name = request.form.get('student_name')
    student_surname = request.form.get('student_surname')
    test_name = request.form.get('test_name')
    professor_username = request.form.get('professor_username')
    professor_email = mongo.schoolDB.profesori.find_one({'username': professor_username, 'verified': True})['email']
    for question in questions:
        total_points += question['points']
        earned_points = question['points']
        question['correct_incorrect'] = ''
        selected_option = request.form.get(f'question_{question["id"]}')
        if question.get('help_level'):
            app.logger.info(question['help_level'])
            if question['help_level'] == 1:
                earned_points = 0.75*question['points']
                question['help_level_table'] = 'Koristili ste jednu pomoć'
            elif question['help_level'] == 2:
                earned_points = 0.5*question['points']
                question['help_level_table'] = 'Koristili ste dve pomoći'
            elif question['help_level'] == 10:
                question['help_level_table'] = 'Prikazan rezultat'
                earned_points = 0
        else:
            question['help_level_table'] = 'Pomoć nije korišćena'
        app.logger.info('/////////////////////////////////////')
        app.logger.info('Izabrana opcija' + str(selected_option))
        app.logger.info('Tacan odgovor' +str(question['correct_answer']))
        app.logger.info('/////////////////////////////////////')
        if selected_option == str(question['correct_answer']):
            question['correct_incorrect'] = 'Tačan odgovor'
        else:
            earned_points = 0
            question['correct_incorrect'] = 'Netačan odgovor'
        points += earned_points
        question['earned_points'] = int(earned_points)


    minutes, seconds = divmod(total_time, 60)
    total_time_string = f'{int(minutes):02d}:{int(seconds):02d}'

    if points/total_points<=0.60:
        grade = 1
    elif points/total_points > 0.60 and points/total_points <=0.70:
        grade = 2
    elif points/total_points > 0.70 and points/total_points <=0.80:
        grade = 3
    elif points/total_points > 0.80 and points/total_points <=0.90:
        grade = 4
    else:
        grade = 5


    existing_doc = mongo.schoolDB.rezultati.find_one({'test_name': test_name})
    new_result = {f'{student_name} {student_surname}': grade}
    if existing_doc:
        # If the document exists, update the 'results' array
        mongo.schoolDB.rezultati.update_one(
            {'test_name': test_name},
            {'$push': {'results': new_result}}
        )
    else:
        # If the document doesn't exist, create a new one
        new_doc = {'test_name': test_name, 'results': [new_result]}
        mongo.schoolDB.rezultati.insert_one(new_doc)

    client = pdfcrowd.HtmlToPdfClient('ana_master', '6e029203285c2197c8385d40acb14817')
    client.setPageSize('A4')
    with open('static/css/result.css','r') as css:
        style = css.read()
        style += "h2{font-size: 20px;}"
        client.setCustomCss(style)

    results_pdf = f"{student_name} {student_surname} rezultati testa za {test_name}.pdf"

    html_body_content = render_template('result.html', points=int(points), total_points=total_points, questions=questions,
                           total_time_string=total_time_string, student_name=student_name,student_surname=student_surname,
                           test_name = test_name, professor_email=professor_email, grade=grade)
    client.convertStringToFile(html_body_content, f'rezultati/{results_pdf}')



    msg = Message(results_pdf[:-4],
                  sender='noreply@demo.com', recipients=[professor_email])

    with app.open_resource(f'rezultati/{results_pdf}') as pdf_file:
        msg.attach(f'{results_pdf}', 'application/pdf', pdf_file.read())

    try:
        mail.send(msg)
        app.logger.info('Poslata poruka')
        # Delete the PDF file after sending

        pdf_file_path = f'rezultati/{results_pdf}'
        os.remove(pdf_file_path)
        app.logger.info(f'Deleted PDF file: {pdf_file_path}')

    except Exception as e:
        app.logger.error(f"Error sending email: {e}")
    
    return render_template('result.html', points=int(points), total_points=total_points, questions=questions,
                           total_time_string=total_time_string, student_name=student_name,student_surname=student_surname,
                           test_name = test_name, professor_email=professor_email, grade=grade)


# @app.route('/send_pdf_results', methods=['POST'])
# def send_pdf_results():
#     # Get HTML body content from the request
#     data = request.get_json()
#     html_body_content = data.get('html_content', '')
#     professor_email = data.get('professor_email', '')
#     title = data.get('title', '')
#
#     # Process the HTML body content (you can save it, manipulate it, etc.)
#     # For now, let's just print it
#     client = pdfcrowd.HtmlToPdfClient('ana_master', '6e029203285c2197c8385d40acb14817')
#     client.setPageSize('A4')
#     with open('static/css/result.css','r') as css:
#         client.setCustomCss(css.read())
#
#     results_pdf = title.replace(' ', '_')
#
#
#     client.convertStringToFile(html_body_content, f'rezultati/{results_pdf}')
#
#
#
#     msg = Message(title,
#                   sender='noreply@demo.com', recipients=[professor_email])
#
#     with app.open_resource(f'rezultati/{results_pdf}') as pdf_file:
#         msg.attach(f'{results_pdf}', 'application/pdf', pdf_file.read())
#
#     try:
#         mail.send(msg)
#         app.logger.info('Poslata poruka')
#         # Delete the PDF file after sending
#
#         pdf_file_path = f'rezultati/{results_pdf}'
#         os.remove(pdf_file_path)
#         app.logger.info(f'Deleted PDF file: {pdf_file_path}')
#
#     except Exception as e:
#         app.logger.error(f"Error sending email: {e}")
#
#     return 'Poslao'

if __name__ == '__main__':
    app.run(debug=True, port=8000)
