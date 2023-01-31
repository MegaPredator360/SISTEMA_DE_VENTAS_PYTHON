
USE BIBLIOTECA_VENTAS;

CREATE TABLE CLIENTES(
CEDULA_CLIENTE INT,
NOMBRE_CLIENTE VARCHAR (100),
TELEFONO_CLIENTE INT,
CORREO_CLIENTE VARCHAR(100),
DIRECCION_CLIENTE VARCHAR(100),
CONSTRAINT PK_CLIENTES PRIMARY KEY (CEDULA_CLIENTE)
)

DROP TABLE CLIENTES;

CREATE TABLE EMPLEADOS(
ID_EMPLEADO INT,
CEDULA_EMPLEADO INT,
NOMBRE_EMPLEADO VARCHAR(100),
TELEFONO_EMPLEADO VARCHAR(100),
CORREO_EMPLEADO VARCHAR(100),
DIRECCION_EMPLEADO VARCHAR(100),
CONSTRAINT PK_EMPLEADOS PRIMARY KEY (ID_EMPLEADO)
)

DROP TABLE EMPLEADOS;

CREATE TABLE GENERO(
ID_GENERO INT,
NOMBRE_GENERO VARCHAR(100)
CONSTRAINT PK_GENERO PRIMARY KEY (ID_GENERO)
)

DROP TABLE GENERO;

CREATE TABLE LIBROS(
ID_LIBRO INT,
NOMBRE_LIBRO VARCHAR(100),
ID_AUTOR INT,
ID_EDITORIAL INT,
ID_GENERO INT,
NUMERO_PAGINAS INT,                  --ULTIMA TABLA POR CORRER--
FECHA_LANZAMIENTO DATE,
CANTIDAD INT,
PRECIO_VENTA INT, 
PRECIO_RENTA INT,
CONSTRAINT PK_LIBRO PRIMARY KEY (ID_LIBRO),
CONSTRAINT FK_AUTOR FOREIGN KEY (ID_AUTOR) REFERENCES AUTOR(ID_AUTOR),
CONSTRAINT FK_EDITORIAL FOREIGN KEY (ID_EDITORIAL) REFERENCES EDITORIALES(ID_EDITORIAL),
CONSTRAINT FK_GENERO FOREIGN KEY (ID_GENERO) REFERENCES GENERO(ID_GENERO)
)

DROP TABLE LIBROS

CREATE TABLE EDITORIALES(
ID_EDITORIAL INT,
NOMBRE_EDITORIAL VARCHAR(100),
PAIS_EDITORIAL VARCHAR(100),
CORREO_EDITORIAL VARCHAR(100),
DIRECCION_EDITORIAL VARCHAR(100),
TELEFONO_EDITORIAL INT
CONSTRAINT PK_EDITORIAL PRIMARY KEY (ID_EDITORIAL)
)


CREATE TABLE AUTOR (
ID_AUTOR INT,
NOMBRE_AUTOR VARCHAR(100),
APELLIDO_AUTOR VARCHAR(100),
PAIS_AUTOR VARCHAR(100),
CONSTRAINT PK_AUTOR PRIMARY KEY (ID_AUTOR)
)

CREATE TABLE FACTURA(
ID_FACTURA INT,
CEDULA_CLIENTE INT,
ID_EMPLEADO INT,
FECHA_FACTURA DATE,
DESCUENTO INT,
TOTAL_FACTURA INT,
METODO_PAGO VARCHAR(50),
PAGO INT,
VUELTO INT,
CONSTRAINT PK_FACTURA PRIMARY KEY (ID_FACTURA),
CONSTRAINT FK_CLIENTE FOREIGN KEY (CEDULA_CLIENTE) REFERENCES [dbo].[CLIENTES](CEDULA_CLIENTE),
CONSTRAINT FK_EMPLEADO FOREIGN KEY (ID_EMPLEADO) REFERENCES EMPLEADOS(ID_EMPLEADO)
)


CREATE TABLE DETALLE_FACTURAS(
ID_DETALLE_FACTURA INT,
ID_FACTURA INT,
ID_LIBRO INT,
ID_TIPO_SERVICIO INT,    --no corrido--
CANTIDAD_LIBROS INT,
CANTIDAD_DIAS_PRESTAMO INT,
PRECIO INT,
CONSTRAINT PK_DETALLE_FACTURA PRIMARY KEY (ID_DETALLE_FACTURA),
CONSTRAINT FK_FACTURA FOREIGN KEY (ID_FACTURA) REFERENCES FACTURA(ID_FACTURA),
CONSTRAINT FK_LIBRO FOREIGN KEY (ID_LIBRO) REFERENCES LIBROS(ID_LIBRO),
CONSTRAINT FK_TIPO_SERVICIO FOREIGN KEY (ID_TIPO_SERVICIO) REFERENCES TIPOS_SERVICIOS(ID_TIPO_SERVICIO)
)

CREATE TABLE TIPOS_SERVICIOS(
ID_TIPO_SERVICIO INT,
NOMBRE_SERVICIO VARCHAR(5)
CONSTRAINT PK_TIPO_SERVICIO PRIMARY KEY (ID_TIPO_SERVICIO)
)


SELECT @@SERVERNAME