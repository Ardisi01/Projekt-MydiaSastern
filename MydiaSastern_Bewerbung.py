import numpy as np
# Hier ist die Ablage für alle Eigenschaften und Attribute, die der Charakter hochleveln kann.
Level = 0
Leben = 100
Rank = "arbeitslos"
Attribute = np.array([["Taschendiebstahl", 0],
                      ["Schlösser knacken", 0],
                      ["Schleichen", 0],
                      ["Redekunst", 0],
                      # Die ersten vier Zeilen sind die Gaunerfähigkeiten
                      ["Stärke", 0],
                      ["Einschüchtern", 0],
                      ["Geschicklichkeit", 0],
                      ["Wahrnehmung", 0],
                      ])
                      # Die nächsten vier Zeilen sind die Jägerfähigkeiten
# Hier sind einige Standartaktionen, die man relativ am Anfang erlernt (Sie sind entweder 0 oder 1. Je nachdem, ob man sie erlernt hat)

# Die Schleifen sind der Rahemn des Spiels, da immer wenn der Spieler Etwas eingibt, für das wir keine Option haben, die ENtscheidung wiederholt werden muss. Durch die Schleifen passiert das automatisch, bis der Spieler eine passende Antwort gibt und es weitergeht
while Level < 10:
    while Level < 1:
        print("Es ist stock Dunkel. Du siehst noch nicht einmal deine eigene Hand vor Augen.")
        Desicion_1 = input("Doch da!\nDu siehst einen lackernden Lichtschein. Er scheint von einer defekten LED zu kommen, die an der Wand neben dir befestigt ist.\nJetzt siehst du auch endlich die Kiste mit der Aufschrift 'IPhone-Lieferung', wegen der du hier eingebrochen bist.\nDu kannst nun entweder verschwinden, um auf keinen Fall erwischt zu werden oder du ziehst die Sache durch und verdienst dir dein 'ehrliches Geld'. Gebe nun '1' oder '2' ein.")
        if Desicion_1 == "1":
            print("Du drehst dich langsam um und machst dich auf den Weg zu Ausgang.\nDu fragst dich, warum du eigentlich hier eingebrochen bist.\nDu hast nun die Tür erreicht und versuchst durch das Schlüsselloch zu schauen, doch du kannst Nichts erkennen.\nDu nimmst all deinen Mut zusammen und öffnest die Tür. Da hörst du eine Stimme die ruft: 'Da ist jemand im Lager! Ein Dieb, haltet ihn!'.\nDu schlägst die Tür noch im selben Moment zu, drehst dich um und rennst los.\nDank der LED kannst du die Umrisse der Kisten erkennen und siehst nun auch eine Klappe im Boden.")
            Desicion_2 = input("Du versuchts die Klappe zu öffnen, doch sie ist verschlossen.\nDu hast nun mehrere Möglichkeiten: Entweder du schaust dich um [1], oder du nimmst zuerst die Kiste, die nun einladend vor dir steht [2].")
            if Desicion_2 == "1":
                print("Du siehst einen verbogenen und verosteten Nagel aus der Wand der Kiste herausragen. Du ziehst mit all deiner Kraft und schaffst es schließlich, ihn herauszuziehen.\nNun steckst du den Nagel in das Schloss, probierst etwas rum und evoila: Die Klappe lässt sich nun öffnen.\nDu schaust dich erneut um, überlegst kurz, greifst dir schließlich die Kiste und steigst mit ihr hinab: Erneut in die Dunkelheit")
            elif Desicion_2 == "2":
                print("Du greifst dir zuerst die Kiste und willst gerade weiter gehen, doch da fällt dir etwas Glizernes auf:\nNeben der Klappe liegt etwas auf dem Boden.\nDu spürst, wie die Gier in dir aufsteigt und und beugst dich ohne zu zögern herunter\num es mit der Hand zu greifen, die nun nicht mehr die Kiste trägt.\nNun siehst du, dass der Gegenstand nur eine wertlose Kupfermünze war.\nNoch im gleichen Moment schwächelt deine andere Hand und die Kiste ruscht dir aus der Hand und fällt geradewegs auf die Klappe.\nMit einem lauten Knacken kommt die Kiste auf. Du hebst sie an und siehst, dass das Schloss durch sie zerstört wurde.\nDu atmest erleichtert auf und steigst mit der Kiste hinab: Erneut in die Dunkelheit.")
            else:
                print("Diese Entscheidung kannst du leider nicht treffen. Bitte versuche es erneut.")
        elif Desicion_1 == "2":
            print("Du greuifst dir die Kiste, drehst dich langsam um und machst dich auf den Weg zu Ausgang.\nDu hast nun die Tür erreicht und versuchst durch das Schlüsselloch zu schauen, doch du kannst Nichts erkennen.\nDu nimmst all deinen Mut zusammen und öffnest die Tür. Da hörst du eine Stimme die ruft: 'Da ist jemand im Lager! Ein Dieb, haltet ihn!'.\nDu schlägst die Tür noch im selben Moment zu, drehst dich um und rennst los.\nDank der LED kannst du die Umrisse der Kisten erkennen und siehst nun auch eine Klappe im Boden.")
            print("Du drehst dich erneut um um zu sehen, ob dir Jemand gefolgt ist.\nDoch da ruscht dir die Kiste aus den Händen und fällt geradewegs auf die Klappe.\nMit einem lauten Knacken kommt die Kiste auf. Du hebst sie an und siehst, dass das Schloss durch sie zerstört wurde.\nDu atmest erleichtert auf und steigst mit der Kiste hinab: Erneut in die Dunkelheit.")
        else:
            print("Diese Entscheidung kannst du leider nicht treffen. Bitte versuche es erneut.")
        # An diesem Punkt kannst du die Story nun weiterführen. Das Level muss nach der ersten Serquenz erhöt werden, damit die While-Schleife endet und die nächste Sewuenz beginnt.
        Level += 1