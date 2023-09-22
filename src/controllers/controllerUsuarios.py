#Flask
from flask import Blueprint, redirect, url_for, flash, request, session
#Login Seguro
from flask_login import login_required
#Generador de password hash para encriptación
from werkzeug.security import generate_password_hash
#Modelos
from models.consultas.consultaUsuarios import consultaUsuarios
#Entidades
from models.entidades.Usuarios import Usuarios

userBP = Blueprint('adminUsers', __name__)

@userBP.route('/add_user', methods=['POST'])
@login_required
def add_user():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            new_user = Usuarios(None, request.form['usuario_Usuarios'], generate_password_hash(request.form['clave_Usuarios']), 
                                request.form['nombre_Usuarios'], request.form['id_Rol_Usuarios'], request.form['estado_Usuarios'], 
                                request.form['fecha_Usuarios'])
            respuesta_Add_usuario = consultaUsuarios.usuarios_Agregar(db, new_user)
            if respuesta_Add_usuario == "existe":
                flash('Nombre o Usuario ya existe...')
                return redirect(url_for('edit_user'))
            else:
                if respuesta_Add_usuario == True:
                    flash('Usuario agregado con éxito...')
                    return redirect(url_for('edit_user'))
                else:
                    flash('Algo salio mal...')
                    return redirect(url_for('edit_user'))
        else:
            return redirect(url_for('edit_user'))
    else:
        return redirect(url_for('logout'))
    
@userBP.route('/update_user/', methods=['POST'])
@login_required
def update_user():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            editar_user = Usuarios(request.form['id'], request.form['usuario_Usuarios'], None, request.form['nombre_Usuarios'], request.form['id_Rol_Usuarios'], 
                                request.form['estado_Usuarios'], request.form['fecha_Usuarios'])
            respuesta_Editar_usuario = consultaUsuarios.usuarios_Editar(db, editar_user)
            if respuesta_Editar_usuario == True:
                flash('Usuario actualizado con éxito...')
                return redirect(url_for('edit_user'))
            else:
                flash('Algo salio mal...')
                return redirect(url_for('edit_user'))
                
        else:
            return redirect(url_for('edit_user'))
    else:
        return redirect(url_for('logout'))
    
@userBP.route('/delete_user', methods=['POST'])
@login_required
def delete_user():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            eliminar_user = Usuarios(request.form['id'], None, None, None, None, None, None)
            respuesta_Eliminar_usuario = consultaUsuarios.usuarios_Eliminar(db, eliminar_user)
            if respuesta_Eliminar_usuario == True:
                flash('Usuario Eliminado con éxito...')
                return redirect(url_for('edit_user'))
            else:
                flash('Algo salio mal...')
                return redirect(url_for('edit_user'))
        else:
            return redirect(url_for('edit_user'))
    else:
        return redirect(url_for('logout'))
    
@userBP.route('/update_clave/', methods=['POST'])
@login_required
def update_clave():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            user_actual = session["user_actual"]
            user = Usuarios(None, user_actual, request.form['mi_contraseña'], None, None, None, None)
            logged_user = consultaUsuarios.usuarios_Validar_Login(db, user)
            if logged_user != None:
                if logged_user.clave_Usuarios:
                    new_clave = request.form['new_clave']
                    confirm_clave = request.form['confirm_clave']
                    if new_clave == confirm_clave:
                        clave_user = Usuarios(request.form['id'], None, generate_password_hash(request.form['new_clave']), None, None, None, None)
                        respuesta_Clave_usuario = consultaUsuarios.usuarios_Clave(db, clave_user)
                        if respuesta_Clave_usuario == True:
                            flash('Clave de usuario cambiada con éxito...')
                            return redirect(url_for('edit_user'))
                        else:
                            flash('Algo salio mal...')
                            return redirect(url_for('edit_user'))
                    else:
                        flash("Claves no coinciden...")
                        return redirect(url_for('edit_user'))
                else:
                    flash("Tu contraseña no es correcta...")
                    return redirect(url_for('edit_user'))
            else:
                flash("Ocurrió un problema con tu usuario...")
                return redirect(url_for('edit_user'))
        else:
            return redirect(url_for('edit_user'))
    else:
        return redirect(url_for('logout'))
    
