import os 
os.system('clear')

welcom = """
                    The best
    Bienvenido a la calculadora de voluemenes de cilindro
"""

def volumen_cilindro():
    menu = """
        Necesito algunos datos 

      -*--*--*--*--*--*--*--*-*--*-
      
      1) Tengo la altura y el radio 
      2) Tengo la altura y el diametro 

      Elige alguna opcion
    """
    opcion = int(input(menu))
    height = float(input('Por favor escribe la altura => '))
    PI = 3.1416

    if opcion == 1:
        radio = float(input('Escribe el radio por favor  => '))

    elif opcion == 2:
        diametro = float(input('Escribe el diametro por favor => '))
        radio = diametro / 2
        
    area_de_base = round(PI  * (radio ** 2), 2)
    volumen = area_de_base * height 
    return volumen  





def run():
    print(welcom)
    cilindro = volumen_cilindro()
    print('el volumen del cilindro es =>  ', str(cilindro), ' cm3')
   
    

if __name__ == '__main__':
    run()

