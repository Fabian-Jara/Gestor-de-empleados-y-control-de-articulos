from models.entidades.vistas.VistaHardwareListaAll import VistaHardwareListaAll
from models.entidades.Hardware import Hardware

class consultasHardware():
    @classmethod
    def hardware_Listar(self ,db):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Hardware_Listar()"
            cur.execute(query_sql)
            data = cur.fetchall()
            cur.close()
            
            if data != None:
                oHardware = []
                for row in data:
                    listaHardware = VistaHardwareListaAll(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7], row[8])
                    oHardware.append(listaHardware)

                return oHardware
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def hardware_Agregar(self, db, new_Hardware):
        respuesta = False

        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Hardware_Existe('{}')".format(new_Hardware.serial_Hardware)
            cur.execute(query_sql)
            row = cur.fetchone()
            cur.close()
            if row != None:
                mensaje = "existe"
                return mensaje  
            else:
                cur = db.connection.cursor()
            
                query_sql = "CALL sp_Hardware_Agregar('{}','{}','{}','{}','{}','{}','{}')".format(new_Hardware.id_Empleados_Hardware, new_Hardware.componente_Hardware, 
                                                                                                    new_Hardware.descripcion_Hardware, new_Hardware.marca_Hardware, 
                                                                                                    new_Hardware.modelo_Hardware, new_Hardware.serial_Hardware, 
                                                                                                    new_Hardware.proveedor_Hardware)
                cur.execute(query_sql)
                db.connection.commit()
                cur.close()
                respuesta = True
                if respuesta == True:
                    return respuesta
                else:
                    return respuesta
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def hardware_Editar(self, db, editar_hardware):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Hardware_Editar('{}','{}','{}','{}','{}','{}','{}','{}')".format(editar_hardware.id, editar_hardware.id_Empleados_Hardware, 
                                                                                                    editar_hardware.componente_Hardware, editar_hardware.descripcion_Hardware,
                                                                                                    editar_hardware.marca_Hardware, editar_hardware.modelo_Hardware, 
                                                                                                    editar_hardware.serial_Hardware, editar_hardware.proveedor_Hardware) 
            cur.execute(query_sql)
            db.connection.commit()
            cur.close()
            respuesta = True
            if respuesta == True:
                return respuesta
            else:
                return respuesta
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def hardware_Eliminar(self, db, eliminar_hardware):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Hardware_Eliminar('{}')".format(eliminar_hardware.id) 
            cur.execute(query_sql)
            db.connection.commit()
            cur.close()
            respuesta = True
            if respuesta == True:
                return respuesta
            else:
                return respuesta
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def hardware_ListarXReporte(self ,db, id_reporte):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Hardware_ListarXId('{}')".format(id_reporte.id_Empleados_Hardware) 
            cur.execute(query_sql)
            data = cur.fetchall()
            cur.close()
            
            if data != None:
                oHardware = []
                for row in data:
                    listaReporte = VistaHardwareListaAll(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7], row[8])
                    oHardware.append(listaReporte)

                return oHardware
            else:
                return None
        except Exception as ex:
            raise Exception(ex)