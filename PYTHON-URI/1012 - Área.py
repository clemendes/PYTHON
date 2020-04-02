leitura = input().split(" ")
a, b, c = leitura

pi = 3.14159

triangulo = (( float(a) * float(c) )/2)
circulo = pi * (float(c)**2)
trapezio = ((float(a)+float(b))/2)*float(c)
quadrado = float(b) * float(b)
retangulo = float(a) * float(b)

print("TRIANGULO: %0.3f" %triangulo)
print("CIRCULO: %0.3f" %circulo)
print("TRAPEZIO: %0.3f" %trapezio)
print("QUADRADO: %0.3f" %quadrado)
print("RETANGULO: %0.3f" %retangulo)
