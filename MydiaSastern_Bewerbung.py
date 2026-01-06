# Hier werden die Libraries importiert

import numpy as np
import sys
import time
import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Hier werden alle Variablen deklariert
    # Hier werden die Farben deklariert  
orange = "\033[33m"
Gold = "\033[93m"
Grün = "\033[32m"
Rot = "\033[31m"
Blau = "\033[34m"
Reset = "\033[0m" # Setzt Farbe wieder auf weiß

    # Hier werden alle weiteren Variablen Deklariert
Warteschleife = "\n<---Eine Stunde später--->"
Social_Credits = 20 # Aktionen haben Einfluss -> Credits gewähren dir Erlaubnis oder Ausnahmeregeln bei guter/schlechter Punktzahl -> 20C = Start
Level = 0
Leben = 100
Rank = "Sklavenarbeiter"
Fußbruch = 35
Raub_counter = 0
Raublimit = None
Raubversuch = None
Knock_Out = False
Spieler_Inventar = ["Smartphone","Cuttermesser"]


                      # Die ersten vier Zeilen sind die Gaunerfähigkeiten
Attribute = np.array([
                    ["Diebstahl", 1], # 1/10
                    ["Schlösser knacken", 1],
                    ["Schleichen", 1],
                    ["Redekunst", 1],
                    # Die nächsten vier Zeilen sind die Jägerfähigkeiten
                    ["Stärke", 1],
                    ["Einschüchtern", 1],
                    ["Geschicklichkeit", 1],
                    ["Wahrnehmung", 1],
                    ], dtype=object) # Hier erlaubt die Liste jeden Datentyp und erzwingt die nicht zu String, damit die Zahlen darin addiert werden können
                                            
#####Lösch: wir könnten die Gegenstände in Kategorien tun, und wenn es bsp. Kategorie Essen ist, kann man Leben bekommen
Mitarbeiter_Inventar = ["Smartphone","Portmonaiee","Schreibblock","Taschentücher","50€","Apfel","Messer","Brotdose","Kopfhörer","Uhr"]
Filialleiter_Inventar = ["Smartphone","Büroschlüssel","Portmonaiee","Roter Schlüssel","300€"]
Kiste_Inventar = ["Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", ]
Kundin_1_inventar = ["Handy", "Tablet", "Air Pods"]
Dealer_Inventar = ["Handy"]


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Hier werden alle Definitionen deklariert

def situation(Inventar, Skills): # Hiermit können wir uns jederzeit ohne Schreibarbeit die Attribute, das Inventar oder beides anzeigen lassen
    if Inventar == 1:
        print("Das ist dein aktualisiertes Inventar:\n",Spieler_Inventar)
    if Skills == 1:
        print("\n\n",Attribute,"\n\n")

def clean_print(text): # Ruft die DEF auf // Clean ("dein Text") lässt den Text fließend darstellen
    for c in text:
        sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.000006) #0000000000

def Zeit_vergangen(text): # Fließtext langsamer als clean_print
    for c in text:
        sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.8)
 
def clear_screen(): # Löscht die vorherigen Eingaben im Terminal
    os.system("cls")

def Diebstahl_Lvl_up():
    global Raub_counter # Ich habe die Raubcounter hier auch dazu gepackt; Spart Schreibarbeit
    Raub_counter += 1
    Lvl_up = random.choice([1,1,0,0,0,0,0,0,0,0]) 
    if Lvl_up == 1: 
        Attribute[0,1] += 1 
        print("Dein Glück segnet dich mit einem Level Up im Diebstahl! Glückwunsch!!")
        situation(0, 1)

def Diebstahl(Ziel_inventar): # Was Ziel ist, definieren wir, wenn wir die Funktion aufrufen und es sollte immer eine Liste sein (auch wenn es nur ein Gegenstand ist)
    global Diebstahl_Erfolg 
    global Beute
    Beute = None

    if Ziel_inventar == []:
        print("Hier ist Nichts mehr zu holen")
        return Ziel_inventar

    if 2 >= Attribute[0, 1] >= 1:
        Diebstahl_Erfolg = random.choice([1,1,0,0,0,0,0,0,0,0])

    elif 4 >= Attribute[0, 1] >= 3:
        Diebstahl_Erfolg = random.choice([1,1,1,1,0,0,0,0,0,0])

    elif 6 >= Attribute[0, 1] >= 5:
        Diebstahl_Erfolg = random.choice([1,1,1,1,1,1,0,0,0,0])

    elif 8 >= Attribute[0, 1] >= 7:
        Diebstahl_Erfolg = random.choice([1,1,1,1,1,1,1,1,0,0])

    elif Attribute[0, 1] == 10:
        Diebstahl_Erfolg = 1

    # Was genau passiert, wenn wir (nicht) erfolgreich sind, ist durch die Story unterschiedlich und schreiben wir auserhalb der Funtion, daher reicht hier ein kurzes Feedback aus
    if Diebstahl_Erfolg == 1:
        Beute = random.choice(Ziel_inventar)
        Spieler_Inventar.append(Beute)
        Ziel_inventar.remove(Beute)
        Diebstahl_Lvl_up()
        print("Der Diebstahl war erfolgreich! Du hast Folgendes erbeutet:",Rot+"", Beute,""+Reset)

    elif Diebstahl_Erfolg == 0:
        print("\nDu hattest leider keinen Erfolg!")

def Diebstahl_Schleife(Raubversuch, Raublimit, Ziel_inventar):
    while Raubversuch <= Raublimit:
        clean_print("Möchtest du es erneut versuchen?[1=Ja],[2=Nein]")
        get_choice(2)
        if X == 1:
            Diebstahl(Ziel_inventar)
            Raubversuch += 1
            if Diebstahl_Erfolg == 1:
                    situation(1, 0)
        elif X == 2:
            break

def Schleichen_Lvl_up():
    Lvl_up = random.choice([1,1,1,0,0,0,0,0,0,0]) 
    if Lvl_up == 1: 
        Attribute[2,1] += 1 
        print("Dein Glück segnet dich mit einem Level Up im Schleichen! Glückwunsch!!")
        situation(0, 1)

def Schleichen():
    global Schleichen_Erfolg

    if 1 <= Attribute[2,1] <= 3:
        Schleichen_Erfolg = random.choice([1,1,1,1,0,0,0,0,0,0])
    elif 4 <= Attribute[2,1] <= 6:
        Schleichen_Erfolg = random.choice([1,1,1,1,1,1,1,0,0,0])
    elif 7 <= Attribute[2,1] <= 9:
        Schleichen_Erfolg = random.choice([1,1,1,1,1,1,1,1,1,0])
    elif Attribute[2,1] == 10:
        Schleichen_Erfolg = 1

    if Schleichen_Erfolg == 1:
        print("Du bist erfolgreich geschlichen, Niemand hat dich gehört!")
        Schleichen_Lvl_up()

    elif Schleichen_Erfolg == 0:
        print("Oh nein! Du bist auf irgendetwas draufgetreten und hast ein Geräusch gemacht!")
    

def Geschicklichkeit_Lvl_up():
    Lvl_up = random.choice([1,1,1,0,0,0,0,0,0,0]) 
    if Lvl_up == 1: 
        Attribute[6,1] += 1 
        print("Dein Glück segnet dich mit einem Level Up in der Geschicklichkeit! Glückwunsch!!")
        situation(0, 1)

def geschickter_zug():
    global geschickt_Erfolg
    if 1 <= Attribute[6,1] <= 3:
        geschickt_Erfolg = random.choice([1,1,1,1,0,0,0,0,0,0])
    elif 4 <= Attribute[6,1] <= 6:
        geschickt_Erfolg = random.choice([1,1,1,1,1,1,1,0,0,0])
    elif 7 <= Attribute[6,1] <= 9:
        geschickt_Erfolg = random.choice([1,1,1,1,1,1,1,1,1,0])
    elif Attribute[6,1] == 10:
        geschickt_Erfolg = 1

    if geschickt_Erfolg == 1:
        print("Das war ein geschickter Zug und es ist Niemandem aufgefallen.")
        Geschicklichkeit_Lvl_up()

    elif geschickt_Erfolg == 0:
        print("Oh nein! Du warst nicht erfolgreich!!")
    

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


