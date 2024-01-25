import secrets
from datetime import datetime,timedelta
from pymongo.mongo_client import MongoClient
import bcrypt
URI = "mongodb+srv://lijeskicaleksandraa:yqXROe1L3xT77oZO@schooldb.pxelh19.mongodb.net/?retryWrites=true&w=majority"

mongo = MongoClient(URI)

class User:
    """
    Klasa koja predstavlja jednog korisnika (profesora) koji ima sledeće atribute:
        - korisničko ime
        - email
        - šifra
        - token
    """
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.token_data = generate_token()
        new_user = {'email': self.email, 'username': self.username, 'password': self.password, 'verified': False,
                    'token_data': self.token_data}
        mongo.schoolDB.profesori.insert_one(new_user)



def is_username_email_taken(username,email):
    """
    Funkcija proverava da li korisnicko ime i email vec postoje u bazi podataka.
    :param username: korisnicko ime
    :param email: email
    :return:
            - username_taken: korisnicko ime se koristi
            - email_taken: email se koristi
            - username_taken_verified: korisnicko ime se koristi i profil je verifikovan
            - email_taken_verified: email se koristi i profil je verifikovan
    """
    username_t = mongo.schoolDB.profesori.find_one({'username': username})
    email_t = mongo.schoolDB.profesori.find_one({'email': email})
    result = {}
    result["username_taken"] = username_t is not None
    result["email_taken"] = email_t is not None
    result["username_taken_verified"] = result["username_taken"] and username_t['verified']
    result["email_taken_verified"] = result["email_taken"] and email_t['verified']
    return result



def delete_user_by_email(email):
    """
    Funkcija koja briše korisnika pomoću emaila.
    :param email: email korisnika
    :return:
    """
    mongo.schoolDB.profesori.delete_one({'email': email, 'verified': False})

def user_authentication(username,password):
    """
    Verifikuje profesorovo korisničko ime i sifru da li se podudaraju sa onima u bazi podataka.
    :param username: korisnicko ime
    :param password: šifra
    :return:
            - user_exist: korisnik postoji
            - user_verified: korisnik postoji i profil je verifikovan
            - user_authentication: korisnik postoji i profil je verifikovan i šifra je tačna
    """
    result = {}
    user = mongo.schoolDB.profesori.find_one({'username': username})
    result['user_exist'] = user is not None
    result['user_verified'] = result['user_exist'] and user['verified']
    result['user_authentication'] = result['user_exist'] and result['user_verified']\
                                    and bcrypt.checkpw(password.encode('utf-8'), user['password'])
    return result

def token_verification(token):
    """
    Funkcija koja verifikuje korisnikov profil, na osnovu njegovog tokena.
    :param token: korisnikov token
    :return:
    """
    user = mongo.schoolDB.profesori.find_one({'token_data.token': token, 'verified': False})
    token_timestamp = user['token_data']['timestamp']
    expiration_time = token_timestamp + timedelta(hours=24)
    if datetime.utcnow() > expiration_time:
        # Token has expired, delete the user
        mongo.schoolDB.profesori.delete_one({'_id': user['_id']})
        return False
    else:
        # Mark the token as used
        mongo.schoolDB.profesori.update_one({'_id': user['_id']}, {'$set': {'verified': True}})
        return True

def generate_token():
    """
    Funkcija koja generiše jedinstveni token za korisnika.
    :return:
            - token
    """
    token = secrets.token_urlsafe(16)  # Adjust the length of the token as needed
    timestamp = datetime.utcnow()  # type: ignore
    return {'token': token, 'timestamp': timestamp}


def delete_expired_unverified_users():
    """
    Funkcija koja briše profile koji u 24 sata nisu verifikovali svoj profil.
    :return:
    """
    expiration_time = datetime.utcnow() - timedelta(minutes=30)  # type: ignore
    mongo.schoolDB.profesori.delete_many({'verified': False, 'token_data.timestamp': {'$lt': expiration_time}})

