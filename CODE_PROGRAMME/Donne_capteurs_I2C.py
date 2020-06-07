# Générer, puis affecté a un ficher text au qu'elle on aura accées a travers une émulation de trame i2c.
print("""

 I   Utilisation de l'utilitaire intégré a raspberry pi permettant la lecture de l'I2C sur les ports GPIO 
 
    Le retour de la commande bash --> i2cdetect -y 1 renvois :

            0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
        00:          -- -- -- -- -- -- -- -- -- -- -- -- --
        10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        60: 60 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        70: -- -- -- -- -- -- -- --

# en effet le BUS i2C posséde 127 adresse ;)

    La valeur 0x60 correspond à l'adresse I2C du capteur avec lequel on veut intéragire,

    Exemple de script python récupérant une valeur stocker à une adresse i2c définit 
    et qui fait varier l'intensité d'une lumière  :

import smbus
import time
bus = smbus.SMBus(0)
address = 0x60


def lightlevel():
        light = bus.read_byte_data(address, 1)
        return light

def range():
        range1 = bus.read_byte_data(address, 2)
        range2 = bus.read_byte_data(address, 3)
        range3 = (range1 << 8) + range2
        return range3

while True:
        write(0x60)
        time.sleep(0.7)
        lightlvl = lightlevel()
        rng = range()
        print lightlvl
        print rng

