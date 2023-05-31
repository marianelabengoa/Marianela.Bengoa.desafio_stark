from data_stark import *

# 12/6 PRESENCIAL PROGRAMACION
# 146 PRESENCIAL LABORATORIO
# 16/6 PRESENCIAL SPD


def mostrar_heroe_fila(heroe: dict) -> None:
    print(f"nombre: {heroe['nombre']:10s}  id: {heroe['identidad']:10}  empresa: {heroe['empresa']:8} altura: {heroe['altura']} peso: {heroe['peso']} genero: {heroe['genero']} color de ojos: {heroe['color_ojos']:10}  color de pelo: {heroe['color_pelo']:10} fuerza: {heroe['fuerza']:10} inteligencia:  {heroe['inteligencia']:10}")


def listar_heroe(lista: list) -> None:
    print("***lista heroes***")
    for heroe in lista:
        mostrar_heroe_fila(heroe)


def esta_en_lista(lista: list, item: str) -> bool:
    esta = False
    for elemento in lista:
        if (elemento == item):
            esta = True
            break
    return esta


def quitar_repetidos(lista: list) -> list:
    lista_sin_repe = []
    for item in lista:
        if (not esta_en_lista(lista_sin_repe, item)):
            lista_sin_repe.append(item)
    return lista_sin_repe


def proyectar_heroe(lista: list, key: str) -> list:
    lista_filtrada = []
    for heroe in lista:
        lista_filtrada.append(heroe[key])
    return lista_filtrada


def mostrar_lista(lista: list, title: str) -> None:
    print(f"{title}")
    for item in lista:
        print(item)


def mostrar_heroe(nombre: str, title: str) -> None:
    print(f"{title}")
    print(nombre)


def stark_normalizar_datos(lista: list, primera_key: str, funcion: str) -> None:
    for personaje in lista:
        personaje[primera_key] = float(personaje[primera_key])


def filtrar_heroes(lista: list, key: str, valor: str) -> list:
    lista_filtrada = []
    for heroe in lista:
        if (heroe[key] == valor):
            lista_filtrada.append(heroe)
    return lista_filtrada


def filtrar_heroe_dos(lista: list, key: str, otra: str, valor: str) -> list:
    lista_filtrada = []
    for heroe in lista:
        if (heroe[key] == valor):
            lista_filtrada.append(heroe)
    return lista_filtrada


# l=listar_heroe(lista_personajes)
# listar_heroe(l)

# l = filtrar_heroes(lista_personajes, "nombre", "M")
# nombres_masc=proyectar_heroe(lista_personajes, "nombre")
# mostrar_lista(nombres_masc,"Masculinos de ojos marrones")

def dos_elementos(lista: list, primer_valor: str, segundo_valor: int, titulo: str) -> None:
    lista_filtro = []
    for i in range(0, len(lista), 2):
        lista_filtro.append((lista[primer_valor], lista[int(segundo_valor)]))
        primer_valor = lista[i]
        segundo_valor = lista[i + 1]
        print(f"{primer_valor} - {segundo_valor}")


def proyectar_heroe_dos_elementos(lista: list, key: str, key2: str) -> list:
    lista_filtrada = []
    for heroe in lista:
        lista_filtrada.extend([heroe[key], heroe[key2]])
    return lista_filtrada


def mostrar_lista_dos_elementos(lista: list, title: str) -> None:
    print(f"{title}")
    for i in range(0, len(lista), 2):
        primer_valor = lista[i]
        segundo_valor = lista[i+1]
        print(f"{primer_valor} - {segundo_valor}")


def calcular_mayor(lista: list, primer_key: str, segunda_key: str) -> float:
    flag = False
    for personaje in lista:
        if (flag == False):
            personaje_mayor = personaje[primer_key]
            nom_personaje_mayor = personaje[segunda_key]
            flag = True

        elif (personaje[primer_key] > personaje_mayor):
            personaje_mayor = personaje[primer_key]
            nom_personaje_mayor = personaje[segunda_key]
    return personaje_mayor, nom_personaje_mayor


def calcular_menor(lista: list, primer_key: str, segunda_key: str) -> str:
    flag_altura = False
    for personaje in lista:
        if (flag_altura == False):
            personaje_menor = personaje[primer_key]
            nom_personaje_menor = personaje[segunda_key]
            flag_altura = True

        elif (personaje[primer_key] < personaje_menor):
            personaje_menor = personaje[primer_key]
            nom_personaje_menor = personaje[segunda_key]
    return personaje_menor, nom_personaje_menor

# def calcular_mayor(lista: list, primer_key: str, segunda_key: str) -> str:
#     flag_altura = False
#     for personaje in lista:
#         if (flag_altura == False):
#             personaje_menor = personaje[primer_key]
#             nom_personaje_menor = personaje[segunda_key]
#             flag_altura = True

#         elif (personaje[primer_key] > personaje_menor):
#             personaje_menor = personaje[primer_key]
#             nom_personaje_menor = personaje[segunda_key]
#     return personaje_menor, nom_personaje_menor


