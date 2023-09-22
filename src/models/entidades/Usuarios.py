from werkzeug.security import check_password_hash#, generate_password_hash
from flask_login import UserMixin

class Usuarios(UserMixin):
    def __init__(self, id, usuario_Usuarios, clave_Usuarios, nombre_Usuarios, id_Rol_Usuarios, estado_Usuarios, fecha_Usuarios) -> None:
        self.id = id
        self.usuario_Usuarios = usuario_Usuarios
        self.clave_Usuarios = clave_Usuarios
        self.nombre_Usuarios = nombre_Usuarios
        self.id_Rol_Usuarios = id_Rol_Usuarios
        self.estado_Usuarios = estado_Usuarios
        self.fecha_Usuarios = fecha_Usuarios
    
    @classmethod
    def check_Clave(self, hashed_Clave_Usuarios, clave_Usuarios):
        return check_password_hash(hashed_Clave_Usuarios, clave_Usuarios)

#print(generate_password_hash('fabian'))
