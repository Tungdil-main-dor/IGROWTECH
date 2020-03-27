from RGN_CAPTEURS import *

os.chdir("/home/mint-on-fire/Bureau/Projet_BTS/DONNEE_CAPTEURS")


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

Capteurs_EC()