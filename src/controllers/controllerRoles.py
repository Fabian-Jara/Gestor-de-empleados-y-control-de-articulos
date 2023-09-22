#Flask
from flask import Blueprint, redirect, url_for, flash, request, session
#Login Seguro
from flask_login import login_required
#Modelos
from models.consultas.consultasRoles import consultasRoles
#Entidades
from models.entidades.Roles import Roles

rolesBP = Blueprint('adminRoles', __name__)

@rolesBP.route('/add_rol', methods=['POST'])
@login_required
def add_Rol():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            new_Rol = Roles(None, request.form['nombre_Rol'], request.form['estado_Rol'], request.form['fecha_Rol'])
            respuesta_Add_Rol = consultasRoles.rol_Agregar(db, new_Rol)
            if respuesta_Add_Rol == "existe":
                flash('El Rol ya esta existe...')
                return redirect(url_for('edit_roles'))
            else:
                if respuesta_Add_Rol == True:
                    flash('Rol agregado con éxito...')
                    return redirect(url_for('edit_roles'))
                else:
                    flash('Algo salio mal...')
                    return redirect(url_for('edit_roles'))
        else:
            return redirect(url_for('edit_roles'))
    else:
        return redirect(url_for('logout'))

@rolesBP.route('/update_rol/', methods=['POST'])
@login_required
def update_rol():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            editar_Rol = Roles(request.form['id'], request.form['nombre_Rol'], request.form['estado_Rol'],
                                    request.form['fecha_Rol'])
            
            respuesta_Editar_Rol = consultasRoles.rol_Editar(db, editar_Rol)
            if respuesta_Editar_Rol == True:
                flash('Rol actualizado con éxito...')
                return redirect(url_for('edit_roles'))
            else:
                flash('Algo salio mal...')
                return redirect(url_for('edit_roles'))
                
        else:
            return redirect(url_for('edit_roles'))
    else:
        return redirect(url_for('logout'))

@rolesBP.route('/delete_rol/', methods=['POST'])
@login_required
def delete_rol():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            eliminar_Rol = Roles(request.form['id'], None, None, None)
            respuesta_Eliminar_Rol = consultasRoles.rol_Eliminar(db, eliminar_Rol)
            if respuesta_Eliminar_Rol == True:
                flash('Rol eliminado con éxito...')
                return redirect(url_for('edit_roles'))
            else:
                flash('Algo salio mal...')
                return redirect(url_for('edit_roles'))
                
        else:
            return redirect(url_for('edit_roles'))
    else:
        return redirect(url_for('logout'))