def visualize(bilddatei):
    plt.title("Schließe dieses Fenster, um die Story weiter zu lesen...")
    img = mpimg.imread(bilddatei)# Lädt Bild
    plt.imshow(img) # Zeigt Bild
    plt.axis('off') # Entfernt Koordinatensystem 
    plt.show()


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Story: Startsequenz

if Level == 0:

    clear_screen()
    clean_print("Es ist stockdunkel. Du erkennst nicht einmal deine eigene Hand. Doch plötzlich – ein flackernder Lichtschein! \nEine defekte LED an der Wand blitzt auf und wirft kaltes Licht in den Raum.Jetzt siehst du sie – \ndie Kiste mit der Aufschrift „iPhone-Lieferung“. Der Grund, warum du hier bist. Dein Herz schlägt schneller. \nNiemand darf dich sehen. Wirst du verschwinden, bevor es zu spät ist – oder die Sache durchziehen und dir dein \n„ehrliches Geld“ verdienen?\n")
    get_choice(2)
    if X == 1: 
        clean_print("Du drehst dich langsam um und schleichst Richtung Ausgang. Warum hast du das überhaupt getan? Die Frage bleibt hängen, unbeantwortet. \nAn der Tür hältst du, legst dein Auge ans Schlüsselloch — doch dahinter ist nur schwarz. \nMit einem kurzen Ruck öffnest du die Tür. \nEine Stimme reißt die Stille auf: „Da ist jemand im Lager! Ein Dieb, haltet ihn!“ Die Tür schlägt zu. \nDu wirfst dich herum und rennst. Das flackernde LED-Licht zeichnet die Umrisse der Kisten; \nDein Blick fällt auf eine verschlossene Klappe im Boden.Du versuchst, sie zu öffnen — kein Glück. \nJetzt hast du die Wahl: Schau dich um — oder schnapp dir zuerst die einladende Kiste.\n\n")
        get_choice(2)
        if X == 1:
            clean_print("Ein verbogener, verrosteter Nagel ragt aus der Wand der Kiste — ein kalter, rostiger Finger. Du packst zu, ziehst mit aller Kraft; \ner gibt nach und kommt knirschend frei. Behutsam steckst du den Nagel ins Schloss, tastest, drehst — und siehe da: \nein leises Klicken. Die Klappe öffnet sich. Noch einmal prüfst du die Umgebung, nickst dir selbst zu, \ngreifst die Kiste und kletterst hinab — wieder in die Dunkelheit.")
            Warte = input("\nDrücke eine beliebige Taste, um fortzufahren.")
        elif X == 2:
            clean_print("Du hältst die Kiste fest im Arm, bereit weiterzugehen — doch dann fängt dein Blick etwas Glitzerndes am Boden. \nNeben der Klappe schimmert es schwach im Licht der flackernden LED. Die Gier kriecht in dir hoch. \nDu hältst die Kiste nun nur noch mit einer Hand, beugst dich hinunter und greifst nach dem funkelnden Etwas. \n\nEine Münze. Kupfer. Wertlos. \n\nIn diesem Moment gibt deine andere Hand nach — \ndie Kiste rutscht dir aus den Fingern und kracht auf die Klappe. Ein splitterndes Geräusch hallt durch den Raum. \nDas Schloss ist zerstört. Du starrst kurz fassungslos auf die aufgebrochene Öffnung, \natmest erleichtert auf und steigst mit der Kiste hinab — wieder in die Dunkelheit.")
            Warte = input("\nDrücke eine beliebige Taste, um fortzufahren.")
    elif X == 2:
        clean_print("Du greifst die Kiste, drehst dich langsam um und schleichst zum Ausgang. An der Tür hältst du inne, \nbeugst dich vor und blickst durch das Schlüsselloch — nichts. Nur Schwärze. Du atmest tief ein, \nsammelst Mut und drückst die Klinke hinunter. „Da ist jemand im Lager! Ein Dieb, haltet ihn!“ \nDie Worte schneiden wie ein Messer durch die Stille. Du schlägst die Tür zu, drehst dich um und rennst. \nDas flackernde Licht der LED zeigt dir flüchtig den Weg — Umrisse von Kisten, Schatten an der Wand — und da: eine Klappe im Boden. \nDu drehst dich hastig um, um zu sehen, ob dir jemand folgt. In diesem Moment rutscht dir die Kiste aus den Händen und \nkracht auf die Klappe. Ein lautes Knacken hallt durch den Raum. Du hebst die Kiste an — das Schloss ist zerstört. \nErleichtert atmest du aus und steigst mit der Kiste hinab — wieder in die Dunkelheit.")
        Warte = input("\nDrücke eine beliebige Taste, um fortzufahren.")
        clear_screen()   
    Level += 1
clean_print("\n\nDu hast das Ende des  Startkapitels erreicht.")



# Level: 1 (Spieler im Unterlager)

if Level == 1:
    clear_screen()
    clean_print(f"Erneut ist es stockdunkel. Ein lautes Tropfen füllt deine Ohren, als würde die Stille selbst gegen dich arbeiten.{Rot} \n\n„Oh Mann, wie konnte mir das passieren? Es ist, als hätte etwas von mir Besitz ergriffen… Ich wollte doch nur kurz eine Kiste holen — \nund dann konnte ich nicht anders.“{Reset} Du spürst, wie sich Schuld und Wut in dir vermischen. \nIm Innern kennst du die Wahrheit über deinen Charakter, doch mit diesen Worten versuchst du, dich der Verantwortung zu entziehen. \nDie Erkenntnis brennt wie Feuer in dir und macht dich zornig. Die Wut fordert eine Reaktion. \nDu stehst nun vor einer Wahl: Trittst du mit voller Wucht gegen den Eimer neben dir, um die Wut hinauszulassen[1],\noder schließt du die Augen und machst eine Atemübung, um dich zu beruhigen?[2]\n")     
    get_choice(2)
    if X == 1: # Wut-Option
        Leben -= Fußbruch # Spieler verletzt sich, erleidet Schaden
        clean_print(f"Von Wut getrieben trittst du mit voller Wucht gegen den nahestehenden Eimer — in der Hoffnung, dass danach alles besser wird \n\n{Rot}'AAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHH!'{Reset}\n\nDer Schmerz fährt wie ein Blitz durch dein Bein. Nun merkst du, dass der Eimer bis obenhin mit Steinen gefüllt war — \nEin scharfes Knacken, dann brennt dein Fuß; irgendwo in dir ahnst du, dass etwas gebrochen ist. \n\n++Du hast nur noch {str(Leben)} Leben. Deine Entscheidungen haben Folgen.++\n\nTrotzdem rollst du, gepeinigt, auf die Knie, kämpfst dich auf die Füße und tastest, von Schmerz begleitet, nach Klebeband.\nMit zitternden Händen willst du die Handys an deinem Körper fixieren — ungesehen, verzweifelt — und sie so hinausschmuggeln.")
        clean_print("Du hast 15 Handys in der Kiste, damit steht dir die Möglichkeit, zu versuchen, alle an deinen Körper zu befestigen. \nSomit stehen dir genau 15 mögliche Versuche für deine Schandtat. Mit 'Ja' befestigst du ein Gerät an deinen Körper, \nmit 'Nein', lässt du die übrigen Smartphones liegen, und versucht mit dem, was du erbeutet hast, zu fliehen. Zu Beginn steht deine Chance bei 20%, \ndass jeglicher Raub glückt. Die Gier kann dich aber in Gefahr bringen, also nutze es mit bedacht.\n\nMöchtest du beginnen?[1=Ja],[2=Nein]")
        Warte = input("\nDrücke eine beliebige Taste, um fortzufahren.")
        clear_screen()       
#--------------
        Diebstahl_Schleife(1, 15, Kiste_Inventar)
