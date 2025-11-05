# Hier werden die Libraries importiert

import numpy as np
import sys
import time
import os
import random


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Hier werden alle Variablen deklariert

Rot = "\033[31m"
Blau = "\033[34m"
Reset = "\033[0m" # Setzt Farbe wieder auf weiß
Warteschleife = "<---Eine Stunde später--->"
Social_Credits = 20 # Aktionen haben Einfluss -> Credits gewähren dir Erlaubnis oder Ausnahmeregeln bei guter/schlechter Punktzahl -> 20C = Start
Level = 0
Leben = 100
Rank = "Sklavenarbeiter"
Fußbruch = 35
Diebstahl_Erfolg = 0
aktueller_Gegenstand = None
                      # Die ersten vier Zeilen sind die Gaunerfähigkeiten
Attribute = np.array([["Taschendiebstahl", 1],#1/10
                      ["Schlösser knacken", 1],
                      ["Schleichen", 1],
                      ["Redekunst", 1],
                      # Die nächsten vier Zeilen sind die Jägerfähigkeiten
                      ["Stärke", 1],
                      ["Einschüchtern", 1],
                      ["Geschicklichkeit", 1],
                      ["Wahrnehmung", 1],
                      ],dtype=object)#Von ChatGPT, Funktion wenig bekannt, hier erlaubt die Liste jeden Datentyp und erzwingt die nicht zu String, damit die Zahlen darin addiert werden können

#####Lösch: wir könnten die Gegenstände in Kategorien tun, und wenn es bsp. Kategorie Essen ist, kann man Leben bekommen
Mitarbeiter_Inventar =["Smartphone","Portmonaiee","Schreibblock","Taschentücher","50€","Apfel","Messer","Brotdose","Kopfhörer","Uhr"]
Filialleiter_Inventar =["Smartphone","Büroschlüssel","Portmonaiee","Roter Schlüssel","300€"]
Spieler_Inventar = ["Smartphone","Cuttermesser"]
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Hier werden alle Definitionen deklariert

def clean_print(text): # Ruft die DEF auf // Clean ("dein Text") lässt den Text fließend darstellen
    for c in text:
        sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.00045)

def Zeit_vergangen(text): # Fließtext langsamer als clean_print
    for c in text:
        sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.8)

def clear_screen(): # Löscht die vorherigen Eingaben im Terminal
    os.system("cls")

def Räuberinstinkt(Tascheninhalt): # Was der Tascheninhalt ist, definieren wir, wenn wir die Funktion aufrufen
    global Diebstahl_Erfolg 
    global Mitarbeiter_Inventar
    global aktueller_Gegenstand

    if Attribute[0, 1] == 1 or Attribute[0,1] == 2:
        Diebstahl_Erfolg = random.choice([1,1,0,0,0,0,0,0,0,0])
        if Diebstahl_Erfolg == 1:
            aktueller_Gegenstand = random.choice(Mitarbeiter_Inventar)
            if Attribute[0, 1] == 1:# Falls Attribut Taschendiebstahl = 1
                Attribute[0,1] = Attribute[0,1] + 1                        # Taschendiebstahl + 1 auf das nächste Level
            elif Attribute[0,1] == 2:# Falls Attribut Taschendiebstahl = 2 usw.
                Attribute[0,1] = Attribute[0,1] + 1
            print("Dein Glück segnet dich mit einem Level Up im Taschendiebskill! Glückwunsch!!")

    elif Attribute[0, 1] == 3 or Attribute[0,1] == 4:
        Diebstahl_Erfolg = random.choice([1,1,1,1,0,0,0,0,0,0])
        if Diebstahl_Erfolg == 1:
            aktueller_Gegenstand = random.choice(Mitarbeiter_Inventar)
            if Attribute[0, 1] == 3:
                Attribute[0,1] = Attribute[0,1] + 1
            elif Attribute[0,1] == 4:
                Attribute[0,1] = Attribute[0,1] + 1
            print("Dein Glück segnet dich mit einem Level Up im Taschendiebskill! Glückwunsch!!")

    elif Attribute[0, 1] == 5 or Attribute[0,1] == 6:
        Diebstahl_Erfolg = random.choice([1,1,1,1,1,1,0,0,0,0])
        if Diebstahl_Erfolg == 1:
            aktueller_Gegenstand = random.choice(Mitarbeiter_Inventar)
            if Attribute[0, 1] == 5:
                Attribute[0,1] = Attribute[0,1] + 1
            elif Attribute[0,1] == 6:
                Attribute[0,1] = Attribute[0,1] + 1
            print("Dein Glück segnet dich mit einem Level Up im Taschendiebskill! Glückwunsch!!")

    elif Attribute[0, 1] == 7 or Attribute[0,1] ==  8 or Attribute[0,1] ==  9:
        Diebstahl_Erfolg = random.choice([1,1,1,1,1,1,1,1,0,0])
        if Diebstahl_Erfolg == 1:
            aktueller_Gegenstand = random.choice(Mitarbeiter_Inventar)
            if Attribute[0, 1] == 7:
                Attribute[0,1] = Attribute[0,1] + 1
            elif Attribute[0,1] == 8:
                Attribute[0,1] = Attribute[0,1] + 1
            elif Attribute[0,1] == 9:
                Attribute[0,1] = Attribute[0,1] + 1
            print("Dein Glück segnet dich mit einem Level Up im Taschendiebskill! Glückwunsch!!")

    elif int(Attribute[0, 1]) == 10:
        Diebstahl_Erfolg = 1
        aktueller_Gegenstand = random.choice(Mitarbeiter_Inventar)
    
    # Was genau passiert, wenn wir (nicht) erfolgreich sind, ist durch die Story unterschiedlich und schreiben wir auserhalb der Funtion, daher reicht hier ein kurzes Feedback aus
    if Diebstahl_Erfolg == 1:
        print("Der Diebstahl war erfolgreich! Du hast Folgendes erbeutet:",Rot+"", aktueller_Gegenstand,""+Reset)
    elif Diebstahl_Erfolg == 0:
        print("Du hattest keinen Erfolg und wurdest erwischt!") ######Lösch: Erwischen wird auch gewürfelt, man kann es auch so machen, dass auch Mal nichts passiert


