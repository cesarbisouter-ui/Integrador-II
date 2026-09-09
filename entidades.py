from dataclasses import dataclass

@dataclass
class PlatoTradicional:
    codigo: str
    nombre: str
    dieta: str          # Ej: "Tradicional", "Vegetariano"
    precio: float
    disponibilidad: int = 0

@dataclass
class Restaurante:
    codigo: str
    nombre: str
    ubicacion: str      # Ej: "Managua, cerca de la universidad"
    especialidad: str
    mesas_libres: int = 0

@dataclass
class Usuario:
    codigo: str
    nombre: str
    correo: str
    dieta_preferida: str  # Para recomendar platos según su dieta
    puntos_fidelidad: int = 0

@dataclass
class Resena:
    codigo: str
    autor: str
    local_o_plato: str
    calificacion: int   # Ej: 1 al 5
    comentario: str
    likes: int = 0      # Funciona como el valor numérico actualizable

@dataclass
class Promocion:
    codigo: str
    restaurante: str
    descripcion: str
    descuento_porcentaje: float
    cupones_disponibles: int = 0 # Valor numérico actualizable  AS