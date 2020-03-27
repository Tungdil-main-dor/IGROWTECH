import threading
import random
import time
import os

os.chdir("/home/mint-on-fire/Bureau/Projet_BTS/DONNEE_CAPTEURS")

# Declaration des variables correspondant au mesurent effectué par les capteurs sur le système
Ph = float(random.uniform(0, 14))
Ec = float(random.uniform(0, 3))
LUX = int(random.randint(300, 50000))
Température = float(random.uniform(5, 50))
lvl_bac_culture = int(random.randint(0, 100))
lvl_bac_eau = int(random.randint(0, 100))
lvl_bac_engrais = int(random.randint(0, 100))
Humidity = int(random.randint(0, 100))

# Declaration des variables nécéssaire au fonctionement du Script
limite_backup_log = 0
actionneur_RGN =0
a = 0
i = 1

# Demande la durré d'attente entre chaque mesure réaliser sur le système
Delais_Mesure = int(input("Veillez fournir le delais entre chaque mesure (exprimé en secondes ) :"))

while i == 1:
    # # Ph de la solution
    # def PH_Solution():
    #     while a != 0:
    #         Ph = float(random.uniform(0, 14)) 
    #         print("Ec","%.2f" % Ph)
    #         return Ph

    # # Ec de la solution
    # def EC_Solution():
    #     while a != 0:
    #         Ec = float(random.uniform(0, 3))
    #         print("Ec","%.2f" % Ec)
    #         return Ec


    # # Luminosité ambiante
    # def Luminosité_Système():
    #     while a != 0:
    #         LUX = int(random.randint(300, 50000))
    #         print("LUX","%.0f" % LUX)
    #         return LUX


    # # Temperature
    # def Temperature_système():
    #     while a != 0:
    #         Température = float(random.uniform(5, 50))
    #         print("Température","%.2f" % Température)
    #         return Température


    # # Niveau reservoir Culture
    # def Niveaux_Reservoire_culture():
    #     while a != 0:
    #         lvl_bac_culture = int(random.randint(0, 100))
    #         print("Niv_Bac_culture","%.2f" % lvl_bac_culture)
    #         return lvl_bac_culture


    # # Niveaux_reservoir_EAU
    # def Niveaux_reservoir_EAU():
    #     while a != 0:
    #         lvl_bac_eau = int(random.randint(0, 100))
    #         print("Niv_Bac_Eau","%.2f" % lvl_bac_eau)
    #         return lvl_bac_eau


    # # Niveau_Reservoir_Engrais
    # def Niveau_Reservoir_Engrais():
    #     while a != 0:
    #         lvl_bac_engrais = int(random.randint(0, 100))
    #         print("Niv_Bac_Engrais","%.2f" % lvl_bac_engrais)
    #         return lvl_bac_engrais


    # # Humidité_système
    # def Humidité_système():
    #     while a != 0:
    #         Humidity = int(random.randint(0, 100))
    #         print("Humidity","%.2f" % Humidity)
    #         return Humidity


    def Output_DONNE_CAPTEURS_LOG():
            with open("DONNEE_CAPTEURS.log", "a") as data_log:
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
                data_log.write("\n")
                data_log.close()
                data_log = open("DONNEE_CAPTEURS.log", "r")
                data = str(data_log.read())
                return data
                data_log.close()


    def Capteurs_lvl_BAC_Culture():
        data_lvl = open("bac_culture", "w")
        data_lvl.write(str(lvl_bac_culture))
        data_lvl.close()
        data_lvl = open("bac_culture", "r")
        data = int(data_lvl.read())
        return data
        data_lvl.close()
    print( "Niv bac culture                  = ",Capteurs_lvl_BAC_Culture(),"%")


    def Capteurs_lvl_BAC_EAU():
        data_lvl = open("bac_eau", "w")
        data_lvl.write(str(lvl_bac_eau))
        data_lvl.close()
        data_lvl = open("bac_eau", "r")
        data = int(data_lvl.read())
        return data
        data_lvl.close()
    print( "Niv bac eau                      = ",Capteurs_lvl_BAC_EAU(),"%")


    def Capteurs_lvl_BAC_engrais():
        data_lvl = open("bac_engrais", "w")
        data_lvl.write(str(lvl_bac_engrais))
        data_lvl.close()
        data_lvl = open("bac_engrais", "r")
        data = int(data_lvl.read())
        return data
        data_lvl.close()
    print( "Niv bac engrais                  = ",Capteurs_lvl_BAC_engrais(),"%")


    def Capteurs_Humidité():
        data_lvl = open("Hydro", "w")
        data_lvl.write(str(Humidity))
        data_lvl.close()
        data_lvl = open("Hydro", "r")
        data = int(data_lvl.read())
        return data
        data_lvl.close()
    print( "Niv humidité                     = ",Capteurs_Humidité(), "%")


    def Capteurs_PH():
        data_lvl = open("ph", "w")
        data_lvl.write(str(Ph))
        data_lvl.close()
        data_lvl = open("ph", "r")
        data = float(data_lvl.read())
        return data
        data_lvl.close()
    print( "Niv de pH                        = ","%.2f" % Capteurs_PH(), "pH")


    def Capteurs_EC():
        data_lvl = open("ec", "w")
        data_lvl.write(str(Ec))
        data_lvl.close()
        data_lvl = open("ec", "r")
        data = float(data_lvl.read())
        return data
        data_lvl.close()
    print( "Niv d'EC                         = ","%.2f" % Capteurs_EC(), "EC")

    def Capteurs_Température():
        data_lvl = open("température", "w")
        data_lvl.write(str(Température))
        data_lvl.close()
        data_lvl = open("température", "r")
        data = float(data_lvl.read())
        return data
        data_lvl.close()
    print( "Température dans la pièce        = ","%.2f" % Capteurs_Température(), "C°")

    def Capteurs_LUX():
        data_lvl = open("lux", "w")
        data_lvl.write(str(LUX))
        data_lvl.close()
        data_lvl = open("lux", "r")
        data = int(data_lvl.read())
        return data
        data_lvl.close()
    print( "Niv luminosité                   = ",Capteurs_LUX(), "lux")


