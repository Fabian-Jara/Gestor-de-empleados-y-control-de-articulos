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
from models.consultas.consultasNoticias import consultasNoticias
#Entidades
from models.entidades.Noticias import Noticias
#Para usar variables de entorno
from decouple import config

noticiasBP = Blueprint('adminNoticias', __name__)

def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio

@noticiasBP.route('/add_Noticias/', methods=['POST'])
@login_required
def add_Noticias():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            new_new_Noticias = Noticias(None, request.form['titulo_Noticias'], request.form['sub_Titulo_Noticias'],
                                            request.form['cuerpo_Noticias'], None, request.form['estado_Noticias'], request.form['fecha_Noticias'])
                
            respuesta_Add_Noticias = consultasNoticias.noticias_Agregar(db, new_new_Noticias)
            if respuesta_Add_Noticias == "existe":
                flash('Este titulo de noticia ya existe...')
                return redirect(url_for('edit_noticias'))
            else:
                if respuesta_Add_Noticias == True:
                    flash('Noticia agregado con éxito...')
                    return redirect(url_for('edit_noticias'))
                else:
                    flash('Algo salio mal...')
                    return redirect(url_for('edit_noticias'))
    else:
        return redirect(url_for('logout'))

@noticiasBP.route('/update_img_noticias/', methods=['POST'])
@login_required
def update_img_noticias():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            #procesamiento de imágenes
            file = request.files['imagen_Noticias']
            base_path = os.path.dirname (__file__)
            filename = secure_filename(file.filename)
            extension = os.path.splitext(filename)[1]
            if extension == ".jpg" or extension == ".png" or extension == ".jpeg":
                nuevoNombreFile = stringAleatorio() + extension
                upload_path = os.path.join (base_path, config('RUTA_IMG_NOTICIAS'), nuevoNombreFile) 
                file.save(upload_path)
                #modifico el path
                start = int(config('CORTAR_RUTA'))
                url_imagen = upload_path[start:]
                
                edit_Imagen = Noticias(request.form['id'], None, None, None, url_imagen, None, None)
                
                respuesta_Edit_Imagen_Noticias = consultasNoticias.noticias_Editar_Imagen(db, edit_Imagen)
                
                if respuesta_Edit_Imagen_Noticias == True:
                    flash('Imagen actualizada con éxito...')
                    return redirect(url_for('edit_noticias'))
                else:
                    os.remove(upload_path)
                    flash('Algo salio mal...')
                    return redirect(url_for('edit_noticias'))

            else:
                flash("Formato de imagen invalido")
                return redirect(url_for('edit_noticias'))
        else:
            return redirect(url_for('edit_noticias'))
    else:
        return redirect(url_for('logout'))

@noticiasBP.route('/update_noticias/', methods=['POST'])
@login_required
def update_noticias():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            editar_Noticias = Noticias(request.form['id'], request.form['titulo_Noticias'], request.form['sub_Titulo_Noticias'],
                                        request.form['cuerpo_Noticias'], None, request.form['estado_Noticias'], request.form['fecha_Noticias'])
            
            respuesta_Editar_Noticias = consultasNoticias.noticias_Editar(db, editar_Noticias)
            if respuesta_Editar_Noticias == True:
                flash('Noticia actualizada con éxito...')
                return redirect(url_for('edit_noticias'))
            else:
                flash('Algo salio mal...')
                return redirect(url_for('edit_noticias'))
                
        else:
            return redirect(url_for('edit_noticias'))
    else:
        return redirect(url_for('logout'))

@noticiasBP.route('/delete_noticias/', methods=['POST'])
@login_required
def delete_noticias():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            eliminar_Noticias = Noticias(request.form['id'], None, None, None, None, None, None)
            respuesta_Eliminar_Noticias = consultasNoticias.noticias_Eliminar(db, eliminar_Noticias)
            if respuesta_Eliminar_Noticias == True:
                flash('Noticia eliminada con éxito...')
                return redirect(url_for('edit_noticias'))
            else:
                flash('Algo salio mal...')
                return redirect(url_for('edit_noticias'))
                
        else:
            return redirect(url_for('edit_noticias'))
    else:
        return redirect(url_for('logout'))