def get_choice(option_number): # Das ist die Funktion für alle Entscheidungen. Die Variable gibt die Anzahl der Optionen an
    global X # X ist auch die Anzahl der Optionen. Im Gegensatz zu option_number können wir X jetzt aber global verwenden. Es wirkt zwar unübersichlich, aber verschafft uns einen riesen Vorteil
    while True:
        if option_number == 2: # Für zwei Optionen
            choice = input("\nGib '1' oder '2' ein.-->")
            if choice in ['1', '2']: # Die möglichen Eingaben
                X = int(choice)
                return int(choice) # While-Schleife bricht
            else: # Falls keine der Optionen gewählt wurde, wird die Entscheidung einfach wiederholt
                clean_print(random.choice(["So kommst du hier nicht weiter." , "Probier es anderweitig nochmal" , "Das ist nicht das, wonach du gefragt wurdest."]))
        elif option_number == 3: # Für drei Optionen
            choice = input("\nGib '1', '2' oder '3' ein.-->")
            if choice in ['1', '2', '3']: 
                X = int(choice)
                return int(choice)
            else:
                clean_print(random.choice(["So kommst du hier nicht weiter." , "Probier es anderweitig nochmal" , "Das ist nicht das, wonach du gefragt wurdest."]))
        elif option_number == 4: # Für vier Optionen
            choice = input("\nGib '1', '2', '3' oder '4' ein.-->")
            if choice in ['1', '2', '3', '4']:
                X = int(choice)
                return int(choice)
            else:
                clean_print(random.choice(["So kommst du hier nicht weiter." , "Probier es anderweitig nochmal" , "Das ist nicht das, wonach du gefragt wurdest."]))


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Hier werden wir alle Level, also das eigentliche Spielgeschehen coden

