from models.entidades.Paginas import Paginas

class consultasPaginas():
    @classmethod
    def paginas_Listar(self ,db):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Paginas_Listar()"
            cur.execute(query_sql)
            data = cur.fetchall()
            cur.close()
            
            if data != None:
                page = []
                for row in data:
                    pagina = Paginas(row[0], row[1], row[2], row[3], row[4], row[5])
                    page.append(pagina)
                    
                return page
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def paginas_ListarXEstado(self ,db):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Paginas_ListarXEstado()"
            cur.execute(query_sql)
            data = cur.fetchall()
            cur.close()
            
            if data != None:
                page = []
                for row in data:
                    pagina = Paginas(row[0], row[1], None, None, None, None)
                    page.append(pagina)
                    
                return page
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def paginas_Agregar(self, db, new_Page):
        respuesta = False

        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Paginas_Existe('{}')".format(new_Page.url_Paginas)
            cur.execute(query_sql)
            row = cur.fetchone()
            cur.close()
            if row != None:
                mensaje = "existe"
                return mensaje  
            else:
                cur = db.connection.cursor()
            
                query_sql = "CALL sp_Paginas_Agregar('{}','{}','{}','{}','{}')".format(new_Page.nombre_Paginas, new_Page.url_Paginas, 
                                                                                        new_Page.imagen_Paginas, new_Page.estado_Paginas, 
                                                                                        new_Page.fecha_Paginas) 
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
    def paginas_Editar_imagen(self, db, edit_Imagen):
        respuesta = False

        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Paginas_Editar_imagen('{}','{}')".format(edit_Imagen.id, edit_Imagen.imagen_Paginas) 
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
    def paginas_Editar(self, db, editar_Paginas):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Paginas_Editar('{}','{}','{}','{}','{}')".format(editar_Paginas.id, editar_Paginas.nombre_Paginas, 
                                                                                    editar_Paginas.url_Paginas, editar_Paginas.estado_Paginas, 
                                                                                    editar_Paginas.fecha_Paginas) 
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
    def paginas_Eliminar(self, db, eliminar_Paginas):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Paginas_Eliminar('{}')".format(eliminar_Paginas.id) 
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
    def paginas_ListarXPermisos(self, db, roll):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Paginas_ListarXPermisos('{}')".format(roll) 
            cur.execute(query_sql)
            data = cur.fetchall()
            cur.close()
            
            if data != None:
                page = []
                for row in data:
                    pagina = Paginas(None, row[0], row[1], row[2], None, None)
                    page.append(pagina)
                    
                return page
            else:
                return None
        except Exception as ex:
            raise Exception(ex)