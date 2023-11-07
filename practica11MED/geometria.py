import math

def calcular_area_circulo(radio):
  
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
   
    return 2 * math.pi * radio

def calcular_area_rectangulo(base, altura):
    
    return base * altura

def calcular_perimetro_rectangulo(base, altura):
    
    return 2 * (base + altura)

def calcular_area_triangulo(base, altura):
    
    return (base * altura) / 2

def calcular_perimetro_triangulo(lado1, lado2, lado3):
    
    return lado1 + lado2 + lado3
