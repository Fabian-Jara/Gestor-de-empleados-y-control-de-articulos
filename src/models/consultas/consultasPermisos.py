from models.entidades.Permisos import Permisos
from models.entidades.vistas.VistaPermisosListaAll import VistaPermisosListaAll

class consultasPermisos():
    @classmethod
    def permisos_Listar(self ,db):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Permisos_Listar()"
            cur.execute(query_sql)
            data = cur.fetchall()
            cur.close()
            
            if data != None:
                oPermiso = []
                for row in data:
                    listaPermiso = VistaPermisosListaAll(row[0], row[1], row[2], row[3], row[4], row[5])
                    oPermiso.append(listaPermiso)
                    
                return oPermiso
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def permisos_Agregar(self, db, new_Permiso):
        respuesta = False

        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Permiso_Existe('{}', '{}')".format(new_Permiso.id_Rol_Permisos, new_Permiso.id_Paginas_Permisos)
            cur.execute(query_sql)
            row = cur.fetchone()
            cur.close()
            if row != None:
                mensaje = "existe"
                return mensaje  
            else:
                cur = db.connection.cursor()
            
                query_sql = "CALL sp_Permisos_Agregar('{}','{}','{}')".format(new_Permiso.id_Rol_Permisos, new_Permiso.id_Paginas_Permisos, 
                                                                                new_Permiso.estado_Permisos) 
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
    def permisos_Editar(self, db, editar_permiso):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Permisos_Editar('{}','{}','{}','{}')".format(editar_permiso.id, editar_permiso.id_Rol_Permisos, 
                                                                                editar_permiso.id_Paginas_Permisos, editar_permiso.estado_Permisos) 
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
    def permisos_Eliminar(self, db, eliminar_Permisos):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Permisos_Eliminar('{}')".format(eliminar_Permisos.id) 
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
    def permisos_EliminarXPaginas(self, db, id_Pagina):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Permisos_EliminarXPaginas('{}')".format(id_Pagina) 
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