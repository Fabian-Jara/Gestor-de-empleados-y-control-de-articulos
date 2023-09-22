#Flask
from flask import Blueprint, redirect, url_for, flash, request, session
#Login Seguro
from flask_login import login_required
#Modelos
from models.consultas.consultasPermisos import consultasPermisos
#Entidades
from models.entidades.Permisos import Permisos

permisosBP = Blueprint('adminPermisos', __name__)

@permisosBP.route('/add_permiso', methods=['POST'])
@login_required
def add_permiso():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            new_Permiso = Permisos(None, request.form['id_Rol_Permisos'], request.form['id_Paginas_Permisos'], 
                                    request.form['estado_Permisos'])
            respuesta_Add_Permiso = consultasPermisos.permisos_Agregar(db, new_Permiso)
            if respuesta_Add_Permiso == "existe":
                flash('El permiso ya esta habilitado...')
                return redirect(url_for('edit_permisos'))
            else:
                if respuesta_Add_Permiso == True:
                    flash('Permiso agregado con éxito...')
                    return redirect(url_for('edit_permisos'))
                else:
                    flash('Algo salio mal...')
                    return redirect(url_for('edit_permisos'))
        else:
            return redirect(url_for('edit_permisos'))
    else:
        return redirect(url_for('logout'))
    
@permisosBP.route('/update_permisos/', methods=['POST'])
@login_required
def update_permisos():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            editar_permiso = Permisos(request.form['id'], request.form['id_Rol_Permisos'], request.form['id_Paginas_Permisos'],
                                        request.form['estado_Permisos'])
            
            respuesta_Editar_Permiso = consultasPermisos.permisos_Editar(db, editar_permiso)
            if respuesta_Editar_Permiso == True:
                flash('permiso actualizado con éxito...')
                return redirect(url_for('edit_permisos'))
            else:
                flash('Algo salio mal...')
                return redirect(url_for('edit_permisos'))
                
        else:
            return redirect(url_for('edit_permisos'))
    else:
        return redirect(url_for('logout'))

@permisosBP.route('/delete_permisos/', methods=['POST'])
@login_required
def delete_permisos():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            eliminar_Permisos = Permisos(request.form['id'], None, None, None)
            respuesta_Eliminar_Permisos = consultasPermisos.permisos_Eliminar(db, eliminar_Permisos)
            if respuesta_Eliminar_Permisos == True:
                flash('Permiso eliminado con éxito...')
                return redirect(url_for('edit_permisos'))
            else:
                flash('Algo salio mal...')
                return redirect(url_for('edit_permisos'))
                
        else:
            return redirect(url_for('edit_permisos'))
    else:
        return redirect(url_for('logout'))