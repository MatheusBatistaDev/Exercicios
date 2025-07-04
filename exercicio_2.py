import math

raio_do_circulo = float(input("Digite o raio do circulo: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)

print(f"A área do círculo com raio {raio_do_circulo} é: {area_do_circulo_formatada}")       

      