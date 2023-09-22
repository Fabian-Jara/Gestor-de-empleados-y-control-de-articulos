USE nombre_de_la_base ;

CREATE TABLE rol (
    id INT NOT NULL AUTO_INCREMENT,
    nombre_Rol VARCHAR(45) NOT NULL,
    estado_Rol BOOLEAN NOT NULL,
    fecha_Rol DATE NOT NULL,
    PRIMARY KEY (id),
    UNIQUE INDEX nombre_Rol_UNIQUE (nombre_Rol ASC) VISIBLE);

CREATE TABLE usuarios (
    id INT NOT NULL AUTO_INCREMENT,
    usuario_Usuarios VARCHAR(45) NOT NULL,
    clave_Usuarios VARCHAR(102) NOT NULL,
    nombre_Usuarios VARCHAR(45) NOT NULL,
    id_Rol_Usuarios INT NOT NULL,
    estado_Usuarios BOOLEAN NOT NULL,
    fecha_Usuarios DATE NOT NULL,
    PRIMARY KEY (id),
    UNIQUE INDEX usuario_Usuarios_UNIQUE (usuario_Usuarios ASC) VISIBLE,
    UNIQUE INDEX nombre_Usuarios_UNIQUE (nombre_Usuarios ASC) VISIBLE);

ALTER TABLE usuarios ADD CONSTRAINT fk_Rol_Usuarios
FOREIGN KEY (id_Rol_Usuarios) REFERENCES rol (id);

CREATE TABLE paginas (
    id INT NOT NULL AUTO_INCREMENT,
    nombre_Paginas VARCHAR(45) NOT NULL,
    url_Paginas VARCHAR(190) NOT NULL,
    imagen_Paginas VARCHAR(102) NOT NULL,
    estado_Paginas BOOLEAN NOT NULL,
    fecha_Paginas DATE NOT NULL,
    PRIMARY KEY (id),
    UNIQUE INDEX url_Paginas_UNIQUE (url_Paginas ASC) VISIBLE);

CREATE TABLE permisos (
    id INT NOT NULL AUTO_INCREMENT,
    id_Rol_Permisos INT NOT NULL,
    id_Paginas_Permisos INT NOT NULL,
    estado_Permisos BOOLEAN NOT NULL,
    PRIMARY KEY (id));

ALTER TABLE permisos ADD CONSTRAINT fk_Rol_Permisos
FOREIGN KEY (id_Rol_Permisos) REFERENCES rol (id);

ALTER TABLE permisos ADD CONSTRAINT fk_Paginas_Permisos
FOREIGN KEY (id_Paginas_Permisos) REFERENCES paginas (id);

CREATE TABLE empleados (
    id INT NOT NULL AUTO_INCREMENT,
    nombre_Empleados VARCHAR(45) NOT NULL,
    imagen_Empleados VARCHAR(102) NOT NULL,
    estado_Empleados BOOLEAN NOT NULL,
    fecha_Empleados DATE NOT NULL,
    PRIMARY KEY (id),
    UNIQUE INDEX nombre_Empleados_UNIQUE (nombre_Empleados ASC) VISIBLE);

CREATE TABLE hardware (
	id INT NOT NULL AUTO_INCREMENT,
    id_Empleados_Hardware INT NOT NULL,
    componente_Hardware VARCHAR(102) NOT NULL,
    descripcion_Hardware VARCHAR(502) NOT NULL,
    marca_Hardware VARCHAR(102) NOT NULL,
    modelo_Hardware VARCHAR(102) NOT NULL,
    serial_Hardware VARCHAR(102) NOT NULL,
    proveedor_Hardware VARCHAR(102) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE INDEX serial_Hardware_UNIQUE (serial_Hardware ASC) VISIBLE);

ALTER TABLE hardware ADD CONSTRAINT fk_Empleados_Hardware
FOREIGN KEY (id_Empleados_Hardware) REFERENCES empleados (id);

CREATE TABLE carrusel (
    id INT NOT NULL AUTO_INCREMENT,
    nombre_Carrusel VARCHAR(45) NOT NULL,
    imagen_Carrusel VARCHAR(102) NOT NULL,
    estado_Carrusel BOOLEAN NOT NULL,
    fecha_Carrusel DATE NOT NULL,
    PRIMARY KEY (id),
    UNIQUE INDEX nombre_Carrusel_UNIQUE (nombre_Carrusel ASC) VISIBLE);

