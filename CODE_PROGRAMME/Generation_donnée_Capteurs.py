import random
import os
import time

os.chdir("/home/mint-on-fire/Bureau/Projet_BTS/DONNEE_CAPTEURS")

Ph = float(random.uniform(0, 14))
Ec = float(random.uniform(0, 3))
LUX = int(random.randint(300, 50000))
Température = float(random.uniform(5, 50))
lvl_bac_culture = int(random.randint(0, 100))
lvl_bac_eau = int(random.randint(0, 100))
lvl_bac_engrais = int(random.randint(0, 100))
Humidity = int(random.randint(0, 100))


while(True):
    
    if Ph <= 3:
        Ph = Ph + float(random.uniform(0, 1))
        print("Ph","%.2f" % Ph)

    elif Ph >= 11:
        Ph = Ph - float(random.uniform(0, 1))
        print("Ph","%.2f" % Ph)
    else:
        print("Ph","%.2f" % Ph)
    break

while(True):

    if Ec <= 1:
        Ec = Ec + float(random.uniform(0,1))
        print("Ec","%.2f" % Ec)

    elif Ec >= 2:
        Ec = Ec - float(random.uniform(0, 1))
        print("Ec","%.2f" % Ec)

    else:
        print("Ec","%.2f" % Ec)
    break

while(True):

    if LUX <= 500:
        LUX = LUX + int(random.randint(0, 5000))
        print("LUX","%.2f" % LUX)

    elif LUX >= 45000:
        LUX = LUX - int(random.randint(0, 4500))
        print("LUX","%.2f" % LUX)
    
    else:
        print("LUX","%.2f" % LUX)
    break

while(True):

    if Température <= 10:
        Température = Température + float(random.uniform(0, 7))
        print("Température","%.2f" % Température)

    elif Température >= 45:
        Température = Température - float(random.uniform(0, 7))
        print("Température","%.2f" % Température)

    else:
        print("Température","%.2f" % Température)
    break

while(True):

    if lvl_bac_culture <= 10:
        lvl_bac_culture = lvl_bac_culture + int(random.uniform(0, 15))
        print("Niv_Bac_culture","%.2f" % lvl_bac_culture)
    
    elif lvl_bac_culture >= 98:
        lvl_bac_culture = lvl_bac_culture - int(random.uniform(0,45))
        print("Niv_Bac_culture","%.2f" % lvl_bac_culture)

    else:
        print("Niv_Bac_culture","%.2f" % lvl_bac_culture)
    break

while(True):

    if lvl_bac_eau <= 10:
        lvl_bac_eau = lvl_bac_eau + int(random.uniform(0, 15))
        print("Niv_Bac_Eau","%.2f" % lvl_bac_eau)
    
    elif lvl_bac_eau >= 98:
        lvl_bac_eau = lvl_bac_eau - int(random.uniform(0,45))
        print("Niv_Bac_Eau","%.2f" % lvl_bac_eau)
    break

while(True):

    if lvl_bac_engrais <= 10:
        lvl_bac_engrais = lvl_bac_engrais + int(random.uniform(0, 15))
        print("Niv_Bac_Engrais","%.2f" % lvl_bac_engrais)
    
    elif lvl_bac_engrais >= 98:
        lvl_bac_engrais = lvl_bac_engrais - int(random.uniform(0,45))
        print("Niv_Bac_Engrais","%.2f" % lvl_bac_engrais)

    else:
        print("Niv_Bac_Engrais","%.2f" % lvl_bac_engrais)
    break

while(True):

    if Humidity <= 10:
        Humidity = Humidity + int(random.uniform(0, 15))
        print("Humidity","%.2f" % Humidity)
    
    elif Humidity >= 98:
        Humidity = Humidity - int(random.uniform(0,45))
        print("Humidity","%.2f" % Humidity)

    else:
        print("Humidity","%.2f" % Humidity)
    break
