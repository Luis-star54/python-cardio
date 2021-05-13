import os , random
os.system('clear')


    
def run():
    nivel_jugador1 = 0
    nivel_jugador2 = 0

    for i in range(3):
        player1 = input('Jugador 1 elige  piedra , papel o tijera => ').lower()
        player2 = input('Jugador 2 piedra , papel o tijera => ').lower()

        if player1 == 'piedra' and player2 == 'tijera' or player1 == 'papel' and player2 == 'piedra'  or player1 == 'tijera' and player2 == 'papel':
            print(' Jugador 1 ganaste esta ronda')
            nivel_jugador1 += 1
            if nivel_jugador1 == 2:
                print(' jugador 1 ERES EL GANADO ! ')
                break
        else:
            print('Jugador 2 ganaste esta ronda ')
            nivel_jugador2 += 1
            if nivel_jugador2 == 2:
                print('Jugador 2 ERES EL GANADOR')
                break    
            

    


if __name__ == '__main__':
    run()