CREATE TABLE noticias (
    id INT NOT NULL AUTO_INCREMENT,
    titulo_Noticias VARCHAR(102) NOT NULL,
    sub_Titulo_Noticias VARCHAR(102) NOT NULL,
    cuerpo_Noticias VARCHAR(1000) NOT NULL,
    imagen_Noticias VARCHAR(102) NULL,
    estado_Noticias BOOLEAN NOT NULL,
    fecha_Noticias DATE NOT NULL,
    PRIMARY KEY (id),
    UNIQUE INDEX titulo_Noticias_UNIQUE (titulo_Noticias ASC) VISIBLE);

DELIMITER //
CREATE PROCEDURE sp_Rol_Agregar (
	in vsp_Nombre_Rol VARCHAR(45),
    in vsp_Estado_Rol BOOLEAN,
    in vsp_Fecha_rol DATE
)
BEGIN
	INSERT INTO rol (
		nombre_Rol, 
        estado_Rol, 
        fecha_Rol
	) 
    VALUES (
		vsp_Nombre_Rol, 
        vsp_Estado_Rol, 
        vsp_Fecha_rol 
	);
END//
DELIMITER ;

CALL sp_Rol_Agregar('Administrador', '1', '2023-02-16');

DELIMITER //
CREATE PROCEDURE sp_Rol_Listar ()
BEGIN
	SELECT 
		id, 
        nombre_Rol, 
        estado_Rol, 
        fecha_Rol 
	FROM 
		rol;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Rol_ListarXEstado ()
BEGIN
	SELECT 
		id, 
        nombre_Rol
	FROM 
		rol
	WHERE
		estado_Rol = 1;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Rol_Existe (
	in vsp_Nombre_Rol varchar(45)
)
BEGIN
	SELECT 
		id 
	FROM 
		rol 
	WHERE 
		nombre_Rol = vsp_Nombre_Rol;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Rol_Editar (
	in vsp_Id INT,
	in vsp_Nombre_Rol VARCHAR(45),
    in vsp_Estado_Rol BOOLEAN,
    in vsp_Fecha_rol DATE
)
BEGIN
	UPDATE 
		rol 
	SET 
		nombre_Rol = vsp_Nombre_Rol, 
        estado_Rol = vsp_Estado_Rol, 
        fecha_Rol = vsp_Fecha_rol 
	WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Rol_Eliminar (
	in vsp_Id INT
)
BEGIN
	DELETE FROM 
		rol 
	WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Usuarios_Agregar (
	in vsp_Usuario_Usuarios VARCHAR(45),
    in vsp_Clave_Usuarios VARCHAR(102),
    in vsp_Nombre_Usuarios VARCHAR(45),
    in vsp_Id_Rol_Usuarios INT,
    in vsp_Estado_Usuarios BOOLEAN,
    in vsp_Fecha_Usuarios DATE
)
BEGIN
	INSERT INTO usuarios (
		usuario_Usuarios, 
        clave_Usuarios, 
        nombre_Usuarios, 
        id_Rol_Usuarios, 
		estado_Usuarios, 
        fecha_Usuarios
	) 
    VALUES (
		vsp_Usuario_Usuarios, 
        vsp_Clave_Usuarios, 
        vsp_Nombre_Usuarios, 
        vsp_Id_Rol_Usuarios, 
		vsp_Estado_Usuarios, 
        vsp_Fecha_Usuarios
	);
END//
DELIMITER ;

CALL sp_Usuarios_Agregar('admin', 'contraseña cifrada', 'Administrador', '1', '1', '2023-02-16');

