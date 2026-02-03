# Hier werden die Libraries importiert
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from Defs import Defs
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Hier werden alle Variablen deklariert
    # Hier werden die Farben deklariert 
Orange = "\033[33m"
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
dealer_gesehen = False
Startkiste_stehlen = False
Spieler_Inventar = ["Smartphone","Cuttermesser"]

Spieler_Kampfliste = np.array([
                    ["Faustschlag", 5, 10],
                    ["Fußtritt", 10, 5],
                    ["Kinnhaken", 20, 3]
])

Feind_Kampfliste = np.array([
                    ["Faustschlag", 5, 10],
                    ["Fußtritt", 10, 5],
                    ["Kinnhaken", 20, 3]
])

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
Kiste_Inventar = ["Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy", "Handy"]
Kundin_1_inventar = ["Handy", "Tablet", "Air Pods"]
Dealer_Inventar = ["Handy"]


# nimmt deine main-Variablen als Dict
state = globals()
D = Defs()
D.set_state(state)
#Mit D. rufen wir Variablen/Methoden aus der anderen Datei auf

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

P = [1, 0, 0] # Jeder Slot ist für ein Level. Wenn du z.B. an erster Postion Null einträgst wird das erste Level übersprungen. Das macht es einfacher, wenn du ein Level öfter überprüfen willstt und macht es auch übersichtlicher :)

# Story: Startsequenz

if Level == 0 and P[0] == 1:

    D.clear_screen()
    D.clean_print("Es ist stockdunkel. Du erkennst nicht einmal deine eigene Hand. Doch plötzlich – ein flackernder Lichtschein! \nEine defekte LED an der Wand blitzt auf und wirft kaltes Licht in den Raum.Jetzt siehst du sie – \ndie Kiste mit der Aufschrift „iPhone-Lieferung“. Der Grund, warum du hier bist. Dein Herz schlägt schneller. \nNiemand darf dich sehen. Wirst du verschwinden, bevor es zu spät ist [1] – oder die Sache durchziehen und dir dein \n„ehrliches Geld“ verdienen[2]?\n")
    D.get_choice(2)
    if D.X == 1: 
        D.clean_print("Du drehst dich langsam um und schleichst Richtung Ausgang. Warum hast du das überhaupt getan? Die Frage bleibt hängen, unbeantwortet. \nAn der Tür hältst du inne, legst dein Auge ans Schlüsselloch — doch dahinter ist nur Dunkelheit. \nMit einem kurzen Ruck öffnest du die Tür. \nEine Stimme reißt die Stille auf: „Da ist jemand im Lager! Ein Dieb, haltet ihn!“ Die Tür schlägt zu. \nDu drehst dich hhastig um und rennst. Das flackernde LED-Licht zeichnet die Umrisse der Kisten; \nDein Blick fällt auf eine verschlossene Klappe im Boden.Du versuchst, sie zu öffnen — kein Glück. \nJetzt hast du die Wahl: Schau dich um — oder schnapp dir zuerst die einladende Kiste.\n\n")
        D.get_choice(2)
        if D.X == 1:
            D.clean_print("Ein verbogener, verrosteter Nagel ragt aus der Wand der Kiste. Du packst zu und ziehst mit aller Kraft; \nEr gibt nach und kommt knirschend frei. Behutsam steckst du den Nagel ins Schloss, tastest, drehst — und siehe da: \nEin leises Klicken. Die Klappe öffnet sich. Noch einmal prüfst du die Umgebung, nickst dir selbst zu, \ngreifst die Kiste und kletterst hinab — wieder in die Dunkelheit.")
            Warte = input("\nDrücke eine beliebige Taste, um fortzufahren.")
        elif D.X == 2:
            D.clean_print("Du hältst die Kiste fest im Arm, bereit weiterzugehen — doch dann fällt dein Blick auf Etwas Glitzerndes am Boden. \nNeben der Klappe schimmert es schwach im Licht der flackernden LED. Die Gier kriecht in dir hoch. \nDu hältst die Kiste nun nur noch mit einer Hand, beugst dich hinunter und greifst nach dem funkelnden Etwas. \n\nEine Münze. Kupfer. Wertlos. \n\nIn diesem Moment gibt deine andere Hand nach — \ndie Kiste rutscht dir aus den Fingern und kracht auf die Klappe. Ein splitterndes Geräusch hallt durch den Raum. \nDas Schloss ist zerstört. Du starrst kurz fassungslos auf die aufgebrochene Öffnung, \natmest erleichtert auf und steigst mit der Kiste hinab — wieder in die Dunkelheit.")
            Warte = input("\nDrücke eine beliebige Taste, um fortzufahren.")
    elif D.X == 2:
        D.clean_print("Du greifst die Kiste, drehst dich langsam um und schleichst zum Ausgang. An der Tür hältst du inne, \nbeugst dich vor und blickst durch das Schlüsselloch — Nichts. Nur Schwärze. Du atmest tief ein, \nsammelst Mut und drückst die Klinke hinunter. „Da ist jemand im Lager! Ein Dieb, haltet ihn!“ \nDie Worte schneiden wie ein Messer durch die Stille. Du schlägst die Tür zu, drehst dich um und rennst. \nDas flackernde Licht der LED zeigt dir flüchtig den Weg — Umrisse von Kisten, Schatten an der Wand — und da: eine Klappe im Boden. \nDu drehst dich hastig um, um zu sehen, ob dir jemand folgt. In diesem Moment rutscht dir die Kiste aus den Händen und \nkracht auf die Klappe. Ein lautes Knacken hallt durch den Raum. Du hebst die Kiste an — das Schloss ist zerstört. \nErleichtert atmest du auf und steigst mit der Kiste hinab — wieder in die Dunkelheit.")
        Warte = input("\nDrücke eine beliebige Taste, um fortzufahren.")
        D.clear_screen()  
    D.clean_print(f"\nDu läufst gebückt durch einen kleinen Gang, nach einigem Gehen siehst du ein den Eingang zu einem Lüftungsschacht. Du willst weiter gehen, doch du hörst etwas. Du bleibst stehen und horchst: \n{Blau}'Wir sollten uns verbünden, dann könnten wir ihn stürtzen!' \n{Grün}'Pass auf was du sagst, der letzte der so gerdet hat ist verschwunden und zwei Tage später hing sein Kopf am Brunnen in der Innenstadt!' \n{Blau}'Trotzdem können wir es schaffen, dann werden wir der nächste El C...' \n{Grün}'Psssst! Ich hab Etwas aus dem Lüftungsschacht gehört. Hier ist es nicht sicher, lass uns woanders weiterreden!'{Reset}")
Level += 1
D.clean_print("\n\nDu hast das Ende des  Startkapitels erreicht.")
D.Skill(3)



# Level: 1 (Spieler im Unterlager)

if Level == 1 and P[1] == 1:
    Startkiste_stehlen = True
    D.clear_screen()
    D.clean_print(f"Erneut ist es stockdunkel. Ein lautes Tropfen füllt deine Ohren, als würde die Stille selbst gegen dich arbeiten.{Rot} \n\n„Oh Mann, wie konnte mir das passieren? Es ist, als hätte etwas von mir Besitz ergriffen… Ich wollte doch nur kurz eine Kiste holen — \nund dann konnte ich nicht anders.“{Reset} Du spürst, wie sich Schuld und Wut in dir vermischen. \nIm Innern kennst du die Wahrheit über deinen Charakter, doch mit diesen Worten versuchst du, dich der Verantwortung zu entziehen. \nDie Erkenntnis brennt wie Feuer in dir und macht dich zornig. Die Wut fordert eine Reaktion. \nDu stehst nun vor einer Wahl: Trittst du mit voller Wucht gegen den Eimer neben dir, um die Wut hinauszulassen[1],\noder schließt du die Augen und machst eine Atemübung, um dich zu beruhigen?[2]\n")     
    D.get_choice(2)
    if D.X == 1: # Wut-Option
        Leben -= Fußbruch # Spieler verletzt sich, erleidet Schaden
        D.clean_print(f"Von Wut getrieben trittst du mit voller Wucht gegen den nahestehenden Eimer — in der Hoffnung, dass danach alles besser wird \n\n{Rot}'AAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHH!'{Reset}\n\nDer Schmerz fährt wie ein Blitz durch dein Bein. Nun merkst du, dass der Eimer bis obenhin mit Steinen gefüllt war — \nEin scharfes Knacken, dann brennt dein Fuß; irgendwo in dir ahnst du, dass etwas gebrochen ist. \n\n++Du hast nur noch {str(Leben)} Leben. Deine Entscheidungen haben Folgen.++\n\nTrotzdem rollst du, gepeinigt, auf die Knie, kämpfst dich auf die Füße und tastest, von Schmerz begleitet, nach Klebeband.\nMit zitternden Händen willst du die Handys an deinem Körper fixieren — ungesehen, verzweifelt — und sie so hinausschmuggeln.")
        Warte = input("\n\nDrücke eine beliebige Taste, um fortzufahren.")
        D.clear_screen() 
        D.clean_print("Du hast 15 Handys in der Kiste, damit steht dir die Möglichkeit, zu versuchen, alle an deinen Körper zu befestigen. \nSomit stehen dir genau 15 mögliche Versuche für deine Schandtat. Mit 'Ja' befestigst du ein Gerät an deinen Körper, \nmit 'Nein', lässt du die übrigen Smartphones liegen, und versucht mit dem, was du erbeutet hast, zu fliehen. Zu Beginn steht deine Chance bei 20%, \ndass jeglicher Raub glückt. Die Gier kann dich aber in Gefahr bringen, also nutze es mit bedacht.")      
