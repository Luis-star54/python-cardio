import os
os.system('clear')

menu = """
            The best converter
            1) Convertir millas a km 
            2) COnvertir km a millas 
"""

def conversor_kilometro(kilometro):
    METROS = 1000
    MILLAS = 1609
    resultado = round((kilometro * METROS) / MILLAS, 2)
    return resultado


def conversor_millas(millas):
    METROS = 1609
    KILOMETROS = 1000
    resultado = (millas * METROS) / KILOMETROS
    return resultado
    



def main():
    print(menu)
    opcion = int(input('Elige aqui => '))
    if opcion == 1:
        cantidad_millas = float(input('¿Cuantas millas quieres convertir => '))
        resultado = conversor_millas(cantidad_millas)
        print(str(cantidad_millas), 'millas equivalen a ' , str(resultado), 'km')
    elif opcion == 2:
        kilometros = float(input('¿Cuantos km quieres convertir? => '))
        resultado_de_km = conversor_kilometro(kilometros)
        print(str(kilometros) , ' km equivalen a ', str(resultado_de_km), 'millas')

    print('Gracias por confiar en mi ')        
   

if __name__ == '__main__':
    main()