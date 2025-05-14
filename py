from datetime import date
from typing import List

class Libro:
    def _init_(self, titulo, autor, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        self.disponible = True

class Prestamo:
    def _init_(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fechaInicio = date.today()
        self.fechaFin = None
        self.estado = "activo"

    def finalizarPrestamo(self):
        self.fechaFin = date.today()
        self.estado = "finalizado"
        self.libro.devolver()

class Usuario:
    def _init_(self, nombre, idUsuario):
        self.nombre = nombre
        self.idUsuario = idUsuario
        self.prestamos: List[Prestamo] = []

    def solicitarPrestamo(self, libro):
        if libro.prestar():
            prestamo = Prestamo(libro, self)
            self.prestamos.append(prestamo)
            return prestamo
        return None

    def devolverLibro(self, prestamo):
        prestamo.finalizarPrestamo()

class Bibliotecario:
    def _init_(self, nombre, idEmpleado):
        self.nombre = nombre
        self.idEmpleado = idEmpleado

    def registrarUsuario(self, biblioteca, usuario):
        biblioteca.usuarios.append(usuario)

    def añadirLibro(self, biblioteca, libro):
        biblioteca.libros.append(libro)

class Biblioteca:
    def _init_(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.libros: List[Libro] = []
        self.usuarios: List[Usuario] = []
        self.bibliotecarios: List[Bibliotecario] = []

    def buscarLibro(self, titulo):
        return [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]

    def listarUsuarios(self):
        return self.usuarios