#--------------
        if 0 == Raub_counter:
            clean_print("Bei dem Versuch, die Handys zu klauen, lässt der enorme Schmerz am Fuß dich nicht konzentriert arbeiten,\nweshalb du kein Handy erbeuten konntest und somit die Kiste in der Ecke liegen lässt.")
        elif 1 <= Raub_counter <= 4:
            clean_print(f"Anzahl der erbrachten Beute:{Rot}{Raub_counter}{Reset} \nDas war kein solider Raub, du hast viel liegen lassen, jedoch ist es deine Anfangsphase, weshalb du dich über jedes Handy freust.\n\n")
        elif 5 <= Raub_counter <=8:
            clean_print(f"Anzahl der erbrachten Beute:{Grün}{Raub_counter}{Reset} \nDas war ein erfolgreicher Raubzug den du so schnell nicht vergessen wirst.\n\n")
        elif 9 <= Raub_counter:
            clean_print(f"Anzahl der erbrachten Beute:{Gold}{Raub_counter}{Reset} \nDu stellst dir schon vor, wie du all diese Geräte verkaufst und damit der jüngste Reiche unter deinen Freunden sein kannst!!!\n\n") 
        
        
        warte = input("Drücke eine beliebige Taste, um fortzufahren..")
        clear_screen()

        clean_print(f"Gerade als du beschließt, mit dem Wenigen, das du erbeuten konntest, unauffällig die sichere Flucht zu ergreifen, legt sich plötzlich eine schwere Hand von hinten auf deine Schulter.\nFür einen Moment bleibt dir der Atem weg..{orange}\n\n'Was machst du denn hier?'{Reset} zischt eine Stimme dicht an deinem Ohr. {orange}'Wieder mal am Klauen?'{Reset}\n\nDein Herz hämmert gegen deine Brust, dein Kopf rast. Du siehst dich schon gefeuert, abgeführt, bloßgestellt. Die Stimme kommt dir bekannt vor… und doch kannst du sie im ersten Moment nicht einordnen.\nLangsam, viel zu langsam, drehst du dich um.\n\nUnd dann siehst du ihn.\n\nEs ist… niemand Bestimmtes. Ein Typ. Irgendein komischer Kerl. Sein Blick ist wachsam, sein Grinsen schief.")
        visualize("dealer.png")
        clean_print(f"\nDu fragst dich, ob er hier überhaupt arbeitet. Oder ob er nur so tut.\nWie kann das sein?\nWer ist dieser Mann?\n\nEr beugt sich näher zu dir und sagt leise, fast verschwörerisch: \n\n{orange}'Gib mir die Hälfte und ich sage nichts. Hahahahaha.'{Reset}\n\nDu zwingst dich zu einem unsicheren Lachen. Du weißt nicht, ob er dich wirklich erwischt hat – oder ob er nur blufft. Dein Magen zieht sich zusammen.\n\nWas willst du tun?\nIhn fragen, wer er überhaupt ist [1]\nIhm die Hälfte anbieten [2]\nOder alles abstreiten und leugnen, dass du irgendetwas gestohlen hast [3]?")
        get_choice(3)
        if X == 1:
            clean_print(f"{Rot}'Sorry, arbeitest du hier? Ich habe dich noch nie gesehen..'{Reset}\n\nSelbstsicher schaust du ihn an, da sagt er:\n\n{orange}'Nein aber..hast du ein Problem damit?'{Reset}[1=ja],[2=nein]")
            get_choice(2)
            if X == 1:
                clean_print(f"{Rot}'Natürlich, wie bist du hier rein gekommen, du darfst nicht hier sein.'{orange}\n'Du darfst doch genauso wenig hier sein, was macht ein normaler Mitarbeiter im Unterlager?\nVor allem mit den gestohlenen Handys, die du an deinem Körper befestigt hast.'{Reset}.\n\nVöllig blass bist du sprachlos, da er natürlich recht hat und dich nun in der Hand hat.\nVersuchst du wegzulaufen[1], oder ihn anzugreifen[2]?")
                get_choice(2)
                if X == 1: #Weglaufen
                    clean_print("Ohne irgendetwas zu sagen rennst du so schnell, wie du kannst und blickst nicht zurück. \nEs ist ein langer Weg, den du hinter dir bringst, bis du endlich am Verkaufsbereich stehst. Doch Zeit, dich auszuruhen ist nicht.")
                elif X == 2: #Angriff
                    clean_print("Völlig überfordert haust du ihm mit voller Wucht einen Haken in sein Gesicht, sodass er sofort umfällt.\nMöchtest du ihn liegen lassen[1]\noder in eine Ecke verstecken[2]?")
                    get_choice(2)
                    if X == 1:
                        clean_print("Du lässt ihn genau so liegen und rennst nach oben in der Hoffnung, dass dich Niemand gesehen hat. \nIn deinem Kopf ist alles durcheinander und du weißt nicht was mit dir passiert, doch die Zeit erlaubt keine Bedenken.\nOben angekommen versuchst du durch den Verkaufsbereich in die Personalräume zu gelangen, \num die Handys weiter zu verstecken, doch dann passiert das, was immer passiert. ")
                        Knock_Out = True # Das fragen wir später ab um Lvl-übergreifend daran anknüpfen zu können
                        # Der Vorfall mit der bewusstlosen Person soll später wieder aufgegriffen werden
                    elif X == 2:
                        clean_print("Du ziehst ihn an den Beinen und versuchst ihn an einer Ecke zu verstecken. \nAnschließend legst du einige Kartons über ihn, sodass man ihn nicht sieht und flüchtest.\nDie Flucht trägt dich nach oben in den Verkaufsraum, damit du an ihn vorbei an die Personalräume gelangen kannst.\nLeider stehen auch jetzt Kunden um dich herum und es passiert Folgendes:")
            elif X == 2: 
                clean_print(f"{Rot}'Nein Nein, mach nur ruhig, lass mich meinen Kram machen und du machst deinen.'{Reset}\nEr schaut dich an, denkt einen Moment nach und sagt anschließend:\n{orange}'Sieht so aus, als würdest du ein paar Drogen gebrauchen, ich habe was für dich, hier.'{Reset}\nEr drückt dir einen Plastikbeutel in die Hand und zwinkert dir zu. \nDu befürchtest schlimmes, aber bist so sprachlos, dass du dem nichts entgegenwirken kannst. Er sagt:{orange}'Seit Jahren versorge ich diese Filiale und ich lebe in jenen Mauern'{Reset}\nNach dieser Aussage fragst du dich ob du schon beim Anfassen des Päckchens auf einen Trip geschickt wurdest, \noder was er da sagt...")
                clean_print(f"Du überlegst kurz: DU könntest jetzt entweder an dem Päckchen riechen[1], es ebenfalls an deinem Körper befestigen[2] oder es ihm zurückgeben[3] ")
                get_choice(3)
                if X == 1:
                    clean_print(f"Du riechst vorsichtig an dem Päckchen. Plötzlich wird dir schwindelig und schließlich schwarz vor Augen.", Warteschleife,)
                    clean_print(f"Du wachst auf, es ist mal wieder stock Dunkel. Als du versuchst dich zu bewegen,, merkst du dass du gefesselt bist und, Moment mal. Die Handys, sie sind weg. Mit deinen Händen ertastest du eine Glasscherbe auf dem Boden und befreist dich von den fesseln. Du tastest dich eine Weile lang im Dunkeln bis du eine Tür ertastest Tür. Du öffnestt sie, tritst heraus und da passiert es: ")
                    while "Handy" in Spieler_Inventar:
                        Spieler_Inventar.remove("Handy")
                        Dealer_Inventar.append("Handy")
                elif X == 2:
                    clean_print(f"Als du versuchst das Päckchen an deinem Körper zu befestigen siehst du im Augenwinkel, wie er zum Schlag ausholt und weichst aus. Geshockt lässt du das Päckchen fallen und fängst an zu rennen. Sobald du die Tür erreicht hast öffnest du sie und trittst in den Kundenbereich. Doch dann passier Folgendes:")
                elif X == 3:
                    clean_print(f"Du gibst ihm das Päckchen zurück und er sagt:{Rot}'Selbst Schuld wenn du eine Kostprobe verpasst.'{Reset} Du machst dich auf den Rückweg und findest schließlich die Tür zum Kundenbereich, öffnest sie und:")
        elif X == 2:
            clean_print(f"{Rot}Ich möchte ehrlich zu dir sein. Ich habe das Geld dringend nötig, ich habe unter meinem Hemd {Raub_counter} Handys.\n")
            if Raub_counter % 2 == 0: # Prüft, ob die Zahl gerade oder ungerade ist
                clean_print(f"Ich biete dir die Hälfte an, somit {Raub_counter // 2}. Was sagst du?{Reset}")
            elif Raub_counter % 2 != 0:
                Raub_counter_hälfte = Raub_counter - 1
                clean_print(f"{Rot}Ich biete dir fast die Hälfte an, somit {Raub_counter_hälfte // 2}. Was sagst du?{Reset}'")
            
            clean_print(f"\n\nEr mustert dich, erst fragend, dann enttäuscht. Sein Blick schweift durch die Gänge, er winkt jemanden heran. Panik schnürt dir die Kehle zu – du bereust, gestanden zu haben. Und dann, plötzlich, taucht um die Ecke niemand Geringeres als der Filialleiter auf. NEIN! Alles wirbelt an dir vorbei, du bist in die Falle getappt, direkt in seine Falle.")
            clean_print(f"Der fremde Mann sagt zum Filialleiter:'{Gold}Wird langsam Zeit, dass wir gehen. Wir müssen nach oben. \nDu hast doch gesagt, dass ich mir einen Sklaven aussuchen kann, oder?{Reset}'\n\n'{Blau}Ja klar, soll es der junge Herr sein?{Reset}\n\nDu, der gerade mitten im Geschehen steht, versteht nichts, \nvöllig verwirrt und noch immer mit Adrenalin im Blut stehst du wie verwurzelt und sagst nichts.\nDu kannst nichts sagen, dieser Mann hat dich in der Hand...")
            clean_print("Drücke eine beliebige Taste, um fortzufahren..")
            warte = input()
            clear_screen()
            clean_print(f"Dein Kopf rast. Du hast nur Sekunden.\nWas, wenn du schlau genug bist, den Filialleiter abzulenken und dem Mann unbemerkt ein Handy unterzuschieben?\nDie Chancen stehen schlecht – ein falscher Schritt, und alles ist vorbei. Aber wenn es gelingt, endet diese lähmende Angst.\n\n[1 = Risiko eingehen]\n[2 = Kein Risiko eingehen]")
            get_choice(2)
            if X == 1:
                clean_print(f"Du wirfst dich vor auf die Knie und schreist ganz laut. Du versuchst einen Schmerz am Bauch vorzutäuschen, \ndamit der Mann näher kommt und das tut er. Er kommt näher und sagt:'{Gold}Was ist los? Ist alles in Ordnung?{Reset}'\n Du greifst eines deiner geklauten Handys und versuchst es in seine Hosentasche zu legen und....\n\n")
                geschickter_zug()
                geschickt_Erfolg = 0 ###
                if geschickt_Erfolg == 1: # aus der Def geschickter_zug
                    clean_print(f"Nachdem du es geschafft hast, sagst du: '{Rot}Geh mir weg, du Dieb. Von dir brauche ich keine Hilfe.{Reset}'\n\nStille im Raum. Dann erhebt der Mann seine Stimme:\n\n'{Gold}Was redest du? Ich bin kein Dieb!'{Rot} 'Du klaust Handys und hast keinen Respekt vor dem Chef!'\n{Blau}'Nik, was redet er da? Du hast doch nicht schon wieder was geklaut, wir hatten doch darüber geredet. \nWas ist mit dir falsch, Mann??'\n{Gold}'Ich war es nicht! Der ist auf den Kopf gefallen, was redet er da?'\n{Rot}'Schauen Sie sich mal seine Taschen an.'{Reset}\n\nDer Filialleiter blickt hinein, entdeckt das neue iPhone 17 Pro und sagt: \n\n'{Blau}Verschwinde und komm nie wieder hierher. Unsere Geschäfte sind hiermit beendet.{Reset}'\n\nDer Mann verschwindet wütend. Der Chef dreht sich zu dir, reicht dir das iPhone.\n\nDu hast dir soeben 35 Social Credits verdient und das Handy wirst du nachher natürlich versuchen zu stehlen.\n Aber was gerade passiert ist, bleibt unklar, jedoch sollst du das IPhone erstmal oben in den Verkauf bringen. – Zugleich erwartet dich oben aber schon eine Kundin, \ndie auf dich zukommt.")
                    Social_Credits += 35
                elif geschickt_Erfolg == 0: # Gewisse Optionen werden das Spielaus bedeuten
                    clean_print(f"{Gold}'Guter Versuch, du hast versucht, mich zum Schweigen zu bringen. Hiermit bist du gefeuert.'{Reset}\n\nDer Filialleiter schaut dich nur wütend und Kommentarlos an. Die Enttäuschung macht sich in deren Gesichtern breit, \ndoch tun oder sagen kannst du nichts mehr.")
                    clean_print("Drücke eine beliebige Taste, um fortzufahren..")
                    warte = input() 
                    clean_print("Der Filialleiter schaut dich kurz an und sagt zu dem Typen \n'Es ist dein Sklave, mach mit ihm was du willst'\nDer Typ kommt auf dich zu undstellt sich hinter dich. Du fühlst dich unwohl und plötzlich zieht er dir eine Plastiktüte über den Kopf. Du bekommst keine Luft mehr und sinkst zu Boden. Das ist das Ende deiner Geschichte") 
                    clean_print("\nDu hast das Spiel verloren. Das war ein viel zu riskanter Spielzug, der das Aus bedeutet.")
                    while True:
                        X += 1
                        X -= 1                      
            elif X == 2:
                clean_print(f"'{Gold}Ich möchte ihn zum Sklaven machen – als würde ich die ganze Drecksarbeit für dich erledigen. Er übernimmt das einfach. Die Drogen kann er ja für uns verticken.{Reset}'\n\nWas? Drogen? Dein Herz setzt aus. Das kann nicht wahr sein … dein Chef steckt in sowas drin? Du sagst kein Wort. Stumm gehst du nach oben, nur ein Gedanke im Kopf: diese Handys fertig machen. Doch um dorthin zu kommen, musst du am Verkauf vorbei – und kaum setzt du einen Fuß hinein, passiert es.")
        elif X == 3:
            clean_print(f"{Rot}'Was meinst du? Ich habe nichts genommen. Wie kommt man überhaupt auf sowas?'{Reset}\n\nEr mustert dich mit einem schiefen, fast hinterhältigen Grinsen. Dann sagt er mit einer Stimme, die halb verspielt, halb bedrohlich klingt:\n{orange}'Jaaa jaaa, ich weiß es. Ich weiß es sogar ganz genau! Beweise? Noch nicht. Aber keine Sorge, ich behalte dich ganz genau im Auge, Sportsfreund.'{Reset}\n\nEin unheilvolles, krächzendes Lachen hallt durch die Gänge, während er in den dunklen Hinterräumen verschwindet. Zurück bleibt nur ein eisiges Gefühl der Unsicherheit und ein Kopf voller Fragen.\n\nDu versuchst, das Geschehene zu ignorieren, atmest tief durch und gehst vorsichtig auf deinen verletzten Fuß gestützt in Richtung Personalräume, um ihn genauer unter die Lupe zu nehmen.\n\nDoch dann passiert genau das, was du schon geahnt hast:")
            



    elif X == 2: # Selbstkontrolle-Option
        clean_print("Du bewahrst Ruhe und weißt, dass Kontrolle die einzig vernünftige Lösung ist. Also schließt du die Augen, um dich zu entspannen. \nAls du die Augen erneut öffnest, wirst du bleich im Gesicht. Der Filialleiter persönlich steht vor dir.. \n\n")
        visualize("Filialleiter.jpg")
        clean_print(f"{Blau}'Darf ich fragen, was genau Sie hier machen?'{Reset}\n\nEs hätte nicht schlimmer kommen können, der schmierie Geldsack persönlich steht vor dir, denkst du dir im Inneren.\nWas tust du jetzt? Sagst du ihm die Wahrheit[1], dass du krank bist und dich ausruhen würdest[2] - oder erzählst du ihm, dass du dich verlaufen hast?[3]\n")
        get_choice(3)
        if X == 1: # Diebstahlbeichte-Option
            clean_print(f"{Rot}'Ich… ehm… ich habe versucht, diese Box zu klauen…'{Reset} Er schaut dich einen Moment lang mit einem merkwürdigen Blick an — \nals würde er abwägen, ob du ein Witz bist oder eine Gefahr. Dann bricht er in Gelächter aus und sagt schließlich: {Blau}\n\n„Hahahahahahaha — der war gut! Wer würde schon ins Unterlager gehen, um etwas zu stehlen? Weißt du, du hast meinen Tag gerettet. \nMeine Frau und die Kinder nerven mich gerade ohne Ende, da flüchte ich mich auf die Arbeit.“{Reset}\n\nHilflos denkst du: Wo bin ich hier gelandet? Du wolltest stehlen, nicht seine Lebensgeschichte hören. \nBevor seine Erzählung Fahrt aufnimmt, musst du reagieren. Du sagst entweder, dass du wieder hoch musst, denn du hättest viel zu tun — oder du behauptest, du hättest dich hier versteckt, weil du krank seist -\noder Ihm direkt sagen, dass du kein Bock hast, ihm weiter zuzuhören, du müsstest arbeiten gehen {Rot}(Nicht zu empfehlen){Reset}\nEntscheide weise.\n")
            get_choice(3)
            if X == 1: # Zu beschäftigt für eine Unterhaltung-Option
                clean_print(f"{Rot}'Schauen Sie, ich müsste eigentlich noch weiterarbeiten, auch wenn ich am liebsten hier unten bleiben würde.'\n\n{Reset}{Blau}'Das weiß ich doch. Sie sind ein zuverlässiger, vertrauenswürdiger Mitarbeiter. Ach, und bevor Sie es vergessen: \nSie haben die Kiste hier liegen lassen. Bringen Sie sie bitte nach oben, ja?'{Reset}\n\nDu stehst da, erstarrt, während die Realität langsam in dir versickert: Der Filialleiter gibt dir persönlich den Auftrag, \ndie Kiste nach oben zu bringen. Dieser Tag scheint von einem merkwürdigen Schicksal geprägt zu sein — \nein Tag, an dem alles möglich ist.")
                clean_print(f"Bevor du dich auf dem Weg machst, macht sich ein Gefühl in dir laut, das das Verlangen erweckt, deinen Chef um einige seine Gegenstände, die er gerade bei sich trägt, zu erleichtern. \nAlso stellst du dir die Frage, soll ich ihn bestehlen[1] {Rot}(Riskant){Reset} oder lieber nicht[2]?")
                get_choice(2)
                if X == 1:
                    #------------------
                    Diebstahl_Schleife(1, 4, Filialleiter_Inventar)
                    #------------------
                    clean_print("Mit der Kiste machst du dich auf dem Weg nach oben und überlegst, wie du die Handys in der Box sicher klauen kannst.\nDoch im Verkaufsraum passiert das, was immer passiert..")
                elif X == 2:
                    clean_print("Mit der Kiste machst du dich auf dem Weg nach oben und überlegst, wie du die Handys in der Box sicher klauen kannst.\nDoch im Verkaufsraum passiert das, was immer passiert..")
        elif X == 2: # Krank-Option
            clean_print (f"{Rot}\n'Ich fühle mich heute sehr krank und deshalb musste ich hier eine kleine Pause einlegen.'\nDer Filialleiter erwidert:{Blau}'Und warum genau hier??'{Reset}\nJetzt stehst du da und brichst in Schweißausbrüchen aus. Er fährt fort und sagt.\n{Blau}Hören Sie, Sie scheinen mir kerngesund zu sein. Besser Sie gehen schnell wieder nach oben, \nes gibt noch genug zu tun.'{Rot}'Aber ich habe ein gewisses Unwohlsein und\n ich habe Schmerzen im Bereich des Herzens.'\n{Blau}'Stellen Sie sich mal nicht so an, solange Ihr Herz noch schlägt, ist alles in Ordnung.'\n{Reset}Völlig gekränkt senkst du deine Stimme und fühlst dich vollkommen zertreten.\n {Blau}Und vergessen Sie diese Kiste nicht! Muss ich Ihnen jetzt sagen, wie Ihre Arbeit funktioniert?{Reset}\nNimmst du die Kiste und gehst wieder nach oben[1], oder machst du dich stark und lässt dich nicht von einer autoritären Stimme denunzieren[2]? ")
            get_choice(2)
            if X == 1:# Kommentarlos nach oben gehen
                clean_print(f"Zu tiefst beschämt und zugleich wütend, steigst du wieder hoch in den Verkaufsbereich, um deine Arbeit fortzusetzen.\nDeine Gedanken wirbeln durcheinander, und dir fallen hundert fiese Sprüche ein, wie du ihn kontern könntest.\nDoch keine Sekunde lang kannst du verschnaufen, da ruft eine Kundin'{Grün}\n\n")
            elif X == 2: # Gegen Äutorität auflehnen
                clean_print(f"\nVon Mut getrieben und einer Wut, die sich breit macht, \ndass du es satt hast, der schwächliche Sklavenarbeiter zu sein,\n richtest du dich auf und sagst:{Rot}'Hören Sie ich brauche manchmal auch meine Pause!\nEs kann nicht sein, dass Sie mich so behandeln.'{Reset}\n\nWährenddessen macht sich ein Gefühl von Selbstsicherheit in dir breit. \nMöchtest du eskalieren und den Chef strategisch in eine Ecke drängen[1], \noder willst du in Tränen ausbrechen, um deinen Plan, die Kiste sicher zu stehlen, abzuschließen[2]?")
                get_choice(2)
                if X == 1:#Chef anschreien
                    clean_print(f"Du beginnst immer lauter zu werden und stampfst mit den Füßen, in Hoffnung, \ndass der Chef klein bei gibt, doch dann, ehe du reagieren kannst, packt er dich am Hals, \ndass nicht einmal deine eigene Stimme hören kannst.\nVöllig verängstigt entsteht eine Stille und er sagt dir:\n{Blau}Wenn ich noch so ein Theater von dir erlebe, bist du fällig.'{Reset}\nDu stürzt zu boden und denkst aber nur daran, dass er dich nicht mit der Kiste in Verbindung setzt.\nOhne weitere Kommentare verschwindet der Chef in mysteriösen Hinterzimmern.")
                    Social_Credits -=15
                    clean_print(f"\nDu hast gerade 15 Social Credits verloren. Es sieht ganz schlecht für dich aus.\n Wenn du zu viele Punkte verlierst, kann es zu schweren Konsequenzen führen.\n Dir bleiben noch {Social_Credits} übrig.")
                    clean_print("Drücke eine beliebige Taste, um fortzufahren..")
                    warte = input()
                    clear_screen()
                    clean_print("Als du dich von diesem Übergriff erholt hast, stehst du langsam auf, nimmst die Kiste in die Hand \nund begibst dich emotionslos nach oben in den Verkaufsraum, um daran vorbei, \nan die anderen Lagerstellen zu gelangen.")
                elif X == 2: # Tränenausbruch
                    clean_print(f"Du brichst also in Tränen aus und hoffst, dass in ihn ein Stück Menschlichkeit noch ist.\n Nach einem langen Monolog von dir sagt der Chef:\n{Blau}'Das habe ich doch nicht so gemeint, Sie müssen sich wieder beruhigen, es tut mir leid,\nbleiben Sie so lange hier, bis es Ihnen besser geht. Ich lasse Sie so lange in Ruhe'{Reset}\n")
                    Social_Credits -=5
                    clean_print(f"Du hast gerade 5 Social Credits verloren, jedoch für einen guten Zweck, zu viele riskante Taten,\nkönnen dich aber in Bedrängnis bringen")
                    clean_print("Noch einige Zeit weinst du vor dir hin, um die Show aufrecht zu erhalten. \n\nAls du dir sicher bist, dass er weg ist, stehst du auf, nimmst die Kiste und \ngehst wieder in den Verkaufsraum. Du hoffst, die Handys in der Kiste irgendwie noch klauen zu können,\naber erstmal brauchst du einen besseren Plan.")
            elif X == 3: # Respektlose-Option
                clean_print(f"{Rot}'Hör Mal Opa, dieses Zeug interessiert mich nicht. Klär deine Sachen allein und nerv nicht mich damit.'{Reset}Das hättest du gerne gesagt, stattdessen habt ihr euch hingesetzt und er hat dir von seiner ganzen Geschichte erzählt.")
                Weiter = input("\n\nDrücke eine beliebige Taste, um fortzufahren..")
                clear_screen()
                print("\n" * 15 + " " * 60, end="")
                Zeit_vergangen(Warteschleife) # Erstellt einen Loading Screen
                clear_screen()
                clean_print("")
                Social_Credits += 5
                clean_print(f"Du hast dir durch das Gespräch mit dem Filialleiter 5 Social_Credits verdient. Somit hast du nun {Social_Credits} Social_Credits.")
                clean_print(f"\nDu sagst: {Rot}'Schauen Sie, ich müsste eigentlich noch weiterarbeiten, auch wenn ich am liebsten hier unten bleiben würde.'\n\n{Reset}{Blau}'Das weiß ich doch. Sie sind ein zuverlässiger, vertrauenswürdiger Mitarbeiter. Ach, und bevor Sie es vergessen: \nSie haben die Kiste hier liegen lassen. Bringen Sie sie bitte nach oben, ja?'{Reset}\n\nDu stehst da, erstarrt, während die Realität langsam einsickert: Der Filialleiter gibt dir persönlich den Auftrag, \ndie Kiste nach oben zu bringen. Dieser Tag scheint von einem merkwürdigen Schicksal geprägt zu sein — \nein Tag, an dem alles möglich ist.")
                clean_print("Du gehst nun also hoch und und gehst durch den Verkaufsraum, um deinen Raub mit der Kiste \nneu zu planen, doch dann ruft eine Kundin dich.")
        elif X == 3: # Verlaufen-Option
            clean_print(f"{Rot}'Wissen Sie, ich… ehh… i-ich haab mich verlaufen und da… da wollte i-ich—'{Blau}\n'Sie wollten *was*? Warum stottern Sie so??\nSie dürfen hier überhaupt nicht rein!' {Rot}\n'D-der… dessen bin ich mir bewusst, aber—'\n{Blau}'Unterbrechen Sie mich jetzt auch noch? Eine absolute Frechheit! Ich fasse es nicht.\nDas war Ihre letzte Verwarnung! Wenn ich Sie hier unten noch ein einziges Mal sehe — und das ohne triftigen Grund —\ndann hagelt es eine Abmahnung, klar und deutlich! Verstanden???' {Rot}'Jawohl…' {Blau}\n'Und diese Kiste neben Ihnen…' Er beugt sich leicht vor, sein Blick bohrt sich misstrauisch in Sie.\n'Wollten Sie die etwa… klauen????'{Reset}  [1 = ja]  [2 = nein]")
            get_choice(2)
            if X == 1:
                clean_print(f"{Blau}'Also für solche Spielchen habe ich wirklich keine Zeit. Herr… Herr… wie auch immer — sagen Sie mir eins: Arbeiten Sie überhaupt hier?'\nEr tritt einen Schritt näher, seine Augen verengen sich misstrauisch, als würde er versuchen, direkt in Ihre Gedanken zu sehen.\n'Ich schwöre, ich habe Sie hier noch nie gesehen… nicht ein einziges Mal. Wie ist Ihr Name?'{Reset}")
                Spielername = input("--->")
                clean_print(f"{Blau}'Sie sind also {Spielername}…' Seine Stimme wird tiefer, beinahe drohend. Er spricht deinen Namen aus, als würde er ihn schmecken wollen, als ob er ihn sich für später merken müsste.\nLangsam beugt er sich vor, sein Blick bohrt sich in dich wie eine kalte Klinge.\n'Seien Sie sich sicher… ich werde Sie im Auge behalten. Und wehe, ich erwische Sie noch ein einziges Mal hier unten.'{Reset}")
            elif X == 2:
                clean_print(f"{Blau}'Das will ich auch schwer für Sie hoffen. Da fällt mir gerade ein, ich kenne Sie gar nicht. Arbeiten Sie überhaupt hier?? Wie ist Ihr Name??'{Reset}")
                Spielername = input()
                clean_print(f"{Blau}'Sie sind also {Spielername}…' Seine Stimme senkt sich, wird schneidend ruhig, während sein Blick sich wie ein Schatten an Ihnen festklammert. 'Seien Sie sich ganz sicher… ich werde Sie im Auge behalten. Und wehe, ich sehe Sie noch ein einziges Mal hier.'{Reset}")
            Social_Credits -= 5
            clean_print(f"\n\nDu hast gerade 5 Social_Credits verloren. Nun bleiben dir nur noch {Social_Credits}.\nPass gut auf, dass du nicht zu viele davon verlierst, sonst warten unangenehme Konsequenzen auf dich.\n\n")
            clean_print(f"Zu tiefst beschämt und zugleich wütend, steigst du wieder hoch in den Verkaufsbereich, um deine Arbeit fortzusetzen.\nDeine Gedanken wirbeln durcheinander, und dir fallen hundert fiese Sprüche ein, wie du ihn kontern könntest.\nDoch keine Sekunde lang kannst du verschnaufen, da ruft eine Kundin'{Grün}\n\n")
            
            
    clean_print(f"{Grün}\n\n'Verzeihen Sie, ich habe eine kurze Frage'")
    visualize("nervige_kundin_glücklich.png")
    clean_print(f"{Reset}\n\nWas tust du nun?[1] Sie in den Laden willkommen heißen und bedienen oder [2] weiterlaufen und die Kundin ignorieren?")         
    get_choice(2)
    if X == 1: # Kundin willkommen heißen und bedienen
            clean_print(f"Du drehst dich zu ihr und sagst{Rot}'Was kann ich für Sie tun?'{Grün}'\nIch möchte ehm alsooo... ich weiß nicht, wie genau das heißt... dieses eine Gerät, wissen Sie, was ich meine?'{Reset}\nVöllig verstört fragst du dich, wovon sie spricht, doch du bleibst ernst und sagst {Rot}'Nein, verzeihen Sie, leider nicht..'{Grün}\n'Ah, dieses eine Teil für meinen Staubsauger! Der funktioniert nicht. Haben Sie ein Ersatzteil davon?'{Rot}'Wie bitte? Ich kann Ihnen nicht folgen.\nWovon reden Sie?'{Reset}\n\nEin weiteres Mal stehst du vor der Wahl: Ob du ihr weiter zuhörst [1], einfach ins Mitarbeiter-Badezimmer flüchtest [2], oder ob du sie ausnimmst wie eine Weihnachtsganz [3].")
            get_choice(3)
            visualize("nervige_kundin_wütend.png")
            if X == 1: # Kundin empfangen
                clean_print(f"{Blau}'Ach, Sie haben keine Ahnung… nicht schlimm, einen kompetenten Mitarbeiter werde ich hier schon noch finden.'{Reset}\nEtwas so Asoziales hast du noch nie erlebt, weshalb du erneut vor der Wahl stehst: [1] dich an ihr zu rächen,\noder [2] sie zu ignorieren und einfach weiterzugehen.")
                get_choice(3) # An Kundin rächen 
                if X == 1:
                    clean_print(f"{Rot}'Verzeihen Sie bitte, dass Sie nicht zufrieden mit unserem Service sind. Für solche Fälle haben wir Mitarbeiter\nhier eine Geschenkkarte im Wert von 50 Euro.'{Grün}'Was wirklich?? Ja dann muss man sich hier ja mal etwas öfters beschweren Hahahahaha. Tschüss!'{Reset}\n\nSie steckt die Karte ein und schlendert weiter, völlig ahnungslos. Doch nun beginnt dein Racheplan zu atmen—wie ein dunkler Gedanke, der endlich Gestalt annimmt. Du rufst die Security an:{Rot}'Hi mein Bester, ich bins. Schau mal, wir haben hier in der Staubsaugerabteilung eine Frau mit blonden Haaren und einer roten Tasche.\nIch sah, wie sie etwas eingesteckt hat. Komm dir das mal anschauen.'{Reset}\n\nDu legst auf und gehst in Deckung, lauerst wie ein Jäger im Neonlicht des Ladens. Der Security-Mann erscheint, breit wie ein Schrank, und marschiert direkt zu der Frau. Du kannst nicht genau hören, was gesprochen wird, also stehst du auf und tust so, als würdest du im Service weiterarbeiten… doch dann siehst du im Augenwinkel, wie ein Schatten sich löst: die Frau holt aus und trifft den Security mit voller Wucht ins Gesicht—er kippt wie ein gefällter Baum!\nSie brüllt:{Grün}\n\n'Sooo sooo, ein Geschenk jaa… warte ab, ich werde dich jetzt suchen und dann erklärst du mir das noch ein Mal..'{Reset}\n\nDein Herz rast, als würde jemand mit Fäusten von innen gegen deinen Brustkorb schlagen. Du duckst dich hinter ein Regal, der Atem stockt dir. Dann, völlig unerwartet, richtet sich der Security-Mann wieder auf, zieht einen Elektroschocker hervor und jagt der Frau eine Ladung Strom durch den Körper—sie fällt wie ein nasser Sack um. Das Chaos sprengt deine Nerven, du kannst nicht mehr. Du flüchtest zur Toilette, während hinter dir die sirrende Stille nach dem Schocker in der Luft hängt.")
                elif X == 2: # Kundin in Ruhe lassen
                    Social_Credits += 3
                    clean_print(f"Genau in dem Moment, als du die Kundin ziehen lässt, taucht hinter dir die Abteilungsleiterin auf und sagt dir, {Blau}'\nDas hast du aber richtig gut gemacht! Der Chef wird sich freuen zu hören, dass er solch engagierte Mitarbeiter hat. Aber ich muss weiter, bis nachher!'\n\nSoeben hast du dir 3 Social_Credits verdient, und ein kleines Gefühl von Stolz breitet sich in dir aus, deutlich besser als vorhin.")
                elif X == 3: # Kundin beklauen
                    clean_print("Du holst tief Luft und sagst: 'Zeigen Sie mal her. Was genau funktioniert denn nicht und wie ist es kaputt gegeangen?'. Während Sie erneut von Dingen redet, von denen du keine Ahnung hast, versuchst du dein Glück beim Taschendiebstahl.")
                    #--------------
                    Diebstahl_Schleife(1, 4, Kundin_1_inventar)
                    #--------------
                    if Raub_counter == 0:
                        clean_print("Du konntest bei der Kundin leider nichts stehlen, also lässt du sie einfach weiterziehen.")
                    elif Raub_counter == 1:
                        clean_print("Du freust dich über die Beute, doch plötzlich fällt dir auf, dass der Gegenstand noch eine Diebstahlsicherung hat. Bei genauerem hinschauen fällt dir auf, dass der Gegenstand aus dem Sortiment des Ladens stammt. Du lässt die Kundin weiterziehen, bevor sie dich verdächtigt. Doch du hast jetzt ein anderes Problem: Du hast einen Gegenstand gestohlen, den die Kundin zuvor aus dem Laden gestohlen hat, wenn dich jetzt der Fillialleiter ertwischt, wird es schwierig ihm das zu erklären. Du musst den Gegenstand irgendwie loswerden, bevor du Ärger bekommst.")
                    elif Raub_counter >= 2:
                        clean_print("Du hast erfolgreich bei der Kundin gestohlen und konntest mehrere Gegenstände entwenden. Doch plötzlich fällt dir auf, dass einige der Gegenstände noch eine Diebstahlsicherung haben. Bei genauerem hinschauen fällt dir auf, dass die Gegenstände aus dem Sortiment des Ladens stammen. Du lässt die Kundin weiterziehen, bevor sie dich verdächtigt. Doch du hast jetzt ein anderes Problem: Du hast mehrere Gegenstände gestohlen, die die Kundin zuvor aus dem Laden gestohlen hat, wenn dich jetzt der Fillialleiter ertwischt, wird es schwierig ihm das zu erklären. Du musst die Gegenstände irgendwie loswerden, bevor du Ärger bekommst.")
                        Raub_counter = 0
                # Fortsetzung ////////////////////////////////
            elif X == 2:
                clean_print()
                #Fortsetzung /////////////////////////////////
            elif X == 3:
                clean_print()
                #Fortsetzung /////////////////////////////////

    elif X == 2: # Kundin ignorieren und weiter gehen
        clean_print(f"Du ignorierst die Kundin und gehst weiter, doch plötzlich hörst du hinter dir eine Stimme:{Grün}\n\n'Entschuldigung, ich habe Sie etwas gefragt!'")
        visualize("nervige_kundin_wütend.png")
        clean_print(f"{Reset} Du bleibst stehen, drehst dich um und sagst {Rot}'Oh, verzeihen Sie bitte, ich bin momentan sehr beschäftigt' Sie hört dir nicht zu und fängt einfach an zu reden{Grün}\n'Ich suche dieses eine Teil für meinen Staubsauger. Haben Sie so etwas hier?'{Reset}\n\nDu überlegst kurz, dann sagst du {Rot}'Ja natürlich, dort drüben.' {Reset} Du zeigst auf die Decke. Während die Kundin nach oben schaut, versuchst du leise weg zu schleichen.")
        Schleichen()
        if Schleichen_Erfolg == 1:
            print("Geschafft! Aus der Ferne kannst du erkennen, wie sie zuerst verwirrt, aber dann wütend umerherschaut und dich sucht. du solltest dieser Kundin nicht nochmal begegnen.")
        elif Schleichen_Erfolg == 0:
            print(f"Die Kundin bemerkt das Geräusch und ruft verärgert {Rot} 'Hey! Wollen Sie sich etwa aus dem Staub machen?!!'{Reset} \nDu bleibst wie erstarrt stehen und überlegst verzweifelt, was du jetzt tun solltest. \nDu könntest dich der Kundin entweder stellen und ihr nun doch helfen [1], \noder du rächst dich an ihr [2].")       
            get_choice(2)
            if X == 1: # Kundin doch helfen
                clean_print(f"Du drehst dich zu ihr und sagst{Rot}'Verzeihen Sie mir mein Auftreten. Was kann ich für Sie tun?'{Grün}'\nLeute wie Sie enden auf der Straße, wie Sie es verdienen, aber wie auch immer. Ich möchte ehm alsooo... ich weiß nicht, wie genau das heißt... dieses eine Gerät, wissen Sie, was ich meine?'{Reset}\nVöllig verstört fragst du dich, wovon sie spricht, doch du bleibst ernst und sagst {Rot}\n'Nein, verzeihen Sie, leider nicht..'{Grün}\n'Ah, dieses eine Teil für meinen Staubsauger! Der funktioniert nicht. Haben Sie ein Ersatzteil davon?'\n{Rot}'Wie bitte? Ich kann Ihnen nicht folgen. Wovon reden Sie?'{Reset}\n\nEin weiteres Mal stehst du vor der Wahl: Ob du ihr weiter zuhörst [1], \neinfach ins Mitarbeiter-Badezimmer flüchtest [2], oder ob du sie ausnimmst wie eine Weihnachtsganz [3].")
                get_choice(2)
                if X == 1: # Kundin empfangen
                    clean_print(f"{Blau}'Ach, Sie haben keine Ahnung… nicht schlimm, einen kompetenten Mitarbeiter werde ich hier schon noch finden.'{Reset}\nEtwas so Asoziales hast du noch nie erlebt, weshalb du erneut vor der Wahl stehst: [1] dich an ihr zu rächen,\noder [2] sie zu ignorieren und einfach weiterzugehen.")
                    get_choice(3) # An Kundin rächen
                    if X == 1:
                        clean_print(f"{Rot}'Verzeihen Sie bitte, dass Sie nicht zufrieden mit unserem Service sind. Für solche Fälle haben wir Mitarbeiter\nhier eine Geschenkkarte im Wert von 50 Euro.'{Grün}'Was wirklich?? Ja dann muss man sich hier ja mal etwas öfters beschweren Hahahahaha. Tschüss!'{Reset}\n\nSie steckt die Karte ein und schlendert weiter, völlig ahnungslos. Doch nun beginnt dein Racheplan zu atmen—wie ein dunkler Gedanke, der endlich Gestalt annimmt. Du rufst die Security an:{Rot}'Hi mein Bester, ich bins {Spielername}. Schau mal, wir haben hier in der Staubsaugerabteilung eine Frau mit blonden Haaren und einer roten Tasche.\nIch sah, wie sie etwas eingesteckt hat. Komm dir das mal anschauen.'{Reset}\n\nDu legst auf und gehst in Deckung, lauerst wie ein Jäger im Neonlicht des Ladens. Der Security-Mann erscheint, breit wie ein Schrank, und marschiert direkt zu der Frau. Du kannst nicht genau hören, was gesprochen wird, also stehst du auf und tust so, als würdest du im Service weiterarbeiten… doch dann siehst du im Augenwinkel, wie ein Schatten sich löst: die Frau holt aus und trifft den Security mit voller Wucht ins Gesicht—er kippt wie ein gefällter Baum!\nSie brüllt:{Grün}\n\n'Sooo sooo, ein Geschenk jaa… warte ab, ich werde dich jetzt suchen und dann erklärst du mir das noch ein Mal..'{Reset}\n\nDein Herz rast, als würde jemand mit Fäusten von innen gegen deinen Brustkorb schlagen. Du duckst dich hinter ein Regal, der Atem stockt dir. Dann, völlig unerwartet, richtet sich der Security-Mann wieder auf, zieht einen Elektroschocker hervor und jagt der Frau eine Ladung Strom durch den Körper—sie fällt wie ein nasser Sack um. Das Chaos sprengt deine Nerven, du kannst nicht mehr. Du flüchtest zur Toilette, während hinter dir die sirrende Stille nach dem Schocker in der Luft hängt.")
                    elif X == 2: # Kundin in Ruhe lassen
                        Social_Credits += 3
                        clean_print(f"Genau in dem Moment, als du die Kundin ziehen lässt, taucht hinter dir die Abteilungsleiterin auf und sagt dir, {Blau}'\nDas hast du aber richtig gut gemacht! Der Chef wird sich freuen zu hören, dass er solch engagierte Mitarbeiter hat. Aber ich muss weiter, bis nachher!'\n\nSoeben hast du dir 3 Social_Credits verdient, und ein kleines Gefühl von Stolz breitet sich in dir aus, deutlich besser als vorhin.")
                    elif X == 3: # Kundin beklauen
                        clean_print("Du holst tief Luft und sagst: 'Zeigen Sie mal her. Was genau funktioniert denn nicht und wie ist es kaputt gegeangen?'. Während Sie erneut von Dingen redet, von denen du keine Ahnung hast, versuchst du dein Glück beim Taschendiebstahl.")
                        #--------------
                        Diebstahl_Schleife(1, 4, Kundin_1_inventar)
                        #--------------
                        if Raub_counter == 0:
                            clean_print("Du konntest bei der Kundin leider nichts stehlen, also lässt du sie einfach weiterziehen.")
                        elif Raub_counter == 1:
                            clean_print("Du freust dich über die Beute, doch plötzlich fällt dir auf, dass der Gegenstand noch eine Diebstahlsicherung hat. Bei genauerem hinschauen fällt dir auf, dass der Gegenstand aus dem Sortiment des Ladens stammt. Du lässt die Kundin weiterziehen, bevor sie dich verdächtigt. Doch du hast jetzt ein anderes Problem: Du hast einen Gegenstand gestohlen, den die Kundin zuvor aus dem Laden gestohlen hat, wenn dich jetzt der Fillialleiter erwischt, wird es schwierig ihm das zu erklären. Du musst den Gegenstand irgendwie loswerden, bevor du Ärger bekommst.")
                        elif Raub_counter >= 2:
                            clean_print("Du hast erfolgreich bei der Kundin gestohlen und konntest mehrere Gegenstände entwenden. Doch plötzlich fällt dir auf, dass einige der Gegenstände noch eine Diebstahlsicherung haben. Bei genauerem hinschauen fällt dir auf, dass die Gegenstände aus dem Sortiment des Ladens stammen. Du lässt die Kundin weiterziehen, bevor sie dich verdächtigt. Doch du hast jetzt ein anderes Problem: Du hast mehrere Gegenstände gestohlen, die die Kundin zuvor aus dem Laden gestohlen hat, wenn dich jetzt der Fillialleiter ertwischt, wird es schwierig ihm das zu erklären. Du musst die Gegenstände irgendwie loswerden, bevor du Ärger bekommst.")
                            Raub_counter = 0
                    elif X == 2: # An Kundin rächen
                            clean_print(f"{Rot} 'Ach nun verstehe ich wovon Sie sprechen. Das Teil was Sie suchen, haben wir zwar nicht hier, aber im Lager. Folgen Sie mir bitte.' {Reset} Du führst die Kundin an einigen Regalen vorbei bis zu einer alten verrosteten Tür. Du öffnest die Tür und sagst {Rot} 'Hier entlang bitte.' {Reset} Die Kundin folgt dir neugierig in den dunklen Lagerraum. Kaum hat sie die Tür hinter sich geschlossen, schließt du sie schnell ab und hörst noch wie Sie an der Tür rüttelt und schreit {Rot} 'Hey! Lassen Sie mich hier raus! Ich will hier raus!' {Reset} Du lachst leise in dich hinein und gehst zurück in den Laden, während die Kundin im dunklen Lagerraum gefangen ist.")
                            clean_print("Nun musst du schnell handeln, beover sich die Kundin befreit. Du gehst direkt zum Büro des Filialleiters und sagst ihm {Rot} 'Ich habe gerade komische geräusche aus dem Lagerraum gehört, doch alle Mitarbeiter sind im Laden, deshalb habe ich den Lagerraum abgeschlossen. Ich glaube da versucht gerade jemand, uns zu beklauen.' {Reser} Während du überlegst sagt er {Rot} 'Besser wir rufen die Polizei, das ist ja eine ernste Sache.' {Reset} Du nickst und sagst {Rot} 'Ja, das ist wohl das beste.' {Reset} Du rufst die Polizei und berichtest von der verdächtigen Person im Lagerraum. Kurz darauf trifft die Polizei ein und befreit die Kundin aus dem Lagerraum. Als Sie abgeführt wird, schaust du Sie an und sagst du zu einem der Polizisten {Rot} 'Leute wie die enden auf der Straße, wie Sie es verdienen' Du lachst erneut in dich hinein und als du gerade wieder an die Arbeit gehen willst sagt der Fillialleiter {Rot} 'Danke für Ihre Hilfe, auf Leute wie Sie kann man sich verlassen. Und falls Sie irgendetwas brauchen: Sie wissen ja, wo Sie mich finden' {Reset}")
                            Social_Credits += 10
            Warte = input()

    Level += 1
