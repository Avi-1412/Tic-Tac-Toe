# Representamos el tablero como lista de 9 posiciones
def tablero(board):
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        

def ganador(board):
    # Posibles líneas ganadoras
    lines = [
        [0,1,2], [3,4,5], [6,7,8],  # filas
        [0,3,6], [1,4,7], [2,5,8],  # columnas
        [0,4,8], [2,4,6]            # diagonales
    ]
    for a,b,c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    if " " not in board:
        return "Empate"
    return None

# Minimax con divide y vencerás
def minimax(board, maximizar):
    winner = ganador(board)
    if winner == "O":  # IA gana
        return 1
    elif winner == "X":  # Humano gana
        return -1
    elif winner == "Empate":
        return 0

    if maximizar:
        MrP = -999
        for i in range(9):
            if board[i] == " ":
                Ntab = board[:]
                Ntab[i] = "O"
                puntaje = minimax(Ntab, False)
                MrP = max(MrP, puntaje)
        return MrP
    else:
        MrP = 999
        for i in range(9):
            if board[i] == " ":
                Ntab = board[:]
                Ntab[i] = "X"
                puntaje = minimax(Ntab, True)
                MrP = min(MrP, puntaje)
        return MrP

def Mejormov(board):
    MrP = -999
    move = None
    for i in range(9):
        if board[i] == " ":
            Ntab= board[:]
            Ntab[i] = "O"
            puntaje = minimax(Ntab, False)
            if puntaje > MrP:
                MrP = puntaje
                move = i
    return move

def play():
    board = [" "] * 9
    print("juguemos gato : Tú = X | IA = O")
    tablero(board)

    while True:
        # Turno humano
        move = int(input("Tu movimiento (1-9): "))-1
        if board[move] != " ":
            print("Posición ocupada, intenta otra.")
            continue
        board[move] = "X"

        if ganador(board):
            break

        # Turno IA
        ia_move = Mejormov(board)
        board[ia_move] = "O"
        print("\nIA juega en posición", (ia_move +1))
        tablero(board)

        if ganador(board):
            break
   
    result = ganador(board)
    if result=="X":
         print("\nGano la humanidad: ", result)
    elif result=="O":
         print("\nGano la IA :", result)
    else:
         print("\nResultado:", result)

play()