# Level: 0 (Spieler im Hauptlager)
while Level == 0:
    clear_screen()
    clean_print("Es ist stockdunkel. Du erkennst nicht einmal deine eigene Hand. Doch plötzlich – ein flackernder Lichtschein! \nEine defekte LED an der Wand blitzt auf und wirft kaltes Licht in den Raum.Jetzt siehst du sie – \ndie Kiste mit der Aufschrift „iPhone-Lieferung“. Der Grund, warum du hier bist. Dein Herz schlägt schneller. \nNiemand darf dich sehen. Wirst du verschwinden, bevor es zu spät ist – oder die Sache durchziehen und dir dein \n„ehrliches Geld“ verdienen?\n")
    print(get_choice(2))
    if X == 1: 
        clean_print("Du drehst dich langsam um und schleichst Richtung Ausgang. Warum hast du das überhaupt getan? Die Frage bleibt hängen, unbeantwortet. \nAn der Tür hältst du, legst dein Auge ans Schlüsselloch — doch dahinter ist nur schwarz. \nMit einem kurzen Ruck öffnest du die Tür. \nEine Stimme reißt die Stille auf: „Da ist jemand im Lager! Ein Dieb, haltet ihn!“ Die Tür schlägt zu. \nDu wirfst dich herum und rennst. Das flackernde LED-Licht zeichnet die Umrisse der Kisten; \nDein Blick fällt auf eine verschlossene Klappe im Boden.Du versuchst, sie zu öffnen — kein Glück. \nJetzt hast du die Wahl: Schau dich um — oder schnapp dir zuerst die einladende Kiste.\n\n")
        print(get_choice(2))
        if X == 1:
            clean_print("Ein verbogener, verrosteter Nagel ragt aus der Wand der Kiste — ein kalter, rostiger Finger. Du packst zu, ziehst mit aller Kraft; \ner gibt nach und kommt knirschend frei. Behutsam steckst du den Nagel ins Schloss, tastest, drehst — und siehe da: \nein leises Klicken. Die Klappe öffnet sich. Noch einmal prüfst du die Umgebung, nickst dir selbst zu, \ngreifst die Kiste und kletterst hinab — wieder in die Dunkelheit.")
            Warte = input("Drücke eine beliebige Taste, um fortzufahren.")
        elif X == 2:
            clean_print("Du hältst die Kiste fest im Arm, bereit weiterzugehen — doch dann fängt dein Blick etwas Glitzerndes am Boden. \nNeben der Klappe schimmert es schwach im Licht der flackernden LED. Gier kriecht in dir hoch. \nDu hältst die Kiste nun nur noch mit einer Hand, beugst dich hinunter und greifst nach dem funkelnden Etwas. \n\nEine Münze. Kupfer. Wertlos. \n\nIn diesem Moment gibt deine andere Hand nach — \ndie Kiste rutscht dir aus den Fingern und kracht auf die Klappe. Ein splitterndes Geräusch hallt durch den Raum. \nDas Schloss ist zerstört. Du starrst kurz fassungslos auf die aufgebrochene Öffnung, \natmest erleichtert auf und steigst mit der Kiste hinab — wieder in die Dunkelheit.")
    elif X == 2:
        clean_print("Du greifst die Kiste, drehst dich langsam um und schleichst zum Ausgang. An der Tür hältst du inne, \nbeugst dich vor und blickst durch das Schlüsselloch — nichts. Nur Schwärze. Du atmest tief ein, \nsammelst Mut und drückst die Klinke hinunter. „Da ist jemand im Lager! Ein Dieb, haltet ihn!“ \nDie Worte schneiden wie ein Messer durch die Stille. Du schlägst die Tür zu, drehst dich um und rennst. \nDas flackernde Licht der LED zeigt dir flüchtig den Weg — Umrisse von Kisten, Schatten an der Wand — und da: eine Klappe im Boden. \nDu drehst dich hastig um, um zu sehen, ob dir jemand folgt. In diesem Moment rutscht dir die Kiste aus den Händen und \nkracht auf die Klappe. Ein lautes Knacken hallt durch den Raum. Du hebst die Kiste an — das Schloss ist zerstört. \nErleichtert atmest du aus und steigst mit der Kiste hinab — wieder in die Dunkelheit.")
    Level += 1


