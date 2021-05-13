import os 
os.system('clear')



def run():
    limite_inferior = int(input('Elige un limite inferior => '))
    limite_superior = int(input('Elige un limite superior => '))
    comparacion = int(input('Elige un numero  => '))

    for numero in range(limite_inferior , limite_superior + 1):
        
        if comparacion > limite_inferior and comparacion < limite_superior:
            if comparacion == numero:
                print(comparacion)
        else:
            comparacion = int(input('elige otro numero => '))
            if comparacion == numero:
                print(comparacion)
                
        
if __name__ == '__main__':
    run()