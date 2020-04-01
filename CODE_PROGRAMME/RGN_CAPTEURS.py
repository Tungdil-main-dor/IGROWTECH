import threading
import random
import time
import os

# Chemin écrit en dure par facilité a remplacer par les variables système $USER......
os.chdir("/home/mint-on-fire/Bureau/Projet_BTS/DONNEE_CAPTEURS")
os.system("mkdir archive_donnee_capteurs")


# Declaration des variables nécéssaire au fonctionement du Script
limite_backup_log = 0
i = 1

# Demande la durée d'attente entre chaque mesure réaliser sur le système
Delais_Mesure = int(input("Veuillez fournir le delais entre chaque mesure (exprimé en secondes ) :"))

# Demander si l'utilisateur et certain de vouloir générer des valeurs 
print("Générer des données capteurs ?")
choix = input("y or n:")
if choix.lower() == "y":
    print("Lancement du script dans :")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
else:
    raise Exception("Sorry no more code for u....HOoOo sad larry...")

# actionneur_RGN = str(input("Voulez-vous utiliser le générateur de valeur ? (Y/N) :"))

# while True:
#     valide_lancement = "Y"
#     print("Selon l'ordre lexicographique, ", end = "")
#     if actionneur_RGN < valide_lancement:
#         raise Exception("Sorry no more code for u....HOoOo sad larry...")
#     if actionneur_RGN == valide_lancement:
#         print("Ce script vas être executer")
#     if actionneur_RGN > valide_lancement:
#         raise Exception("Sorry no more code for u....HOoOo sad larry...") 
#     break
# time.sleep(int(Delais_Mesure))


# Déclaration des fonctions permettant d'écrire les données dans les fichiers texte ( METTRE UNE BASE DE DONNÉE ET CHANGER MÉTHODE ÉCRITURE)
def Capteurs_lvl_BAC_Culture():
    global lvl_bac_culture
    lvl_bac_culture = int(random.randint(0, 100))
    data_lvl = open("bac_culture", "w")
    data_lvl.write(str(lvl_bac_culture))
    data_lvl.close()
    data_lvl = open("bac_culture", "r")
    data = int(data_lvl.read())
    return data
    data_lvl.close()
print( "Niv bac culture                  = ",Capteurs_lvl_BAC_Culture(),"%")

def Capteurs_lvl_BAC_EAU():
    global lvl_bac_eau
    lvl_bac_eau = int(random.randint(0, 100))
    data_lvl = open("bac_eau", "w")
    data_lvl.write(str(lvl_bac_eau))
    data_lvl.close()
    data_lvl = open("bac_eau", "r")
    data = int(data_lvl.read())
    return data
    data_lvl.close()
print( "Niv bac eau                      = ",Capteurs_lvl_BAC_EAU(),"%")

def Capteurs_lvl_BAC_engrais():
    global lvl_bac_engrais
    lvl_bac_engrais = int(random.randint(0, 100))
    data_lvl = open("bac_engrais", "w")
    data_lvl.write(str(lvl_bac_engrais))
    data_lvl.close()
    data_lvl = open("bac_engrais", "r")
    data = int(data_lvl.read())
    return data
    data_lvl.close()
print( "Niv bac engrais                  = ",Capteurs_lvl_BAC_engrais(),"%")

def Capteurs_Humidité():
    global Humidity
    Humidity = int(random.randint(0, 100))
    data_lvl = open("Hydro", "w")
    data_lvl.write(str(Humidity))
    data_lvl.close()
    data_lvl = open("Hydro", "r")
    data = int(data_lvl.read())
    return data
    data_lvl.close()
print( "Niv humidité                     = ",Capteurs_Humidité(), "%")

def Capteurs_PH():
    global Ph
    Ph = float(random.uniform(0, 14))
    data_lvl = open("ph", "w")
    data_lvl.write(str(Ph))
    data_lvl.close()
    data_lvl = open("ph", "r")
    data = float(data_lvl.read())
    return data
    data_lvl.close()