# Level: 1 (Spieler im Unterlager)
while Level == 1:
    clear_screen()
    clean_print("Erneut ist es stockdunkel. Ein lautes Tropfen füllt deine Ohren, als würde die Stille selbst gegen dich arbeiten."+Rot+" \n\n„Oh Mann, wie konnte mir das passieren? Es ist, als hätte mich etwas Besitz ergriffen… Ich wollte doch nur kurz eine Kiste holen — \nund dann konnte ich nicht anders.“"+Reset+" Du spürst, wie Schuld und Wut sich in dir vermischen. \nInnerlich kennst du die Wahrheit über deinen Charakter, doch mit diesen Worten versuchst du, die Verantwortung abzuschieben. \nDie Erkenntnis brennt wie Feuer in dir, macht dich zornig und ungestüm. Die Wut fordert eine Reaktion. \nDu stehst nun vor einer Wahl: Trittst du mit voller Wucht gegen den Eimer, um die Wut hinauszulassen,\noder schließt du die Augen und machst eine Atemübung, um dich zu beruhigen?\n")     
    print(get_choice(2))
    if X == 1: # Wut-Option
        Leben -= Fußbruch # Spieler verletzt sich, erleidet Schaden
        clean_print("Von Wut getrieben trittst du mit voller Wucht gegen den nahestehenden Eimer — in der Hoffnung, dass danach alles besser wi— \n\n"+Rot+"'AAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHH!'"+Reset+"\n\nDer Schmerz fährt wie ein Blitz durch dein Bein. Du hattest nicht gewusst, dass der Eimer bis obenhin mit Steinen gefüllt war — \nein scharfes Knacken, dann brennt dein Fuß; irgendwo in dir ahnst du, dass etwas gebrochen ist. \n\nDu hast nur noch "+str(Leben)+" Leben. Deine Entscheidungen haben Folgen.\n\nTrotzdem rollst du, gepeinigt, auf die Knie, kämpfst dich auf die Füße und tastest, von Schmerz begleitet, nach Klebeband.\nMit zitternden Händen willst du die Handys an deinem Körper fixieren — ungesehen, verzweifelt — und sie so hinausschmuggeln.")
        get_choice(4)
        if X == 1:
            Räuberinstinkt(Tascheninhalt=aktueller_Gegenstand) # Hier hattest du zuletzt aufgehört
            Spieler_Inventar.append(aktueller_Gegenstand)
            print("Das ist dein aktualisiertes Inventar:\n",Spieler_Inventar)
            print("\n\n",Attribute,"\n\n")######Lösch: zeigt es nur zur Veranschaulichung

    elif X == 2: # Selbstkontrolle-Option
        clean_print("Du bewahrst Ruhe und weißt, dass Kontrolle die einzig vernünftige Lösung ist. Also schließt du die Augen, um dich zu entspannen. \nAls du die Augen erneut öffnest, wirst du bleich im Gesicht. Der Filialleiter persönlich steht vor dir.. \n\n"+Blau+'Darf ich fragen, was Sie hier genau machen?'+Reset+"\n\nEs hätte nicht schlimmer kommen können, dieser geldschmierige Endboss steht persönlich vor dir, denkst du dir im Inneren.\nWas tust du jetzt? Sagst du ihm die Wahrheit - oder erzählst du ihm, dass du dich verlaufen hast?\n")
        print(get_choice(2))
        if X == 1: # Diebstahlbeichte-Option
            clean_print(Rot+"„Ich… ehm… ich habe versucht, diese Box zu klauen…“"+Reset+" Er schaut dich einen Moment lang mit einem merkwürdigen Blick an — \nals würde er abwägen, ob du ein Witz bist oder Gefahr. Dann bricht er in Gelächter aus und sagt schließlich: "+Blau+"\n\n„Hahahahahahaha — der war gut! Wer würde schon ins Unterlager gehen, um etwas zu stehlen? Weißt du, du hast meinen Tag gerettet. \nMeine Frau und die Kinder nerven mich gerade ohne Ende, da flüchte ich mich auf die Arbeit.“"+Reset+"\n\nHilfeflos denkst du: Wo bin ich hier gelandet? Du wolltest stehlen, nicht seine Lebensgeschichte hören. \nBevor seine Erzählung Fahrt aufnimmt, musst du reagieren. Du sagst entweder, dass du wieder hoch musst, denn du hättest viel zu tun — oder du behauptest, du hättest dich hier versteckt, weil du krank seist -\noder Ihm direkt sagen, dass du kein Bock hast, ihm weiter zuzuhören, du müsstest arbeiten gehen (Nicht zu empfehlen)\nEntscheide weise.\n")
            print(get_choice(3))
            if X == 1: # Zu beschäftigt für eine Unterhaltung-Option
                clean_print(Rot + "'Schauen Sie, ich müsste eigentlich noch weiterarbeiten, auch wenn ich am liebsten hier unten bleiben würde.'\n\n" + Reset + Blau + "'Das weiß ich doch. Sie sind ein zuverlässiger, vertrauenswürdiger Mitarbeiter. Ach, und bevor Sie es vergessen: \nSie haben die Kiste hier liegen lassen. Bringen Sie sie bitte nach oben, ja?'" + Reset + "\n\nDu stehst da, erstarrt, während die Realität langsam einsickert: Der Filialleiter gibt dir persönlich den Auftrag, \ndie Kiste nach oben zu bringen. Dieser Tag scheint von einem merkwürdigen Schicksal geprägt zu sein — \nein Tag, an dem alles möglich ist.")
                # Fortsetzung/////////////////////////////////
            elif X == 2: # Krank-Option
                clean_print ("")# Fortsetzung///////////////////////////////////
            elif X == 3: # Respektlose-Option
                clean_print(Rot+"'Hör Mal Opa, pass auf, dieses Zeug interessiert mich nicht. Klär deine Sachen allein und nerv nicht mich damit.'"+Reset+"Das hättest du gerne gesagt, stattdessen habt ihr euch hingesetzt und er hat dir seine von seiner ganzen Geschichte erzählt.")
                Weiter = input("\n\nDrücke eine beliebige Taste, um fortzufahren..")
                clear_screen()
                print("\n" * 15 + " " * 60, end="")
                Zeit_vergangen(Warteschleife)#Erstellt einen Loading Screen
                clear_screen()
                clean_print("") # Fortsetzung/////////////////////////////
        elif X == 2: # Verlaufen-Option
            clean_print("") # Fortsetzung//////////////////////////
    Level += 1


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#                                                  ******Unterhaltung******

# 04.11:Bro wieder nicht an der Story gearbeitet......Raubmechanismus ist wichtiger :(
# Ich glaube aber, dass wir die Story jetzt langsam voran bringen können, wo wir jetzt so viel um die Story gebaut haben.