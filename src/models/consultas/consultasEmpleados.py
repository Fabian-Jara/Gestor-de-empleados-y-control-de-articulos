from models.entidades.Empleados import Empleados

class consultasEmpleados():
    @classmethod
    def empleados_Listar(self ,db):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Empleados_Listar()"
            cur.execute(query_sql)
            data = cur.fetchall()
            cur.close()
            
            if data != None:
                empleados = []
                for row in data:
                    empleado = Empleados(row[0], row[1], row[2], row[3], row[4])
                    empleados.append(empleado)
                    
                return empleados
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def empleados_ListarXEstado(self ,db):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Empleados_ListarXEstado()"
            cur.execute(query_sql)
            data = cur.fetchall()
            cur.close()
            
            if data != None:
                empleados = []
                for row in data:
                    empleado = Empleados(row[0], row[1], row[2], None, None)
                    empleados.append(empleado)
                    
                return empleados
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def empleados_Agregar(self, db, new_Empleados):
        respuesta = False

        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Empleados_Existe('{}')".format(new_Empleados.nombre_Empleados)
            cur.execute(query_sql)
            row = cur.fetchone()
            cur.close()
            if row != None:
                mensaje = "existe"
                return mensaje  
            else:
                cur = db.connection.cursor()
            
                query_sql = "CALL sp_Empleados_Agregar('{}','{}','{}','{}')".format(new_Empleados.nombre_Empleados, new_Empleados.imagen_Empleados, 
                                                                                        new_Empleados.estado_Empleados, new_Empleados.fecha_Empleados) 
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
    def empleados_Editar_Imagen(self, db, edit_Imagen):
        respuesta = False

        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Empleados_Editar_Imagen('{}','{}')".format(edit_Imagen.id, edit_Imagen.imagen_Empleados) 
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
    def empleados_Editar(self, db, editar_Empleados):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Empleados_Editar('{}','{}','{}','{}')".format(editar_Empleados.id, editar_Empleados.nombre_Empleados, 
                                                                                editar_Empleados.estado_Empleados, editar_Empleados.fecha_Empleados) 
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
    def empleados_Eliminar(self, db, eliminar_empleados):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Empleados_Eliminar('{}')".format(eliminar_empleados.id) 
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