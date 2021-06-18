import time
import board
import neopixel

# 1 = Red
# 2 = Green
# 3 = Blue 

pixel_pin = board.D21
num_pixels = 150
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

pixels.fill((0, 0, 255))
pixels.show()
print('Blue')
