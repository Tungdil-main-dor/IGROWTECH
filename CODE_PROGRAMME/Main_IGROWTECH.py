import RPi.GPIO as GPIO
from RGN_CAPTEURS import *

configuration = GPIO.getmode()

print("Configuration GPIO actuelle du Raspberry PI :", configuration)

# Définis le mode d'adressage des pin GPIO comme étant BCM
# PLus d'information sur https://pinout.xyz

if configuration != "none":
    GPIO.setmode(GPIO.BCM)
else :
    print(OK)

# Les valeurs qui suivents sont générer à partir du programme RNG_CAPTEURS,
# Il n'est donc plus nécéssaire de les entrées en dure dans le système

# Capteurs_PH = 0
# Capteurs_EC = 1
# Capteurs_LUX = 7
# Capteurs_Température = 8
# Capteurs_Humidité = 0
# Capteurs_lvl_BAC_Culture = 25
# Capteurs_lvl_BAC_EAU = 9
# Capteurs_lvl_BAC_engrais = 10
# Pompe de brassage = alimenter en continue
# Pompe a air = alimenter en continue


# ici, les ports GPIO sont déclarer comme étant des sorties (OUT), initialiser à l'état HIGH ( activer )
# Bien qu'il puisse (et même très probablement) par la suite être initialiser à LOW ( inactif )
# les ligne de code GPIO.output permette de modifier les valeurs d'état initiales rapidement

GPIO.setup(Pompe_Arrosage,GPIO.OUT,initial=GPIO.HIGH)
GPIO.output(Pompe_Arrosage,1)
GPIO.setup(Pompe_Engrais,GPIO.OUT,initial=GPIO.HIGH)
GPIO.output(Pompe_Engrais,1)
GPIO.setup(Pompe_Remplissage_BAC,GPIO.OUT,initial=GPIO.HIGH)
GPIO.output(Pompe_Remplissage_BAC,1)
GPIO.setup(Pompe_Vidange,GPIO.OUT,initial=GPIO.HIGH)
GPIO.output(Pompe_Vidange,1)
GPIO.setup(LED,GPIO.OUT,initial=GPIO.HIGH)
GPIO.output(LED,1)
GPIO.setup(Ventilateur,GPIO.OUT,initial=GPIO.HIGH)
GPIO.output(Ventilateur,1)
GPIO.setup(Pompe_PH,GPIO.OUT,initial=GPIO.HIGH)
GPIO.output(Pompe_PH,GPIO.OUT,1)

try:

    while(True):

        request = input("Entre etat GPIO : \n 0 = desactiver \n 1 = activer \n On attend 6 valeurs a la suite, 0 ou 1, ecrit a la suite sans espace -->")

        if (len(request) == 6):

            GPIO.output(Pompe_Arrosage,int(request[0]))

            GPIO.output(Pompe_Engrais,int(request[1]))

            GPIO.output(Pompe_Remplissage_reservoir_principale,int(request[2]))

            GPIO.output(Pompe_Vidange,int(request[3]))

            GPIO.output(LED,int(request[4]))

            GPIO.output(Ventilateur,int(request[5]))
        else :
            print("pas de violence, lire : append.... !!! \n cordialement <3 \n \n")

except KeyboardInterrupt:
    GPIO.cleanup()
# La fonction GPIO.cleanup() sert a retablir les paramettres par default du GPIO