"""
# idée optimisation : Utiliser 2 listes (int, float) pour réduire le nombre de ligne de code.


os.system("python3 /home/mint-on-fire/Bureau/Projet_BTS/CODE_PROGRAMME/RGN_CAPTEURS.py | grep 202* | tee -a /home/mint-on-fire/Bureau/Projet_BTS/DONNEE_CAPTEURS/DONNEE_CAPTEURS.log")
# os.system("tail -n 10 /home/mint-on-fire/Bureau/Projet_BTS/DONNEE_CAPTEURS/DONNEE_CAPTEURS.log | egrep Ph | tee /home/mint-on-fire/Bureau/Projet_BTS/DONNEE_CAPTEURS/ph.txt")
# os.system("python3 /home/mint-on-fire/Bureau/Projet_BTS/CODE_PROGRAMME/test_osbash.py | egrep 202* | tee -a /home/mint-on-fire/Bureau/Projet_BTS/DONNEE_CAPTEURS/DONNEE_CAPTEURS.log")
# os.system("python3 /home/mint-on-fire/Bureau/Projet_BTS/CODE_PROGRAMME/test_osbash.py | egrep 202* | tee -a /home/mint-on-fire/Bureau/Projet_BTS/DONNEE_CAPTEURS/DONNEE_CAPTEURS.log")
# os.system("python3 /home/mint-on-fire/Bureau/Projet_BTS/CODE_PROGRAMME/test_osbash.py | egrep 202* | tee -a /home/mint-on-fire/Bureau/Projet_BTS/DONNEE_CAPTEURS/DONNEE_CAPTEURS.log")
# os.system("python3 /home/mint-on-fire/Bureau/Projet_BTS/CODE_PROGRAMME/test_osbash.py | egrep 202* | tee -a /home/mint-on-fire/Bureau/Projet_BTS/DONNEE_CAPTEURS/DONNEE_CAPTEURS.log")
# os.system("python3 /home/mint-on-fire/Bureau/Projet_BTS/CODE_PROGRAMME/test_osbash.py | egrep 202* | tee -a /home/mint-on-fire/Bureau/Projet_BTS/DONNEE_CAPTEURS/DONNEE_CAPTEURS.log")
# os.system("python3 /home/mint-on-fire/Bureau/Projet_BTS/CODE_PROGRAMME/test_osbash.py | egrep 202* | tee -a /home/mint-on-fire/Bureau/Projet_BTS/DONNEE_CAPTEURS/DONNEE_CAPTEURS.log")
# os.system("python3 /home/mint-on-fire/Bureau/Projet_BTS/CODE_PROGRAMME/test_osbash.py | egrep 202* | tee -a /home/mint-on-fire/Bureau/Projet_BTS/DONNEE_CAPTEURS/DONNEE_CAPTEURS.log")
# os.system("python3 /home/mint-on-fire/Bureau/Projet_BTS/CODE_PROGRAMME/test_osbash.py | egrep 202* | tee -a /home/mint-on-fire/Bureau/Projet_BTS/DONNEE_CAPTEURS/DONNEE_CAPTEURS.log")

#Solution initiale utilisant la fonction open de python 3:
"""
def Output_DONNE_CAPTEURS_LOG():
        data_log = open("DONNEE_CAPTEURS_0.txt", "a+")
        data_log.write("\n \n \n") 
        data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
        data_log.write(":")
        data_log.write("   Valeur sonde Ph =")
        data_log.write("%.2f" % Ph)
        data_log.write("\n")
        data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
        data_log.write(":")
        data_log.write( "   Valeur sonde EC =")
        data_log.write( "%.2f" % Ec)
        data_log.write("\n")
        data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
        data_log.write(":")
        data_log.write( "   Lux = ")
        data_log.write("%.2f" % LUX)
        data_log.write("\n")
        data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
        data_log.write(":")
        data_log.write("   Température = ")
        data_log.write("%.2f" % Température)
        data_log.write("\n")
        data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
        data_log.write(":")
        data_log.write("   niv_bac_culture = ")
        data_log.write("%.2f" % lvl_bac_culture)
        data_log.write("\n")
        data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
        data_log.write(":")
        data_log.write("   niv_bac_eau = ")
        data_log.write("%.2f" % lvl_bac_eau)
        data_log.write("\n")
        data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
        data_log.write(":")
        data_log.write("   niv_bac_engrais = ")
        data_log.write("%.2f" % lvl_bac_engrais)
        data_log.write("\n")
        data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
        data_log.write(":")
        data_log.write("   niv_Humidity = ")
        data_log.write("%.2f" % Humidity)
        data_log.write("\n")
        data_log.write("\n Valeurs aléatoire générer le ")
        data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
        data_log.write("\n")
        data_log.close()
#        print(" \n Valeurs aléatoire générer à", time.strftime("%A %d %B %Y %H:%M:%S")," \n"))
# print Output_LOG()
        data_log = open("DONNEE_CAPTEURS_0.txt", "r")
        data = str(data_log.read())
        return data
        data_log.close()
print (Output_DONNE_CAPTEURS_LOG())