# Wersja zmodyfikowana na SERWERZE
import math

pi = math.pi
# wzór: P = pi * r ** 2

pizza1_srednica = 42
pizza1_cena = 36
promien_1 = pizza1_srednica/2
pizza2_srednica = 56
pizza2_cena = 42.5
promien_2 = pizza2_srednica/2
stosunek_1 = pi*promien_1 **2
stosunek_2 = pi*promien_2 **2
print('Stosunek ilości do ceny dla')
print(f'pizza 1: {stosunek_1/pizza1_cena:.2f}')
print(f'pizza 2: {stosunek_2/pizza2_cena:.2f}')
#wersja kolejna

