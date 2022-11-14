import json
from flask import Flask, jsonify,  render_template, request, redirect, url_for, session,make_response # pip install Flask
from typing import List, Dict
from notifypy import Notify
from os import path #pip install notify-py
import mysql.connector

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
def test_table() -> List[Dict]:
    config = {
        'user': 'uynv2tnynvplpgon',
        'password': '8rzJP0pyuiq1VkMLELfx',
        'host': 'b0manp20m3mu8n6jdwgo-mysql.services.clever-cloud.com',
        'port': '3306',
        'database': 'b0manp20m3mu8n6jdwgo'
    }
    connection = mysql.connector.connect(**config)
    cur = connection.cursor()
    cur.execute("SELECT * FROM tip_usu")
    tipo =[{'id_tip_usu':id_tip_usu,'nom_tip_usu': nom_tip_usu} for (id_tip_usu, nom_tip_usu) in cur] 
    connection.close()
    return jsonify({"Usuario":tipo})
    
@app.route('/')
def index() -> str:
        #return json.dumps({'test_table': test_table()})
        return render_template("contenido.html")    
@app.route('/layout', methods = ["GET", "POST"])
def layout():
    session.clear()
    return render_template("contenido.html")
@app.route('/getUsers', methods= ["GET"])
def getUsers():
        config = {
        'user': 'uynv2tnynvplpgon',
        'password': '8rzJP0pyuiq1VkMLELfx',
        'host': 'b0manp20m3mu8n6jdwgo-mysql.services.clever-cloud.com',
        'port': '3306',
        'database': 'b0manp20m3mu8n6jdwgo'
          }
        connection = mysql.connector.connect(**config)
        cur = connection.cursor()
        cur.execute("SELECT name,email,interes FROM users")
        tipo =[{'name':name,'email': email,'interes': interes} for (name, email,interes) in cur] 
        connection.close()
        return make_response(jsonify({"Usuario":tipo}),200)
@app.route('/getUser/<email>', methods= ["GET"])
def getUser(email):
        config = {
        'user': 'uynv2tnynvplpgon',
        'password': '8rzJP0pyuiq1VkMLELfx',
        'host': 'b0manp20m3mu8n6jdwgo-mysql.services.clever-cloud.com',
        'port': '3306',
        'database': 'b0manp20m3mu8n6jdwgo'
          }
        connection = mysql.connector.connect(**config)
        cur = connection.cursor()
        cur.execute("SELECT name,email,interes FROM users WHERE email=%s",(email,))
        user = cur.fetchone()                
        connection.close()
        if user is not None:        
            return make_response(({"Usuario":user}),200)
        else:
            return make_response(jsonify({"Error":"Usuario no encontrado"}),400)
@app.route('/createUser/<email>', methods= ["POST"])
def createUsers(email):
        req=request.get_json()
        config = {
        'user': 'uynv2tnynvplpgon',
        'password': '8rzJP0pyuiq1VkMLELfx',
        'host': 'b0manp20m3mu8n6jdwgo-mysql.services.clever-cloud.com',
        'port': '3306',
        'database': 'b0manp20m3mu8n6jdwgo'
        }
        connection = mysql.connector.connect(**config)
        cur = connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s",(email,))
        user = cur.fetchone()               
        connection.close()
        if user is None:
            connection = mysql.connector.connect(**config)
            cur = connection.cursor()
            cur.execute("INSERT INTO users (name, email, password, id_tip_usu, interes) VALUES (%s,%s,%s,%s,%s)", (req["name"],req["email"],req["password"],req["id_tip_usu"],req["interes"]))
            connection.commit()
            connection.close()
            return make_response(jsonify({"Respuesta":"El usuario ha sido creado"}),200)
        else:
            return make_response(jsonify({"Error":"El usuario ya existe"}),400)
