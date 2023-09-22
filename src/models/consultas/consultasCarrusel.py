from models.entidades.Carrusel import Carrusel

class consultasCarrusel():
    @classmethod
    def carrusel_Listar(self ,db):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Carrusel_Listar()"
            cur.execute(query_sql)
            data = cur.fetchall()
            cur.close()
            
            if data != None:
                carro = []
                for row in data:
                    carrusel = Carrusel(row[0], row[1], row[2], row[3], row[4])
                    carro.append(carrusel)
                    
                return carro
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def carrusel_ListarXEstado(self ,db):
        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Carrusel_ListarXEstado()"
            cur.execute(query_sql)
            data = cur.fetchall()
            cur.close()
            
            if data != None:
                carro = []
                for row in data:
                    carrusel = Carrusel(None, None, row[0], None, None)
                    carro.append(carrusel)
                    
                return carro
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def carrusel_Agregar(self, db, new_Carrusel):
        respuesta = False

        try:
            cur = db.connection.cursor()
            query_sql = "CALL sp_Carrusel_Existe('{}')".format(new_Carrusel.nombre_Carrusel)
            cur.execute(query_sql)
            row = cur.fetchone()
            cur.close()
            if row != None:
                mensaje = "existe"
                return mensaje  
            else:
                cur = db.connection.cursor()
            
                query_sql = "CALL sp_Carrusel_Agregar('{}','{}','{}','{}')".format(new_Carrusel.nombre_Carrusel, new_Carrusel.imagen_Carrusel, 
                                                                                        new_Carrusel.estado_Carrusel, new_Carrusel.fecha_Carrusel) 
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
    def carrusel_Editar_imagen(self, db, edit_Imagen):
        respuesta = False

        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Carrusel_Editar_Imagen('{}','{}')".format(edit_Imagen.id, edit_Imagen.imagen_Carrusel) 
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
    def carrusel_Editar(self, db, editar_Carrusel):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Carrusel_Editar('{}','{}','{}','{}')".format(editar_Carrusel.id, editar_Carrusel.nombre_Carrusel, 
                                                                                editar_Carrusel.estado_Carrusel, editar_Carrusel.fecha_Carrusel) 
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
    def carrusel_Eliminar(self, db, eliminar_Carrusel):
        respuesta = False
        try:
            cur = db.connection.cursor()
            
            query_sql = "CALL sp_Carrusel_Eliminar('{}')".format(eliminar_Carrusel.id) 
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