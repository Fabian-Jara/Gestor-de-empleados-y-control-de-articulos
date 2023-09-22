#Flask
from flask import Blueprint, redirect, url_for, flash, request, session
#Login Seguro
from flask_login import login_required
#Subir archivos seguros
from werkzeug.utils import secure_filename
#Funciones de sistema operativo (os)
import os
#Crear valores random
from random import sample
#Modelos
from models.consultas.consultasPaginas import consultasPaginas
from models.consultas.consultasPermisos import consultasPermisos
#Entidades
from models.entidades.Paginas import Paginas
#Para usar variables de entorno
from decouple import config

pageBP = Blueprint('adminPages', __name__)

def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio

@pageBP.route('/add_Paginas/', methods=['POST'])
@login_required
def add_Paginas():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            #procesamiento de imágenes
            file = request.files['imagen_Paginas']
            base_path = os.path.dirname (__file__)
            filename = secure_filename(file.filename)
            extension = os.path.splitext(filename)[1]
            
            if extension == ".jpg" or extension == ".png" or extension == ".jpeg":
                nuevoNombreFile = stringAleatorio() + extension
                upload_path = os.path.join (base_path, config('RUTA_IMG_PAGINAS'), nuevoNombreFile) 
                file.save(upload_path)
                #modifico el path
                start = int(config('CORTAR_RUTA'))
                url_imagen = upload_path[start:]
                
                new_Page = Paginas(None, request.form['nombre_Paginas'], request.form['url_Paginas'], url_imagen, 
                                    request.form['estado_Paginas'], request.form['fecha_Paginas'])
                
                respuesta_Add_Pagina = consultasPaginas.paginas_Agregar(db, new_Page)
                if respuesta_Add_Pagina == "existe":
                    os.remove(upload_path)
                    flash('Esta pagina ya existe...')
                    return redirect(url_for('edit_paginas'))
                else:
                    if respuesta_Add_Pagina == True:
                        flash('Pagina agregada con éxito...')
                        return redirect(url_for('edit_paginas'))
                    else:
                        os.remove(upload_path)
                        flash('Algo salio mal...')
                        return redirect(url_for('edit_paginas'))

            else:
                flash("Formato de imagen invalido")
                return redirect(url_for('edit_paginas'))
        else:
            return redirect(url_for('edit_paginas'))
    else:
        return redirect(url_for('logout'))

@pageBP.route('/update_img_paginas/', methods=['POST'])
@login_required
def update_img_paginas():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            #procesamiento de imágenes
            file = request.files['imagen_Paginas']
            base_path = os.path.dirname (__file__)
            filename = secure_filename(file.filename)
            extension = os.path.splitext(filename)[1]
            
            if extension == ".jpg" or extension == ".png" or extension == ".jpeg":
                nuevoNombreFile = stringAleatorio() + extension
                upload_path = os.path.join (base_path, config('RUTA_IMG_PAGINAS'), nuevoNombreFile) 
                file.save(upload_path)
                #modifico el path
                start = int(config('CORTAR_RUTA'))
                url_imagen = upload_path[start:]
                
                edit_Imagen = Paginas(request.form['id'], None, None, url_imagen, None, None)
                
                respuesta_Edit_Imagen_Paginas = consultasPaginas.paginas_Editar_imagen(db, edit_Imagen)
                
                if respuesta_Edit_Imagen_Paginas == True:
                        flash('Imagen actualizada con éxito...')
                        return redirect(url_for('edit_paginas'))
                else:
                    os.remove(upload_path)
                    flash('Algo salio mal...')
                    return redirect(url_for('edit_paginas'))
            else:
                flash("Formato de imagen invalido")
                return redirect(url_for('edit_paginas'))
        else:
            return redirect(url_for('edit_paginas'))
    else:
        return redirect(url_for('logout'))

@pageBP.route('/update_paginas/', methods=['POST'])
@login_required
def update_paginas():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            editar_Paginas = Paginas(request.form['id'], request.form['nombre_Paginas'], request.form['url_Paginas'], None, 
                                request.form['estado_Paginas'], request.form['fecha_Paginas'])
            respuesta_Editar_Paginas = consultasPaginas.paginas_Editar(db, editar_Paginas)
            if respuesta_Editar_Paginas == True:
                flash('Pagina actualizada con éxito...')
                return redirect(url_for('edit_paginas'))
            else:
                flash('Algo salio mal...')
                return redirect(url_for('edit_paginas'))
                
        else:
            return redirect(url_for('edit_paginas'))
    else:
        return redirect(url_for('logout'))

@pageBP.route('/delete_pagina/', methods=['POST'])
@login_required
def delete_pagina():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            respuesta_Eliminar_permiso = consultasPermisos.permisos_EliminarXPaginas(db, request.form['id'])

            if respuesta_Eliminar_permiso ==  True:
                eliminar_Paginas = Paginas(request.form['id'], None, None, None, None, None)
                respuesta_Eliminar_Paginas = consultasPaginas.paginas_Eliminar(db, eliminar_Paginas)
                if respuesta_Eliminar_Paginas == True:
                    flash('Pagina eliminada con éxito...')
                    return redirect(url_for('edit_paginas'))
                else:
                    flash('Algo salio mal...')
                    return redirect(url_for('edit_paginas'))
                
        else:
            return redirect(url_for('edit_paginas'))
    else:
        return redirect(url_for('logout'))