clean_print("\n\nDu hast das Ende des ersten Kapitels erreicht.")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#                                                  ******Unterhaltung******


# Das hier ist das Storyregister, wo wir aufschreiben, wo der Spieler am Ende des jeweiligen Storystrangs ist. "..." Bedeutet da müssen wir nich weiterschreiben, wenn dort Nichts steht heißt das, ich bin nicht dazu gekommen, mir diesen Strang anzusehen

#                                                  ******Story-Register****** 
# Level: 0
#
# - 1: - 1: Erfolgreiche Flucht aus dem Lager mit der Kiste
#      - 2: ""
#
# - 2:      ""
#
# Level: 1
#
# - 1: - 1: - 1: - 1: --> XB
#                - 2: - 1: Angriff [bewusstlos, liegen lassen] --> XB
#                     - 2: Angriff [bewusstlos, versteckt] --> XB
#           - 2: --> XB
#      - 2: ... 
#      - 3: --> XB
#
# - 2: - 1: - 1: - 1: Auftrag, Kiste nach oben zu bringen. Vorher Diebstahlversuch beim Filialleiter, ...
#                - 2: Auftrag, Kiste nach oben zu bringen, ...
#           - 2: ...
#           - 3: 
#      - 2: - 1:
#           - 2: - 1:
#                - 2:
#           - 3:
#      - 3: - 1:
#           - 2:
# --------------------------------------------------
# - 1B
# - 2B 