DELIMITER //
CREATE PROCEDURE sp_Usuarios_Listar ()
BEGIN
	SELECT 
		usuarios.id, 
		usuarios.usuario_Usuarios, 
		usuarios.nombre_Usuarios,
		rol.id,
		rol.nombre_Rol, 
		usuarios.estado_Usuarios,
		usuarios.fecha_Usuarios
	FROM rol
	JOIN usuarios ON rol.id = usuarios.id_Rol_Usuarios;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Usuarios_Existe (
	in vsp_Usuario_Usuarios varchar(45),
    in vsp_Nombre_Usuarios	varchar(45)
)
BEGIN
	SELECT 
		id 
	FROM 
		usuarios 
	WHERE 
		usuario_Usuarios = vsp_Usuario_Usuarios OR nombre_Usuarios = vsp_Nombre_Usuarios;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Usuarios_Validar_Login (
	vsp_Usuario_Usuarios VARCHAR(45)
)
BEGIN
	SELECT 
		id,
        usuario_Usuarios,
        clave_Usuarios,
        nombre_Usuarios,
        id_Rol_Usuarios, 
		Estado_Usuarios 
	FROM 
		usuarios
    WHERE 
		usuario_Usuarios = vsp_Usuario_Usuarios;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Usuarios_Editar (
	in vsp_Id INT,
	in vsp_Usuario_Usuarios VARCHAR(45),
    in vsp_Nombre_Usuarios VARCHAR(45),
    in vsp_Id_Rol_Usuarios INT,
    in vsp_Estado_Usuarios BOOLEAN,
    in vsp_Fecha_Usuarios DATE
)
BEGIN
	UPDATE 
		usuarios 
	SET 
		usuario_Usuarios = vsp_Usuario_Usuarios, 
        nombre_Usuarios = vsp_Nombre_Usuarios, 
		id_Rol_Usuarios = vsp_Id_Rol_Usuarios, 
        estado_Usuarios = vsp_Estado_Usuarios, 
        fecha_Usuarios = vsp_Fecha_Usuarios 
    WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Usuarios_Editar_Clave (
	in vsp_Id INT,
	in vsp_Clave_Usuarios VARCHAR(102)
)
BEGIN
	UPDATE 
		usuarios 
	SET 
		clave_Usuarios = vsp_Clave_Usuarios 
    WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Usuarios_Eliminar (
	in vsp_Id INT
)
BEGIN
	DELETE FROM 
		usuarios 
	WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Usuarios_Obtener (
	in vsp_Id INT
)
BEGIN
	SELECT 
		id, 
        usuario_Usuarios, 
        nombre_Usuarios, 
        id_Rol_Usuarios, 
        estado_Usuarios, 
        fecha_Usuarios
    FROM 
		usuarios 
	WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Usuarios_Bloquear (
	in vsp_Usuario_Usuarios VARCHAR(45),
	in vsp_Estado_Usuarios BOOLEAN
)
BEGIN
	UPDATE 
		usuarios 
	SET 
		estado_Usuarios = vsp_Estado_Usuarios 
    WHERE 
		usuario_Usuarios = vsp_Usuario_Usuarios;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Permisos_Agregar (
    in vsp_Id_Rol_Permisos INT,
    in vsp_Id_Paginas_Permisos INT,
    in vsp_Estado_Permisos BOOLEAN
)
BEGIN
	INSERT INTO permisos (
		id_Rol_Permisos, 
        id_Paginas_Permisos, 
        estado_Permisos
	) 
    VALUES (
		vsp_Id_Rol_Permisos, 
        vsp_Id_Paginas_Permisos, 
        vsp_Estado_Permisos
	);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Permisos_Listar ()
BEGIN
	SELECT permisos.id, rol.id, paginas.id, rol.nombre_Rol, paginas.nombre_Paginas, permisos.estado_Permisos
	FROM rol
	JOIN permisos ON rol.id = permisos.id_Rol_Permisos
	JOIN paginas ON permisos.id_Paginas_Permisos = paginas.id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Permiso_Existe (
	in vsp_Id_Rol_Permisos INT,
    in vsp_Id_Paginas_Permisos INT
)
BEGIN
	SELECT 
		id 
	FROM 
		permisos
	WHERE 
		id_Rol_Permisos = vsp_Id_Rol_Permisos AND
        id_Paginas_Permisos = vsp_Id_Paginas_Permisos;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Permisos_Editar (
	in vsp_Id INT,
	in vsp_Id_Rol_Permisos INT,
    in vsp_Id_Paginas_Permisos INT,
    in vsp_Estado_Carrusel BOOLEAN
)
BEGIN
	UPDATE 
		permisos 
	SET 
		id_Rol_Permisos = vsp_Id_Rol_Permisos,
        id_Paginas_Permisos = vsp_Id_Paginas_Permisos, 
        estado_Permisos = vsp_Estado_Carrusel 
    WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Permisos_Eliminar (
	in vsp_Id INT
)
BEGIN
	DELETE FROM 
		permisos 
	WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Permisos_EliminarXPaginas (
	in vsp_id_Paginas_Permisos INT
)
BEGIN
	DELETE FROM 
		permisos 
	WHERE 
		id_Paginas_Permisos = vsp_id_Paginas_Permisos;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Carrusel_Agregar (
	in vsp_Nombre_Carrusel VARCHAR(45),
    in vsp_Imagen_Carrusel VARCHAR(102),
    in vsp_Estado_Carrusel BOOLEAN,
    in vsp_Fecha_Carrusel DATE
)
BEGIN
	INSERT INTO carrusel (
		nombre_Carrusel, 
        imagen_Carrusel, 
        estado_Carrusel, 
		fecha_Carrusel
	) 
    VALUES (
		vsp_Nombre_Carrusel, 
        vsp_Imagen_Carrusel, 
        vsp_Estado_Carrusel, 
		vsp_Fecha_Carrusel
	);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Carrusel_Listar ()
