# Hier werden die Libraries importiert

import numpy as np
import sys
import time
import os
import random


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Hier werden alle Variablen deklariert
    # Hier werden die Farben deklariert  
Gold = "\033[93m"
Grün = "\033[32m"
Rot = "\033[31m"
Blau = "\033[34m"
Reset = "\033[0m" # Setzt Farbe wieder auf weiß

    # Hier werden alle weiteren Variablen Deklariert
Warteschleife = "<---Eine Stunde später--->"
Social_Credits = 20 # Aktionen haben Einfluss -> Credits gewähren dir Erlaubnis oder Ausnahmeregeln bei guter/schlechter Punktzahl -> 20C = Start
Level = 0
Leben = 100
Rank = "Sklavenarbeiter"
Fußbruch = 35
Raub_counter = 0
Raublimit = None
Raubversuch = None
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
Kundin_1_inventar = ["Handy", "Tablet", "Air Ports"]


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Hier werden alle Definitionen deklariert

def situation(Inventar, Skills): # Hiermit können wir uns jederzeit ohne Schreibarbeit die Attribute, das Inventar oder beides anzeigen lassen
    if Inventar == 1:
        print("Das ist dein aktualisiertes Inventar:\n",Spieler_Inventar)
    if Skills == 1:
        print("\n\n",Attribute,"\n\n")

def clean_print(text): # Ruft die DEF auf // Clean ("dein Text") lässt den Text fließend darstellen
    for c in text:
        sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.00000003) #0000000000

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
        print("Dein Glück segnet dich mit einem Level Up im Taschendiebstahl! Glückwunsch!!")
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
        Raub_counter += 1

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

if Level == 0:
    clear_screen()
    clean_print("Es ist stockdunkel. Du erkennst nicht einmal deine eigene Hand. Doch plötzlich – ein flackernder Lichtschein! \nEine defekte LED an der Wand blitzt auf und wirft kaltes Licht in den Raum.Jetzt siehst du sie – \ndie Kiste mit der Aufschrift „iPhone-Lieferung“. Der Grund, warum du hier bist. Dein Herz schlägt schneller. \nNiemand darf dich sehen. Wirst du verschwinden, bevor es zu spät ist – oder die Sache durchziehen und dir dein \n„ehrliches Geld“ verdienen?\n")
    get_choice(2)
    if X == 1: 
        clean_print("Du drehst dich langsam um und schleichst Richtung Ausgang. Warum hast du das überhaupt getan? Die Frage bleibt hängen, unbeantwortet. \nAn der Tür hältst du, legst dein Auge ans Schlüsselloch — doch dahinter ist nur schwarz. \nMit einem kurzen Ruck öffnest du die Tür. \nEine Stimme reißt die Stille auf: „Da ist jemand im Lager! Ein Dieb, haltet ihn!“ Die Tür schlägt zu. \nDu wirfst dich herum und rennst. Das flackernde LED-Licht zeichnet die Umrisse der Kisten; \nDein Blick fällt auf eine verschlossene Klappe im Boden.Du versuchst, sie zu öffnen — kein Glück. \nJetzt hast du die Wahl: Schau dich um — oder schnapp dir zuerst die einladende Kiste.\n\n")
        get_choice(2)
        if X == 1:
            clean_print("Ein verbogener, verrosteter Nagel ragt aus der Wand der Kiste — ein kalter, rostiger Finger. Du packst zu, ziehst mit aller Kraft; \ner gibt nach und kommt knirschend frei. Behutsam steckst du den Nagel ins Schloss, tastest, drehst — und siehe da: \nein leises Klicken. Die Klappe öffnet sich. Noch einmal prüfst du die Umgebung, nickst dir selbst zu, \ngreifst die Kiste und kletterst hinab — wieder in die Dunkelheit.")
            Warte = input("Drücke eine beliebige Taste, um fortzufahren.")
        elif X == 2:
            clean_print("Du hältst die Kiste fest im Arm, bereit weiterzugehen — doch dann fängt dein Blick etwas Glitzerndes am Boden. \nNeben der Klappe schimmert es schwach im Licht der flackernden LED. Gier kriecht in dir hoch. \nDu hältst die Kiste nun nur noch mit einer Hand, beugst dich hinunter und greifst nach dem funkelnden Etwas. \n\nEine Münze. Kupfer. Wertlos. \n\nIn diesem Moment gibt deine andere Hand nach — \ndie Kiste rutscht dir aus den Fingern und kracht auf die Klappe. Ein splitterndes Geräusch hallt durch den Raum. \nDas Schloss ist zerstört. Du starrst kurz fassungslos auf die aufgebrochene Öffnung, \natmest erleichtert auf und steigst mit der Kiste hinab — wieder in die Dunkelheit.")
    elif X == 2:
        clean_print("Du greifst die Kiste, drehst dich langsam um und schleichst zum Ausgang. An der Tür hältst du inne, \nbeugst dich vor und blickst durch das Schlüsselloch — nichts. Nur Schwärze. Du atmest tief ein, \nsammelst Mut und drückst die Klinke hinunter. „Da ist jemand im Lager! Ein Dieb, haltet ihn!“ \nDie Worte schneiden wie ein Messer durch die Stille. Du schlägst die Tür zu, drehst dich um und rennst. \nDas flackernde Licht der LED zeigt dir flüchtig den Weg — Umrisse von Kisten, Schatten an der Wand — und da: eine Klappe im Boden. \nDu drehst dich hastig um, um zu sehen, ob dir jemand folgt. In diesem Moment rutscht dir die Kiste aus den Händen und \nkracht auf die Klappe. Ein lautes Knacken hallt durch den Raum. Du hebst die Kiste an — das Schloss ist zerstört. \nErleichtert atmest du aus und steigst mit der Kiste hinab — wieder in die Dunkelheit.")
        Warte = input("\nDrücke eine beliebige Taste, um fortzufahren.")
        clear_screen()   
    Level += 1


