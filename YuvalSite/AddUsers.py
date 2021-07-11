
import json
from werkzeug.security import generate_password_hash, check_password_hash
from website.models import Movies, Users
from website import db, create_app

#The following is necessary cuase we make db actions and we need the application for running the script
app = create_app()
app.app_context().push()

#this func 'create_users' reads data from json file and loads it to DB
#This file runs just one time 
def create_users():

    f=open('MyUsers.json')
    data=json.load(f)
    for i in data:
        first_name=i['first_name']
        email=i['email']
        password=i['password']
        new_user=Users(email=email, first_name=first_name, password=generate_password_hash(password, method='sha256'),Movies='')
        db.session.add(new_user)
        db.session.commit()

        
    print('Good Sign')

create_users()
