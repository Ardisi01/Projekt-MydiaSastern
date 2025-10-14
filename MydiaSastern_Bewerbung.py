import numpy as np
import sys
import time
import os

# Hier ist die Ablage für alle Eigenschaften und Attribute, die der Charakter hochleveln kann.
Rot = "\033[31m"
Blau = "\033[34m"
Reset = "\033[0m"
Level = 0
Leben = 100
Rank = "arbeitslos"
Ausbruch = False #brauchen eine andere Lösung, ist zu unübersichtlich


                      # Die ersten vier Zeilen sind die Gaunerfähigkeiten
Attribute = np.array([["Taschendiebstahl", 0],
                      ["Schlösser knacken", 0],
                      ["Schleichen", 0],
                      ["Redekunst", 0],
                      # Die nächsten vier Zeilen sind die Jägerfähigkeiten
                      ["Stärke", 0],
                      ["Einschüchtern", 0],
                      ["Geschicklichkeit", 0],
                      ["Wahrnehmung", 0],
                      ])




#Hier werden alle Definitionen deklariert

def clean_print(text): #clean("dein Text") ruft die DEF auf // Clean ("dein Text") lässt den Text fließend darstellen
    for c in text:
        sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.045)

def clear_screen(): #clean_screen() löscht die vorherigen Eingaben im Terminal
    os.system("cls")

# Hier sind einige Standartaktionen, die man relativ am Anfang erlernt (Sie sind entweder 0 oder 1. Je nachdem, ob man sie erlernt hat)

