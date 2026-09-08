from funciones import (
    registrar_plato, registrar_restaurante, registrar_usuario,
    obtener_directorio_platos, obtener_directorio_restaurantes, obtener_directorio_usuarios,
    buscar_plato_por_codigo, buscar_usuario_por_codigo,
    actualizar_disponibilidad_plato, actualizar_puntos_usuario,
    obtener_historial
)

while True:
    print("\n===== APP GASTRONOMÍA: NicaCrave / YumyDish / Güensebs =====")
    print("1. Registrar Plato Tradicional")
    print("2. Registrar Restaurante")
    print("3. Registrar Usuario")
    print("4. Listar Todo (Platos, Restaurantes y Usuarios)")
    print("5. Buscar Plato por Código")
    print("6. Buscar Usuario por Código")
    print("7. Actualizar Disponibilidad de Plato")
    print("8. Actualizar Puntos de Usuario")
    print("9. Mostrar Historial de Movimientos")
    print("10. Salir")
    opcion = input("Seleccione una opción: ").strip()
    
    if opcion == "1":
        try:
            codigo = input("Código del plato (Ej. P001): ").strip().lower()
            nombre = input("Nombre (Ej. Vigorón): ").strip().lower()
            dieta = input("Preferencia dietética: ").strip().lower()
            precio = float(input("Precio promedio: "))
            disponibilidad = int(input("Disponibilidad inicial: "))
            
            if codigo == "" or nombre == "" or dieta == "":
                print("Los datos de texto son obligatorios.")
            elif precio < 0 or disponibilidad < 0:
                print("El precio y disponibilidad no pueden ser negativos.")
            elif registrar_plato(codigo, nombre, dieta, precio, disponibilidad):
                print("Plato registrado correctamente.")
            else:
                print("Ya existe un plato con ese código.")
        except ValueError:
            print("Precio o disponibilidad no válidos.")
            
    elif opcion == "2":
        try:
            codigo = input("Código del restaurante (Ej. R001): ").strip()
            nombre = input("Nombre del local: ").strip()
            ubicacion = input("Ubicación exacta: ").strip()
            especialidad = input("Especialidad (Ej. Asados): ").strip()
            mesas = int(input("Mesas libres iniciales: "))
            
            if codigo == "" or nombre == "" or ubicacion == "":
                print("Los datos de texto son obligatorios.")
            elif mesas < 0:
                print("Las mesas libres no pueden ser negativas.")
            elif registrar_restaurante(codigo, nombre, ubicacion, especialidad, mesas):
                print("Restaurante registrado correctamente.")
            else:
                print("Ya existe un restaurante con ese código.")
        except ValueError:
            print("El número de mesas no es válido.")
            
    elif opcion == "3":
        try:
            codigo = input("Código de usuario (Ej. U001): ").strip()
            nombre = input("Nombre del usuario: ").strip()
            correo = input("Correo electrónico: ").strip()
            dieta = input("Dieta preferida (Ej. Tradicional): ").strip()
            puntos = int(input("Puntos de fidelidad iniciales: "))
            
            if codigo == "" or nombre == "" or correo == "":
                print("Los datos de texto son obligatorios.")
            elif puntos < 0:
                print("Los puntos no pueden ser negativos.")
            elif registrar_usuario(codigo, nombre, correo, dieta, puntos):
                print("Usuario registrado correctamente.")
            else:
                print("Ya existe un usuario con ese código.")
        except ValueError:
            print("El valor de puntos no es válido.")
            
    elif opcion == "4":
        platos = obtener_directorio_platos()
        restaurantes = obtener_directorio_restaurantes()
        usuarios = obtener_directorio_usuarios()
        
        print("\n--- PLATOS TRADICIONALES ---")
        if len(platos) == 0:
            print("No hay platos registrados.")
        else:
            for p in platos:
                print(f"{p.codigo} | {p.nombre} | {p.dieta} | C${p.precio} | Disp: {p.disponibilidad}")
                
        print("\n--- RESTAURANTES CERCANOS ---")
        if len(restaurantes) == 0:
            print("No hay restaurantes registrados.")
        else:
            for r in restaurantes:
                print(f"{r.codigo} | {r.nombre} | {r.ubicacion} | Mesas: {r.mesas_libres}")
                
        print("\n--- USUARIOS REGISTRADOS ---")
        if len(usuarios) == 0:
            print("No hay usuarios registrados.")
        else:
            for u in usuarios:
                print(f"{u.codigo} | {u.nombre} | {u.correo} | Dieta: {u.dieta_preferida} | Pts: {u.puntos_fidelidad}")
                
    elif opcion == "5":
        codigo = input("Código de plato a buscar: ").strip().lower()
        plato = buscar_plato_por_codigo(codigo)
        if plato == None:
            print("Plato no encontrado.")
        else:
            print(plato)
            
    elif opcion == "6":
        codigo = input("Código de usuario a buscar: ").strip().lower()
        usuario = buscar_usuario_por_codigo(codigo)
        if usuario == None:
            print("Usuario no encontrado.")
        else:
            print(usuario)
            
    elif opcion == "7":
        try:
            codigo = input("Código del plato: ").strip().lower()
            cantidad = int(input("Cantidad positiva (agregar) o negativa (restar): "))
            
            if actualizar_disponibilidad_plato(codigo, cantidad):
                print("Disponibilidad actualizada.")
            else:
                print("No fue posible actualizar la disponibilidad.")
        except ValueError:
            print("La cantidad debe ser un número entero.")
            
    elif opcion == "8":
        try:
            codigo = input("Código del usuario: ").strip().lower()
            cantidad = int(input("Puntos a sumar (positivos) o canjear (negativos): "))
            
            if actualizar_puntos_usuario(codigo, cantidad):
                print("Puntos actualizados.")
            else:
                print("No fue posible actualizar los puntos (fidelidad insuficiente o usuario no existe).")
        except ValueError:
            print("La cantidad debe ser un número entero.")
            
    elif opcion == "9":
        historial = obtener_historial()
        if len(historial) == 0:
             print("No hay movimientos registrados.")
        else:
             for movimiento in historial:
                 print(movimiento)
            
    elif opcion == "10":
        print("Programa finalizado.")
        break
        
    else:
        print("Seleccione una opción válida.")