#    Permet d'écrire dans le fichier DONNE_CAPTEURS.log
    Output_DONNE_CAPTEURS_LOG()

#    time.sleep(int(Delais_Mesure))
    Ph = float(random.uniform(0, 14))
    Ec = float(random.uniform(0, 3))
    LUX = int(random.randint(300, 50000))
    Température = float(random.uniform(5, 50))
    lvl_bac_culture = int(random.randint(0, 100))
    lvl_bac_eau = int(random.randint(0, 100))
    lvl_bac_engrais = int(random.randint(0, 100))
    Humidity = int(random.randint(0, 100))
    # Niveau_Reservoir_Engrais()
    # Niveaux_reservoir_EAU()
    # Niveaux_Reservoire_culture
    # PH_Solution()
    # EC_Solution()
    # Temperature_système()
    # Luminosité_Système()
    # Humidité_système()
    with open ('DONNEE_CAPTEURS.log', 'r') as log:
        data_leng = (log.read())
        data_leng_1 = data_leng.split('\n')
        limite_backup_log = len(data_leng_1)
        print("\n","Nombre de ligne présent dans le fichier de log       :",limite_backup_log,"\n","\n")
        if limite_backup_log >= 50000:
            os.system("tar -czf DONNEE_CAPTEURS.log.$(date +%d-%m-%Y-%H%M%S)h DONNEE_CAPTEURS.log && mv DONNEE_CAPTEURS.log.* ./archive_donnee_capteurs/ && rm -f DONNEE_CAPTEURS.log")
            limite_backup_log = 0
            print("Le fichier de log ayant atteint sa taille limite, une archive de celui-ci à étais générer dans le dossier archive_donnee_capteurs ")
            os.system("touch DONNEE_CAPTEURS.log")
            Output_DONNE_CAPTEURS_LOG()
            print(limite_backup_log)
# idée optimisation : Utiliser 2 listes (int, float) pour réduire le nombre de ligne de code.

