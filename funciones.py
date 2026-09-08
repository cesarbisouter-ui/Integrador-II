from entidades import PlatoTradicional, Restaurante, Usuario
from datos import (
    lista_platos, platos_por_codigo, 
    lista_restaurantes, restaurantes_por_codigo,
    lista_usuarios, usuarios_por_codigo,
    historial_movimientos
)

# FUNCIONES DE PLATOS
def registrar_plato(codigo, nombre, dieta, precio, disponibilidad):
    if codigo in platos_por_codigo:
        return False
        
    nuevo_plato = PlatoTradicional(codigo, nombre, dieta, precio, disponibilidad)
    lista_platos.append(nuevo_plato)
    platos_por_codigo[codigo] = nuevo_plato
    
    historial_movimientos.append({
        "tipo": "REGISTRO PLATO",
        "codigo": codigo,
        "cantidad": disponibilidad
    })
    return True

def obtener_directorio_platos():
    return lista_platos

def buscar_plato_por_codigo(codigo):
    return platos_por_codigo.get(codigo)

def actualizar_disponibilidad_plato(codigo, cantidad):
    plato = platos_por_codigo.get(codigo)
    if plato == None:
        return False
    if plato.disponibilidad + cantidad < 0:
        return False
        
    plato.disponibilidad += cantidad
    
    if cantidad > 0:
        tipo = "ENTRADA PLATO"
    else:
        tipo = "SALIDA PLATO"
        
    historial_movimientos.append({
        "tipo": tipo,
        "codigo": codigo,
        "cantidad": cantidad
    })
    return True

# FUNCIONES DE RESTAURANTES
def registrar_restaurante(codigo, nombre, ubicacion, especialidad, mesas):
    if codigo in restaurantes_por_codigo:
        return False
        
    nuevo_restaurante = Restaurante(codigo, nombre, ubicacion, especialidad, mesas)
    lista_restaurantes.append(nuevo_restaurante)
    restaurantes_por_codigo[codigo] = nuevo_restaurante
    
    historial_movimientos.append({
        "tipo": "REGISTRO RESTAURANTE",
        "codigo": codigo,
        "cantidad": mesas
    })
    return True

def obtener_directorio_restaurantes():
    return lista_restaurantes

# FUNCIONES DE USUARIOS
def registrar_usuario(codigo, nombre, correo, dieta_preferida, puntos):
    if codigo in usuarios_por_codigo:
        return False
        
    nuevo_usuario = Usuario(codigo, nombre, correo, dieta_preferida, puntos)
    lista_usuarios.append(nuevo_usuario)
    usuarios_por_codigo[codigo] = nuevo_usuario
    
    historial_movimientos.append({
        "tipo": "REGISTRO USUARIO",
        "codigo": codigo,
        "cantidad": puntos
    })
    return True

def obtener_directorio_usuarios():
    return lista_usuarios

def buscar_usuario_por_codigo(codigo):
    return usuarios_por_codigo.get(codigo)

def actualizar_puntos_usuario(codigo, cantidad):
    usuario = usuarios_por_codigo.get(codigo)
    if usuario == None:
        return False
    if usuario.puntos_fidelidad + cantidad < 0:
        return False
        
    usuario.puntos_fidelidad += cantidad
    
    if cantidad > 0:
        tipo = "ASIGNACION PUNTOS"
    else:
        tipo = "CANJE PUNTOS"
        
    historial_movimientos.append({
        "tipo": tipo,
        "codigo": codigo,
        "cantidad": cantidad
    })
    return True

# HISTORIAL GENERAL
def obtener_historial():
    return historial_movimientos