@app.route('/updateUser/<email>', methods= ["PUT"])
def updateUser(email):
        req=request.get_json()
        config = {
        'user': 'uynv2tnynvplpgon',
        'password': '8rzJP0pyuiq1VkMLELfx',
        'host': 'b0manp20m3mu8n6jdwgo-mysql.services.clever-cloud.com',
        'port': '3306',
        'database': 'b0manp20m3mu8n6jdwgo'
        }
        connection = mysql.connector.connect(**config)
        cur = connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s",(email,))
        user = cur.fetchone()               
        connection.close()
        if user is None:
            return make_response(jsonify({"Error":"El usuario no existe"}),400)           
        else:
            connection = mysql.connector.connect(**config)
            cur = connection.cursor()
            cur.execute("UPDATE users set name= '"+req["name"]+"' WHERE email='"+email+"'")
            connection.commit()
            connection.close()
            return make_response(jsonify({"Respuesta":"El usuario ha modificado"}),200) 
@app.route('/login', methods= ["GET", "POST"])
def login():
    #notificacion = Notify()

    if request.method == 'POST':
        config = {
        'user': 'uynv2tnynvplpgon',
        'password': '8rzJP0pyuiq1VkMLELfx',
        'host': 'b0manp20m3mu8n6jdwgo-mysql.services.clever-cloud.com',
        'port': '3306',
        'database': 'b0manp20m3mu8n6jdwgo'
        }
        connection = mysql.connector.connect(**config)

        email = request.form['email']
        password = request.form['password']

        cur = connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s",(email,))
        user = cur.fetchone()
        cur.close()
        
        if len(user)>0:
            if password == user[3]:
                session['name'] = user[1]
                session['email'] = user[2]
                session['tipo'] = user[4]

                if session['tipo'] == 1:
                    return render_template("premium/home.html")
                elif session['tipo'] == 2:
                    return render_template("estandar/homeTwo.html")


            else:
                #notificacion.title = "Error de Acceso"
                #notificacion.message="Correo o contraseña no valida"
                #notificacion.send()
                return render_template("login.html")
        else:
            #notificacion.title = "Error de Acceso"
            #notificacion.message="No existe el usuario"
            #notificacion.send()
            return render_template("login.html")
    else:        
        return render_template("login.html")


@app.route('/registro', methods = ["GET", "POST"])
def registro():
    config = {
        'user': 'uynv2tnynvplpgon',
        'password': '8rzJP0pyuiq1VkMLELfx',
        'host': 'b0manp20m3mu8n6jdwgo-mysql.services.clever-cloud.com',
        'port': '3306',
        'database': 'b0manp20m3mu8n6jdwgo'
         }
    connection = mysql.connector.connect(**config)
    cur = connection.cursor()
    cur.execute("SELECT * FROM tip_usu")
    tipo =[{'id_tip_usu':id_tip_usu,'nom_tip_usu': nom_tip_usu} for (id_tip_usu, nom_tip_usu) in cur] 

    cur = connection.cursor()
    cur.execute("SELECT * FROM sexo_interes")
    interes = [{'id_sex':id_sex,'nom_sex': nom_sex} for (id_sex, nom_sex) in cur]
    cur.close()

    #notificacion = Notify()
    
    

    if request.method == 'GET':
        return render_template("registro.html", tipo = tipo, interes = interes )
    
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        tip = request.form['tipo']
        interes = request.form['interes']  
        config = {
        'user': 'uynv2tnynvplpgon',
        'password': '8rzJP0pyuiq1VkMLELfx',
        'host': 'b0manp20m3mu8n6jdwgo-mysql.services.clever-cloud.com',
        'port': '3306',
        'database': 'b0manp20m3mu8n6jdwgo'
         }
        connection = mysql.connector.connect(**config)
        cur = connection.cursor()
        cur.execute("INSERT INTO users (name, email, password, id_tip_usu, interes) VALUES (%s,%s,%s,%s,%s)", (name, email, password,tip,interes,))
        connection.commit()
        #notificacion.title = "Registro Exitoso"
        #notificacion.message="ya te encuentras registrado en 🤵 MORE LOVE 👰, por favor inicia sesión y empieza a descubrir este nuevo mundo."
        #notificacion.send()
        return redirect(url_for('login'))



if __name__ == '__main__':
   
#print( json.dumps({'test_table': test_table()}))
   #test_table()    
    app.run(host='0.0.0.0')