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
from models.consultas.consultasCarrusel import consultasCarrusel
#Entidades
from models.entidades.Carrusel import Carrusel
#Para usar variables de entorno
from decouple import config

carruselBP = Blueprint('adminCarrusel', __name__)

def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio

@carruselBP.route('/add_carrusel/', methods=['POST'])
@login_required
def add_carrusel():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            #procesamiento de imágenes
            file = request.files['imagen_Carrusel']
            base_path = os.path.dirname (__file__)
            filename = secure_filename(file.filename)
            extension = os.path.splitext(filename)[1]
            
            if extension == ".jpg" or extension == ".png" or extension == ".jpeg":
                nuevoNombreFile = stringAleatorio() + extension
                upload_path = os.path.join (base_path, config('RUTA_IMG_CARRUSEL'), nuevoNombreFile) 
                file.save(upload_path)
                #modifico el path
                start = int(config('CORTAR_RUTA'))
                url_imagen = upload_path[start:]
                
                new_Carrusel = Carrusel(None, request.form['nombre_Carrusel'], url_imagen, 
                                    request.form['estado_Carrusel'], request.form['fecha_Carrusel'])
                
                respuesta_Add_Carrusel = consultasCarrusel.carrusel_Agregar(db, new_Carrusel)
                if respuesta_Add_Carrusel == "existe":
                    os.remove(upload_path)
                    flash('Este carrusel ya existe...')
                    return redirect(url_for('edit_carrusel'))
                else:
                    if respuesta_Add_Carrusel == True:
                        flash('Carrusel agregada con éxito...')
                        return redirect(url_for('edit_carrusel'))
                    else:
                        os.remove(upload_path)
                        flash('Algo salio mal...')
                        return redirect(url_for('edit_carrusel'))

            else:
                flash("Formato de imagen invalido")
                return redirect(url_for('edit_carrusel'))
        else:
            return redirect(url_for('edit_carrusel'))
    else:
        return redirect(url_for('logout'))

@carruselBP.route('/update_img_carrusel/', methods=['POST'])
@login_required
def update_img_carrusel():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            #procesamiento de imágenes
            file = request.files['imagen_Carrusel']
            base_path = os.path.dirname (__file__)
            filename = secure_filename(file.filename)
            extension = os.path.splitext(filename)[1]
            
            if extension == ".jpg" or extension == ".png" or extension == ".jpeg":
                nuevoNombreFile = stringAleatorio() + extension
                upload_path = os.path.join (base_path, config('RUTA_IMG_CARRUSEL'), nuevoNombreFile) 
                file.save(upload_path)
                #modifico el path
                start = int(config('CORTAR_RUTA'))
                url_imagen = upload_path[start:]
                
                edit_Imagen = Carrusel(request.form['id'], None, url_imagen, None, None)
                
                respuesta_Edit_Imagen_Carrusel = consultasCarrusel.carrusel_Editar_imagen(db, edit_Imagen)
                
                if respuesta_Edit_Imagen_Carrusel == True:
                        flash('Imagen actualizada con éxito...')
                        return redirect(url_for('edit_carrusel'))
                else:
                    os.remove(upload_path)
                    flash('Algo salio mal...')
                    return redirect(url_for('edit_carrusel'))

            else:
                flash("Formato de imagen invalido")
                return redirect(url_for('edit_carrusel'))
        else:
            return redirect(url_for('edit_carrusel'))
    else:
        return redirect(url_for('logout'))

@carruselBP.route('/update_carrusel/', methods=['POST'])
@login_required
def update_carrusel():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            editar_Carrusel = Carrusel(request.form['id'], request.form['nombre_Carrusel'], None, 
                                request.form['estado_Carrusel'], request.form['fecha_Carrusel'])
            respuesta_Editar_Carrusel = consultasCarrusel.carrusel_Editar(db, editar_Carrusel)
            if respuesta_Editar_Carrusel == True:
                flash('Carrusel actualizado con éxito...')
                return redirect(url_for('edit_carrusel'))
            else:
                flash('Algo salio mal...')
                return redirect(url_for('edit_carrusel'))
                
        else:
            return redirect(url_for('edit_carrusel'))
    else:
        return redirect(url_for('logout'))

@carruselBP.route('/delete_carrusel/', methods=['POST'])
@login_required
def delete_carrusel():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            eliminar_Carrusel = Carrusel(request.form['id'], None, None, None, None)
            respuesta_Eliminar_Carrusel = consultasCarrusel.carrusel_Eliminar(db, eliminar_Carrusel)
            if respuesta_Eliminar_Carrusel == True:
                flash('Carrusel eliminado con éxito...')
                return redirect(url_for('edit_carrusel'))
            else:
                flash('Algo salio mal...')
                return redirect(url_for('edit_carrusel'))
                
        else:
            return redirect(url_for('edit_carrusel'))
    else:
        return redirect(url_for('logout'))