BEGIN
	SELECT 
		id, 
        nombre_Carrusel, 
        imagen_Carrusel, 
        estado_Carrusel, 
        fecha_Carrusel 
	FROM 
		carrusel;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Carrusel_ListarXEstado ()
BEGIN
	SELECT
        imagen_Carrusel
	FROM 
		carrusel
	WHERE
		estado_Carrusel = '1';
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Carrusel_Existe (
	in vsp_Nombre_Carrusel varchar(45)
)
BEGIN
	SELECT 
		id 
	FROM 
		carrusel 
	WHERE 
		nombre_Carrusel = vsp_Nombre_Carrusel;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Carrusel_Editar (
	in vsp_Id INT,
	in vsp_Nombre_Carrusel VARCHAR(45),
    in vsp_Estado_Carrusel BOOLEAN,
    in vsp_Fecha_Carrusel DATE
)
BEGIN
	UPDATE 
		carrusel 
	SET 
		nombre_Carrusel = vsp_Nombre_Carrusel,
        estado_Carrusel = vsp_Estado_Carrusel, 
        fecha_Carrusel = vsp_Fecha_Carrusel 
    WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Carrusel_Editar_Imagen (
	in vsp_Id INT,
	in vsp_Imagen_Carrusel VARCHAR(102)
)
BEGIN
	UPDATE 
		carrusel 
	SET 
		imagen_Carrusel = vsp_Imagen_Carrusel
    WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Carrusel_Eliminar (
	in vsp_Id INT
)
BEGIN
	DELETE FROM 
		carrusel 
	WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Empleados_Agregar (
	in vsp_Nombre_Empleados VARCHAR(45),
    in vsp_Imagen_Empleados VARCHAR(102),
	in vsp_Estado_Empleados BOOLEAN,
	in vsp_Fecha_Empleados	DATE
)
BEGIN
	INSERT INTO empleados (
		nombre_Empleados, 
        imagen_Empleados, 
        estado_Empleados, 
        fecha_Empleados
	) 
    VALUES (
		vsp_Nombre_Empleados, 
        vsp_Imagen_Empleados, 
        vsp_Estado_Empleados, 
        vsp_Fecha_Empleados
	);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Empleados_Listar ()
BEGIN
	SELECT 
		id, 
        nombre_Empleados, 
        imagen_Empleados, 
        estado_Empleados, 
        fecha_Empleados 
	FROM 
		empleados;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Empleados_ListarXEstado ()
BEGIN
	SELECT 
		id,
        nombre_Empleados, 
        imagen_Empleados
	FROM 
		empleados
	WHERE
		estado_Empleados = 1;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Empleados_Existe (
	in vsp_Nombre_Empleados varchar(45)
)
BEGIN
	SELECT 
		id 
	FROM 
		empleados 
	WHERE 
		nombre_Empleados = vsp_Nombre_Empleados;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Empleados_Editar (
	in vsp_Id INT,
	in vsp_Nombre_Empleados VARCHAR(45),
	in vsp_Estado_Empleados BOOLEAN,
	in vsp_Fecha_Empleados	DATE
)
BEGIN
	UPDATE 
		empleados 
	SET 
		nombre_Empleados = vsp_Nombre_Empleados, 
		estado_Empleados = vsp_Estado_Empleados, 
        fecha_Empleados = vsp_Fecha_Empleados 
    WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Empleados_Editar_Imagen (
	in vsp_Id INT,
	in vsp_imagen_Empleados VARCHAR(102)
)
BEGIN
	UPDATE 
		empleados 
	SET 
        imagen_Empleados = vsp_imagen_Empleados
    WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Empleados_Eliminar (
	in vsp_Id INT
)
BEGIN
	DELETE FROM 
		empleados 
	WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Hardware_Agregar (
	in vsp_Id_Empleados_Hardware INT,
    in vsp_Componente_Hardware VARCHAR(102),
	in vsp_Descripcion_Hardware VARCHAR(502),
	in vsp_Marca_Hardware VARCHAR(102),
    in vsp_Modelo_Hardware VARCHAR(102),
    in vsp_Serial_Hardware VARCHAR(102),
    IN vsp_Proveedor_Hardware VARCHAR(102)
)
BEGIN
	INSERT INTO  hardware(
		id_Empleados_Hardware, 
        componente_Hardware, 
        descripcion_Hardware, 
        marca_Hardware,
        modelo_Hardware,
        serial_Hardware,
        proveedor_Hardware
	) 
    VALUES (
		vsp_Id_Empleados_Hardware,
		vsp_Componente_Hardware,
		vsp_Descripcion_Hardware,
		vsp_Marca_Hardware,
		vsp_Modelo_Hardware,
		vsp_Serial_Hardware,
        vsp_Proveedor_Hardware
	);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Hardware_Listar ()
