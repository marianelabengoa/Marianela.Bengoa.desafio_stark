
from data_stark import *
from funciones import *
import os

flag_0=False

while True:
    os.system("cls")

    print("""    MENU DE OPCIONES   """)
    print("0. Normalizar datos")
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
        stark_normalizar_datos(lista_personajes, "altura", float)
        stark_normalizar_datos(lista_personajes, "peso", float)
        stark_normalizar_datos(lista_personajes, "fuerza", int)
        flag_0=True
    elif opcion == 1:
            mostrar_nombres(lista_personajes)
    elif opcion == 2:
        if flag_0==True:
            mostrar_nombres_altura(lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 3:
        if flag_0==True:
            mostrar_altura_mas_alta(lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 4:
        if flag_0==True:
            mostrar_altura_mas_baja(lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 5:
        if flag_0==True:
            mostrar_promedio(lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 6:
        if flag_0==True:
            mostrar_nombre_del_mayor_y_menor(lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 7:
        if flag_0==True:
            mostrar_mas_pesado_y_liviano(lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 8:
        mostrar_masculinos(lista_personajes)
    elif opcion == 9:
        mostrar_femeninos(lista_personajes)
    elif opcion == 10:
        if flag_0==True:
            mostrar_masculino_mas_alto(lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 11:
        if flag_0==True:
            mostrar_femenino_mas_alto(lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 12:
        if flag_0==True:
            mostrar_masculino_mas_bajo(lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 13:
        if flag_0==True:
            mostrar_femenino_mas_bajo(lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 14:
        if flag_0==True:
            promedio_alturas_masc(lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 15:
        if flag_0==True:
            promedio_alturas_fem(lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 16:
        if flag_0==True:
            nombres_masculino_mas_alto_y_bajo(lista_personajes)
            nombres_femenino_mas_alto_y_bajo(lista_personajes)
        else:
            print("Primero normaliza datos (opcion 0)")
    elif opcion == 17:
        cantidad_por_valor(lista_personajes, "color_ojos")
    elif opcion == 18:
        cantidad_por_valor(lista_personajes, "color_pelo")
    elif opcion == 19:
        inteligencia(lista_personajes, "inteligencia")
    elif opcion == 20:
        mostrar_nombre_valor(lista_personajes, "color_ojos", "color de ojos")
    elif opcion == 21:
        mostrar_nombre_valor(lista_personajes, "color_pelo", "color de pelo")
    elif opcion == 22:
        mostrar_nombre_valor(
            lista_personajes, "inteligencia", "tipo de inteligencia")
    elif opcion == 23:
        break

    os.system("pause")
