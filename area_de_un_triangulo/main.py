import os 
os.system('clear')

menu = """
                The boss of geometry
    Elige el 1 si quieres saber el area de un triangulo
    Elige el 2 si quieres saber el tipo de triangulo 
"""


def tipo_de_triangulo():
    lado1 = int(input('Escribe el primer lado => '))
    lado2 = int(input('Escribe el segundo lado => '))
    lado3 = int(input('Escribe el tercer lado => '))
    if lado1 == lado2 and lado2 == lado3:
        print('ESte es un triangulo equilatero ')
    elif lado1 == lado2 and lado2 != lado3:
        print('Este es un triangulo Isóceles')
    elif lado1 != lado2 and lado2 != lado3:
        print('ES un triangulo Escaleno ')
    return True            


def calcular_area():
    base = int(input('Escribe la base por favor => '))
    altura =  int(input('Escribe la altura por favor => '))
    area = (base * altura) // 2
    return area
    


def main():
    print(menu)
    try:
        opcion = int(input('Escribe aqui =>  '))
        if opcion == 1:
            resultado = calcular_area()
            print('El area del triangulo es ' + str(resultado))
        elif opcion == 2:
            tipo = tipo_de_triangulo()
            print(tipo)
        else:
            print('Coloca el numero correcto')    
    except ValueError:
        print('Escribe un numero por favor')

if __name__ == '__main__':
    main() 