BEGIN
	SELECT hardware.id, empleados.id, empleados.nombre_Empleados, hardware.componente_Hardware, hardware.descripcion_Hardware, 
		hardware.marca_Hardware, hardware.modelo_Hardware, hardware.serial_Hardware, hardware.proveedor_Hardware
	FROM empleados
	JOIN hardware ON empleados.id = hardware.id_Empleados_Hardware;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Hardware_ListarXId (
	in vsp_Id VARCHAR(5)
)
BEGIN
	SELECT hardware.id, empleados.id, empleados.nombre_Empleados, hardware.componente_Hardware, hardware.descripcion_Hardware, 
		hardware.marca_Hardware, hardware.modelo_Hardware, hardware.serial_Hardware, hardware.proveedor_Hardware
	FROM empleados
	JOIN hardware ON empleados.id = hardware.id_Empleados_Hardware
    WHERE empleados.id LIKE vsp_Id
    ORDER BY empleados.nombre_Empleados ASC;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Hardware_Existe (
	in vsp_Serial_Hardware varchar(102)
)
BEGIN
	SELECT 
		id 
	FROM 
		hardware 
	WHERE 
		serial_Hardware = vsp_Serial_Hardware;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Hardware_Editar (
	in vsp_Id INT,
    in vsp_Id_Empleados_Hardware INT,
    in vsp_Componente_Hardware VARCHAR(102),
	in vsp_Descripcion_Hardware VARCHAR(502),
	in vsp_Marca_Hardware VARCHAR(102),
    in vsp_Modelo_Hardware VARCHAR(102),
    in vsp_Serial_Hardware VARCHAR(102),
    IN vsp_Proveedor_Hardware VARCHAR(102)
)
BEGIN
	UPDATE 
		hardware 
	SET 
		id_Empleados_Hardware = vsp_Id_Empleados_Hardware, 
        componente_Hardware = vsp_Componente_Hardware, 
        descripcion_Hardware = vsp_Descripcion_Hardware, 
        marca_Hardware = vsp_Marca_Hardware,
        modelo_Hardware = vsp_Modelo_Hardware,
        serial_Hardware = vsp_Serial_Hardware,
        proveedor_Hardware = vsp_Proveedor_Hardware
    WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Hardware_Eliminar (
	in vsp_Id INT
)
BEGIN
	DELETE FROM 
		hardware 
	WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Noticias_Agregar (
	in vsp_Titulo_Noticias	VARCHAR(102),
	in vsp_Sub_Titulo_Noticias	VARCHAR(102),
	in vsp_Cuerpo_Noticias	VARCHAR(1000),
	in vsp_Estado_Noticias	BOOLEAN,
	in vsp_Fecha_Noticias	DATE
)
BEGIN
	INSERT INTO noticias (
		titulo_Noticias, 
		sub_Titulo_Noticias, 
        cuerpo_Noticias, 
        estado_Noticias, 
        fecha_Noticias
	) 
    VALUES (
		vsp_Titulo_Noticias, 
        vsp_Sub_Titulo_Noticias, 
        vsp_Cuerpo_Noticias, 
        vsp_Estado_Noticias, 
        vsp_Fecha_Noticias
	);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Noticias_Listar ()
BEGIN
	SELECT 
		id, 
        titulo_Noticias, 
        sub_Titulo_Noticias, 
        cuerpo_Noticias, 
        imagen_Noticias,
        estado_Noticias, 
        fecha_Noticias  
	FROM 
		noticias;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Noticias_ListarXEstado ()