#--------------
        D.Diebstahl_Schleife(15, Kiste_Inventar)
        Startkiste_stehlen = True
#--------------
        if 0 == Raub_counter:
            D.clean_print("Bei dem Versuch, die Handys zu klauen, lässt der enorme Schmerz am Fuß dich nicht konzentriert arbeiten,\nweshalb du kein Handy erbeuten konntest und somit die Kiste in der Ecke liegen lässt.")
        elif 1 <= Raub_counter <= 4:
            D.clean_print(f"Anzahl der erbrachten Beute:{Rot}{Raub_counter}{Reset} \nDas war kein solider Raub, du hast viel liegen lassen, jedoch ist es deine Anfangsphase, weshalb du dich über jedes Handy freust.\n\n")
        elif 5 <= Raub_counter <=8:
            D.clean_print(f"Anzahl der erbrachten Beute:{Grün}{Raub_counter}{Reset} \nDas war ein erfolgreicher Raubzug den du so schnell nicht vergessen wirst.\n\n")
        elif 9 <= Raub_counter:
            D.clean_print(f"Anzahl der erbrachten Beute:{Gold}{Raub_counter}{Reset} \nDu stellst dir schon vor, wie du all diese Geräte verkaufst und damit der jüngste Reiche unter deinen Freunden sein kannst!!!\n\n") 
        
        
        warte = input("Drücke eine beliebige Taste, um fortzufahren..")
        D.clear_screen()

        D.clean_print(f"Gerade als du beschließt, mit dem Wenigen, das du erbeuten konntest, unauffällig die sichere Flucht zu ergreifen, legt sich plötzlich eine schwere Hand von hinten auf deine Schulter.\nFür einen Moment bleibt dir der Atem weg..{Orange}\n\n'Was machst du denn hier?'{Reset} zischt eine Stimme dicht an deinem Ohr. {Orange}'Wieder mal am Klauen?'{Reset}\n\nDein Herz hämmert gegen deine Brust, dein Kopf rast. Du siehst dich schon gefeuert, abgeführt, bloßgestellt. \nDie Stimme kommt dir bekannt vor… und doch kannst du sie im ersten Moment nicht einordnen.\nLangsam, viel zu langsam, drehst du dich um.\n\nUnd dann siehst du ihn.\n\nEs ist… niemand Bestimmtes. Ein Typ. Irgendein komischer Kerl. Sein Blick ist wachsam, sein Grinsen schief.")
        D.visualize("dealer.png")
        dealer_gesehen = True
        D.clean_print(f"\nDu fragst dich, ob er hier überhaupt arbeitet. Oder ob er nur so tut.\nWie kann das sein?\nWer ist dieser Mann?\n\nEr beugt sich näher zu dir und sagt leise, fast verschwörerisch: \n\n{Orange}'Gib mir die Hälfte und ich sage nichts. Hahahahaha.'{Reset}\n\nDu zwingst dich zu einem unsicheren Lachen. Du weißt nicht, ob er dich wirklich erwischt hat – oder ob er nur blufft. Dein Magen zieht sich zusammen.\n\nWas willst du tun?\nIhn fragen, wer er überhaupt ist [1]\nIhm die Hälfte anbieten [2]\nOder alles abstreiten und leugnen, dass du irgendetwas gestohlen hast [3]?")
        D.get_choice(3)
        if D.X == 1:
            D.clean_print(f"{Rot}'Sorry, arbeitest du hier? Ich habe dich noch nie gesehen..'{Reset}\n\nSelbstsicher schaust du ihn an, da sagt er:\n\n{Orange}'Nein aber..hast du ein Problem damit?'{Reset}[1=ja],[2=nein]")
            D.get_choice(2)
            if D.X == 1:
                D.clean_print(f"{Rot}'Natürlich, wie bist du hier rein gekommen, du darfst nicht hier sein.'{Orange}\n'Du darfst doch genauso wenig hier sein, was macht ein normaler Mitarbeiter im Unterlager?\nVor allem mit den gestohlenen Handys, die du an deinem Körper befestigt hast.'{Reset}.\n\nVöllig blass bist du sprachlos, da er natürlich recht hat und dich nun in der Hand hat.\nVersuchst du wegzulaufen[1], oder ihn anzugreifen[2]?")
                D.get_choice(2)
                if D.X == 1: #Weglaufen
                    D.clean_print("Ohne irgendetwas zu sagen rennst du so schnell, wie du kannst und blickst nicht zurück. \nEs ist ein langer Weg, den du hinter dir bringst, bis du endlich am Verkaufsbereich stehst. Doch Zeit, dich auszuruhen ist nicht.")
                elif D.X == 2: #Angriff
                    D.clean_print("Völlig überfordert haust du ihm mit voller Wucht einen Haken in sein Gesicht, sodass er sofort umfällt.\nMöchtest du ihn liegen lassen[1]\noder in eine Ecke verstecken[2]?")
                    D.get_choice(2)
                    if D.X == 1:
                        D.clean_print("Du lässt ihn genau so liegen und rennst nach oben in der Hoffnung, dass dich Niemand gesehen hat. \nIn deinem Kopf ist alles durcheinander und du weißt nicht was mit dir passiert, doch die Zeit erlaubt keine Bedenken.\nOben angekommen versuchst du durch den Verkaufsbereich in die Personalräume zu gelangen, \num die Handys weiter zu verstecken, doch dann passiert das, was immer passiert. ")
                        Knock_Out = True # Das fragen wir später ab um Lvl-übergreifend daran anknüpfen zu können
                        # Der Vorfall mit der bewusstlosen Person soll später wieder aufgegriffen werden
                    elif D.X == 2:
                        D.clean_print("Du ziehst ihn an den Beinen und versuchst ihn an einer Ecke zu verstecken. \nAnschließend legst du einige Kartons über ihn, sodass man ihn nicht sieht und flüchtest.\nDie Flucht trägt dich nach oben in den Verkaufsraum, damit du an ihn vorbei an die Personalräume gelangen kannst.\nLeider stehen auch jetzt Kunden um dich herum und es passiert Folgendes:")
            elif D.X == 2: 
                D.clean_print(f"{Rot}'Nein Nein, mach nur ruhig, lass mich meinen Kram machen und du machst deinen.'{Reset}\nEr schaut dich an, denkt einen Moment nach und sagt anschließend:\n{Orange}'Sieht so aus, als würdest du ein paar Drogen gebrauchen, ich habe was für dich, hier.'{Reset}\nEr drückt dir einen Plastikbeutel in die Hand und zwinkert dir zu. \nDu befürchtest schlimmes, aber bist so sprachlos, dass du dem nichts entgegenwirken kannst. Er sagt:{Orange}'Seit Jahren versorge ich diese Filiale und ich lebe in jenen Mauern'{Reset}\nNach dieser Aussage fragst du dich ob du schon beim Anfassen des Päckchens auf einen Trip geschickt wurdest, \noder was er da sagt...")
                D.clean_print(f"Du überlegst kurz: DU könntest jetzt entweder an dem Päckchen riechen[1], es ebenfalls an deinem Körper befestigen[2] oder es ihm zurückgeben[3] ")
                D.get_choice(3)
                if D.X == 1:
                    D.clean_print(f"Du riechst vorsichtig an dem Päckchen. Plötzlich wird dir schwindelig und schließlich schwarz vor Augen.", Warteschleife,)
                    D.clean_print(f"Du wachst auf, es ist mal wieder stock Dunkel. Als du versuchst dich zu bewegen,, merkst du dass du gefesselt bist und, Moment mal. Die Handys, sie sind weg. Mit deinen Händen ertastest du eine Glasscherbe auf dem Boden und befreist dich von den fesseln. Du tastest dich eine Weile lang im Dunkeln bis du eine Tür ertastest Tür. Du öffnestt sie, tritst heraus und da passiert es: ")
                    while "Handy" in Spieler_Inventar:
                        Spieler_Inventar.remove("Handy")
                        Dealer_Inventar.append("Handy")
                    Startkiste_stehlen = False
                elif D.X == 2:
                    D.clean_print(f"Als du versuchst das Päckchen an deinem Körper zu befestigen siehst du im Augenwinkel, wie er zum Schlag ausholt und weichst aus. Geshockt lässt du das Päckchen fallen und fängst an zu rennen. Sobald du die Tür erreicht hast öffnest du sie und trittst in den Kundenbereich. Doch dann passiert Folgendes:")
                elif D.X == 3:
                    D.clean_print(f"Du gibst ihm das Päckchen zurück und er sagt:{Rot}'Selbst Schuld wenn du eine Kostprobe verpasst.'{Reset} Du machst dich auf den Rückweg und findest schließlich die Tür zum Kundenbereich, öffnest sie und:")
        elif D.X == 2:
            D.clean_print(f"{Rot}Ich möchte ehrlich zu dir sein. Ich habe das Geld dringend nötig, ich habe unter meinem Hemd {Raub_counter} Handys.\n")
            if Raub_counter % 2 == 0: # Prüft, ob die Zahl gerade oder ungerade ist
                D.clean_print(f"Ich biete dir die Hälfte an, somit {Raub_counter // 2}. Was sagst du?{Reset}")
            elif Raub_counter % 2 != 0:
                Raub_counter_hälfte = Raub_counter - 1
                D.clean_print(f"{Rot}Ich biete dir fast die Hälfte an, somit {Raub_counter_hälfte // 2}. Was sagst du?{Reset}'")
            
            D.clean_print(f"\n\nEr mustert dich, erst fragend, dann enttäuscht. Sein Blick schweift durch die Gänge, er winkt jemanden heran. Panik schnürt dir die Kehle zu – du bereust, gestanden zu haben. Und dann, plötzlich, taucht um die Ecke niemand Geringeres als der Filialleiter auf. NEIN! Alles wirbelt an dir vorbei, du bist in die Falle getappt, direkt in seine Falle.")
            D.clean_print(f"Der fremde Mann sagt zum Filialleiter:'{Gold}Wird langsam Zeit, dass wir gehen. Wir müssen nach oben. \nDu hast doch gesagt, dass ich mir einen Sklaven aussuchen kann, oder?{Reset}'\n\n'{Blau}Ja klar, soll es der junge Herr sein?{Reset}\n\nDu, der gerade mitten im Geschehen steht, versteht nichts, \nvöllig verwirrt und noch immer mit Adrenalin im Blut stehst du wie verwurzelt und sagst nichts.\nDu kannst nichts sagen, dieser Mann hat dich in der Hand...")
            D.clean_print("Drücke eine beliebige Taste, um fortzufahren..")
            warte = input()
            D.clear_screen()
            D.clean_print(f"Dein Kopf rast. Du hast nur Sekunden.\nWas, wenn du schlau genug bist, den Filialleiter abzulenken und dem Mann unbemerkt ein Handy unterzuschieben?\nDie Chancen stehen schlecht – ein falscher Schritt, und alles ist vorbei. Aber wenn es gelingt, endet diese lähmende Angst.\n\n[1 = Risiko eingehen]\n[2 = Kein Risiko eingehen]")
            D.get_choice(2)
            if D.X == 1:
                D.clean_print(f"Du wirfst dich vor auf die Knie und schreist ganz laut. Du versuchst einen Schmerz am Bauch vorzutäuschen, \ndamit der Mann näher kommt und das tut er. Er kommt näher und sagt:'{Gold}Was ist los? Ist alles in Ordnung?{Reset}'\n Du greifst eines deiner geklauten Handys und versuchst es in seine Hosentasche zu legen und....\n\n")
                D.geschickter_zug()
                geschickt_Erfolg = 0 ###
                if geschickt_Erfolg == 1: # aus der Def geschickter_zug
                    D.clean_print(f"Nachdem du es geschafft hast, sagst du: '{Rot}Geh mir weg, du Dieb. Von dir brauche ich keine Hilfe.{Reset}'\n\nStille im Raum. Dann erhebt der Mann seine Stimme:\n\n'{Gold}Was redest du? Ich bin kein Dieb!'{Rot} 'Du klaust Handys und hast keinen Respekt vor dem Chef!'\n{Blau}'Nik, was redet er da? Du hast doch nicht schon wieder was geklaut, wir hatten doch darüber geredet. \nWas ist mit dir falsch, Mann??'\n{Gold}'Ich war es nicht! Der ist auf den Kopf gefallen, was redet er da?'\n{Rot}'Schauen Sie sich mal seine Taschen an.'{Reset}\n\nDer Filialleiter blickt hinein, entdeckt das neue iPhone 17 Pro und sagt: \n\n'{Blau}Verschwinde und komm nie wieder hierher. Unsere Geschäfte sind hiermit beendet.{Reset}'\n\nDer Mann verschwindet wütend. Der Chef dreht sich zu dir, reicht dir das iPhone.\n\nDu hast dir soeben 35 Social Credits verdient und das Handy wirst du nachher natürlich versuchen zu stehlen.\n Aber was gerade passiert ist, bleibt unklar, jedoch sollst du das IPhone erstmal oben in den Verkauf bringen. – Zugleich erwartet dich oben aber schon eine Kundin, \ndie auf dich zukommt.")
                    Spieler_Inventar.remove("Handy")
                    Social_Credits += 35
                elif geschickt_Erfolg == 0: # Gewisse Optionen werden das Spielaus bedeuten
                    D.clean_print(f"{Gold}'Guter Versuch, du hast versucht, mich zum Schweigen zu bringen. Hiermit bist du gefeuert.'{Reset}\n\nDer Filialleiter schaut dich nur wütend und Kommentarlos an. Die Enttäuschung macht sich in deren Gesichtern breit, \ndoch tun oder sagen kannst du nichts mehr.")
                    D.clean_print("Drücke eine beliebige Taste, um fortzufahren..")
                    warte = input() 
                    D.clean_print("Der Filialleiter schaut dich kurz an und sagt zu dem Typen \n'Es ist dein Sklave, mach mit ihm was du willst'\nDer Typ kommt auf dich zu und stellt sich hinter dich. Du fühlst dich unwohl und plötzlich zieht er dir eine Plastiktüte über den Kopf. Du bekommst keine Luft mehr und sinkst zu Boden. Das ist das Ende deiner Geschichte") 
                    D.clean_print("\nDu hast das Spiel verloren. Das war ein viel zu riskanter Spielzug, der das Aus bedeutet.")
                    while True:
                        D.X += 1
                        D.X -= 1                      
            elif D.X == 2:
                D.clean_print(f"'{Gold}Ich möchte ihn zum Sklaven machen – als würde ich die ganze Drecksarbeit für dich erledigen. Er übernimmt das einfach. Die Drogen kann er ja für uns verticken.{Reset}'\n\nWas? Drogen? Dein Herz setzt aus. Das kann nicht wahr sein … dein Chef steckt in sowas drin? Du sagst kein Wort. Stumm gehst du nach oben, nur ein Gedanke im Kopf: diese Handys fertig machen. Doch um dorthin zu kommen, musst du am Verkauf vorbei – und kaum setzt du einen Fuß hinein, passiert es.")
        elif D.X == 3:
            D.clean_print(f"{Rot}'Was meinst du? Ich habe nichts genommen. Wie kommt man überhaupt auf sowas?'{Reset}\n\nEr mustert dich mit einem schiefen, fast hinterhältigen Grinsen. Dann sagt er mit einer Stimme, die halb verspielt, halb bedrohlich klingt:\n{Orange}'Jaaa jaaa, ich weiß es. Ich weiß es sogar ganz genau! Beweise? Noch nicht. Aber keine Sorge, ich behalte dich ganz genau im Auge, Sportsfreund.'{Reset}\n\nEin unheilvolles, krächzendes Lachen hallt durch die Gänge, während er in den dunklen Hinterräumen verschwindet. Zurück bleibt nur ein eisiges Gefühl der Unsicherheit und ein Kopf voller Fragen.\n\nDu versuchst, das Geschehene zu ignorieren, atmest tief durch und gehst vorsichtig auf deinen verletzten Fuß gestützt in Richtung Personalräume, um ihn genauer unter die Lupe zu nehmen.\n\nDoch dann passiert genau das, was du schon geahnt hast:")
            



    elif D.X == 2: # Selbstkontrolle-Option
        D.clean_print("Du bewahrst Ruhe und weißt, dass Kontrolle die einzig vernünftige Lösung ist. Also schließt du die Augen, um dich zu entspannen. \nAls du die Augen erneut öffnest, wirst du bleich im Gesicht. Der Filialleiter persönlich steht vor dir.. \n\n")
        D.visualize("Filialleiter.jpg")
        D.clean_print(f"{Blau}'Darf ich fragen, was genau Sie hier machen?'{Reset}\n\nEs hätte nicht schlimmer kommen können, der schmierie Geldsack persönlich steht vor dir, denkst du dir im Inneren.\nWas tust du jetzt? Sagst du ihm die Wahrheit[1], dass du krank bist und dich ausruhen würdest[2] - oder erzählst du ihm, dass du dich verlaufen hast?[3]\n")
        D.get_choice(3)
        D.clean_print(f"{Rot}'Ich… ehm… ich habe versucht, diese Box zu klauen…'{Reset} Er schaut dich einen Moment lang mit einem merkwürdigen Blick an — \nals würde er abwägen, ob du ein Witz bist oder eine Gefahr. Dann bricht er in Gelächter aus und sagt schließlich: {Blau}\n\n„Hahahahahahaha — der war gut! Wer würde schon ins Unterlager gehen, um etwas zu stehlen? Weißt du, du hast meinen Tag gerettet. \nMeine Frau und die Kinder nerven mich gerade ohne Ende, da flüchte ich mich auf die Arbeit.“{Reset}\n\nHilflos denkst du: Wo bin ich hier gelandet? Du wolltest stehlen, nicht seine Lebensgeschichte hören. \nBevor seine Erzählung Fahrt aufnimmt, musst du reagieren. Du sagst, dass du wieder hoch müsstest, denn du hättest viel zu tun.\n")
        if D.X == 1: # Zu beschäftigt für eine Unterhaltung-Option
            D.clean_print(f"{Rot}'Schauen Sie, ich müsste eigentlich noch weiterarbeiten, auch wenn ich am liebsten hier unten bleiben würde.'\n\n{Reset}{Blau}'Das weiß ich doch. Sie sind ein zuverlässiger, vertrauenswürdiger Mitarbeiter. Ach, und bevor Sie es vergessen: \nSie haben die Kiste hier liegen lassen. Bringen Sie sie bitte nach oben, ja?'{Reset}\n\nDu stehst da, erstarrt, während die Realität langsam in dir versickert: Der Filialleiter gibt dir persönlich den Auftrag, \ndie Kiste nach oben zu bringen. Dieser Tag scheint von einem merkwürdigen Schicksal geprägt zu sein — \nein Tag, an dem alles möglich ist.")
            D.clean_print(f"Bevor du dich auf dem Weg machst, macht sich ein Gefühl in dir laut, das das Verlangen erweckt, deinen Chef um einige seine Gegenstände, die er gerade bei sich trägt, zu erleichtern. \nAlso stellst du dir die Frage, soll ich ihn bestehlen[1] {Rot}(Riskant){Reset} oder lieber nicht[2]?")
            D.get_choice(2)
            if D.X == 1:
                #------------------
                D.Diebstahl_Schleife(5, Filialleiter_Inventar)
                #------------------
                D.clean_print("Mit der Kiste machst du dich auf dem Weg nach oben und überlegst, wie du die Handys in der Box sicher klauen kannst.\nDoch im Verkaufsraum passiert das, was immer passiert..")
            elif D.X == 2:
                D.clean_print("Mit der Kiste machst du dich auf dem Weg nach oben und überlegst, wie du die Handys in der Box sicher klauen kannst.\nDoch im Verkaufsraum passiert das, was immer passiert..")
        elif D.X == 2: # Krank-Option
            D.clean_print (f"{Rot}\n'Ich fühle mich heute sehr krank und deshalb musste ich hier eine kleine Pause einlegen.'\nDer Filialleiter erwidert:{Blau}'Und warum genau hier??'{Reset}\nJetzt stehst du da und brichst in Schweißausbrüchen aus. Er fährt fort und sagt.\n{Blau}Hören Sie, Sie scheinen mir kerngesund zu sein. Besser Sie gehen schnell wieder nach oben, \nes gibt noch genug zu tun.'{Rot}'Aber ich habe ein gewisses Unwohlsein und\n ich habe Schmerzen im Bereich des Herzens.'\n{Blau}'Stellen Sie sich mal nicht so an, solange Ihr Herz noch schlägt, ist alles in Ordnung.'\n{Reset}Völlig gekränkt senkst du deine Stimme und fühlst dich vollkommen zertreten.\n {Blau}Und vergessen Sie diese Kiste nicht! Muss ich Ihnen jetzt sagen, wie Ihre Arbeit funktioniert?{Reset}\nNimmst du die Kiste und gehst wieder nach oben[1], oder machst du dich stark und lässt dich nicht von einer autoritären Stimme denunzieren[2]? ")
            D.get_choice(2)
            if D.X == 1:# Kommentarlos nach oben gehen
                D.clean_print(f"Zu tiefst beschämt und zugleich wütend, steigst du wieder hoch in den Verkaufsbereich, um deine Arbeit fortzusetzen.\nDeine Gedanken wirbeln durcheinander, und dir fallen hundert fiese Sprüche ein, wie du ihn kontern könntest.\nDoch keine Sekunde lang kannst du verschnaufen, da ruft eine Kundin'{Grün}\n\n")
            elif D.X == 2: # Gegen Äutorität auflehnen
                D.clean_print(f"\nVon Mut getrieben und einer Wut, die sich breit macht, \ndass du es satt hast, der schwächliche Sklavenarbeiter zu sein,\n richtest du dich auf und sagst:{Rot}'Hören Sie ich brauche manchmal auch meine Pause!\nEs kann nicht sein, dass Sie mich so behandeln.'{Reset}\n\nWährenddessen macht sich ein Gefühl von Selbstsicherheit in dir breit. \nMöchtest du eskalieren und den Chef strategisch in eine Ecke drängen[1], \noder willst du in Tränen ausbrechen, um deinen Plan, die Kiste sicher zu stehlen, abzuschließen[2]?")
                D.get_choice(2)
                if D.X == 1:#Chef anschreien
                    D.clean_print(f"Du beginnst immer lauter zu werden und stampfst mit den Füßen, in Hoffnung, \ndass der Chef klein bei gibt, doch dann, ehe du reagieren kannst, packt er dich am Hals, \ndass nicht einmal deine eigene Stimme hören kannst.\nVöllig verängstigt entsteht eine Stille und er sagt dir:\n{Blau}Wenn ich noch so ein Theater von dir erlebe, bist du fällig.'{Reset}\nDu stürzt zu boden und denkst aber nur daran, dass er dich nicht mit der Kiste in Verbindung setzt.\nOhne weitere Kommentare verschwindet der Chef in mysteriösen Hinterzimmern.")
                    Social_Credits -=15
                    D.clean_print(f"\nDu hast gerade 15 Social Credits verloren. Es sieht ganz schlecht für dich aus.\n Wenn du zu viele Punkte verlierst, kann es zu schweren Konsequenzen führen.\n Dir bleiben noch {Social_Credits} übrig.")
                    D.clean_print("Drücke eine beliebige Taste, um fortzufahren..")
                    warte = input()
                    D.clear_screen()
                    D.clean_print("Als du dich von diesem Übergriff erholt hast, stehst du langsam auf, nimmst die Kiste in die Hand \nund begibst dich emotionslos nach oben in den Verkaufsraum, um daran vorbei, \nan die anderen Lagerstellen zu gelangen.")
                elif D.X == 2: # Tränenausbruch
                    D.clean_print(f"Du brichst also in Tränen aus und hoffst, dass in ihn ein Stück Menschlichkeit noch ist.\n Nach einem langen Monolog von dir sagt der Chef:\n{Blau}'Das habe ich doch nicht so gemeint, Sie müssen sich wieder beruhigen, es tut mir leid,\nbleiben Sie so lange hier, bis es Ihnen besser geht. Ich lasse Sie so lange in Ruhe'{Reset}\n")
                    Social_Credits -=5
                    D.clean_print(f"Du hast gerade 5 Social Credits verloren, jedoch für einen guten Zweck, zu viele riskante Taten,\nkönnen dich aber in Bedrängnis bringen")
                    D.clean_print("Noch einige Zeit weinst du vor dir hin, um die Show aufrecht zu erhalten. \n\nAls du dir sicher bist, dass er weg ist, stehst du auf, nimmst die Kiste und \ngehst wieder in den Verkaufsraum. Du hoffst, die Handys in der Kiste irgendwie noch klauen zu können,\naber erstmal brauchst du einen besseren Plan.")
            elif D.X == 3: # Respektlose-Option
                D.clean_print(f"{Rot}'Hör Mal Opa, dieses Zeug interessiert mich nicht. Klär deine Sachen allein und nerv nicht mich damit.'{Reset}Das hättest du gerne gesagt, stattdessen habt ihr euch hingesetzt und er hat dir von seiner ganzen Geschichte erzählt.")
                Weiter = input("\n\nDrücke eine beliebige Taste, um fortzufahren..")
                D.clear_screen()
                print("\n" * 15 + " " * 60, end="")
                D.Zeit_vergangen(Warteschleife) # Erstellt einen Loading Screen
                D.clear_screen()
                D.clean_print("")
                Social_Credits += 5
                D.clean_print(f"Du hast dir durch das Gespräch mit dem Filialleiter 5 Social_Credits verdient. Somit hast du nun {Social_Credits} Social_Credits.")
                D.clean_print(f"\nDu sagst: {Rot}'Schauen Sie, ich müsste eigentlich noch weiterarbeiten, auch wenn ich am liebsten hier unten bleiben würde.'\n\n{Reset}{Blau}'Das weiß ich doch. Sie sind ein zuverlässiger, vertrauenswürdiger Mitarbeiter. Ach, und bevor Sie es vergessen: \nSie haben die Kiste hier liegen lassen. Bringen Sie sie bitte nach oben, ja?'{Reset}\n\nDu stehst da, erstarrt, während die Realität langsam einsickert: Der Filialleiter gibt dir persönlich den Auftrag, \ndie Kiste nach oben zu bringen. Dieser Tag scheint von einem merkwürdigen Schicksal geprägt zu sein — \nein Tag, an dem alles möglich ist.")
                D.clean_print("Du gehst nun also hoch und und gehst durch den Verkaufsraum, um deinen Raub mit der Kiste \nneu zu planen, doch dann ruft eine Kundin dich.")
        elif D.X == 3: # Verlaufen-Option
            D.clean_print(f"{Rot}'Wissen Sie, ich… ehh… i-ich haab mich verlaufen und da… da wollte i-ich—'{Blau}\n'Sie wollten *was*? Warum stottern Sie so??\nSie dürfen hier überhaupt nicht rein!' {Rot}\n'D-der… dessen bin ich mir bewusst, aber—'\n{Blau}'Unterbrechen Sie mich jetzt auch noch? Das ist eine absolute Frechheit! Ich fasse es nicht.\nDas war Ihre letzte Verwarnung! Wenn ich Sie hier unten noch ein einziges Mal sehe — und das ohne triftigen Grund —\ndann hagelt es eine Abmahnung, klar und deutlich! Verstanden???' {Rot}'Jawohl…' {Blau}\n'Und diese Kiste neben Ihnen…' Er beugt sich leicht vor, sein Blick bohrt sich misstrauisch in Sie.\n'Wollten Sie die etwa… klauen????'{Reset}  [1 = ja]  [2 = nein]")
            D.get_choice(2)
            if D.X == 1:
                D.clean_print(f"{Blau}'Also für solche Spielchen habe ich wirklich keine Zeit. Herr… Herr… wie auch immer — sagen Sie mir eins: Arbeiten Sie überhaupt hier?'\nEr tritt einen Schritt näher, seine Augen verengen sich misstrauisch, als würde er versuchen, direkt in Ihre Gedanken zu sehen.\n'Ich schwöre, ich habe Sie hier noch nie gesehen… nicht ein einziges Mal. Wie ist Ihr Name?'{Reset}")
                Spielername = input("--->")
                D.clean_print(f"{Blau}'Sie sind also {Spielername}…' Seine Stimme wird tiefer, beinahe drohend. Er spricht deinen Namen aus, als würde er ihn schmecken wollen, als ob er ihn sich für später merken müsste.\nLangsam beugt er sich vor, sein Blick bohrt sich in dich wie eine kalte Klinge.\n'Seien Sie sich sicher… ich werde Sie im Auge behalten. Und wehe, ich erwische Sie noch ein einziges Mal hier unten.'{Reset}")
            elif D.X == 2:
                D.clean_print(f"{Blau}'Das will ich auch schwer für Sie hoffen. Da fällt mir gerade ein, ich kenne Sie gar nicht. Arbeiten Sie überhaupt hier?? Wie ist Ihr Name??'{Reset}")
                Spielername = input()
                D.clean_print(f"{Blau}'Sie sind also {Spielername}…' Seine Stimme senkt sich, wird schneidend ruhig, während sein Blick sich wie ein Schatten an Ihnen festklammert. 'Seien Sie sich ganz sicher… ich werde Sie im Auge behalten. Und wehe, ich sehe Sie noch ein einziges Mal hier.'{Reset}")
            Social_Credits -= 5
            D.clean_print(f"\n\nDu hast gerade 5 Social_Credits verloren. Nun bleiben dir nur noch {Social_Credits}.\nPass gut auf, dass du nicht zu viele davon verlierst, sonst warten unangenehme Konsequenzen auf dich.\n\n")
            D.clean_print(f"Zu tiefst beschämt und zugleich wütend, steigst du wieder hoch in den Verkaufsbereich, um deine Arbeit fortzusetzen.\nDeine Gedanken wirbeln durcheinander, und dir fallen hundert fiese Sprüche ein, wie du ihn kontern könntest.\nDoch keine Sekunde lang kannst du verschnaufen, da ruft eine Kundin'{Grün}\n\n")
            
            
    D.clean_print(f"{Grün}\n\n'Verzeihen Sie, ich habe eine kurze Frage'")
    D.visualize("nervige_kundin_glücklich.png")
    D.clean_print(f"{Reset}\n\nWas tust du nun?[1] Sie in den Laden willkommen heißen und bedienen oder [2] weiterlaufen und die Kundin ignorieren?")         
    D.get_choice(2)
    if D.X == 1: # Kundin willkommen heißen und bedienen
            Y = 0
            D.clean_print(f"Du drehst dich zu ihr und sagst{Rot}'Was kann ich für Sie tun?'{Grün}'\nIch möchte ehm alsooo... ich weiß nicht, wie genau das heißt... dieses eine Gerät, wissen Sie, was ich meine?'{Reset}\nVöllig verstört fragst du dich, wovon sie spricht, doch du bleibst ernst und sagst {Rot}'Nein, verzeihen Sie, leider nicht..'{Grün}\n'Ah, dieses eine Teil für meinen Staubsauger! Der funktioniert nicht. Haben Sie ein Ersatzteil davon?'{Rot}'Wie bitte? Ich kann Ihnen nicht folgen.\nWovon reden Sie?'{Reset}\n\nEin weiteres Mal stehst du vor der Wahl: Ob du ihr weiter zuhörst [1], einfach ins Mitarbeiter-Badezimmer flüchtest [2], oder ob du sie ausnimmst wie eine Weihnachtsganz [3].")
            D.get_choice(3)
            D.visualize("nervige_kundin_wütend.png")
            if D.X == 1: # Kundin empfangen
                D.clean_print(f"{Blau}'Ach, Sie haben keine Ahnung… nicht schlimm, einen kompetenten Mitarbeiter werde ich hier schon noch finden.'{Reset}\nEtwas so Asoziales hast du noch nie erlebt, weshalb du erneut vor der Wahl stehst: [1] dich an ihr zu rächen,\noder [2] sie zu ignorieren und einfach weiterzugehen.")
                D.get_choice(3) # An Kundin rächen 
                if D.X == 1:
                    D.clean_print(f"{Rot}'Verzeihen Sie bitte, dass Sie nicht zufrieden mit unserem Service sind. Für solche Fälle haben wir Mitarbeiter\nhier eine Geschenkkarte im Wert von 50 Euro.'{Grün}'Was wirklich?? Ja dann muss man sich hier ja mal etwas öfters beschweren Hahahahaha. Tschüss!'{Reset}\n\nSie steckt die Karte ein und schlendert weiter, völlig ahnungslos. \nDoch nun beginnt dein Racheplan zu atmen—wie ein dunkler Gedanke, der endlich Gestalt annimmt. \nDu rufst die Security an:\n{Rot}'Hi mein Bester, ich bins. Schau mal, wir haben hier in der Staubsaugerabteilung \neine Frau mit blonden Haaren und einer roten Tasche.\nIch sah, wie sie etwas eingesteckt hat. Komm dir das mal anschauen.'{Reset}\n\nDu legst auf und gehst in Deckung, lauerst wie ein Jäger im Neonlicht des Ladens. \nDer Security-Mann erscheint, breit wie ein Schrank, und marschiert direkt zu der Frau.")
                    D.visualize("Security_kontrolliert_kundin.png")
                    D.clean_print(f"\nDu kannst nicht genau hören, was gesprochen wird, also stehst du auf und tust so, \nals würdest du im Service weiterarbeiten… doch dann siehst du im Augenwinkel, \nwie ein Schatten sich löst: die Frau holt aus und trifft den Security mit voller Wucht ins Gesicht—\ner kippt wie ein gefällter Baum!\nSie brüllt:{Grün}\n\n'Sooo sooo, ein Geschenk jaa… warte ab, ich werde dich jetzt suchen und dann \nerklärst du mir das noch ein Mal..'{Reset}\n\nDein Herz rast, als würde jemand mit Fäusten von innen gegen deinen Brustkorb schlagen. \nDu duckst dich hinter ein Regal, der Atem stockt dir. \nDann, völlig unerwartet, richtet sich der Security-Mann wieder auf, \nzieht einen Elektroschocker hervor und jagt der Frau eine Ladung Strom durch den Körper — \nsie fällt wie ein nasser Sack um. Das Chaos sprengt deine Nerven, du kannst nicht mehr. \nDu flüchtest zur Toilette, während hinter dir die sirrende Stille nach dem Schocker in der Luft hängt.")
                elif D.X == 2: # Kundin in Ruhe lassen
                    Social_Credits += 3
                    D.clean_print(f"Genau in dem Moment, als du die Kundin ziehen lässt, taucht hinter dir die Abteilungsleiterin auf und sagt dir, {Blau}'\nDas hast du aber richtig gut gemacht! Der Chef wird sich freuen zu hören, dass er solch engagierte Mitarbeiter hat. Aber ich muss weiter, bis nachher!'\n\nSoeben hast du dir 3 Social_Credits verdient, und ein kleines Gefühl von Stolz breitet sich in dir aus, deutlich besser als vorhin. Du denkst dir {Blau} 'So macht Arbeit Spaß! Ich gönne mir jetzt erstmal eine Pause.'{Reset}\n\nDu machst dich auf den Weg zur Toilette, um eine kleine Auszeit zu nehmen.")
                    Social_Credits += 3
                elif D.X == 3: # Kundin beklauen
                    D.clean_print("Du holst tief Luft und sagst: 'Zeigen Sie mal her. Was genau funktioniert denn nicht und wie ist es kaputt gegeangen?'. Während Sie erneut von Dingen redet, von denen du keine Ahnung hast, versuchst du dein Glück beim Taschendiebstahl.")
                    Y = 1
            elif D.X == 2: # Flucht zur Toilette
                D.clean_print("Du atmest tief durch und sagst: {Rot}'Entschuldigen Sie bitte, aber ich muss auf die Toilette.'{Reset} Daraufhin sagt Sie: {Grün}'Mit dieser Arbeitsmoral werden Sie nicht weit kommen, aber gehen Sie ruhig, wenn Sie nicht anders können.'{Reset} Du antwortest: {Rot}'Sie haben mir die Entscheidung gerade sehr viel einfacher gemacht.'{Reset}, drehst dich um und gehst in Richtung Toiletten.")
            elif D.X == 3: # Kundin beklauen
                D.clean_print("Du holst tief Luft und sagst: {Rot}'Könnten Sie das etwas präziser erklären?'{Reset} Während sie redet versuchst du dein Glück beim Taschendiebstahl.")
                Y = 1
            if Y == 1:
                #--------------
                D.Diebstahl_Schleife(5, Kundin_1_inventar)
                #--------------
                D.clean_print("Nachdem die Kundin ihren Monolog beendet hat, mustert sie dich kurz und sagt: {grün}'Wenn Sie mir nicht helfen können, dann suche ich mir eben jemand anderen.'{Reset}\n\nSie dreht sich um und macht sich auf den Weg zur Kasse. Nachdem sie außer Sichtweite ist, begutachtest du deine Beute:\n")
                if Raub_counter == 0:
                    D.clean_print("Da fällt dir auf: Du konntest bei der Kundin leider nichts erbeuten. Vielleicht hast du beim nächsten Mal ja mehr Glück.\nFrustriert und etwas müde machst du dich auf den Weg zur Toilette, um eine kleine Auszeit zu nehmen.")
                elif Raub_counter == 1:
                    D.clean_print("Du freust dich über die Beute, doch plötzlich fällt dir auf, dass der Gegenstand noch eine Diebstahlsicherung hat. Bei genauerem hinschauen fällt dir auf, dass der Gegenstand aus dem Sortiment des Ladens stammt. Du lässt die Kundin weiterziehen, bevor sie dich verdächtigt. Doch du hast jetzt ein anderes Problem: Du hast einen Gegenstand gestohlen, den die Kundin zuvor aus dem Laden gestohlen hat, wenn dich jetzt der Fillialleiter ertwischt, wird es schwierig ihm das zu erklären. Du musst den Gegenstand irgendwie loswerden, bevor du Ärger bekommst.")
                elif Raub_counter >= 2:
                    D.clean_print("Du hast erfolgreich bei der Kundin gestohlen und konntest mehrere Gegenstände entwenden. Doch plötzlich fällt dir auf, dass einige der Gegenstände noch eine Diebstahlsicherung haben. Bei genauerem hinschauen fällt dir auf, dass die Gegenstände aus dem Sortiment des Ladens stammen. Du lässt die Kundin weiterziehen, bevor sie dich verdächtigt. Doch du hast jetzt ein anderes Problem: Du hast mehrere Gegenstände gestohlen, die die Kundin zuvor aus dem Laden gestohlen hat, wenn dich jetzt der Fillialleiter ertwischt, wird es schwierig ihm das zu erklären. Du musst die Gegenstände irgendwie loswerden, bevor du Ärger bekommst.")
                if Raub_counter >= 1:
                    D.clean_print("Du überlegst kurz und machst dich dann auf den Weg in Richtung Toilette, möglicherweise könntest du die Gegenstände dort unauffällig verstecken und das Problem so aus der Welt schaffen.")
                Raub_counter = 0
            else:
                pass

    elif D.X == 2: # Kundin ignorieren und weiter gehen
        D.clean_print(f"Du ignorierst die Kundin und gehst weiter, doch plötzlich hörst du hinter dir eine Stimme:{Grün}\n\n'Entschuldigung, ich habe Sie etwas gefragt!'")
        D.visualize("nervige_kundin_wütend.png")
        D.clean_print(f"{Reset} Du bleibst stehen, drehst dich um und sagst {Rot}'Oh, verzeihen Sie bitte, ich bin momentan sehr beschäftigt'{Reset} \n\nSie hört dir nicht zu und fängt einfach an zu reden.\n{Grün}\n'Ich suche dieses eine Teil für meinen Staubsauger. Haben Sie so etwas hier?'{Reset}\n\nDu überlegst kurz, dann sagst du {Rot}'Ja natürlich, dort drüben.'{Reset} Du zeigst auf die Decke. Während die Kundin nach oben schaut, versuchst du leise weg zu schleichen.\n")
        D.Schleichen()
        if D.Schleichen_Erfolg == 1:
            print("Geschafft! Aus der Ferne kannst du erkennen, wie sie zuerst verwirrt, aber dann wütend umerherschaut und dich sucht. du solltest dieser Kundin nicht nochmal begegnen.")
        elif D.Schleichen_Erfolg == 0:
            print(f"Die Kundin bemerkt das Geräusch und ruft verärgert {Rot} 'Ey! Wollen Sie sich etwa aus dem Staub machen?!!'{Reset} \nDu bleibst wie erstarrt stehen und überlegst verzweifelt, was du jetzt tun solltest. \nDu könntest dich der Kundin entweder stellen und ihr nun doch helfen [1], \noder du rächst dich an ihr [2].")       
            D.get_choice(2)
            if D.X == 1: # Kundin doch helfen
                D.clean_print(f"Du drehst dich zu ihr und sagst{Rot}'Verzeihen Sie mir mein Auftreten. Was kann ich für Sie tun?'{Grün}'\nLeute wie Sie enden auf der Straße, wie Sie es verdienen, aber wie auch immer. Ich möchte ehm alsooo... ich weiß nicht, wie genau das heißt... dieses eine Gerät, wissen Sie, was ich meine?'{Reset}\nVöllig verstört fragst du dich, wovon sie spricht, doch du bleibst ernst und sagst {Rot}\n'Nein, verzeihen Sie, leider nicht..'{Grün}\n'Ah, dieses eine Teil für meinen Staubsauger! Der funktioniert nicht. Haben Sie ein Ersatzteil davon?'\n{Rot}'Wie bitte? Ich kann Ihnen nicht folgen. Wovon reden Sie?'{Reset}\n\nEin weiteres Mal stehst du vor der Wahl: Ob du ihr weiter zuhörst [1] oder ob du sie ausnimmst wie eine Weihnachtsganz [2].")
                D.get_choice(2)
                if D.X == 1: # Kundin empfangen
                    D.clean_print(f"{Blau}'Ach, Sie haben keine Ahnung… nicht schlimm, einen kompetenten Mitarbeiter werde ich hier schon noch finden.'{Reset}\nEtwas so Asoziales hast du noch nie erlebt, weshalb du erneut vor der Wahl stehst: [1] dich an ihr zu rächen,\noder [2] sie zu ignorieren und einfach weiterzugehen.")
                    D.get_choice(3) 
                    if D.X == 1: # An Kundin rächen
                        D.clean_print(f"{Rot}'Verzeihen Sie bitte, dass Sie nicht zufrieden mit unserem Service sind. Für solche Fälle haben wir Mitarbeiter\nhier eine Geschenkkarte im Wert von 50 Euro.'{Grün}'Was wirklich?? Ja dann muss man sich hier ja mal etwas öfters beschweren Hahahahaha. Tschüss!'{Reset}\n\nSie steckt die Karte ein und schlendert weiter, völlig ahnungslos. Doch nun beginnt dein Racheplan zu atmen—wie ein dunkler Gedanke, der endlich Gestalt annimmt. Du rufst die Security an:{Rot}'Hi mein Bester, ich bins {Spielername}. Schau mal, wir haben hier in der Staubsaugerabteilung eine Frau mit blonden Haaren und einer roten Tasche.\nIch sah, wie sie etwas eingesteckt hat. Komm dir das mal anschauen.'{Reset}\n\nDu legst auf und gehst in Deckung, lauerst wie ein Jäger im Neonlicht des Ladens. Der Security-Mann erscheint, breit wie ein Schrank, und marschiert direkt zu der Frau. Du kannst nicht genau hören, was gesprochen wird, also stehst du auf und tust so, als würdest du im Service weiterarbeiten… doch dann siehst du im Augenwinkel, wie ein Schatten sich löst: die Frau holt aus und trifft den Security mit voller Wucht ins Gesicht—er kippt wie ein gefällter Baum!\nSie brüllt:{Grün}\n\n'Sooo sooo, ein Geschenk jaa… warte ab, ich werde dich jetzt suchen und dann erklärst du mir das noch ein Mal..'{Reset}\n\nDein Herz rast, als würde jemand mit Fäusten von innen gegen deinen Brustkorb schlagen. Du duckst dich hinter ein Regal, der Atem stockt dir. Dann, völlig unerwartet, richtet sich der Security-Mann wieder auf, zieht einen Elektroschocker hervor und jagt der Frau eine Ladung Strom durch den Körper—sie fällt wie ein nasser Sack um. Das Chaos sprengt deine Nerven, du kannst nicht mehr. Du flüchtest zur Toilette, während hinter dir die sirrende Stille nach dem Schocker in der Luft hängt.")
                    elif D.X == 2: # Kundin in Ruhe lassen
                        Social_Credits += 3
                        D.clean_print(f"Genau in dem Moment, als du die Kundin ziehen lässt, taucht hinter dir die Abteilungsleiterin auf und sagt dir, {Blau}'\nDas hast du aber richtig gut gemacht! Der Chef wird sich freuen zu hören, dass er solch engagierte Mitarbeiter hat. Aber ich muss weiter, bis nachher!'\n\nSoeben hast du dir 3 Social_Credits verdient, und ein kleines Gefühl von Stolz breitet sich in dir aus, deutlich besser als vorhin.")
                    elif D.X == 3: # Kundin beklauen
                        D.clean_print("Du holst tief Luft und sagst: 'Zeigen Sie mal her. Was genau funktioniert denn nicht und wie ist es kaputt gegeangen?'. Während Sie erneut von Dingen redet, von denen du keine Ahnung hast, versuchst du dein Glück beim Taschendiebstahl.")
                        #--------------
                        D.Diebstahl_Schleife(5, Kundin_1_inventar)
                        #--------------
                        if Raub_counter == 0:
                            D.clean_print("Du konntest bei der Kundin leider nichts stehlen, also lässt du sie einfach weiterziehen.")
                        elif Raub_counter == 1:
                            D.clean_print("Du freust dich über die Beute, doch plötzlich fällt dir auf, dass der Gegenstand noch eine Diebstahlsicherung hat. Bei genauerem hinschauen fällt dir auf, dass der Gegenstand aus dem Sortiment des Ladens stammt. Du lässt die Kundin weiterziehen, bevor sie dich verdächtigt. Doch du hast jetzt ein anderes Problem: Du hast einen Gegenstand gestohlen, den die Kundin zuvor aus dem Laden gestohlen hat, wenn dich jetzt der Fillialleiter erwischt, wird es schwierig ihm das zu erklären. Du musst den Gegenstand irgendwie loswerden, bevor du Ärger bekommst.")
                            Spieler_Inventar.append("Gegenstände der Kundin")
                        elif Raub_counter >= 2:
                            D.clean_print("Du hast erfolgreich bei der Kundin gestohlen und konntest mehrere Gegenstände entwenden. Doch plötzlich fällt dir auf, dass einige der Gegenstände noch eine Diebstahlsicherung haben. Bei genauerem hinschauen fällt dir auf, dass die Gegenstände aus dem Sortiment des Ladens stammen. Du lässt die Kundin weiterziehen, bevor sie dich verdächtigt. Doch du hast jetzt ein anderes Problem: Du hast mehrere Gegenstände gestohlen, die die Kundin zuvor aus dem Laden gestohlen hat, wenn dich jetzt der Fillialleiter ertwischt, wird es schwierig ihm das zu erklären. Du musst die Gegenstände irgendwie loswerden, bevor du Ärger bekommst.")
                            Spieler_Inventar.append("Gegenstände der Kundin")
                        Raub_counter = 0
                elif D.X == 2: # Kundin beklauen
                    D.clean_print("Du holst tief Luft und sagst: 'Zeigen Sie mal her. Was genau funktioniert denn nicht und wie ist es kaputt gegeangen?'. Während Sie erneut von Dingen redet, von denen du keine Ahnung hast, versuchst du dein Glück beim Taschendiebstahl.")
                    #--------------
                    D.Diebstahl_Schleife(5, Kundin_1_inventar)
                    #--------------
                    if Raub_counter == 0:
                        D.clean_print("Du konntest bei der Kundin leider nichts stehlen, also lässt du sie einfach weiterziehen.")
                    elif Raub_counter == 1:
                        D.clean_print("Du spürst noch das Hochgefühl der Beute, doch plötzlich trifft dich die Erkenntnis: \nDer Gegenstand trägt noch eine aktive Diebstahlsicherung. Als du ihn genauer musterst, wird dir klar,\n dass er eindeutig \naus dem Sortiment des Ladens stammt. Du zwingst dich zur Ruhe und lässt die Kundin weitergehen, \nbevor ihr Misstrauen schöpft. Doch die Gefahr ist nicht vorbei: Du hast einen Gegenstand gestohlen, \nden die Kundin zuvor selbst entwendet hat, und wenn der Filialleiter dich jetzt entdeckt, \nwird es nahezu unmöglich sein, das plausibel zu erklären. \nDu musst den Gegenstand verschwinden lassen, und zwar schnell, bevor alles eskaliert.")
                        Spieler_Inventar.append("Gegenstände der Kundin")
                    elif Raub_counter >= 2:
                        D.clean_print("Der Coup ist gelungen: Du hast der Kundin unbemerkt mehrere Gegenstände abgenommen. \nDoch dann durchzuckt dich ein kalter Gedanke – einige davon tragen noch \neine aktive Diebstahlsicherung. Als du sie genauer prüfst, wird dir klar, dass sie eindeutig \naus dem Sortiment des Ladens stammen. Du bleibst ruhig und lässt die Kundin weitergehen, \nbevor sie misstrauisch wird. Doch das eigentliche Problem beginnt jetzt: Du hast mehrere \nGegenstände gestohlen, die die Kundin zuvor selbst aus dem Laden entwendet hat, \nund wenn der Filialleiter dich jetzt erwischt, wird es nahezu unmöglich sein, \nihm das glaubhaft zu erklären. Du musst die Gegenstände loswerden – \nschnell, bevor der Ärger dich einholt.")
                        Spieler_Inventar.append("Gegenstände der Kundin")
                    Raub_counter = 0
            elif D.X == 2: # An Kundin rächen
                D.clean_print(f"{Rot} 'Ach nun verstehe ich, wovon Sie sprechen. \nDas Teil, was Sie suchen, haben wir zwar nicht hier, es befindet sich jedoch im Lager. \nFolgen Sie mir bitte.' {Reset} \n\nDu führst die Kundin an einigen Regalen vorbei bis zu einer alten verrosteten Tür. \nDu öffnest die Tür und sagst:{Rot}'Hier entlang bitte.'{Reset}\n\nDie Kundin folgt dir neugierig in den dunklen Lagerraum. \nKaum hat sie die Tür hinter sich geschlossen, schließt du sie schnell ab und hörst noch,\n wie Sie an der Tür rüttelt und schreit \n\n{Rot}'Ey! Lassen Sie mich hier raus! Ich will hier raus!' {Reset}\n\n Du lachst leise in dich hinein und gehst zurück in den Laden, während die Kundin \nim dunklen Lagerraum gefangen ist.")
                D.clean_print(f"\nNun musst du schnell handeln, bevor sich die Kundin befreit. Du gehst direkt \nzum Büro des Filialleiters und sagst ihm:\n {Rot} 'Ich habe gerade komische Geräusche aus dem Lagerraum gehört, \ndoch alle Mitarbeiter sind im Verkaufsbereich, weshalb ich den Lagerraum abgeschlossen habe. \nIch glaube da versucht gerade Jemand uns zu beklauen.' {Reset} \nWährend du überlegst sagt er:\n\n {Rot} 'Besser wir rufen die Polizei, das ist ja eine ernste Sache.' {Reset} Du nickst und sagst:\n {Rot} 'Ja, das ist wohl das Beste.' {Reset} Du rufst die Polizei.\nAls die Beamten ankommen, berichtest du von der verdächtigen Person im Lagerraum. \nKurz darauf befreien sie die Kundin aus dem Lagerraum.")
                D.visualize("kundin_verhaftet.png")
                D.clean_print(f"Als Sie abgeführt wird, \nschaust du Sie an und sagst zu einem der Polizisten:\n\n {Rot} 'Leute wie sie enden auf der Straße.' \n\nDu lachst erneut in dich hinein und als du gerade wieder an die Arbeit gehen willst,\nsagt der Fillialleiter:\n{Rot}'Danke für Ihre Hilfe, auf Leute wie Sie kann man sich verlassen. \nUnd falls Sie irgendetwas brauchen: Sie wissen ja, wo Sie mich finden' {Reset}")
                Social_Credits += 10
                D.clean_print(f"Du hast soeben 10 Social Credits erhalten und hast somit insgesamt: {Social_Credits}")
            Weiter = input("\n\nDrücke eine beliebige Taste, um fortzufahren..")          