#Ran_Value_Capteurs = str(print("\n \n \n",time.strftime("%A %d %B %Y %H:%M:%S"), ":", "   Valeur sonde Ph =", "%.2f" % Ph,"\n",time.strftime("%A %d %B %Y %H:%M:%S"), ":", "   Valeur sonde EC =", "%.2f" % Ec,"\n",time.strftime("%A %d %B %Y %H:%M:%S"), ":", "   Lux = ","%.2f" % LUX,"\n",time.strftime("%A %d %B %Y %H:%M:%S"), ":", "   Température = ","%.2f" % Température,"\n",time.strftime("%A %d %B %Y %H:%M:%S"), ":", "   niv_bac_culture = ","%.2f" % lvl_bac_culture,"\n",time.strftime("%A %d %B %Y %H:%M:%S"), ":", "   niv_bac_eau = ","%.2f" % lvl_bac_eau,"\n",time.strftime("%A %d %B %Y %H:%M:%S"), ":", "   niv_bac_engrais = ","%.2f" % lvl_bac_engrais, "\n",time.strftime("%A %d %B %Y %H:%M:%S"), ":", "   niv_Humidity = ","%.2f" % Humidity, "\n"," \n Valeurs aléatoire générer à", time.strftime("%A %d %B %Y %H:%M:%S")," \n"))
#print(Ran_Value_Capteurs)
"""
while(True):
$(date +%d-%m-%Y-%H)h
    while limite_bak <= 50000:

        with open ('DONNEE_CAPTEURS.log', 'r') as log:
            data_leng = (log.read())
            data_leng_1 = data_leng.split('\n')
            limite_bak = len(data_leng_1)
            print(limite_bak)
            Output_DONNE_CAPTEURS_LOG()

    if limite_bak >= 50000:

        os.system("mv DONNEE_CAPTEURS.log DONNEE_CAPTEURS.log.old.*[0-9] ")
        limite_bak = 0
        print(limite_bak)
        os.system("touch DONNEE_CAPTEURS.log")
        Output_DONNE_CAPTEURS_LOG()
        print(limite_bak)

# def Output_DONNE_CAPTEURS_LOG():
#     with open("DONNEE_CAPTEURS.log", "a") as data_log:
#         data_log.write("\n \n \n") 
#         data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
#         data_log.write(":")
#         data_log.write("   Valeur sonde Ph =")
#         data_log.write("%.2f" % Ph)
#         data_log.write("\n")
#         data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
#         data_log.write(":")
#         data_log.write( "   Valeur sonde EC =")
#         data_log.write( "%.2f" % Ec)
#         data_log.write("\n")
#         data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
#         data_log.write(":")
#         data_log.write( "   Lux = ")
#         data_log.write("%.2f" % LUX)
#         data_log.write("\n")
#         data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
#         data_log.write(":")
#         data_log.write("   Température = ")
#         data_log.write("%.2f" % Température)
#         data_log.write("\n")
#         data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
#         data_log.write(":")
#         data_log.write("   niv_bac_culture = ")
#         data_log.write("%.2f" % lvl_bac_culture)
#         data_log.write("\n")
#         data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
#         data_log.write(":")
#         data_log.write("   niv_bac_eau = ")
#         data_log.write("%.2f" % lvl_bac_eau)
#         data_log.write("\n")
#         data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
#         data_log.write(":")
#         data_log.write("   niv_bac_engrais = ")
#         data_log.write("%.2f" % lvl_bac_engrais)
#         data_log.write("\n")
#         data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
#         data_log.write(":")
#         data_log.write("   niv_Humidity = ")
#         data_log.write("%.2f" % Humidity)
#         data_log.write("\n")
#         data_log.write("\n Valeurs aléatoire générer le ")
#         data_log.write(time.strftime("%A %d %B %Y %H:%M:%S"))
#         data_log.write("\n")
#         data_log.write("\n")
#         data_log.close()
#         data_log = open("DONNEE_CAPTEURS.log", "r")
#         data = str(data_log.read())
#         return data
#         data_log.close()

# while(True):
#     while limite_bak <= 50000:
#         with open ('DONNEE_CAPTEURS.log', 'r') as log:
#             data_leng = (log.read())
#             data_leng_1 = data_leng.split('\n')
#             limite_bak = len(data_leng_1)
#             print(limite_bak)
#             Output_DONNE_CAPTEURS_LOG()
#     if limite_bak >= 50000:
#         os.system("mv DONNEE_CAPTEURS.log DONNEE_CAPTEURS.log.old.*[0-9] ")
#         limite_bak = 0
#         print(limite_bak)
#         os.system("touch DONNEE_CAPTEURS.log")
#         Output_DONNE_CAPTEURS_LOG()
#         print(limite_bak)
"""