BEGIN
	SELECT  
        titulo_Noticias, 
        sub_Titulo_Noticias, 
        cuerpo_Noticias, 
        imagen_Noticias,
        fecha_Noticias  
	FROM 
		noticias
	WHERE 
		estado_Noticias = 1;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Noticias_Existe (
	in vsp_Titulo_Noticias varchar(102)
)
BEGIN
	SELECT 
		id 
	FROM 
		noticias 
	WHERE 
		titulo_Noticias = vsp_Titulo_Noticias;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Noticias_Editar (
	in vsp_Id INT,
	in vsp_Titulo_Noticias	VARCHAR(102),
	in vsp_Sub_Titulo_Noticias	VARCHAR(102),
	in vsp_Cuerpo_Noticias	VARCHAR(1000),
	in vsp_Estado_Noticias	BOOLEAN,
	in vsp_Fecha_Noticias	DATE
)
BEGIN
	UPDATE 
		noticias 
	SET 
		titulo_Noticias = vsp_Titulo_Noticias, 
        sub_Titulo_Noticias = vsp_Sub_Titulo_Noticias, 
		cuerpo_Noticias = vsp_Cuerpo_Noticias, 
		estado_Noticias = vsp_Estado_Noticias, 
        fecha_Noticias = vsp_Fecha_Noticias
    WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Noticias_Editar_Imagen (
	in vsp_Id INT,
	in vsp_Imagen_Noticias	VARCHAR(102)
)
BEGIN
	UPDATE 
		noticias 
	SET 
		imagen_Noticias = vsp_Imagen_Noticias
    WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Noticias_Eliminar (
	in vsp_Id INT
)
BEGIN
	DELETE FROM noticias WHERE id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Paginas_Agregar (
	in vsp_Nombre_Paginas	VARCHAR(45),
	in vsp_Url_Paginas	VARCHAR(190),
	in vsp_Imagen_Paginas	VARCHAR(102),
	in vsp_Estado_Paginas	BOOLEAN,
	in vsp_Fecha_Paginas	DATE
)
BEGIN
	INSERT INTO paginas (
		nombre_Paginas, 
        url_Paginas, 
        imagen_Paginas, 
        estado_Paginas, 
        fecha_Paginas
	) 
    VALUES (
		vsp_Nombre_Paginas, 
        vsp_Url_Paginas, 
        vsp_Imagen_Paginas, 
        vsp_Estado_Paginas, 
        vsp_Fecha_Paginas
	);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Paginas_Listar ()
BEGIN
	SELECT 
		id, 
        nombre_Paginas, 
        url_Paginas, 
        imagen_Paginas,
        estado_Paginas, 
        fecha_Paginas 
	FROM 
		paginas;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Paginas_ListarXEstado ()
BEGIN
	SELECT 
		id, 
        nombre_Paginas
	FROM 
		paginas
	WHERE 
		estado_Paginas = 1;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Paginas_Existe (
	in vsp_Url_Paginas varchar(190)
)
BEGIN
	SELECT 
		id 
	FROM 
		paginas 
	WHERE 
		url_Paginas = vsp_Url_Paginas;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Paginas_Editar (
	in vsp_Id INT,
	in vsp_Nombre_Paginas	VARCHAR(45),
	in vsp_Url_Paginas	VARCHAR(190),
	in vsp_Estado_Paginas	BOOLEAN,
	in vsp_Fecha_Paginas	DATE
)
BEGIN
	UPDATE 
		paginas 
	SET 
		nombre_Paginas = vsp_Nombre_Paginas, 
        url_Paginas = vsp_Url_Paginas,
		estado_Paginas = vsp_Estado_Paginas, 
        fecha_Paginas = vsp_Fecha_Paginas
    WHERE id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Paginas_Editar_imagen (
	in vsp_Id INT,
	in vsp_Imagen_Paginas VARCHAR(102)
)
BEGIN
	UPDATE 
		paginas 
	SET 
		imagen_Paginas = vsp_Imagen_Paginas
    WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Paginas_Eliminar (
	in vsp_Id INT
)
BEGIN
	DELETE FROM 
		paginas 
	WHERE 
		id = vsp_Id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_Paginas_ListarXPermisos (
	in vsp_Rol_Id INT
)
BEGIN
	SELECT paginas.nombre_Paginas, paginas.url_Paginas, paginas.imagen_Paginas
	FROM rol
	JOIN permisos ON rol.id = permisos.id_Rol_Permisos
	JOIN paginas ON permisos.id_Paginas_Permisos = paginas.id
	WHERE rol.id = vsp_Rol_Id And paginas.estado_Paginas = 1;
END//
DELIMITER ;