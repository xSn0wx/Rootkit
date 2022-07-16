from banner import banner
import sys

banner()
print()

def choix(int_intro):
    if int_intro == 1:
        from Outils.backdoor_serveur import server
        server()
    elif int_intro == 2:
        from Outils.keylogger import keylogger
        keylogger()
    elif int_intro == 3:
        from Outils.scan_network import scan
        scan()
    elif int_intro == 4:
        from Outils.ddos import ddos
        ddos()
    else:
        print("Merci de choisir entre 1 et 4 !!!")
        print()
        choix()

# Installation des dependences Windows/Linux

while True:
    print()
    print("""
    Que souhaitez vous faire ?
    1) Reverse shell
    2) Keylogger
    3) Scan Network
    4) DDOS
    5) Exit
    """)
    print()
    intro = input("Votre choix : ")
    try:
        int_intro = int(intro)
        if int_intro == 5:
            break
        choix(int_intro)
        continue
    except:
        print("ERREUR: Votre choix doit etre un chiffre ")
        continue
    else:
        break

print()
print("Revenez quand vous voulez :)")

