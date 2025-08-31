#gato gatito gatoso
# Función que revisa si hay un ganador
from os import system #Biblioteca para limpiar consola jiji
def hay_ganador(tablero):
    # Todas las combinaciones posibles pa ganar
    combinaciones = [
        [0,1,2], [3,4,5], [6,7,8],  # filas
        [0,3,6], [1,4,7], [2,5,8],  # columnas
        [0,4,8], [2,4,6]            # diagonales
    ]
    # Revisa cada combinación de filas columnas y diagonales pa ver si ya gano uno arriba estan x si acaso
    for a,b,c in combinaciones:
        if tablero[a] == tablero[b] == tablero[c] and tablero[a] != " ":
            return tablero[a]  # devuelve "X" o "O"
    return None

# Función que revisa si hay empate se hizo pq con un else no jalo xd
def hay_empate(tablero):
    return " " not in tablero and hay_ganador(tablero) is None 
#(linea 18)si ya no hay espacios vacios ni un ganador ps empate,necesitamos tantos comentarios??

# Devuelve los movimientos posibles
def movimientos_posibles(tablero):
    return [i for i, casilla in enumerate(tablero) if casilla == " "]

# MINIMAX
# evalúa el tablero
def minimax(tablero, es_max):
    ganador = hay_ganador(tablero)
    if ganador == "X": return 1   # IA gana
    if ganador == "O": return -1  # humano gana
    if hay_empate(tablero): return 0  # empate

    if es_max:  # turno IA (X) busca maximizar 
        mejor = -999 
        # DIVIDE Y VENCERAS: prueba cada movimiento posible
        for mov in movimientos_posibles(tablero):
            tablero[mov] = "X"           # hace un movimiento
            puntaje = minimax(tablero, False) 
            tablero[mov] = " "           # deshace movimiento
            mejor = max(mejor, puntaje)  # combina resultados
        return mejor
    else:  # turno humano buscar minimizar a la IA
        mejor = 999
        for mov in movimientos_posibles(tablero):
            tablero[mov] = "O" #marca la casilla que elige el humano 
            puntaje = minimax(tablero, True)# hora es turno de la IA (es_max=True)
            tablero[mov] = " "
            mejor = min(mejor, puntaje)
        return mejor

# MEJOR MOVIMIENTO de la IA 
# Busca el mejor movimiento para la IA la tramposota
def mejor_movimiento(tablero):
    mejor_puntaje = -999
    movimiento = None
    for mov in movimientos_posibles(tablero):
        # Simulamos que la IA pone una "X"aqui
        tablero[mov] = "X"
        # Calcula puntaje de ese movimiento
        # Evalúan todas las posibles respuestas
        puntaje = minimax(tablero, False)  # False porque va el humano
        # Deshacemos el movimiento para probar otro
        tablero[mov] = " "
        # Si el puntaje de este mov es mejor que el anterior, lo actualiza
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            movimiento = mov  # Guarda la posición del mejor mov
    # IA coloca su "X"
    return movimiento

# IMPRESIÓN TABLERO
def imprimir_tablero(tablero):
    print()
    # Recorre el tablero de 0 a 8, saltando de 3 en 3 para imprimir filas (yutu patrocina)
    for i in range(0, 9, 3):
        print(tablero[i], "|", tablero[i+1], "|", tablero[i+2])
    print()

# MAIN 
def main():
    #este es el tablero que se mostra impreso se puede agregar valores pa comenzar ya que en la linea 103
    # se evalua que la posicion que el humano elija este en el rango de 0 a 8 y el espacio del tablero en " " que seria vacio 
    tablero = [
        " "," "," ",
        " "," "," ",
        " "," "," "
    ]
    print("Juguemos Gato (IA = X, Tú = O)")
    
    while True:
        system("cls")
        imprimir_tablero(tablero)

        if hay_ganador(tablero) or hay_empate(tablero):
            break

        # Turno humano
        try: 
            mov = int(input("Elige posición (1-9): ")) -1
        except:
            print("Ingresa un número válido.")
            continue

        if mov not in range(9) or tablero[mov] != " ":
            print("Movimiento inválido.")
            continue
        tablero[mov] = "O"

        if hay_ganador(tablero) or hay_empate(tablero):
            break

        # Turno IA
        ia_mov = mejor_movimiento(tablero)  # usa Minimax para decidir donde poner su x
        tablero[ia_mov] = "X"
    system("cls")
    imprimir_tablero(tablero)# imprime el tablero con la actualizacion del juego
    ganador = hay_ganador(tablero)
    if ganador:
        if ganador=="X":
            print("Ganó la IA :c")
        else:
            print("Gano la Humanidad :D")
    else:
        print("Empate :o")

main() # llama a la funcion principal