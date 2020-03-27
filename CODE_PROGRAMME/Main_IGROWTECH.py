import RPi.GPIO as GPIO

from test_fonction_def_python import Capteurs_lvl_BAC_Culture
from test_fonction_def_python import Capteurs_lvl_BAC_EAU
from test_fonction_def_python import Capteurs_lvl_BAC_engrais
from test_fonction_def_python import Capteurs_Humidité
from test_fonction_def_python import Capteurs_PH
from test_fonction_def_python import Capteurs_EC
from test_fonction_def_python import Capteurs_Température
from test_fonction_def_python import Capteurs_LUX

configuration = GPIO.getmode()

print("Configuration actuelle du Raspberry PI :", configuration)

if configuration != "none":
    GPIO.setmode(GPIO.BCM)
else :
    print(OK)





Capteurs_PH = 0
Capteurs_EC = 1
Capteurs_LUX = 7
Capteurs_Température = 8
Capteurs_Humidité = 0
Capteurs_lvl_BAC_Culture = 25
Capteurs_lvl_BAC_EAU = 9
Capteurs_lvl_BAC_engrais = 10

# Pompe de brassage reservoir principale alimenter en continue
# Pompe a air alimenter en continue


# ici les ports GPIO sont declarer comme etant des sortie (OUT), initialise a l'etat HIGH ( activer )
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
            print("ENCULER APPREND A LIRE !!! \n cordialement <3 \n \n")

except KeyboardInterrupt:
    GPIO.cleanup()
# La fonction GPIO.cleanup() sert a retablir les paramettres par default du GPIO