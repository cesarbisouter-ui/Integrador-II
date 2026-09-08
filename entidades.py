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