# Level: 1 (Spieler im Unterlager)

if Level == 1:
    clear_screen()
    clean_print(f"Erneut ist es stockdunkel. Ein lautes Tropfen füllt deine Ohren, als würde die Stille selbst gegen dich arbeiten.{Rot} \n\n„Oh Mann, wie konnte mir das passieren? Es ist, als hätte mich etwas Besitz ergriffen… Ich wollte doch nur kurz eine Kiste holen — \nund dann konnte ich nicht anders.“{Reset} Du spürst, wie Schuld und Wut sich in dir vermischen. \nInnerlich kennst du die Wahrheit über deinen Charakter, doch mit diesen Worten versuchst du, die Verantwortung abzuschieben. \nDie Erkenntnis brennt wie Feuer in dir, macht dich zornig und ungestüm. Die Wut fordert eine Reaktion. \nDu stehst nun vor einer Wahl: Trittst du mit voller Wucht gegen den Eimer neben dir, um die Wut hinauszulassen[1],\noder schließt du die Augen und machst eine Atemübung, um dich zu beruhigen?[2]\n")     
    get_choice(2)
    if X == 1: # Wut-Option
        Leben -= Fußbruch # Spieler verletzt sich, erleidet Schaden
        clean_print(f"Von Wut getrieben trittst du mit voller Wucht gegen den nahestehenden Eimer — in der Hoffnung, dass danach alles besser wi— \n\n{Rot}'AAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHH!'{Reset}\n\nDer Schmerz fährt wie ein Blitz durch dein Bein. Du hattest nicht gewusst, dass der Eimer bis obenhin mit Steinen gefüllt war — \nein scharfes Knacken, dann brennt dein Fuß; irgendwo in dir ahnst du, dass etwas gebrochen ist. \n\n++Du hast nur noch {str(Leben)} Leben. Deine Entscheidungen haben Folgen.++\n\nTrotzdem rollst du, gepeinigt, auf die Knie, kämpfst dich auf die Füße und tastest, von Schmerz begleitet, nach Klebeband.\nMit zitternden Händen willst du die Handys an deinem Körper fixieren — ungesehen, verzweifelt — und sie so hinausschmuggeln.")
        clean_print("Du hast 15 Handys in der Kiste, damit steht dir die Möglichkeit, zu versuchen, die alle an deinen Körper zu befestigen. \nSomit stehen dir genau 15 mögliche Versuche für deine Schandtat. Mit 'Ja' befestigst du ein Gerät an deinen Körper, \nmit 'Nein', lässt du die übrigen Smartphones liegen, und versucht mit dem, was du erbeutet hast, zu fliehen. Zu Beginn steht deine Chance bei 20%, \ndass jeglicher Raub erglückt. Die Gier kann dich aber in Gefahr bringen, also nutze es mit bedacht.\n\nMöchtest du beginnen?[1=Ja],[2=Nein]")
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
            clean_print(f"Anzahl der erbrachten Beute:{Gold}{Raub_counter}{Reset} \nDu stellst dir schon vor, wie du all diese Geräte verkaufst und damit der jüngste reiche unter deinen Freunden sein kannst!!!\n\n")
        Raub_counter = 0

    elif X == 2: # Selbstkontrolle-Option
        clean_print("Du bewahrst Ruhe und weißt, dass Kontrolle die einzig vernünftige Lösung ist. Also schließt du die Augen, um dich zu entspannen. \nAls du die Augen erneut öffnest, wirst du bleich im Gesicht. Der Filialleiter persönlich steht vor dir.. \n\n"+Blau+'Darf ich fragen, was Sie hier genau machen?'+Reset+"\n\nEs hätte nicht schlimmer kommen können, dieser geldschmierige Endboss steht persönlich vor dir, denkst du dir im Inneren.\nWas tust du jetzt? Sagst du ihm die Wahrheit - oder erzählst du ihm, dass du dich verlaufen hast?\n")
        get_choice(2)
        if X == 1: # Diebstahlbeichte-Option
            clean_print(f"{Rot}'Ich… ehm… ich habe versucht, diese Box zu klauen…'{Reset} Er schaut dich einen Moment lang mit einem merkwürdigen Blick an — \nals würde er abwägen, ob du ein Witz bist oder Gefahr. Dann bricht er in Gelächter aus und sagt schließlich: {Blau}\n\n„Hahahahahahaha — der war gut! Wer würde schon ins Unterlager gehen, um etwas zu stehlen? Weißt du, du hast meinen Tag gerettet. \nMeine Frau und die Kinder nerven mich gerade ohne Ende, da flüchte ich mich auf die Arbeit.“{Reset}\n\nHilflos denkst du: Wo bin ich hier gelandet? Du wolltest stehlen, nicht seine Lebensgeschichte hören. \nBevor seine Erzählung Fahrt aufnimmt, musst du reagieren. Du sagst entweder, dass du wieder hoch musst, denn du hättest viel zu tun — oder du behauptest, du hättest dich hier versteckt, weil du krank seist -\noder Ihm direkt sagen, dass du kein Bock hast, ihm weiter zuzuhören, du müsstest arbeiten gehen {Rot}(Nicht zu empfehlen){Reset}\nEntscheide weise.\n")
            get_choice(3)
            if X == 1: # Zu beschäftigt für eine Unterhaltung-Option
                clean_print(f"{Rot}'Schauen Sie, ich müsste eigentlich noch weiterarbeiten, auch wenn ich am liebsten hier unten bleiben würde.'\n\n{Reset}{Blau}'Das weiß ich doch. Sie sind ein zuverlässiger, vertrauenswürdiger Mitarbeiter. Ach, und bevor Sie es vergessen: \nSie haben die Kiste hier liegen lassen. Bringen Sie sie bitte nach oben, ja?'{Reset}\n\nDu stehst da, erstarrt, während die Realität langsam einsickert: Der Filialleiter gibt dir persönlich den Auftrag, \ndie Kiste nach oben zu bringen. Dieser Tag scheint von einem merkwürdigen Schicksal geprägt zu sein — \nein Tag, an dem alles möglich ist.")
                clean_print("Bevor du dich auf dem Weg machst, macht sich ein Gefühl in dir laut, das das Verlangen erweckt, deinen Chef um einige seiner Gegenstände, die er gerade mit sich trägt, zu entbinden. Also stellst du dir die Frage, soll ich ihn auf auf mein Risiko bestehlen[1] oder lieber nicht[2]?")
                get_choice(2)             
            #------------------
                Diebstahl_Schleife(1, 4, Filialleiter_Inventar)
            #------------------
            # Fortsetzung/////////////////////////////////
            elif X == 2: # Krank-Option
                clean_print ("")# Fortsetzung///////////////////////////////////
            elif X == 3: # Respektlose-Option
                clean_print(f"{Rot}'Hör Mal Opa, dieses Zeug interessiert mich nicht. Klär deine Sachen allein und nerv nicht mich damit.'{Reset}Das hättest du gerne gesagt, stattdessen habt ihr euch hingesetzt und er hat dir von seiner ganzen Geschichte erzählt.")
                Weiter = input("\n\nDrücke eine beliebige Taste, um fortzufahren..")
                clear_screen()
                print("\n" * 15 + " " * 60, end="")
                Zeit_vergangen(Warteschleife) # Erstellt einen Loading Screen
                clear_screen()
                clean_print("") # Fortsetzung/////////////////////////////
            Social_Credits += 5
            clean_print(f"Du hast dir durch das Gespräch mit dem Filialleiter 5 Social_Credits verdient. Somit hast du nun {Social_Credits} Social_Credits.")

        elif X == 2: # Verlaufen-Option
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
            clean_print(f"Zu tiefst beschämt und zugleich wütend, steigst du wieder hoch in den Verkaufsbereich, um deine Arbeit fortzusetzen.\nDeine Gedanken wirbeln durcheinander, und dir fallen hundert fiese Sprüche ein, wie du ihn kontern könntest.\nDoch keine Sekunde lang kannst du verschnaufen, da ruft eine Kundin'{Grün}\n\n'Verzeihen Sie, ich habe eine kurze Frage'{Reset}\n\nWas tust du nun?[1] Sie in den Laden willkommen heißen und bedienen oder [2] weiterlaufen und die Kundin ignorieren?")
            get_choice(2)
            if X == 1: # Kundin willkommen heißen und bedienen
                clean_print(f"Du drehst dich zu ihr und sagst{Rot}'Was kann ich für Sie tun?'{Grün}'\nIch möchte ehm alsooo... ich weiß nicht, wie genau das heißt... dieses eine Gerät, wissen Sie, was ich meine?'{Reset}\nVöllig verstört fragst du dich, wovon sie spricht, doch du bleibst ernst und sagst {Rot}'Nein, verzeihen Sie, leider nicht..'{Grün}\n'Ah, dieses eine Teil für meinen Staubsauger! Der funktioniert nicht. Haben Sie ein Ersatzteil davon?'{Rot}'Wie bitte? Ich kann Ihnen nicht folgen.\nWovon reden Sie?'{Reset}\n\nEin weiteres Mal stehst du vor der Wahl: Ob du ihr weiter zuhörst [1], einfach ins Mitarbeiter-Badezimmer flüchtest [2], oder ob du sie ausnimmst wie eine Weihnachtsganz [3].")
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
                            clean_print("Du freust dich über die Beute, doch plötzlich fällt dir auf, dass der Gegenstand noch eine Diebstahlsicherung hat. Bei genauerem hinschauen fällt dir auf, dass der Gegenstand aus dem Sortiment des Ladens stammt. Du lässt die Kundin weiterziehen, bevor sie dich verdächtigt. Doch du hast jetzt ein anderes Problem: Du hast einen Gegenstand gestohlen, den die Kundin zuvor aus dem Laden gestohlen hat, wenn dich jetzt der Fillialleiter ertwischt, wird es schwierig ihm das zu erklären. Du musst den Gegenstand irgendwie loswerden, bevor du Ärger bekommst.")
                        elif Raub_counter >= 2:
                            clean_print("Du hast erfolgreich bei der Kundin gestohlen und konntest mehrere Gegenstände entwenden. Doch plötzlich fällt dir auf, dass einige der Gegenstände noch eine Diebstahlsicherung haben. Bei genauerem hinschauen fällt dir auf, dass die Gegenstände aus dem Sortiment des Ladens stammen. Du lässt die Kundin weiterziehen, bevor sie dich verdächtigt. Doch du hast jetzt ein anderes Problem: Du hast mehrere Gegenstände gestohlen, die die Kundin zuvor aus dem Laden gestohlen hat, wenn dich jetzt der Fillialleiter ertwischt, wird es schwierig ihm das zu erklären. Du musst die Gegenstände irgendwie loswerden, bevor du Ärger bekommst.")
                        Raub_counter = 0
                    # Fortsetzung 
            elif X == 2: # Kundin ignorieren und weiter gehen
                clean_print(f"Du ignorierst die Kundin und gehst weiter, doch plötzlich hörst du hinter dir eine Stimme:{Grün}\n\n'Entschuldigung, ich habe Sie etwas gefragt!' {Reset} Du bleibst stehen, drehst dich um und sagst {Rot}'Oh, verzeihen Sie bitte, ich bin momentan sehr beschäftigt' Sie hört dir nicht zu und fängt einfach an zu reden{Grün}\n'Ich suche dieses eine Teil für meinen Staubsauger. Haben Sie so etwas hier?'{Reset}\n\nDu überlegst kurz, dann sagst du {Rot}'Ja natürlich, dort drüben.' {Reset} Du zeigst auf die Decke. Während die Kundin nach oben schaut, versuchst du leise weg zu schleichen.")
                Schleichen()
                if Schleichen_Erfolg == 1:
                    print("Geschafft! Aus der Ferne kannst du erkennen, wie sie zuerst verwirrt, aber dann wütend umerherschaut und dich sucht. du solltest dieser Kundin nicht nochmal begegnen.")
                elif Schleichen_Erfolg == 0:
                    print("Die Kundin bemerkt das Geräusch und ruft verärgert {Rot} 'Hey! Wollen Sie sich etwa aus dem Staub machen?!!'{Reset} Du bleibst wie erstarrt stehen und überlegst verzweifelt, was du jetzt tun solltest. Du könntest dich der Kundin entweder stellen und ihr nun doch helfen [1], oder du rächst dich an ihr [2].")       
                    get_choice(2)
                    if X == 1: # Kundin doch helfen
                        clean_print(f"Du drehst dich zu ihr und sagst{Rot}'Verzeihen Sie mir mein Auftreten. Was kann ich für Sie tun?'{Grün}'\nLeute wie Sie enden auf der Straße, wie Sie es verdienen, aber wie auch immer. Ich möchte ehm alsooo... ich weiß nicht, wie genau das heißt... dieses eine Gerät, wissen Sie, was ich meine?'{Reset}\nVöllig verstört fragst du dich, wovon sie spricht, doch du bleibst ernst und sagst {Rot}'Nein, verzeihen Sie, leider nicht..'{Grün}\n'Ah, dieses eine Teil für meinen Staubsauger! Der funktioniert nicht. Haben Sie ein Ersatzteil davon?'{Rot}'Wie bitte? Ich kann Ihnen nicht folgen.\nWovon reden Sie?'{Reset}\n\nEin weiteres Mal stehst du vor der Wahl: Ob du ihr weiter zuhörst [1], einfach ins Mitarbeiter-Badezimmer flüchtest [2], oder ob du sie ausnimmst wie eine Weihnachtsganz [3].")
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
                                    clean_print("Du freust dich über die Beute, doch plötzlich fällt dir auf, dass der Gegenstand noch eine Diebstahlsicherung hat. Bei genauerem hinschauen fällt dir auf, dass der Gegenstand aus dem Sortiment des Ladens stammt. Du lässt die Kundin weiterziehen, bevor sie dich verdächtigt. Doch du hast jetzt ein anderes Problem: Du hast einen Gegenstand gestohlen, den die Kundin zuvor aus dem Laden gestohlen hat, wenn dich jetzt der Fillialleiter ertwischt, wird es schwierig ihm das zu erklären. Du musst den Gegenstand irgendwie loswerden, bevor du Ärger bekommst.")
                                elif Raub_counter >= 2:
                                    clean_print("Du hast erfolgreich bei der Kundin gestohlen und konntest mehrere Gegenstände entwenden. Doch plötzlich fällt dir auf, dass einige der Gegenstände noch eine Diebstahlsicherung haben. Bei genauerem hinschauen fällt dir auf, dass die Gegenstände aus dem Sortiment des Ladens stammen. Du lässt die Kundin weiterziehen, bevor sie dich verdächtigt. Doch du hast jetzt ein anderes Problem: Du hast mehrere Gegenstände gestohlen, die die Kundin zuvor aus dem Laden gestohlen hat, wenn dich jetzt der Fillialleiter ertwischt, wird es schwierig ihm das zu erklären. Du musst die Gegenstände irgendwie loswerden, bevor du Ärger bekommst.")
                                Raub_counter = 0
                        elif X == 2: # An Kundin rächen
                            clean_print(f"{Rot} 'Ach nun verstehe ich wovon Sie sprechen. Das Teil was Sie suchen, haben wir zwar nicht hier, aber im Lager. Folgen Sie mir bitte.' {Reset} Du führst die Kundin an einigen Regalen vorbei bis zu einer alten verrosteten Tür. Du öffnest die Tür und sagst {Rot} 'Hier entlang bitte.' {Reset} Die Kundin folgt dir neugierig in den dunklen Lagerraum. Kaum hat sie die Tür hinter sich geschlossen, schließt du sie schnell ab und hörst noch wie Sie an der Tür rüttelt und schreit {Rot} 'Hey! Lassen Sie mich hier raus! Ich will hier raus!' {Reset} Du lachst leise in dich hinein und gehst zurück in den Laden, während die Kundin im dunklen Lagerraum gefangen ist.")
                            clean_print("Nun musst du schnell handeln, beover sich die Kundin befreit. Du gehst direkt zum Büro des Filialleiters und sagst ihm {Rot} 'Ich habe gerade komische geräusche aus dem Lagerraum gehört, doch alle Mitarbeiter sind im Laden, deshalb habe ich den Lagerraum abgeschlossen. Ich glaube da versucht gerade jemand, uns zu beklauen.' {Reser} Während du überlegst sagt er {Rot} 'Besser wir rufen die Polizei, das ist ja eine ernste Sache.' {Reset} Du nickst und sagst {Rot} 'Ja, das ist wohl das beste.' {Reset} Du rufst die Polizei und berichtest von der verdächtigen Person im Lagerraum. Kurz darauf trifft die Polizei ein und befreit die Kundin aus dem Lagerraum. Als Sie abgeführt wird, schaust du Sie an und sagst du zu einem der Polizisten {Rot} 'Leute wie die enden auf der Straße, wie Sie es verdienen' Du lachst erneut in dich hinein und als du gerade wieder an die Arbeit gehen willst sagt der Fillialleiter {Rot} 'Danke für Ihre Hilfe, auf Leute wie Sie kann man sich verlassen. Und falls Sie irgendetwas brauchen: Sie wissen ja, wo Sie mich finden' {Reset}")
                            Social_Credits += 10
            Warte = input()
    Level += 1


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#                                                  ******Unterhaltung******
#