def calcular_promedio(lista: list, key: str) -> float:
    cont = 0
    acumulador = 0
    for personaje in lista:

        acumulador += personaje[key]
        cont += 1

    promedio = acumulador/cont
    return promedio


def buscar_nombre_mas_alto_y_bajo(lista: list, primer_key: str, segunda_key: str) -> str:
    flag_altura = False
    for personaje in lista:
        if (flag_altura == False):
            personaje_mas_alto = personaje[primer_key]
            personaje_mas_bajo = personaje[primer_key]
            nom_personaje_mas_alto = personaje[segunda_key]
            nom_personaje_mas_bajo = personaje[segunda_key]
            flag_altura = True

        elif (personaje[primer_key] > personaje_mas_alto):
            personaje_mas_alto = personaje[primer_key]
            nom_personaje_mas_alto = personaje[segunda_key]
        elif (personaje[primer_key] < personaje_mas_bajo):
            personaje_mas_bajo = personaje[primer_key]
            nom_personaje_mas_bajo = personaje[segunda_key]

    return nom_personaje_mas_alto, nom_personaje_mas_bajo


def calcular_mayor_y_su_nombre(lista: list, primer_key: str, segunda_key: str):
    flag_peso = False
    for personaje in lista:
        if (flag_peso == False):
            personaje_mas_pesado = personaje[primer_key]
            nom_personaje_mas_pesado = personaje[segunda_key]
            flag_peso = True

        elif (personaje[primer_key] > personaje_mas_pesado):
            personaje_mas_pesado = personaje[primer_key]
            nom_personaje_mas_pesado = personaje[segunda_key]

    return nom_personaje_mas_pesado, personaje_mas_pesado


def calcular_menor_y_su_nombre(lista: list, primer_key: str, segunda_key: str) -> int:
    flag_peso = False
    for personaje in lista:
        if (flag_peso == False):
            personaje_mas_liviano = personaje[primer_key]
            nom_personaje_mas_liviano = personaje[segunda_key]
            flag_peso = True
        elif (personaje[primer_key] < personaje_mas_liviano):
            personaje_mas_liviano = personaje[primer_key]
            nom_personaje_mas_liviano = personaje[segunda_key]

    return nom_personaje_mas_liviano, personaje_mas_liviano


def mostrar_mas_alto_M(lista: list, primera_key: str, valor: str, segunda_key: str, tercera_key: str) -> str:
    flag_altura = False
    for personaje in lista:
        if (flag_altura == False and personaje[primera_key] == valor):
            personaje_mas_alto_M = personaje[segunda_key]
            nom_personaje_mas_alto_m = personaje[tercera_key]
            flag_altura = True

        elif (personaje[primera_key] == valor and personaje[segunda_key] > personaje_mas_alto_M):
            personaje_mas_alto_M = personaje[segunda_key]
            nom_personaje_mas_alto_m = personaje[tercera_key]
    return personaje_mas_alto_M


def set_colores(lista: list, valor):
    colores = set()
    for elemento in lista:
        colores.add(elemento[valor])

    return colores


def cantidad_personajes(lista, set, valor):
    color_y_nombre = {}
    cantidad_personajes = 0
    for color in set:
        for personaje in lista:
            if (color == personaje[valor]):
                cantidad_personajes += 1
                color_y_nombre[color] = cantidad_personajes
    print(color_y_nombre)


def nombre_por_color(lista: list, set: set, valor: str, titulo: str):
    titulo.upper
    for color in set:
        print(f"-------------------------\n{titulo} : {color}")
        for personaje in lista:
            if (color == personaje[valor]):
                print(f"{personaje['nombre']}")


def superheroes_inteligencia(lista, set):
    inteligencia = {}
    cantidad_personajes = 0
    for tipo_inteligencia in set:
        for personaje in lista:
            if (tipo_inteligencia == personaje["inteligencia"]):
                cantidad_personajes += 1
                inteligencia[tipo_inteligencia] = cantidad_personajes
            elif (tipo_inteligencia == ""):
                inteligencia[tipo_inteligencia] = "No tiene"
    print(inteligencia)

#              opcion 1                 #
def mostrar_nombres(lista):
    nombres = proyectar_heroe(lista, "nombre")
    mostrar_lista(nombres, "nombres")
    # listar_heroe(lista)


#              opcion 2                 #
def mostrar_nombres_altura(lista):
    altura = proyectar_heroe_dos_elementos(lista, "nombre", "altura")
    mostrar_lista_dos_elementos(altura, "PERSONAJES Y SUS ALTURAS")


#              opcion 3                 #
def mostrar_altura_mas_alta(lista):
    altura_mayor = calcular_mayor(lista, "altura", "nombre")
    mostrar_heroe(altura_mayor, "ALTURA DEL MAS ALTO")


#              opcion 4                 #
def mostrar_altura_mas_baja(lista):
    altura_menor = calcular_menor(lista, "altura", "nombre")
    mostrar_heroe(altura_menor, "ALTURA DEL MAS BAJO")


#              opcion 5                 #
def mostrar_promedio(lista):
    promedio = calcular_promedio(lista, "altura")
    mostrar_heroe(promedio, "PROMEDIO ALTURAS")


