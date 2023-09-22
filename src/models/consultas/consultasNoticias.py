from models.entidades.Noticias import Noticias

class consultasNoticias():
    @classmethod
    def noticias_Listar(self ,db):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Noticias_Listar()"
            cur.execute(query_sql)
            data = cur.fetchall()
            cur.close()
            
            if data != None:
                noticias = []
                for row in data:
                    noticia = Noticias(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    noticias.append(noticia)
                    
                return noticias
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def noticias_ListarXEstado(self ,db):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Noticias_ListarXEstado()"
            cur.execute(query_sql)
            data = cur.fetchall()
            cur.close()
            
            if data != None:
                noticias = []
                for row in data:
                    noticia = Noticias(None, row[0], row[1], row[2], row[3], None, row[4])
                    noticias.append(noticia)
                    
                return noticias
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def noticias_Agregar(self, db, new_Noticias):
        respuesta = False

        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Noticias_Existe('{}')".format(new_Noticias.titulo_Noticias)
            cur.execute(query_sql)
            row = cur.fetchone()
            cur.close()
            if row != None:
                mensaje = "existe"
                return mensaje  
            else:
                cur = db.connection.cursor()
            
                query_sql = "CALL sp_Noticias_Agregar('{}','{}','{}','{}','{}')".format(new_Noticias.titulo_Noticias, new_Noticias.sub_Titulo_Noticias, 
                                                                                        new_Noticias.cuerpo_Noticias, new_Noticias.estado_Noticias, 
                                                                                        new_Noticias.fecha_Noticias) 
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
    def noticias_Editar_Imagen(self, db, edit_Imagen):
        respuesta = False

        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Noticias_Editar_Imagen('{}','{}')".format(edit_Imagen.id, edit_Imagen.imagen_Noticias) 
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
    def noticias_Editar(self, db, editar_Noticias):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Noticias_Editar('{}','{}','{}','{}','{}','{}')".format(editar_Noticias.id, editar_Noticias.titulo_Noticias, 
                                                                                    editar_Noticias.sub_Titulo_Noticias, editar_Noticias.cuerpo_Noticias,
                                                                                    editar_Noticias.estado_Noticias, editar_Noticias.fecha_Noticias) 
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
    def noticias_Eliminar(self, db, eliminar_Noticias):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Noticias_Eliminar('{}')".format(eliminar_Noticias.id) 
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