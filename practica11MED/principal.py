import geometria


radio_circulo = 5
area_circulo = geometria.calcular_area_circulo(radio_circulo)
perimetro_circulo = geometria.calcular_perimetro_circulo(radio_circulo)

print(f"Área del círculo: {area_circulo}")
print(f"Perímetro del círculo: {perimetro_circulo}")

base_rectangulo = 4
altura_rectangulo = 6
area_rectangulo = geometria.calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
perimetro_rectangulo = geometria.calcular_perimetro_rectangulo(base_rectangulo, altura_rectangulo)

print(f"Área del rectángulo: {area_rectangulo}")
print(f"Perímetro del rectángulo: {perimetro_rectangulo}")


base_triangulo = 8
altura_triangulo = 3
area_triangulo = geometria.calcular_area_triangulo(base_triangulo, altura_triangulo)
perimetro_triangulo = geometria.calcular_perimetro_triangulo(base_triangulo, 4, 5)

print(f"Área del triángulo: {area_triangulo}")
print(f"Perímetro del triángulo: {perimetro_triangulo}")


