#Flask
from flask import Flask, render_template, redirect, url_for, flash, request, session
#MySql
from flask_mysqldb import MySQL
#Formularios seguros
from flask_wtf.csrf import CSRFProtect
#Login Seguro
from flask_login import LoginManager, login_user, logout_user, login_required
#Modelos
from models.consultas.consultaUsuarios import consultaUsuarios
from models.consultas.consultasPaginas import consultasPaginas
from models.consultas.consultasCarrusel import consultasCarrusel
from models.consultas.consultasEmpleados import consultasEmpleados
from models.consultas.consultasNoticias import consultasNoticias
from models.consultas.consultasPermisos import consultasPermisos
from models.consultas.consultasRoles import consultasRoles
from models.consultas.consultasHardware import consultasHardware
#Entidades
from models.entidades.Usuarios import Usuarios
#Para usar variables de entorno
from decouple import config

import os

#inicia la app de Flask
app = Flask(__name__)

#Secret key
app.config['SECRET_KEY'] = config('SECRET_KEY')

#Variable token de seguridad
csrf = CSRFProtect(app)

#Configuración de la base de datos
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = config('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = config('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = config('MYSQL_DB')

#Modo desarrollador
app.config['DEBUG'] = True

#Variable de conexión a sql
db = MySQL(app)
#Conteo de intentos fallidos
login_attempts = 0

#Función para guardar datos del usuario logueado
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return consultaUsuarios.usuarios_Obtener(db, id)

#Controller
from controllers.controllerUsuarios import userBP
app.register_blueprint(userBP)
from controllers.controllerPaginas import pageBP
app.register_blueprint(pageBP)
from controllers.controllerCarrusel import carruselBP
app.register_blueprint(carruselBP)
from controllers.controllerEmpleados import empleadosBP
app.register_blueprint(empleadosBP)
from controllers.controllerNoticias import noticiasBP
app.register_blueprint(noticiasBP)
from controllers.controllerPermisos import permisosBP
app.register_blueprint(permisosBP)
from controllers.controllerRoles import rolesBP
app.register_blueprint(rolesBP) 
from controllers.controllerHardware import hardwareBP
app.register_blueprint(hardwareBP) 

#Decorador raíz
@app.route('/')
def index():
    return redirect(url_for('login'))

#decorador de login y método para validar usuario
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
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
                        return render_template('auth/login.html')
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
                            return render_template('auth/login.html')
                    else:
                        flash("No tienes un rol designado...")
                        return render_template('auth/login.html')
            else:
                if logged_user.estado_Usuarios == 0:
                    flash("Usuario bloqueado...")
                    return render_template('auth/login.html')
                
                login_attempts += 1
                if login_attempts == 4:
                    flash("Te queda solo 1 intento y se bloqueara el usuario")
                    return render_template('auth/login.html')
                if login_attempts >= 5:
                    login_attempts = 0
                    estado = Usuarios(None, request.form['usuario_Usuarios'], None, None, None, 0, None)
                    respuestaBloquear = consultaUsuarios.usuarios_Bloquear(db, estado)
                    if respuestaBloquear == True:
                        flash("Su usuario se bloqueó")
                        return render_template('auth/login.html')
                
                mensaje = "Usuario y/o Clave incorrecto. Levas: " + str(login_attempts)
                flash(mensaje)
                return render_template('auth/login.html')
        else:
            flash("Usuario y/o Clave incorrecto...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

#Borra y cierra la sesión 
@app.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('login'))

#Decorador para el usuario común
@app.route('/home_Comun')
@login_required
def home_Comun():
    roll = session["id_Rol_Usuarios"]
    if roll != "1":
        lista_Carrusel = consultasCarrusel.carrusel_ListarXEstado(db)
        lista_Noticias = consultasNoticias.noticias_ListarXEstado(db)
        lista_Empleados = consultasEmpleados.empleados_ListarXEstado(db)
        lista_paginas = consultasPaginas.paginas_ListarXPermisos(db, roll)
        return render_template('common/home_Comun.html', carrusel = lista_Carrusel, noticias = lista_Noticias,
                                empleados = lista_Empleados, paginas = lista_paginas)
    else:
        return redirect(url_for('logout'))

#Decorador para el usuario administrador
@app.route('/home_Admin')
@login_required
def home_Admin():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        lista_Carrusel = consultasCarrusel.carrusel_ListarXEstado(db)
        lista_Noticias = consultasNoticias.noticias_ListarXEstado(db)
        lista_Empleados = consultasEmpleados.empleados_ListarXEstado(db)
        lista_paginas = consultasPaginas.paginas_ListarXPermisos(db, roll)
        return render_template('admin/home_Admin.html', carrusel = lista_Carrusel, noticias = lista_Noticias,
                                empleados = lista_Empleados, paginas = lista_paginas)
    else:
        return redirect(url_for('logout'))

#Decorador para administrar usuarios
@app.route('/edit_user')
@login_required
def edit_user():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        lista_user = consultaUsuarios.usuarios_Listar(db)
        lista_Roles = consultasRoles.rol_ListarXEstado(db)
        return render_template('admin/edit_user.html', users = lista_user, roles = lista_Roles)
    else:
        return redirect(url_for('logout'))

#Decorador para administrar Paginas
@app.route('/edit_paginas')
@login_required
def edit_paginas():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        lista_paginas = consultasPaginas.paginas_Listar(db)
        return render_template('admin/edit_paginas.html', paginas = lista_paginas)
    
    else:
        return redirect(url_for('logout'))
    
#Decorador para administrar el carrusel de imágenes
@app.route('/edit_carrusel')
@login_required
def edit_carrusel():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        lista_Carrusel = consultasCarrusel.carrusel_Listar(db)
        return render_template('admin/edit_carrusel.html', carrusel = lista_Carrusel)
        
    else:
        return redirect(url_for('logout'))

#Decorador para administrar empleados
@app.route('/edit_empleados')
@login_required
def edit_empleados():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        lista_Empleados = consultasEmpleados.empleados_Listar(db)
        return render_template('admin/edit_Empleados.html', empleados = lista_Empleados)
        
    else:
        return redirect(url_for('logout'))
    
#Decorador para administrar el inventario de componentes
@app.route('/edit_Hardware')
@login_required
def edit_Hardware():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        lista_Hardware = consultasHardware.hardware_Listar(db)
        lista_empleados = consultasEmpleados.empleados_ListarXEstado(db)
        return render_template('admin/edit_Hardware.html', hardware = lista_Hardware, empleados = lista_empleados)
        
    else:
        return redirect(url_for('logout'))

#Decorador para administrar noticias
@app.route('/edit_noticias')
@login_required
def edit_noticias():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        lista_Noticias = consultasNoticias.noticias_Listar(db)
        return render_template('admin/edit_noticias.html', noticias = lista_Noticias)
        
    else:
        return redirect(url_for('logout'))

#Decorador para administrar permisos
@app.route('/edit_permisos')
@login_required
def edit_permisos():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        lista_Permisos = consultasPermisos.permisos_Listar(db)
        lista_Roles = consultasRoles.rol_ListarXEstado(db)
        lista_Paginas = consultasPaginas.paginas_ListarXEstado(db)
        return render_template('admin/edit_permisos.html', permisos = lista_Permisos, roles = lista_Roles, paginas = lista_Paginas)
        
    else:
        return redirect(url_for('logout'))

#Decorador para administrar roles
@app.route('/edit_roles')
@login_required
def edit_roles():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        lista_Roles = consultasRoles.rol_Listar(db)
        return render_template('admin/edit_roles.html', roles = lista_Roles)
        
    else:
        return redirect(url_for('logout'))

#Funciones para el control de errores
def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

#Inicia el aplicativo
if __name__ == '__main__':
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(host="0.0.0.0", port=5000)
    