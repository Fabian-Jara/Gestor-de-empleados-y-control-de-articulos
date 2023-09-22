#Flask
from flask import Blueprint, redirect, url_for, flash, request, session
#Login Seguro
from flask_login import LoginManager, login_user
#Modelos
from models.consultas.consultaUsuarios import consultaUsuarios
#Entidades
from models.entidades.Usuarios import Usuarios

loginBP = Blueprint('login', __name__)

login_attempts = 0

#Función para guardar datos del usuario logueado
login_manager_app = LoginManager(loginBP)

@login_manager_app.user_loader
def load_user(id):
    #DB
    from app import db
    return consultaUsuarios.usuarios_Obtener(db, id)

@loginBP.route('/validarLogin', methods=['POST'])
def validarLogin():
    if request.method == 'POST':
        from app import db
        global login_attempts
        user = Usuarios(None, request.form['usuario_Usuarios'], request.form['clave_Usuarios'], None, None, None, None)
        logged_user = consultaUsuarios.usuarios_Validar_Login(db, user)
        if logged_user != None:
            if logged_user.clave_Usuarios:
                login_attempts = 0
                if logged_user.id_Rol_Usuarios == 1:
                    if logged_user.estado_Usuarios == 1:
                        login_attempts = 0
                        session["id_Rol_Usuarios"] = "1"
                        user_actual = logged_user.usuario_Usuarios
                        session["user_actual"] = user_actual
                        login_user(logged_user)
                        return redirect(url_for('home_Admin'))
                    else:
                        flash("Usuario bloqueado...")
                        return redirect(url_for('login'))
                else:
                    if logged_user.id_Rol_Usuarios != 1:
                        if logged_user.estado_Usuarios == 1:
                            login_attempts = 0
                            rol = str(logged_user.id_Rol_Usuarios)
                            session["id_Rol_Usuarios"] = rol
                            login_user(logged_user)
                            return redirect(url_for('home_Comun'))
                        else:
                            flash("Usuario bloqueado...")
                            return redirect(url_for('login'))
                    else:
                        flash("No tienes un rol designado...")
                        return redirect(url_for('login'))
            else:
                if logged_user.estado_Usuarios == 0:
                    flash("Usuario bloqueado...")
                    return redirect(url_for('login'))
                
                login_attempts += 1
                if login_attempts >= 4:
                    login_attempts = 0
                    estado = Usuarios(None, request.form['usuario_Usuarios'], None, None, None, 0, None)
                    respuestaBloquear = consultaUsuarios.usuarios_Bloquear(db, estado)
                    if respuestaBloquear == True:
                        flash("Usuario bloqueado...")
                        return redirect(url_for('login'))
                
                    mensaje = "Usuario y/o Clave incorrecto. Levas: " + str(login_attempts)
                flash(mensaje)
                return redirect(url_for('login'))
        else:
            flash("Usuario y/o Clave incorrecto...")
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))