# Die Schleifen sind der Rahmen des Spiels, da immer wenn der Spieler etwas eingibt, für das wir keine Option haben, die Entscheidung wiederholt werden muss. Durch die Schleifen passiert das automatisch, bis der Spieler eine passende Antwort gibt und es weitergeht
while Level < 10:
    while Level < 1:
        clear_screen()
        clean_print("Es ist stockdunkel. Du siehst noch nicht einmal deine eigene Hand vor Augen.Doch da!\nDu siehst einen lackernden Lichtschein. Er scheint von einer defekten LED zu kommen, die an der Wand neben dir befestigt ist.\nJetzt siehst du auch endlich die Kiste mit der Aufschrift 'IPhone-Lieferung', wegen der du hier eingebrochen bist.\nDu kannst nun entweder verschwinden, um auf keinen Fall erwischt zu werden oder du ziehst die Sache durch und verdienst dir dein 'ehrliches Geld'. Gebe nun '1' oder '2' ein.")
        while True:
            if Ausbruch == True:
                break

            Desicion_1 = input("")
            if Desicion_1 == "1":
                clean_print("Du drehst dich langsam um und machst dich auf den Weg zu Ausgang.\nDu fragst dich, warum du eigentlich hier eingebrochen bist.\nDu hast nun die Tür erreicht und versuchst durch das Schlüsselloch zu schauen, doch du kannst Nichts erkennen.\nDu nimmst all deinen Mut zusammen und öffnest die Tür. Da hörst du eine Stimme die ruft: 'Da ist jemand im Lager! Ein Dieb, haltet ihn!'.\nDu schlägst die Tür noch im selben Moment zu, drehst dich um und rennst los.\nDank der LED kannst du die Umrisse der Kisten erkennen und siehst nun auch eine Klappe im Boden.Du versuchts die Klappe zu öffnen, doch sie ist verschlossen.\nDu hast nun mehrere Möglichkeiten: Entweder du schaust dich um [1], oder du nimmst zuerst die Kiste, die nun einladend vor dir steht [2].\n\n-->")
                while Ausbruch == False:
                    Desicion_2 = input("")
                    if Desicion_2 == "1":
                        clean_print("Du siehst einen verbogenen und verosteten Nagel aus der Wand der Kiste herausragen. Du ziehst mit all deiner Kraft und schaffst es schließlich, ihn herauszuziehen.\nNun steckst du den Nagel in das Schloss, probierst etwas rum und evoila: Die Klappe lässt sich nun öffnen.\nDu schaust dich erneut um, überlegst kurz, greifst dir schließlich die Kiste und steigst mit ihr hinab: Erneut in die Dunkelheit")
                        Ausbruch = True
                        break
                    elif Desicion_2 == "2":
                        clean_print("Du greifst dir zuerst die Kiste und willst gerade weiter gehen, doch da fällt dir etwas Glizernes auf:\nNeben der Klappe liegt etwas auf dem Boden.\nDu spürst, wie die Gier in dir aufsteigt und und beugst dich ohne zu zögern herunter\num es mit der Hand zu greifen, die nun nicht mehr die Kiste trägt.\nNun siehst du, dass der Gegenstand nur eine wertlose Kupfermünze war.\nNoch im gleichen Moment schwächelt deine andere Hand und die Kiste ruscht dir aus der Hand und fällt geradewegs auf die Klappe.\nMit einem lauten Knacken kommt die Kiste auf. Du hebst sie an und siehst, dass das Schloss durch sie zerstört wurde.\nDu atmest erleichtert auf und steigst mit der Kiste hinab: Erneut in die Dunkelheit.")
                        Ausbruch = True
                        break
                    else:
                        clean_print("Diese Entscheidung kannst du leider nicht treffen. Bitte versuche es erneut.")


            elif Desicion_1 == "2":
                clean_print("Du greifst dir die Kiste, drehst dich langsam um und machst dich auf den Weg zu Ausgang.\nDu hast nun die Tür erreicht und versuchst durch das Schlüsselloch zu schauen, doch du kannst Nichts erkennen.\nDu nimmst all deinen Mut zusammen und öffnest die Tür. Da hörst du eine Stimme die ruft: 'Da ist jemand im Lager! Ein Dieb, haltet ihn!'.\nDu schlägst die Tür noch im selben Moment zu, drehst dich um und rennst los.\nDank der LED kannst du die Umrisse der Kisten erkennen und siehst nun auch eine Klappe im Boden.")
                clean_print("Du drehst dich erneut um um zu sehen, ob dir Jemand gefolgt ist.\nDoch da ruscht dir die Kiste aus den Händen und fällt geradewegs auf die Klappe.\nMit einem lauten Knacken kommt die Kiste auf. Du hebst sie an und siehst, dass das Schloss durch sie zerstört wurde.\nDu atmest erleichtert auf und steigst mit der Kiste hinab: Erneut in die Dunkelheit.")
                break
            else:
                clean_print("Diese Entscheidung kannst du leider nicht treffen. Bitte versuche es erneut.")
        # An diesem Punkt kannst du die Story nun weiterführen. Das Level muss nach der ersten Serquenz erhöt werden, damit die While-Schleife endet und die nächste Sewuenz beginnt.
        Level += 1

    while Level < 2:
        clear_screen()
        clean_print("Erneut ist es stockdunkel - ein lautes Tropfen füllt deine Ohren mit Lärm."+Rot+"\n\n'Oh Mann, wie konnte mir das passieren. Es scheint, als hätte Jemand von mir Besitz ergriffen..\nIch wollte doch nur kurz im Lager was holen und da habe ich die Kiste gesehen - Ich konnte nicht anders..'"+Reset+"Innerlich weißt du, was dein wahrer Charakter ist, jedoch nimmst du dir mit dem Satz die Schuld für dein derzeitiges Dilemma.\n Diese Tatsache macht dich derartig wütend, dass du jetzt zwischen zwei Optionen stehst: Entweder du trittst mit voller Wucht\ngegen einen nahestehenden Eimer, um deine Wut rauszulassen[1], oder du schließt die Augen und machst eine Atemübung[2].\n\n-->")     
        while True:
            Wut_Verarbeitung = input()
            if  Wut_Verarbeitung == "1":
                    clean_print("Von Wut getrieben trittst du mit voller Wucht gegen den nahestehenden Eimer, in Hoffnung, dass alles besser wi-:\n\n"+Rot+"'AAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHh!!!!!'"+Reset+"\n\nNur leider wusstest du nicht,\n dass er voll mit Steinen gefüllt war du dir gerade dein Fuß gebrochen hast..weil du noch mitten im Gefecht bist, stehst du irgendwie auf\n und suchst, von Schmerzen begleitet, nach einem Klebeband. Damit willst du die Handys um deinen Körper herum kleben,\n um sie ungesehen hinaus zu tragen.")
            
            elif Wut_Verarbeitung == "2":
                clean_print("Du bewahrst Ruhe und weißt, dass Kontrolle die einzig vernünftige Lösung ist. Also schließt du die Augen, um dich zu entspannen. \nAls du die Augen erneut öffnest, wirst du bleich im Gesicht. Der Filialleiter persönlich steht vor dir.. \n\n"+Blau+'Darf ich fragen, was Sie hier genau machen?'+Reset+"\n\nEs hätte nicht schlimmer kommen können, dieser geldschmierige Endboss steht persönlich vor dir, denkst du dir im Inneren.\n Was tust du jetzt? Sagst du ihm die Wahrheit[1] oder erzählst du ihm, dass du dich verlaufen hast[2]?")
                while True:
                    Chef_Begegnung = input()
                    if Chef_Begegnung == "1":
                        clean_print(Rot+"'Ich ehm ich habe versucht diese Box zu klauen..'"+Reset+"Er schaut dich erst mit einem merkwürdigen Blick an \nund sagt schließlich:"+Blau+"\n\n' Hahahahahahahha Der war gut, wer würde schon ins Unterlager gehen, um etwas zu stehlen? Weißt du, du hast meinen Tag gerettet,\n meine Frau sowie Kinder nerven mich gerade total, weshalb ich mich zur Arbeit flüchte.'"+Reset+"\n\nHilfee, wo bin ich gerade gelandet, denkst du dir. Ich wollte doch gerade etwas stehlen und jetzt kommt er mir mit seinem Zeugs. \nBevor er jetzt seine Geschichten erzählt, musst du da raus und sagst deshalb eines dieser Dinge:\n Entweder, dass du wieder hoch müsstest, weil du viel zu tun hast[1], oder du sagst ihm, du hast dich hier versteckt,\nweil du krank seiest[2]. Entscheide weise:-->")
                        while True:
                            Chefs_Gelaber_entkommen = input()
                            if Chefs_Gelaber_entkommen == "1":
                                clean_print ("")

                            elif Chefs_Gelaber_entkommen == "2":
                                clean_print ("")
                            
                    elif Chef_Begegnung == "2":
                         clean_print("") 

            else:
                clean_print("Diese Entscheidung kannst du leider nicht treffen. Bitte versuche es erneut.")    