from app.model.user import User

from app import response, app, db
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token
import datetime

def buatAdmin():
    try :
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        level = 1

        users = User(name=name, email=email, level=level)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.success('', 'Sukses Menambahkan Data Admin')
    except Exception as e:
        print(e)
        
def singleObject(data):
    data = {
        'id' : data.id,
        'name' : data.name,
        "email" : data.email,
        'level' : data.level
    }
    
    return data

def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if not user:
            return response.badRequest([],'Email tidak terdaftar')
        
        if not user.checkPassword(password):
            return response.badRequest([],'Kombinasi Password Salah')
        
        data = singleObject(user)
        
        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=7)
        
        access_token = create_access_token(data, fresh=True, expires_delta= expires)
        refresh_token = create_refresh_token(data, expires_delta= expires_refresh)
        
        return response.success({
            "data" : data,
            "access_token" : access_token,
            "refresh_token" : refresh_token,
        }, "Sukses Login!")
    except Exception as e:
        print(e)