print( "Niv de pH                        = ","%.2f" % Capteurs_PH(), "pH")

def Capteurs_EC():
    global Ec
    Ec = float(random.uniform(0, 3))
    data_lvl = open("ec", "w")
    data_lvl.write(str(Ec))
    data_lvl.close()
    data_lvl = open("ec", "r")
    data = float(data_lvl.read())
    return data
    data_lvl.close()
print( "Niv d'EC                         = ","%.2f" % Capteurs_EC(), "EC")

def Capteurs_Température():
    global Température
    Température = float(random.uniform(5, 50))
    data_lvl = open("température", "w")
    data_lvl.write(str(Température))
    data_lvl.close()
    data_lvl = open("température", "r")
    data = float(data_lvl.read())
    return data
    data_lvl.close()
print( "Température dans la pièce        = ","%.2f" % Capteurs_Température(), "C°")

def Capteurs_LUX():
    global LUX
    LUX = int(random.randint(300, 50000))
    data_lvl = open("lux", "w")
    data_lvl.write(str(LUX))
    data_lvl.close()
    data_lvl = open("lux", "r")
    data = int(data_lvl.read())
    return data
    data_lvl.close()
print( "Niv luminosité                   = ",Capteurs_LUX(), "lux")


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


while i == 1:


    # Permet d'écrire dans le fichier DONNE_CAPTEURS.log
    Output_DONNE_CAPTEURS_LOG()

    time.sleep(int(Delais_Mesure))
    Capteurs_EC()
    Capteurs_PH()
    Capteurs_LUX()
    Capteurs_Humidité()
    Capteurs_Température()
    Capteurs_lvl_BAC_EAU()
    Capteurs_lvl_BAC_engrais()
    Capteurs_lvl_BAC_Culture()

    with open ('DONNEE_CAPTEURS.log', 'r') as log:
        data_leng = (log.read())
        data_leng_1 = data_leng.split('\n')
        limite_backup_log = len(data_leng_1)
        print("\n","Nombre de ligne présent dans le fichier de log       :",limite_backup_log,"\n","\n")
        if limite_backup_log >= 50000:
            os.system("tar -czf DONNEE_CAPTEURS.log.$(date +%d-%m-%Y-%Hh%M) DONNEE_CAPTEURS.log && mv DONNEE_CAPTEURS.log.* ./archive_donnee_capteurs/ && rm -f DONNEE_CAPTEURS.log")
            limite_backup_log = 0
            print("Le fichier de log ayant atteint sa taille limite, une archive de celui-ci à étais générer dans le dossier archive_donnee_capteurs ")
            time.sleep(int(Delais_Mesure))
            os.system("touch DONNEE_CAPTEURS.log")
            Output_DONNE_CAPTEURS_LOG()
            print(limite_backup_log)
        else:
            # Permet d'afficher dans le terminal les valeurs générées par le script
            print( "Niv de pH                        = ","%.2f" % Capteurs_PH(), "pH")
            print( "Niv d'EC                         = ","%.2f" % Capteurs_EC(), "EC")
            print( "Niv luminosité                   = ",Capteurs_LUX(), "lux")
            print( "Niv humidité                     = ",Capteurs_Humidité(), "%")
            print( "Température dans la pièce        = ","%.2f" % Capteurs_Température(), "C°")
            print( "Niv bac eau                      = ",Capteurs_lvl_BAC_EAU(),"%")
            print( "Niv bac engrais                  = ",Capteurs_lvl_BAC_engrais(),"%")
            print( "Niv bac culture                  = ",Capteurs_lvl_BAC_Culture(),"%")
            
# idée optimisation : Utiliser 2 listes (int, float) pour réduire le nombre de ligne de code.
# Copyright craficafia.lsboagrs34gd.onion
# Crosse platforme euh non, linux :)
