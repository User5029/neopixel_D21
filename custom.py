import time
import board
import neopixel

# 1 = Red
# 2 = Green
# 3 = Blue 

pixel_pin = board.D21
num_pixels = 150
ORDER = neopixel.GRB

R = int(input('Red value: '))
G = int(input('Green value: '))
B = int(input('Blue value: '))
A = float(input('Brightness (default 0.2): '))


pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=A, auto_write=False, pixel_order=ORDER
)

#R = int(input('Red value: '))
#G = int(input('Green value: '))
#B = int(input('Blue value: '))
#A = float(input('Brightness (default 0.2('))

pixels.fill((R, G, B))
pixels.show()
print('Values are: ')
print('Red = ' + str(R))
print('Green = ' + str(G))
print('Blue = ' + str(B))
