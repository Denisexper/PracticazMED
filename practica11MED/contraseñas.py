import random 

str = 'abcdefghijklmnñoprstuvwxyz.,()/&%$#!'
numeros = "1234567890"

unir = f'{str}{numeros}'

longitud = 10

contraseña = random.sample(unir, longitud)
contraseña_final = "".join(contraseña)
print(f"Tu contraseña es: {contraseña_final}")