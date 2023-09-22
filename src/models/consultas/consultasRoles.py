from models.entidades.Roles import Roles

class consultasRoles():
    @classmethod
    def rol_Listar(self ,db):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Rol_Listar()"
            cur.execute(query_sql)
            data = cur.fetchall()
            cur.close()
            
            if data != None:
                oRol = []
                for row in data:
                    listaRoles = Roles(row[0], row[1], row[2], row[3])
                    oRol.append(listaRoles)
                    
                return oRol
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def rol_ListarXEstado(self ,db):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Rol_ListarXEstado()"
            cur.execute(query_sql)
            data = cur.fetchall()
            cur.close()
            
            if data != None:
                oRol = []
                for row in data:
                    listaRoles = Roles(row[0], row[1], None, None)
                    oRol.append(listaRoles)
                    
                return oRol
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def rol_Agregar(self, db, new_Rol):
        respuesta = False

        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Rol_Existe('{}')".format(new_Rol.nombre_Rol)
            cur.execute(query_sql)
            row = cur.fetchone()
            cur.close()
            if row != None:
                mensaje = "existe"
                return mensaje  
            else:
                cur = db.connection.cursor()
            
                query_sql = "CALL sp_Rol_Agregar('{}', '{}', '{}')".format(new_Rol.nombre_Rol, new_Rol.estado_Rol, new_Rol.fecha_Rol)
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
    def rol_Editar(self, db, editar_Rol):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Rol_Editar('{}','{}','{}','{}')".format(editar_Rol.id, editar_Rol.nombre_Rol, 
                                                                            editar_Rol.estado_Rol, editar_Rol.fecha_Rol) 
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
    def rol_Eliminar(self, db, eliminar_Rol):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Rol_Eliminar('{}')".format(eliminar_Rol.id) 
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