Level += 1
D.clean_print("\n\nDu hast das Ende des ersten Kapitels erreicht.")
D.Skill(3)

if Level == 2 and P[2] == 1:
    D.clear_screen()
    D.Zeit_vergangen(Warteschleife)
    D.clear_screen()
    D.clean_print(f"Du siehst die weiße Tür der Herrentoilette vor dir. Du drückst die Klinke herunter und gehst in eine der Kabinen hinein. Kaum hast du die Tür hinter dir geschlossen, hörst du, wie sich die Tür der Herrentoilette erneut hinter dir öffnet. Danach hörst du zwei Männer leise miteinander reden: {Orange}'Hast du es?'{Grün}\n'Es ist alles da, du kannst gerne nachzählen.'{Orange}\n'Das werde ich noch. Aber du weißt ja, wenn da etwas fehlt bist du eine wandelnde Leiche hahahaha.'{Grün}\n'Und du genauso wenn in deinem hübschen silbernen Koffer nicht mein Geld ist hahahaha.'{Reset}\n Du hörst es klicken als würde jemand einen Koffer öffnen. Dann hörst du erneut wie sich die Toilettentür öffnet, und die beiden Männer herausgehen. Du atmest tief durch und öffnest die Kabinentür. Du könntest jetzte entweder versuchen, die beiden Männer zu verfolgen [1], dich auf den Weg zum Filialleiterbüromachen um ihm davon zu erzählen [2] oder versuchen zu vergessen, was du gerade gehört hast und wieder an die Arbeit gehen [3].") 
    D.get_choice(3)
    if D.X == 1: # Männer verfolgen
        D.clean_print(f"Du verlässt die Toilette und siehst die beiden Männer gerade noch um die Ecke verschwinden. \nDu folgst ihnen vorsichtig, immer darauf bedacht, nicht entdeckt zu werden. \nDu folgst ihnen bis zum Treppenhaus und siehst, wie sie in den Keller gehen. \nDu folgst ihnen weiter bis sie schließlich in einem der unteren Stockwerke angekommen sind und \nin einem der Kellerräume verschwinden. Du zögerst kurz, folgst ihnen dann aber weiter. \nNachdem du den stock dunkelen Kellerraum betreten hast und einige Schritte gehst, hörst du, \nwie die Tür hinter dir zugeschlagen wird und das Licht angeht. \nDie beiden Männer stehen vor dir und schauen dich an, als wären sie deine Henker.")
        D.visualize("Henker.png")
        if dealer_gesehen == True:
            D.clean_print(f"{Orange}'Schau mal wen wir da haben, einen Dieb. Einen von ganz fieser Sorte.'")

        D.clean_print(f"\n'Es sieht verdammt übel für dich aus, mein Freund'{Reset}\n\nAngst und kalter Schweiß kleben an dir, während die beiden Männer reglos vor dir stehen und dich mustern wie Beute.\n\n{Grün}'Woher kennst du ihn?'\n\n{Orange}'Ein naiver Student, der glaubte, hier schnelles Geld machen zu können.\nWas meinst du… könnte er für uns noch von Nutzen sein?'{Reset}")
        D.clean_print("\n\nDu musst JETZT die Kontrolle über diese Situation an dich reißen!!! Handle klug – jede Sekunde zählt!!!!\nWenn du [1] eingibst, spielst du den Ahnungslosen und hoffst, dass man dir glaubt.\nBei [2] behauptest du, du seist nur wegen einer Reparatur hier und hättest absolut nichts gesehen.")
        D.get_choice(2)
        if D.X == 1:
            D.clean_print(f"{Rot}'Hallo zz..zusammen.. seid ihr neu hier? '{Orange}'Naja wir verfolgen ein paar kleine Ratten, die uns im Weg sehen.\nUnd was macht jemand wie du hier? Hast du uns etwa verfolgt??'{Reset}[1] = ja, [2] = Nein!!")
            D.get_choice(2)
            if D.X == 1:
                D.clean_print(f"{Rot}'Ehh jaa..ich aber nur, weil ein Kunde da war und er Hilfe brauchte...ich ich konnte ihm aber nicht helfen.\n ich habe ihm versprochen jemanden zu rufen.'{Orange}\n'Soo so. Das macht Sinn, wollen wir ihm glauben, Randan?'\n{Grün}'Er scheint mir sehr verängstigt aber ich fijna  jhefn fiajfi fifjgug kajwrj pö,slpgj fgshnjvng so fjis b9dxr jgri'\n\n{Reset}Langsam aber sicher beginnt deine Überforderung die überhand zu gewinnen, \ndu kannst nicht einmal mehr verstehen was die sagen. Dennoch stehst du da und versuchst stark zu bleiben.\n\n ")
            elif D.X == 2:
                D.clean_print("")#Fortsetzun/////////////////////
        elif D.X == 2:
            D.clean_print("")#Fortsetzung///////////////////

    elif D.X == 2: # Filialleiter informieren
        D.clean_print(f"Du gehst direkt zum Büro des Filialleiters, stürmst hinen und stotterst {Rot} 'Ich habe gerade zwei Männer auf der Toilette gehört, die über einen Koffer gesprochen haben. Es klang irgendwie verdächtig.' {Reset} Während du überlegst sagt er {Rot} 'Danke für die Information, ich werde das im Auge behalten. Aber jetzt zurück an die Arbeit.' {Reset} Du nickst und gehst zurück an deinen Arbeitsplatz.")
    elif D.X == 3: # Vergessen und weiterarbeiten
        D.clean_print("Du entscheidest dich, das Gehörte zu vergessen und machst dich wieder an die Arbeit.")


