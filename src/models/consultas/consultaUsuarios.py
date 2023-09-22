from models.entidades.Usuarios import Usuarios
from models.entidades.vistas.VistaUsuariosListaAll import VistaUsuariosListaAll

class consultaUsuarios():
    @classmethod
    def usuarios_Validar_Login(self, db, user):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Usuarios_Validar_Login('{}')".format(user.usuario_Usuarios)
            cur.execute(query_sql)
            row = cur.fetchone()
            cur.close()
            if row != None:
                user = Usuarios(row[0], row[1], Usuarios.check_Clave(row[2], user.clave_Usuarios), row[3], row[4], row[5], None)
                return user
            else:
                return None
        except Exception as ex:
            print(ex)
            raise Exception(ex)
        
    @classmethod
    def usuarios_Listar(self, db):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Usuarios_Listar()"
            cur.execute(query_sql)
            data = cur.fetchall()
            cur.close()
            
            if data != None:
                user = []
                for row in data:
                    usuario = VistaUsuariosListaAll(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    user.append(usuario)
                    
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def usuarios_Agregar(self, db, new_User):
        respuesta = False

        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Usuarios_Existe('{}','{}')".format(new_User.usuario_Usuarios, new_User.nombre_Usuarios)
            cur.execute(query_sql)
            row = cur.fetchone()
            cur.close()
            if row != None:
                mensaje = "existe"
                return mensaje  
            else:
                cur = db.connection.cursor()
            
                query_sql = "CALL sp_Usuarios_Agregar('{}','{}','{}','{}','{}','{}')".format(new_User.usuario_Usuarios, new_User.clave_Usuarios, 
                                                                                            new_User.nombre_Usuarios, new_User.id_Rol_Usuarios, 
                                                                                            new_User.estado_Usuarios, new_User.fecha_Usuarios) 
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
    def usuarios_Editar(self, db, editar_user):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Usuarios_Editar('{}','{}','{}','{}','{}','{}')".format(editar_user.id, editar_user.usuario_Usuarios, 
                                                                                            editar_user.nombre_Usuarios, editar_user.id_Rol_Usuarios, 
                                                                                            editar_user.estado_Usuarios, editar_user.fecha_Usuarios) 
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
    def usuarios_Eliminar(self, db, eliminar_user):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Usuarios_Eliminar('{}')".format(eliminar_user.id) 
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
    def usuarios_Clave(self, db, clave_user):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Usuarios_Editar_Clave('{}','{}')".format(clave_user.id, clave_user.clave_Usuarios) 
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
    def usuarios_Obtener(self, db, id):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Usuarios_Obtener('{}')".format(id)
            cur.execute(query_sql)
            row = cur.fetchone()
            cur.close()
            if row != None:
                return Usuarios(row[0], row[1], None, row[2], row[3], row[4], row[5])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def usuarios_Bloquear(self, db, estado):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Usuarios_Bloquear('{}','{}')".format(estado.usuario_Usuarios, estado.estado_Usuarios) 
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