from funciones import (
    registrar_plato, registrar_restaurante, registrar_usuario, registrar_resena, registrar_promocion,
    obtener_directorio_platos, obtener_directorio_restaurantes, obtener_directorio_usuarios, obtener_directorio_resenas, obtener_directorio_promociones,
    buscar_plato_por_codigo, buscar_usuario_por_codigo, buscar_resena_por_codigo, buscar_promocion_por_codigo,
    actualizar_disponibilidad_plato, actualizar_puntos_usuario, actualizar_likes_resena, actualizar_cupones_promocion,
    obtener_historial
)

while True:
    print("\n===== APP GASTRONOMÍA: NicaCrave / YumyDish / Güensebs =====")
    print("1. Registrar Plato Tradicional")
    print("2. Registrar Restaurante")
    print("3. Registrar Usuario")
    print("4. Listar Todo (Platos, Restaurantes, Usuarios, Reseñas y Promociones)")
    print("5. Buscar Plato por Código")
    print("6. Buscar Usuario por Código")
    print("7. Actualizar Disponibilidad de Plato")
    print("8. Actualizar Puntos de Usuario")
    print("9. Mostrar Historial de Movimientos")
    # --- Nuevas Opciones ---
    print("10. Registrar Reseña")
    print("11. Registrar Promoción")
    print("12. Buscar Reseña por Código")
    print("13. Buscar Promoción por Código")
    print("14. Actualizar Likes de Reseña")
    print("15. Actualizar Cupones de Promoción")
    print("16. Salir")
    opcion = input("Seleccione una opción: ").strip()
    
    if opcion == "1":
        try:
            codigo = input("Código del plato (Ej. P001): ").strip()
            nombre = input("Nombre (Ej. Vigorón): ").strip()
            dieta = input("Preferencia dietética: ").strip()
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
        resenas = obtener_directorio_resenas()
        promociones = obtener_directorio_promociones()
        
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
                
        print("\n--- RESEÑAS ---")
        if len(resenas) == 0:
            print("No hay reseñas registradas.")
        else:
            for res in resenas:
                print(f"{res.codigo} | {res.autor} opina de {res.local_o_plato}: {res.calificacion}/5 | Likes: {res.likes}")
                
        print("\n--- PROMOCIONES ---")
        if len(promociones) == 0:
            print("No hay promociones registradas.")
        else:
            for prom in promociones:
                print(f"{prom.codigo} | {prom.restaurante} | {prom.descuento_porcentaje}% descuento | Cupones: {prom.cupones_disponibles}")
                
    elif opcion == "5":
        codigo = input("Código de plato a buscar: ").strip()
        plato = buscar_plato_por_codigo(codigo)
        if plato == None:
            print("Plato no encontrado.")
        else:
            print(plato)
            
    elif opcion == "6":
        codigo = input("Código de usuario a buscar: ").strip()
        usuario = buscar_usuario_por_codigo(codigo)
        if usuario == None:
            print("Usuario no encontrado.")
        else:
            print(usuario)
            
    elif opcion == "7":
        try:
            codigo = input("Código del plato: ").strip()
            cantidad = int(input("Cantidad positiva (agregar) o negativa (restar): "))
            
            if actualizar_disponibilidad_plato(codigo, cantidad):
                print("Disponibilidad actualizada.")
            else:
                print("No fue posible actualizar la disponibilidad.")
        except ValueError:
            print("La cantidad debe ser un número entero.")
            
    elif opcion == "8":
        try:
            codigo = input("Código del usuario: ").strip()
            cantidad = int(input("Puntos a sumar (positivos) o canjear (negativos): "))
            
            if actualizar_puntos_usuario(codigo, cantidad):
                print("Puntos actualizados.")
            else:
                print("No fue posible actualizar los puntos.")
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
        try:
            codigo = input("Código de reseña (Ej. REV01): ").strip()
            autor = input("Autor de la reseña: ").strip()
            local_o_plato = input("Restaurante o Plato evaluado: ").strip()
            calificacion = int(input("Calificación (1 al 5): "))
            likes = int(input("Likes iniciales: "))
            
            if codigo == "" or autor == "" or local_o_plato == "":
                print("Los datos de texto son obligatorios.")
            elif calificacion < 1 or calificacion > 5:
                print("La calificación debe ser del 1 al 5.")
            elif likes < 0:
                print("Los likes no pueden ser negativos.")
            elif registrar_resena(codigo, autor, local_o_plato, calificacion, "", likes):
                print("Reseña registrada correctamente.")
            else:
                print("Ya existe una reseña con ese código.")
        except ValueError:
            print("Calificación o likes no válidos.")
            
    elif opcion == "11":
        try:
            codigo = input("Código de promoción (Ej. PROM01): ").strip()
            restaurante = input("Restaurante que ofrece la promoción: ").strip()
            descripcion = input("Descripción de la oferta: ").strip()
            descuento = float(input("Porcentaje de descuento (Ej. 15.5): "))
            cupones = int(input("Cupones disponibles iniciales: "))
            
            if codigo == "" or restaurante == "" or descripcion == "":
                print("Los datos de texto son obligatorios.")
            elif descuento <= 0 or cupones < 0:
                print("El descuento debe ser mayor a 0 y los cupones no pueden ser negativos.")
            elif registrar_promocion(codigo, restaurante, descripcion, descuento, cupones):
                print("Promoción registrada correctamente.")
            else:
                print("Ya existe una promoción con ese código.")
        except ValueError:
            print("Descuento o cupones no válidos.")
            
    elif opcion == "12":
        codigo = input("Código de reseña a buscar: ").strip()
        resena = buscar_resena_por_codigo(codigo)
        if resena == None:
            print("Reseña no encontrada.")
        else:
            print(resena)
            
    elif opcion == "13":
        codigo = input("Código de promoción a buscar: ").strip()
        promocion = buscar_promocion_por_codigo(codigo)
        if promocion == None:
            print("Promoción no encontrada.")
        else:
            print(promocion)
            
    elif opcion == "14":
        try:
            codigo = input("Código de la reseña: ").strip()
            cantidad = int(input("Likes a sumar (positivos) o quitar (negativos): "))
            
            if actualizar_likes_resena(codigo, cantidad):
                print("Likes actualizados.")
            else:
                print("No fue posible actualizar los likes.")
        except ValueError:
            print("La cantidad debe ser un número entero.")
            
    elif opcion == "15":
        try:
            codigo = input("Código de la promoción: ").strip()
            cantidad = int(input("Cupones a sumar (positivos) o canjear (negativos): "))
            
            if actualizar_cupones_promocion(codigo, cantidad):
                print("Cupones actualizados.")
            else:
                print("No fue posible actualizar los cupones.")
        except ValueError:
            print("La cantidad debe ser un número entero.")

    elif opcion == "16":
        print("Programa finalizado.")
        break
        
    else:
        print("Seleccione una opción válida.")