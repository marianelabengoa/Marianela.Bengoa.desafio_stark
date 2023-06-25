
from data_stark import *
from funciones import *
import os

flag_01 = False
flag_02 = False

while True:
    os.system("cls")

    print("""    MENU DE OPCIONES   """)
    print("0. Cargar lista y normalizar datos")
    print("1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe")
    print("2. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo")
    print("3. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)")
    print("4. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)")
    print("5. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)")
    print("6. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)")
    print("7. Calcular e informar cual es el superhéroe más y menos pesado.")
    print("8. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M")
    print("9. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F")
    print("10. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    print("11. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    print("12. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M")
    print("13. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F")
    print("14. Recorrer la lista y determinar la altura promedio de los superhéroes de género M")
    print("15. Recorrer la lista y determinar la altura promedio de los superhéroes de género F")
    print("16. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)")
    print("17. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("18. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("19. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).")
    print("20. Listar todos los superhéroes agrupados por color de ojos.")
    print("21. Listar todos los superhéroes agrupados por color de pelo.")
    print("22. Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("23. Salir")

    opcion = int(input("ingrese opcion "))
    print("""  """)

    if opcion == 0:

        opcion2 = print("""Bienvenido, elija alguna de las siguientes opciones antes de avanzar:
        1- cargar datos
        2-normalizar datos
        """)
        opcion2 = int(input("ingrese opcion:"))

        if opcion2 == 1:
            nueva_lista_personajes = []
            print(nueva_lista(lista_personajes, nueva_lista_personajes))
            flag_01 = True

        if opcion2 == 2:
            if flag_01 == True:
                stark_normalizar_datos(nueva_lista_personajes, "altura", float)
                stark_normalizar_datos(nueva_lista_personajes, "peso", float)
                stark_normalizar_datos(nueva_lista_personajes, "fuerza", int)
                print("Datos normalizados.")
                flag_02 = True
            else:
                print("Lista de heroes vacia.")

    elif opcion == 1:
        if flag_01 == True:
            mostrar_nombres(nueva_lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 2:
        if flag_02 == True:
            mostrar_nombres_altura(nueva_lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 3:
        if flag_02 == True:
            mostrar_altura_mas_alta(nueva_lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0).")
    elif opcion == 4:
        if flag_02 == True:
            mostrar_altura_mas_baja(nueva_lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 5:
        if flag_02 == True:
            mostrar_promedio(nueva_lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 6:
        if flag_02 == True:
            mostrar_nombre_del_mayor_y_menor(nueva_lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 7:
        if flag_02 == True:
            mostrar_mas_pesado_y_liviano(nueva_lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 8:
        mostrar_masculinos(nueva_lista_personajes)
    elif opcion == 9:
        mostrar_femeninos(nueva_lista_personajes)
    elif opcion == 10:
        if flag_02 == True:
            mostrar_masculino_mas_alto(nueva_lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 11:
        if flag_02 == True:
            mostrar_femenino_mas_alto(nueva_lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 12:
        if flag_02 == True:
            mostrar_masculino_mas_bajo(nueva_lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 13:
        if flag_02 == True:
            mostrar_femenino_mas_bajo(nueva_lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 14:
        if flag_02 == True:
            promedio_alturas_masc(nueva_lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 15:
        if flag_02 == True:
            promedio_alturas_fem(nueva_lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 16:
        if flag_02 == True:
            nombres_masculino_mas_alto_y_bajo(nueva_lista_personajes)
            nombres_femenino_mas_alto_y_bajo(nueva_lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 17:
        if flag_01 == True:
            cantidad_por_valor(nueva_lista_personajes, "color_ojos")
        else:
            print("Primero carga la lista (opcion 0)")
    elif opcion == 18:
        if flag_01 == True:
            cantidad_por_valor(nueva_lista_personajes, "color_pelo")
        else:
            print("Primero carga la lista (opcion 0)")
    elif opcion == 19:
        if flag_01 == True:
            inteligencia(nueva_lista_personajes, "inteligencia")
        else:
            print("Primero carga la lista (opcion 0)")
    elif opcion == 20:
        if flag_01 == True:
            mostrar_nombre_valor(nueva_lista_personajes,
                                 "color_ojos", "color de ojos")
        else:
            print("Primero carga la lista (opcion 0)")
    elif opcion == 21:
        if flag_01 == True:
            mostrar_nombre_valor(nueva_lista_personajes,
                                 "color_pelo", "color de pelo")
        else:
            print("Primero carga la lista (opcion 0)")
    elif opcion == 22:
        if flag_01 == True:
            mostrar_nombre_valor(nueva_lista_personajes,
                                 "inteligencia", "tipo de inteligencia")
        else:
            print("Primero carga la lista (opcion 0)")
    elif opcion == 23:
        break

    os.system("pause")
