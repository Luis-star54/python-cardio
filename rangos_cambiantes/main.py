import os 
os.system('clear')



def run():
    limite_inferior = int(input('Elige un limite inferior => '))
    limite_superior = int(input('Elige un limite superior => '))
    comparacion = int(input('Elige un numero  => '))

    while comparacion < limite_inferior or comparacion > limite_superior:
        print('el numero' , str(comparacion), 'esta fuera de rango ' )
        comparacion = int(input('Ingresa otro numero => '))

    print('el numero ', str(comparacion), 'esta dentro del rango' )    
                
        
if __name__ == '__main__':
    run()