Level += 1
D.clean_print("\n\nDu hast das Ende des zweiten Kapitels erreicht.")
D.Skill(3)
D.clear_screen()
D.Zeit_vergangen(Warteschleife)
D.clear_screen()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#                                                  ******Unterhaltung******


# Das hier ist das Storyregister, wo wir aufschreiben, wo der Spieler am Ende des jeweiligen Storystrangs ist. "..." Bedeutet da müssen wir nich weiterschreiben, wenn dort Nichts steht heißt das, ich bin nicht dazu gekommen, mir diesen Strang anzusehen

#                                                  ******Story-Register****** 
# Level: 0
#
# - 1: - 1: Erfolgreiche Flucht aus dem Lager mit der Kiste --> 1
#      - 2: "" --> 1
#
# - 2:      "" --> 1
#
# Level: 1
#
# - 1: - 1: - 1: - 1: --> XB
#                - 2: - 1: Angriff [bewusstlos, liegen lassen] --> XB
#                     - 2: Angriff [bewusstlos, versteckt] --> XB
#           - 2: --> XB
#      - 2: Tot / --> XB
#      - 3: --> XB
#
# - 2: - 1: - 1: Auftrag, Kiste nach oben zu bringen. --> XB
#                - 2: "" --> XB
#      - 2: - 1: --> XB
#           - 2: - 1: --> XB
#                - 2: --> XB
#           - 3: --> XB
#      - 3: - 1: --> XB
#           - 2: --> XB
# --------------------------------------------------
# - 1B: - 1: - 1: Toilette --> 2
#            - 2: Toilette --> 2
#            - 3: Toilette --> 2
#       - 2: Toilette --> 2
#       - 3: Toilette --> 2
# - 2B: - 1: - 1:
#            - 2:
#       - 2:
# ---------------------------------------------------
# Level: 2
#
# - 1:
#  
#
#----------------------TO DO'S----------------------
#
#- Die Lore der wichtigsten Charaktere weiter schreiben
#- Punktesystem in Story implementieren (--> Bestimmte Entscheidungsoptionen benötigen bestimmte Level vonn Attributen)
#- Alle Fähigkeiten definieren und in die Story implementieren
#- Kampffunktion einführen (--> Verschiedene Arten von Angriffen mit verschiedenen Wahrscheinlichkeiten und Schadenswerten)
#- Kampffunktion implementieren (--> Mehrfach Option zu Kämpfen, Kampf kann mit Tod oder Knock-out enden)
#- Wir dürfen von Level 2 erst weiter schreiben, wenn die Kampffunktion und das Punktesystem fertig gestllt sind
#- Die Variable "Startkiste_stehlen" überall da true setzen wo, er die Kiste nimmt und in den Verkaufsraum geht



#((((((((((-Story-Register))))))))))