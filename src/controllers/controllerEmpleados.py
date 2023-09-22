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
from models.consultas.consultasEmpleados import consultasEmpleados
#Entidades
from models.entidades.Empleados import Empleados
#Para usar variables de entorno
from decouple import config

empleadosBP = Blueprint('adminEmpleados', __name__)

def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio

@empleadosBP.route('/add_empleados/', methods=['POST'])
@login_required
def add_empleados():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            #procesamiento de imágenes
            file = request.files['imagen_Empleados']
            base_path = os.path.dirname (__file__)
            filename = secure_filename(file.filename)
            extension = os.path.splitext(filename)[1]
            
            if extension == ".jpg" or extension == ".png" or extension == ".jpeg":
                nuevoNombreFile = stringAleatorio() + extension
                upload_path = os.path.join (base_path, config('RUTA_IMG_EMPLEADOS'), nuevoNombreFile) 
                file.save(upload_path)
                #modifico el path
                start = int(config('CORTAR_RUTA'))
                url_imagen = upload_path[start:]
                
                new_Empleados = Empleados(None, request.form['nombre_Empleados'], url_imagen, 
                                    request.form['estado_Empleados'], request.form['fecha_Empleados'])
                
                respuesta_Add_Empleados = consultasEmpleados.empleados_Agregar(db, new_Empleados)
                if respuesta_Add_Empleados == "existe":
                    os.remove(upload_path)
                    flash('Este empleado ya existe...')
                    return redirect(url_for('edit_empleados'))
                else:
                    if respuesta_Add_Empleados == True:
                        flash('Empleado agregado con éxito...')
                        return redirect(url_for('edit_empleados'))
                    else:
                        os.remove(upload_path)
                        flash('Algo salio mal...')
                        return redirect(url_for('edit_empleados'))
    else:
        return redirect(url_for('logout'))

@empleadosBP.route('/update_img_empleados/', methods=['POST'])
@login_required
def update_img_empleados():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            #procesamiento de imágenes
            file = request.files['imagen_Empleados']
            base_path = os.path.dirname (__file__)
            filename = secure_filename(file.filename)
            extension = os.path.splitext(filename)[1]
            
            if extension == ".jpg" or extension == ".png" or extension == ".jpeg":
                nuevoNombreFile = stringAleatorio() + extension
                upload_path = os.path.join (base_path, config('RUTA_IMG_EMPLEADOS'), nuevoNombreFile) 
                file.save(upload_path)
                #modifico el path
                start = int(config('CORTAR_RUTA'))
                url_imagen = upload_path[start:]
                
                edit_Imagen = Empleados(request.form['id'], None, url_imagen, None, None)
                
                respuesta_Edit_Imagen_Carrusel = consultasEmpleados.empleados_Editar_Imagen(db, edit_Imagen)
                
                if respuesta_Edit_Imagen_Carrusel == True:
                        flash('Imagen actualizada con éxito...')
                        return redirect(url_for('edit_empleados'))
                else:
                    os.remove(upload_path)
                    flash('Algo salio mal...')
                    return redirect(url_for('edit_empleados'))

            else:
                flash("Formato de imagen invalido")
                return redirect(url_for('edit_empleados'))
        else:
            return redirect(url_for('edit_empleados'))
    else:
        return redirect(url_for('logout'))

@empleadosBP.route('/update_empleados/', methods=['POST'])
@login_required
def update_empleados():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            editar_Empleados = Empleados(request.form['id'], request.form['nombre_Empleados'], None, 
                                request.form['estado_Empleados'], request.form['fecha_Empleados'])
            respuesta_Editar_Empleados = consultasEmpleados.empleados_Editar(db, editar_Empleados)
            if respuesta_Editar_Empleados == True:
                flash('Empleado actualizado con éxito...')
                return redirect(url_for('edit_empleados'))
            else:
                flash('Algo salio mal...')
                return redirect(url_for('edit_empleados'))
                
        else:
            return redirect(url_for('edit_empleados'))
    else:
        return redirect(url_for('logout'))

@empleadosBP.route('/delete_empleados/', methods=['POST'])
@login_required
def delete_empleados():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            eliminar_Empleados = Empleados(request.form['id'], None, None, None, None)
            respuesta_Eliminar_Empleados = consultasEmpleados.empleados_Eliminar(db, eliminar_Empleados)
            if respuesta_Eliminar_Empleados == True:
                flash('Empleado eliminado con éxito...')
                return redirect(url_for('edit_empleados'))
            else:
                flash('Algo salio mal...')
                return redirect(url_for('edit_empleados'))
                
        else:
            return redirect(url_for('edit_empleados'))
    else:
        return redirect(url_for('logout'))