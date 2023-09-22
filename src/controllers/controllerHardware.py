#Flask
from flask import Blueprint, redirect, render_template, url_for, flash, request, session
#Login Seguro
from flask_login import login_required
#Modelos
from models.consultas.consultasHardware import consultasHardware
#Entidades
from models.entidades.Hardware import Hardware



hardwareBP = Blueprint('adminHardware', __name__)

@hardwareBP.route('/add_Inventario', methods=['POST'])
@login_required
def add_Inventario():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            
            new_Hardware = Hardware(None, request.form['id_Empleados_Hardware'], request.form['componente_Hardware'], 
                                    request.form['descripcion_Hardware'], request.form['marca_Hardware'], request.form['modelo_Hardware'], 
                                    request.form['serial_Hardware'], request.form['proveedor_Hardware'])
            
            respuesta_Add_Inventario = consultasHardware.hardware_Agregar(db, new_Hardware)
            if respuesta_Add_Inventario == "existe":
                flash('Ya esta existe en el inventario...')
                return redirect(url_for('edit_Hardware'))
            else:
                if respuesta_Add_Inventario == True:
                    flash('Se agregado con éxito al inventario...')
                    return redirect(url_for('edit_Hardware'))
                else:
                    flash('Algo salio mal...')
                    return redirect(url_for('edit_Hardware'))
        else:
            return redirect(url_for('edit_Hardware'))
    else:
        return redirect(url_for('logout'))
    
@hardwareBP.route('/update_Inventario/', methods=['POST'])
@login_required
def update_Inventario():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db

            editar_hardware = Hardware(request.form['id'], request.form['id_Empleados_Hardware'], request.form['componente_Hardware'],
                                        request.form['descripcion_Hardware'], request.form['marca_Hardware'], request.form['modelo_Hardware'],
                                        request.form['serial_Hardware'], request.form['proveedor_Hardware'])
            
            respuesta_Editar_Hardware = consultasHardware.hardware_Editar(db, editar_hardware)
            if respuesta_Editar_Hardware == True:
                flash('Inventario actualizado con éxito...')
                return redirect(url_for('edit_Hardware'))
            else:
                flash('Algo salio mal...')
                return redirect(url_for('edit_Hardware'))
                
        else:
            return redirect(url_for('edit_Hardware'))
    else:
        return redirect(url_for('logout'))
    
@hardwareBP.route('/delete_Inventario/', methods=['POST'])
@login_required
def delete_Inventario():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            eliminar_hardware = Hardware(request.form['id'], None, None, None, None, None, None, None)
            respuesta_Eliminar_NHardware = consultasHardware.hardware_Eliminar(db, eliminar_hardware)
            if respuesta_Eliminar_NHardware == True:
                flash('Inventario eliminado con éxito...')
                return redirect(url_for('edit_Hardware'))
            else:
                flash('Algo salio mal...')
                return redirect(url_for('edit_Hardware'))
                
        else:
            return redirect(url_for('edit_Hardware'))
    else:
        return redirect(url_for('logout'))
    
@hardwareBP.route('/reporte_inventario/', methods=['POST'])
@login_required
def reporte_inventario():
    roll = session["id_Rol_Usuarios"]
    if roll == "1":
        if request.method == 'POST':
            #BD
            from app import db
            
            formato_reporte = request.form['formato']

            id_reporte = Hardware(None, request.form['id_Empleados_Hardware'], None, None, None, None, None, None)

            oReporte = consultasHardware.hardware_ListarXReporte(db, id_reporte)

            if oReporte == None:
                flash('Algo salio mal...')
                return redirect(url_for('edit_Hardware'))
            
            if formato_reporte == "vertical":
                return render_template('admin/reporte_vertical.html', reportes = oReporte)

            if formato_reporte == "horizontal":
                return render_template('admin/reporte_horizontal.html', reportes = oReporte)
                
        else:
            return redirect(url_for('edit_Hardware'))
    else:
        return redirect(url_for('logout'))