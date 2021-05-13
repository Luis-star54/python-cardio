import os 
os.system('clear')



def run():
    limite_inferior = int(input('Elige un limite inferior => '))
    limite_superior = int(input('Elige un limite superior => '))
    comparacion = int(input('Elige un numero  => '))

    for i in range(limite_inferior, limite_superior + 1):
        if i > limite_inferior and i < limite_superior:
            print(comparacion)
        else:
            comparacion = int(input('Elige otro numero => '))


                



if __name__ == '__main__':
    run()