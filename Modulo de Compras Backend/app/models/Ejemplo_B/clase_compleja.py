from app.bdd import db
from .enums import Dias_Semana
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import relationship

class Cliente(db.Model): #Todo OK segun BD
    __tablename__ = "cliente"

    id_cliente = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.Integer, nullable=False) 
    telefono = db.Column(db.String(12), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    contraseña = db.Column(db.String(128), nullable=False)
    sexo = db.Column(db.Enum("M", "F", name="sexo"), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    #Relacion Lazy que permite recuperar los puntos de un cliente de forma simple
    puntos = db.relationship('PuntosCliente', lazy = True)
    
    def __init__(self, dni, telefono, nombre, apellido, sexo, fecha_nacimiento,contraseña):
        self.dni = dni
        self.telefono = telefono
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento  # Como es un sistema medico necesita la edad
        self.set_password(contraseña) 

    def set_password(self, password):
        from app import bcrypt
        """Hash the password."""    
        self.contraseña = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        from app import bcrypt
        """Check hashed password."""
        return bcrypt.check_password_hash(self.contraseña, password)