#              opcion 6                 #
def mostrar_nombre_del_mayor_y_menor(lista):
    nombres_max_min = buscar_nombre_mas_alto_y_bajo(lista, "altura", "nombre")
    mostrar_heroe(nombres_max_min, "PERSONAJE MAYOR, PERSONAJE MENOR")

#              opcion 7                 #
def mostrar_mas_pesado_y_liviano(lista):
    mas_pesado = calcular_mayor_y_su_nombre(lista, "peso", "nombre")
    mas_liviano = calcular_menor_y_su_nombre(lista, "peso", "nombre")
    mostrar_heroe(mas_pesado, "PERSONAJEMAS PESADO Y SU PESO")
    mostrar_heroe(mas_liviano, "PERSONAJE MAS LIVIANO Y SU PESO")


#              opcion 8                 #
def mostrar_masculinos(lista):
    l = filtrar_heroes(lista, "genero", "M")
    nombres_masc = proyectar_heroe(l, "nombre")
    mostrar_lista(nombres_masc, "PERSONAJES MASCULINOS")


#              opcion 9                 #
def mostrar_femeninos(lista):
    li = filtrar_heroes(lista, "genero", "F")
    nombres_fem = proyectar_heroe(li, "nombre")
    mostrar_lista(nombres_fem, "PERSONAJES FEMENINOS")


#              opcion 10                 #
def mostrar_masculino_mas_alto(lista):
    l = filtrar_heroes(lista, "genero", "M")
    altura_mayor = calcular_mayor(l, "altura", "nombre")
    mostrar_heroe(altura_mayor, "ALTURA DEL MASCULINO MAS ALTO")


#              opcion 12                 #
def mostrar_masculino_mas_bajo(lista):
    l = filtrar_heroes(lista, "genero", "M")
    altura_mayor = calcular_menor(l, "altura", "nombre")
    mostrar_heroe(altura_mayor, "ALTURA DEL MASCULINO MAS BAJO")


#              opcion 11                 #
def mostrar_femenino_mas_alto(lista):
    l = filtrar_heroes(lista, "genero", "F")
    altura_mayor = calcular_mayor(l, "altura", "nombre")
    mostrar_heroe(altura_mayor, "ALTURA DEL FEMENINO MAS ALTO")


#              opcion 13                 #
def mostrar_femenino_mas_bajo(lista):
    l = filtrar_heroes(lista, "genero", "F")
    altura_mayor = calcular_menor(l, "altura", "nombre")
    mostrar_heroe(altura_mayor, "ALTURA DEL FEMENINO MAS BAJO")


# def mostrar_promedio_altura_masculino(lista):
#     l = filtrar_heroes(lista, "genero", "F")
#     promedio = calcular_promedio(l, "altura")
#     mostrar_heroe(promedio, "PROMEDIO ALTURAS")


# def mostrar_promedio_altura_femenino(lista):
#     l = filtrar_heroes(lista, "genero", "F")
#     altura_mayor = calcular_menor(l, "altura", "nombre")
#     mostrar_heroe(altura_mayor, "ALTURA DEL FEMENINO MAS BAJO")

#              opcion 14                 #
def promedio_alturas_masc(lista):
    l = filtrar_heroes(lista, "genero", "M")
    promedio = calcular_promedio(l, "altura")
    mostrar_heroe(promedio, "PROMEDIO ALTURAS MASCULINOS")


#              opcion 15                 #
def promedio_alturas_fem(lista):
    l = filtrar_heroes(lista, "genero", "F")
    promedio = calcular_promedio(l, "altura")
    mostrar_heroe(promedio, "PROMEDIO ALTURAS FEMENINOS")


# def mostrar_masculinos(lista):
#     l = filtrar_heroes(lista, "genero", "M")
#     nombres_masc = proyectar_heroe(l, "nombre")
#     mostrar_lista(nombres_masc, "PERSONAJES MASCULINOS")

#              opcion 16                 #
def nombres_masculino_mas_alto_y_bajo(lista):
    l = filtrar_heroes(lista, "genero", "M")
    altura_mayor = buscar_nombre_mas_alto_y_bajo(l, "altura", "nombre")
    mostrar_heroe(altura_mayor, "MASCULINO MAS ALTO / MASCULINO MAS BAJO")

def nombres_femenino_mas_alto_y_bajo(lista):
    l = filtrar_heroes(lista, "genero", "F")
    altura_mayor = buscar_nombre_mas_alto_y_bajo(l, "altura", "nombre")
    mostrar_heroe(altura_mayor, "FEMENINO MAS ALTO/FEMENINO MAS BAJO")


#              opcion 17/18                 #
def cantidad_por_valor(lista, valor):
    sets = set_colores(lista, valor)
    cantidad_personajes(lista, sets, valor)


#              opcion 20/21/22                 #
def mostrar_nombre_valor(lista: list, valor: str, titulo: str):
    sets = set_colores(lista, valor)
    nombre_por_color(lista, sets, valor, titulo)


#              opcion 19                 #
def inteligencia(lista, valor):
    sets = set_colores(lista, valor)
    superheroes_inteligencia(lista, sets)
