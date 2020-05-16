from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if player == ai:
        return 'Empate!'
    elif player == options[0]:
        return 'Perdiste!' if ai == options[1] else 'Ganaste!'       
    elif player == options[1]:
        return 'Perdiste!' if ai == options[2] else 'Ganaste!'    
    elif player == options[2]:
        return 'Perdiste!' if ai == options[0] else 'Ganaste!'
    else:
        return 'Perdiste!'        

# Entry Point
def Game():
    #
    #
    
    #
    #
    
    winner = quienGana(player, ai)

    print(winner)

