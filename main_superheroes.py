# Desafío #00:
# A. Analizar detenidamente el set de datos
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
# la altura del mismo
# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# F. Recorrer la lista y determinar la altura promedio de los superhéroes
# (PROMEDIO)
# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (MÁXIMO, MÍNIMO)
# H. Calcular e informar cual es el superhéroe más y menos pesado.
# I. Ordenar el código implementando una función para cada uno de los valores
# informados.
# J. Construir un menú que permita elegir qué dato obtener

# 0111111111111111111111
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# G. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género M
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género F
# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (ítems C a F)
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).
# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia

from data_stark import *
from funciones import *
import os


while True:
    os.system("cls")

    print("""    MENU DE OPCIONES   """)
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
    elif opcion == 1:
        mostrar_nombres(lista_personajes)
    elif opcion == 2:
        mostrar_nombres_altura(lista_personajes)
    elif opcion == 3:
        mostrar_altura_mas_alta(lista_personajes)
    elif opcion == 4:
        mostrar_altura_mas_baja(lista_personajes)

    elif opcion == 5:
        mostrar_promedio(lista_personajes)

    elif opcion == 6:
        mostrar_nombre_del_mayor_y_menor(lista_personajes)

    elif opcion == 7:
        mostrar_mas_pesado_y_liviano(lista_personajes)
    elif opcion == 8:
        mostrar_masculinos(lista_personajes)
    elif opcion == 9:
        mostrar_femeninos(lista_personajes)
    elif opcion == 10:
        mostrar_masculino_mas_alto(lista_personajes)
    elif opcion == 11:
        mostrar_femenino_mas_alto(lista_personajes)
    elif opcion == 12:
        mostrar_masculino_mas_bajo(lista_personajes)
    elif opcion == 13:
        mostrar_femenino_mas_bajo(lista_personajes)
    elif opcion == 14:
        promedio_alturas_masc(lista_personajes)
    elif opcion == 15:
        promedio_alturas_fem(lista_personajes)

    elif opcion == 16:
        nombres_masculino_mas_alto_y_bajo(lista_personajes)
        nombres_femenino_mas_alto_y_bajo(lista_personajes)

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
        mostrar_nombre_valor(lista_personajes, "inteligencia", "tipo de inteligencia")

    elif opcion == 23:
        break

    os.system("pause")
