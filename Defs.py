import numpy as np
import sys
import time
import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Button

#-------------------------------------------------------------------------------------------------------------------------

# Mit self. rufen wir Variablen/Methoden aus der anderen Funktion auf
# self, muss in jede def, die Werte einer anderen Funktion nutzt
class Defs:
    def __init__(self): 
        self.state = None
        self.X = None
        self.Erfolg = 0
        self.Beute = None
        self.Win = 0
        self.Y = 0
    def set_state(self, state: dict):
        self.state = state

#-------------------------------------------------------------------------------------------------------------------------

# Saubere Übergänge
    def Übergang(self):
        input("\nDrücke eine beliebige Taste, um fortzufahren.")

#-------------------------------------------------------------------------------------------------------------------------

# Anzeige von Inventar und/oder Fähigkeiten
    def situation(self, Inventar, Skills): 
        if Inventar == 1:
            print("Das ist dein aktualisiertes Inventar:\n", self.state["Spieler_Inventar"])
        if Skills == 1:
            print(self.state["Fähigkeiten"], "\n\n")


#-------------------------------------------------------------------------------------------------------------------------

# Text fließend schreiben lassen
    def clean_print(self, text):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.000006)

#-------------------------------------------------------------------------------------------------------------------------

# Text fließend langsam schreiben lassen
    def Slow_print(self, text):  
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.5)

#-------------------------------------------------------------------------------------------------------------------------

# Löscht vorherige Eingaben im Terminal 
    def clear_screen(self):  
        os.system("cls" if os.name == "nt" else "clear")

#-------------------------------------------------------------------------------------------------------------------------

# Nach einer geglückten Aktion erhält der Spieler die Chance auf ein Lvl-Up der jeweiligen Fähigkeit
    def Lvl_Up(self, Zeile): # Die Zeile der Fähigkeit muss hier eingetragen werden (Bsp.: Deibstahl: Zeile: 1)
        if random.choice([1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1:
            self.state["Fähigkeiten"][Zeile-1, 1] += 1
            print("Dein Glück segnet dich mit einem Level Up im "+self.state["Fähigkeiten"][Zeile-1, 0]+"! Glückwunsch!!")
            self.situation(0, 1), self.Übergang()

#-------------------------------------------------------------------------------------------------------------------------

# Leitet eine Diebstahl-Schleife ein, bis der Diebstahl missglückt oder abbgebrochen wird
    def Diebstahl_Schleife(self, Versuche, Ziel_inventar):
        Y, Zähler, Raubcounter = 0
        A = len(self.state["Spieler_Inventar"])
        while Y < Versuche:
            Zähler += 1
            print(f"\n\n{Versuche}.Versuch: Mit [1] kannst du stehlen, mit [2] kannst du den Raubzug abbrechen.")
            self.get_choice(2)
            if self.X == 1:
                self.Diebstahl(Ziel_inventar)
                Raubcounter = len(self.state["Spieler_Inventar"]) - A
                Y += 1
                if self.Erfolg == 1:
                    self.situation(1, 0), self.Übergang()
            elif self.X == 2:
                return Raubcounter
        return Raubcounter

#-------------------------------------------------------------------------------------------------------------------------

# Versuch eines Diebstahls bei einem Zielinventar (Das Ziel ist eine Liste die wir beim Aufrufen definieren)
    def Diebstahl(self, Ziel_inventar):
        self.Beute = None
        if Ziel_inventar == []:
            print("Hier ist Nichts mehr zu holen")
            return Ziel_inventar
        lvl = self.state["Fähigkeiten"][0, 1]
        if lvl % 2 != 0:
            lvl += 1

        self.Erfolg = random.choice(np.concatenate((np.ones(lvl), np.zeros(10-lvl))))

        if self.Erfolg == 1:
            self.Beute = random.choice(Ziel_inventar)
            self.state["Spieler_Inventar"].append(self.Beute)
            Ziel_inventar.remove(self.Beute)
            self.Lvl_Up(1)
            print("Der Diebstahl war erfolgreich! Du hast Folgendes erbeutet:", self.Beute,"\n"+"-"*150)
        else:
            self.clean_print("Du hattest leider keinen Erfolg!\n"+"-"*150)

#-------------------------------------------------------------------------------------------------------------------------

# Versuch von unbemerkter Bewegung (Besonderheit, die Belohnung für Erfolge sind hier zusätzlich Chancen auf Lvl_Ups in Diebstahl und Geschicklichkeit)
    def Schleichen(self):
        lvl = self.state["Fähigkeiten"][2, 1]
        if lvl % 2 != 0:
            lvl += 1

        self.Erfolg = random.choice(np.concatenate((np.ones(lvl), np.zeros(10-lvl))))

        if self.Erfolg == 1:
            print("\nDu bist erfolgreich geschlichen, Niemand hat dich gehört!\n")
            self.Lvl_Up(1), self.Lvl_Up(3), self.Lvl_Up(7)
        else:
            print("\nOh nein! Du bist auf irgendetwas draufgetreten und hast ein Geräusch gemacht!\n")
        self.Übergang()

#-------------------------------------------------------------------------------------------------------------------------

# Versuch eines geschickten Manövers
    def geschickter_zug(self):
        lvl = self.state["Fähigkeiten"][6, 1]
        if lvl % 2 != 0:
            lvl += 1

        self.Erfolg = random.choice(np.concatenate((np.ones(lvl), np.zeros(10-lvl))))

        if self.Erfolg == 1:
            print("Das war ein geschickter Zug und es ist Niemandem aufgefallen.")
            self.Lvl_Up(7)
        else:
            print("Oh nein! Du warst nicht erfolgreich!!")
        self.Übergang()

#-------------------------------------------------------------------------------------------------------------------------

# Noch nicht überarbeitet
    def Überreden(self, zielinventar):
        Redeliste_1 = ["Ich glaube, wir wollen im Kern eigentlich das Selbe.", "Es gibt einen Aspekt, der mir dabei besonders wichtig erscheint.", "Was wäre, wenn wir das einmal pragmatisch betrachten?", "Ich sehe hier eine Möglichkeit, von der wir beide profitieren könnten.", "Es geht weniger um das Ob, als vielmehr um das Wie.","Das scheint eine gute Idee zu sein, doch dafür sind meine Fähigkeiten unabdingbar.","Ich finde, man kann es noch lokrativer gestalten."]
        Redeliste_2 = ["Ich habe über unser letztes Gespräch noch einmal nachgedacht.", "Mir ist seitdem ein Punkt klarer geworden, den ich gern ergänzen würde.", "Vielleicht habe ich mich beim ersten Mal nicht präzise genug ausgedrückt.", "Ich denke man hat mich gerade nicht ganz verstanden.","Die Notwendigkeit besteht darin, es sich mal bildhaft vorzustellen."]
        Redeliste_3 = ["Das ist mein letzter Versuch, meine Sicht verständlich zu machen.", "Ich wollte sicherstellen, dass dieser Gedanke nicht unausgesprochen bleibt.","Am Besten lassen wir das Ganze hier noch einmal Revue passieren, möglicherweise wird sich die Situation klarer lichten."]
        lvl = self.state["Fähigkeiten"][3, 1]

        if 1 <= lvl:
            self.Übergang()
            self.clean_print("\nDu überlegst kurz und sagst dann:\n" + random.choice(Redeliste_1) + "\n")
            self.Redeerfolg = random.choice([1, 0, 0]) # 33,3%
        if self.Redeerfolg == 0 and 4 <= lvl:
            self.clean_print("Es scheint, als hätte der Versuch keinen Erfolg gebracht, weshalb du es nochmal versuchst.")
            self.Übergang()
            self.clean_print("\nDu überlegst kurz und sagst dann:\n" + random.choice(Redeliste_2) + "\n")
            self.Redeerfolg = random.choice([1, 1, 0, 0, 0]) # 40%
        if self.Redeerfolg == 0 and 7 <= lvl:
            self.clean_print("Es scheint, als hätte der Versuch keinen Erfolg gebracht, weshalb du es nochmal versuchst.")
            self.Übergang()
            self.clean_print("\nDu überlegst kurz und sagst dann:\n" + random.choice(Redeliste_3) + "\n")
            self.Redeerfolg = random.choice([1, 0]) # 50%
            if lvl >= 8:
                self.clean_print("Langsam aber sicher findet man gefallen an deiner Sprachwahl und du wirst hierfür respektiert.\nDafür erhälst du 15 Social Credits.")
                self.state ["Social_Credits"] += 15
                self.clean_print(f" Somit hast du insgesamt {self.state["Social_Credits"]} Social Credits.")
        if self.Redeerfolg == 1:
            self.clean_print("Das Gespräch hat sich durch deine Redekunst zu deinen Gunsten gewendet, herzlichen Glückwunsch!!")
            if lvl == 9: 
                self.clean_print("\nWährend dein Überredungsversuch voran geht, überkommt dich das Bedürfnis, deinen Gesprächspartner um seine persönlichen Gegenstände zu erleichtern. Du hast 1 Versuch!\n")
                self.Diebstahl_Schleife(1, zielinventar)
            elif lvl == 10:
                self.clean_print("\nWährend dein Überredungsversuch voran geht, überkommt dich das Bedürfnis, deinen Gesprächspartner um seine persönlichen Gegenstände zu erleichtern. Du hast 3 Versuche!\n")
                self.Diebstahl_Schleife(3, zielinventar)
        else:
            self.clean_print("Dein Überredungsversuch bleibt diesmal leider ohne Erfolg, dennoch erhälst du für den Mut, es zu versuchen, 5 Social Credits.")
            self.state ["Social_Credits"] += 5
            self.clean_print(f" Somit hast du insgesamt {self.state["Social_Credits"]} Social Credits.")

        self.Übergang(), self.clear_screen()
        return self.Redeerfolg

#-------------------------------------------------------------------------------------------------------------------------

# Noch nicht überarbeitet
    def Schloss_knacken(self, Schloss_Qualität, Kisten_Inventar):
        counter = 0
        self.Erfolg = 0
        if "Dietrich" in self.state["Spieler_Inventar"]:
            self.Übergang(), self.clear_screen()
            self.clean_print("Du hast dich also dazu entschieden, das Schloss zu knacken. Wollen wir doch mal sehen, ob du es drauf hast, viel Glück!!")
            self.clean_print("\nDu hast es hier mit einem Schloss der Schwierigkeitsstufe " + str(Schloss_Qualität) + " zu tun.\nNun weißt du, worauf du dich einlässt.")
            self.clean_print("\n\nDu tastet dich mit dem Dietrich vorsichtig in das Schloss hinein, bis du einen leichten Widerstand spürst. Du probierst etwas rum bis du hörst, wie der Dietrich einrastet.")
            self.clean_print("\n\nMöchtest du nun [1]versuchen, den Dietrich herum zu drehen und das Schloss zu öffnen, oder [2]versuchen dich weiter vor zu tasten, um auch wirklich alle Boltzen herunterzudrücken?\n")
            self.get_choice(2)
            if self.X == 1:
                if Schloss_Qualität == 1 or Schloss_Qualität == 2:
                    Bruch_Wahrscheinlichkeit = random.choice([1, 1, 0, 0]) # 50%, dass der Spieler sein Dietrich verliert, weil er sein Dietrich frühzeitig umdreht
                    if Bruch_Wahrscheinlichkeit == 1:
                        self.state["Spieler_Inventar"].remove("Dietrich")
                        self.clean_print("\nLeider ist dein Dietrich bei dem frühzeitigen Drehen abgebrochen und kann nicht weiter genutzt werden.\n")
                    elif Bruch_Wahrscheinlichkeit == 0:
                        self.Erfolg = random.choice([1, 1, 1, 1 ,1 ,1 ,1 ,0 ,0 ,0]) # 70% - Schlössern mit erster Methode
                if Schloss_Qualität == 3:
                    bad_luck = random.choice([1, 1, 0]) # Wenn Stufe 3, dann 66,6% Chance, dass der Dietrich abbricht
                    if bad_luck == 1:
                        self.state["Spieler_Inventar"].remove("Dietrich")
                        self.clean_print("\nLeider ist dein Dietrich bei dem frühzeitigen Drehen abgebrochen und kann nicht weiter genutzt werden.\n")
                    elif bad_luck == 0:
                        self.Erfolg = random.choice(np.concatenate((np.ones(self.state["Fähigkeiten"][1, 1]+4),np.zeros(10 - self.state["Fähigkeiten"][1, 1]+4))))
                        #Lösch: Wenn das erreicht wird, soll der Spieler mit einer weiteren Sache belohnt werden, dass er bei einem Level 3 riskiert hat

            elif self.X == 2:
                if Schloss_Qualität == 1:
                    self.Erfolg = random.choice([1, 1, 1, 0]) # 75%
                if Schloss_Qualität > 1: # bei Stufe 2 und 3 so viel Prozent wie das Attribut gelevelt ist (1 --> 10%)
                    self.Erfolg = random.choice(np.concatenate((np.ones(self.state["Fähigkeiten"][1, 1]),np.zeros(10 - self.state["Fähigkeiten"][1, 1]))))
                if self.Erfolg == 0 and Schloss_Qualität == 2: # Bei Stufe 2 gibt es dann noch einen Versuch, bei 3 nicht mehr
                    self.Erfolg = random.choice(np.concatenate((np.ones(self.state["Fähigkeiten"][1, 1]),np.zeros(10 - self.state["Fähigkeiten"][1, 1])))) 
                if Schloss_Qualität == 3:
                    bad_luck = random.choice([1, 0]) # Wenn Stufe 3, dann 50% Chance, dass der Dietrich abbricht
                    if bad_luck == 1:
                        self.state["Spieler_Inventar"].remove("Dietrich")
            if self.Erfolg == 1:
                self.clean_print("Herzlichen Glückwunsch, du hast das Schloss geknackt!!\n")
                self.clean_print("Hier ist deine Beute:\n\n" + str(Kisten_Inventar))
                self.state["Spieler_Inventar"].append(Kisten_Inventar)
                Kisten_Inventar = []
            elif self.Erfolg == 0:
                self.clean_print("Schade, diesmal hat es leider nicht funktioniert, aber vielleicht beim nächsten Mal.")
                self.Übergang()
            return self.Erfolg, Kisten_Inventar, self.state["Spieler_Inventar"]
        else: 
            self.clean_print("Leider trägst du keinen Dietrich mit dir, um irgendetwas zu knacken.")
            return self.Erfolg, Kisten_Inventar, self.state["Spieler_Inventar"]
                
#-------------------------------------------------------------------------------------------------------------------------

# Funktion für Entscheidungen (Anzahl an Möglichkeiten wird eingetragen)
    def get_choice(self, option_number): 
            while True:
                list_2 = list(range(1, option_number+1))
                try:
                    choice = int(input("\nGib eine der oben genannten Zahlen ein:-> "))
                    if choice in list_2:
                        self.X = int(choice)
                        return self.X 
                except ValueError: 
                    self.clean_print(random.choice([
                        "So kommst du hier nicht weiter.",
                        "Probier es anderweitig nochmal",
                        "Das ist nicht das, wonach du gefragt wurdest."
                    ]))
   
#-------------------------------------------------------------------------------------------------------------------------

# Noch nicht überarbeitet
    """
    def ability_choice(self, Diebstahl, Fliehen, Redekunst, Kampf, Raublimit, Zielinventar, Schloss_Qualität, Spieler_HP, Feind_HP, To_the_Death):
        option_list_1 = [Diebstahl, Fliehen, Redekunst, Kampf]
        option_list_2 = ["Etwas klauen/knacken, ", "Versuchen zu fliehen, ", "Die Person von dir Überzeugen, ", "Gegen die Person kämpfen kämpfen"]
        for x in option_list_2[x-1]:
            if option_list_1[x-1] != 1:
                option_list_2[x-1] = ""
        self.clean_print("Möchtest du " + option_list_2[0] + option_list_2[1] + option_list_2[2] + option_list_2[3] + "?\n")
        self.get_choice()
        if option_list_1[0] == 1
    """

#-------------------------------------------------------------------------------------------------------------------------

# Am Ende jedes Levels gibt der Spieler Skill-Punkte für bestimmte Fähigkeiten aus und formt so sienen individuellen Charakter
    def Skill(self, Skill_Punkte):
        episch_counter_G = 0
        self.clear_screen()
        self.clean_print(f"Bevor du in das nächste Level startest, darfst deine {Skill_Punkte} neuen Skillpunkte ausgeben, um deine Fähigkeiten zu verbessern. Dabei hast du zehn Optionen:\n\nOptionsliste:\n1.Diebstahl\n2.Schlösser knacken\n3.Schleichen\n4.Redekunst\n5.Stärke\n6.Einschüchtern\n7.Geschicklichkeit\n8.Wahrnehmung\n9.Episches Glück (Kosten: 2 Skillpunkte)\n10.Lebensstärke\n\nDein aktueller Stand dieser Fähigkeiten sieht wie folgt aus:\n")
        self.clean_print(f"BEACHTE: Fähigkeiten mit 'Episch' im Namen können lediglich um höchstens einen Wert pro Level erhöht werden.\n")
        self.situation(0,1)
        while Skill_Punkte > 0:
            Y = self.state["Fähigkeiten"][9,1]
            Z = self.state["Fähigkeiten"][4,1]
            self.get_choice(10)
            self.Slow_print("\nPrüfen..")
            #--**---------------------------------------------------
            if self.X == 9 and episch_counter_G == 0: # Falls Glück ausgewählt wird, darf der User das im nächsten Durchlauf nicht nochmal nehmen
                if self.state["Fähigkeiten"][8,1] == 3:# Levellimit für Glück
                    self.clean_print(f"Diese Fähigkeit kann nicht weiter gelevelt werden, versuche bitte eine andere.")
                else:    
                    episch_counter_G += 1
                    self.state["Fähigkeiten"][self.X - 1, 1] += 1
                    Skill_Punkte -= 2
                    self.clean_print("\n\nAkzeptiert, hier nochmal der aktuelle Stand:\n")
                    self.situation(0,1)
            #-----------------------------------------------------
            elif self.X == 9 and episch_counter_G == 1: # Schleife wiederholt sich
                self.clean_print(f"Leider kannst du Glück erst nach dem nächsten Level wieder upgraden. Versuche es noch einmal.")
            #-----------------------------------------------------
            elif self.X != 9: # Falls irgendeine andere Fähigkeit ausgewählt wird
                self.state["Fähigkeiten"][self.X - 1, 1] += 1
                Skill_Punkte -= 1
                self.clean_print("\n\nAkzeptiert, hier nochmal der aktuelle Stand:\n")
                self.situation(0,1)
            #-------------------------------------------**--

            if Y != self.state["Fähigkeiten"][9,1]:# falls das alte Level(gespeichert in Y) geändert wurde, Bonuszuweisung
                self.state["Spieler_Max_HP"] += self.state["Fähigkeiten"][9,1] * 10 - 10
            #---------------------------------------------
            if Z != self.state["Fähigkeiten"][4,1]: # falls das alte Level(gespeichert in Z) geändert wurde, Bonuszuweisung 
                for x in range(len(self.state["Spieler_Kampfliste"])): # len(zählt Inhalt auf), for x in range(weise jedem x einen Wert auf Liste zu z.B. x=0 x=1 x=2)
                    self.state["Spieler_Kampfliste"][x, 1] += self.state["Fähigkeiten"][4, 1] + x
                for x in range(len(self.state["Feind_Kampfliste"])):
                    self.state["Feind_Kampfliste"][x, 1] += int((self.state["Fähigkeiten"][4, 1] + x) / 2)
            #---------------------------------------------
            self.state["Spieler_HP"] = self.state["Spieler_Max_HP"]
        self.Übergang()

#-------------------------------------------------------------------------------------------------------------------------

# Noch nicht überarbeitet
# Kampf zwischen Spieler und einem Feind
    def Kampf(self, Spieler_HP, Feind_HP, To_the_Death):
        Rundentimer = 1
        self.clean_print("Du befindest dich nun in einem Kampf!! Viel Glück, du wirst es brauchen! ")
        if To_the_Death == True:
            B = 0
        else:
            B = 30
        while Spieler_HP > B and Feind_HP > B:
            Treffer = 0

            #Spieler Durchlauf
            self.clean_print(f"\n\n{Rundentimer}. Runde: Für die Runde hast du diese Optionen:\n")
            print(self.state["Spieler_Kampfliste"][:, 0]) # gibt alle (:) Werte aus der Spalte (,0)
            self.get_choice(int(self.state["Spieler_Kampfliste"].shape[0]))
            Einsen = int(self.state["Spieler_Kampfliste"][self.X-1, 2])
            Nullen = 10 - Einsen
            self.Chance = np.concatenate((np.ones(Einsen), np.zeros(Nullen)))
            self.Hit = random.choice(self.Chance)
            if self.Hit == 1:
                Treffer = 1
                Feind_HP -= int(self.state["Spieler_Kampfliste"][self.X-1, 1])
                self.clean_print(f" Glückwunsch, du hast getroffen und deinem Gegner damit {self.state["Spieler_Kampfliste"][self.X-1, 1]} Schaden zugefügt!")
            
            # Feind Durchlauf
            list_1 = list(range(0, self.state["Feind_Kampfliste"].shape[0] + 1))
            Bot_choice = random.choice(list_1)
            Einsen_Feind = int(self.state["Feind_Kampfliste"][Bot_choice-1, 2])
            Nullen_Feind = 10 - Einsen_Feind
            self.Chance = np.concatenate((np.ones(Einsen_Feind), np.zeros(Nullen_Feind)))
            self.Hit = random.choice(self.Chance)
            if self.Hit == 1:
                Treffer = 1
                Spieler_HP -= int(self.state["Feind_Kampfliste"][Bot_choice-1, 1])
                self.clean_print(f"Oh nein!! Dein Gegner hat dich getroffen und dir damit {self.state["Feind_Kampfliste"][Bot_choice-1, 1]} Schaden zugefügt!")
            
            if Treffer == 0:
                self.clean_print("Was für eine Runde, sowohl du als auch dein Feind haben verfehlt, weiter geht es!!")
            self.clean_print(f"\nDer Gegner hat noch {Feind_HP} Leben übrig und du noch {Spieler_HP}.\n\n")
            Rundentimer += 1
            print("-"*150)
        if Spieler_HP <= B:
            self.clean_print("Oh nein!!! Du hast den Kampf verloren!!")
            Win = 0
            self.Warte = input("Drücke eine beliebige Taste um fortzufahren.")
            return Spieler_HP and Win
            
        elif Feind_HP <= B:
            self.clean_print("Hurraaaaaa!!! Du hast den Kampf gewonnen!!")
            Win = 1
            self.Warte = input("Drücke eine beliebige Taste um fortzufahren.")
            return Feind_HP and Win
        
            
#-------------------------------------------------------------------------------------------------------------------------
#Nicht bereit
# gewährt Spieler starke Boni, ist aber deutlich teurer als andere Fähigkeiten
def Episches_Glück (self):
    # Im Kampf
    if self.state["Fähigkeiten"][8,1] == 1:
        Chance = random.choice([1,0,0,0,0])
    elif self.state["Fähigkeiten"][8,1] == 2:
        Chance = random.choice([1,0,0])
        # Bonus
    elif self.state["Fähigkeiten"][8,1] == 3:
        Chance = random.choice([1,0,0])
        # Bonus
        # Bonus

    # Beim erkunden
        # Bsp. Truhen schneller öffnen, mehr Dinge finden

#-------------------------------------------------------------------------------------------------------------------------
        
# Erstellt ein Bild mit der passenden Datei
    def visualize(self, bilddatei, bg_color="black"):
        fig,ax = plt.subplots(figsize=(10, 8),dpi=100)#Erstellt ein Fenster + passt Größe an(1000x800)
        ax.axis("off")# Entfernt Koordinatensystem 

        #Setzt Farben
        fig.patch.set_facecolor(bg_color)
        ax.set_facecolor(bg_color)

        #Titel vom Fenster
        ax.set_title(
            "Schließe dieses Fenster, um die Story weiter zu lesen...",
            color="white"
        )

        #Erstellt Bilder
        img = mpimg.imread(bilddatei)
        ax.imshow(img)

        #Erstellt Texte
        ax.text(
            0.5, # x = 50% von links
            0.05,# y = 5% von unten
            "",#Text
            color="white",
            ha="center",
            va="center",
            transform=ax.transAxes,
            fontsize=14 # Textgröße
        )

        #erstellt Button
        button_ax = plt.axes([0.35, 0.02, 0.3, 0.08])
        button = Button(button_ax, "CLEAR", color="red", hovercolor="darkred")
        button.label.set_color("white")

        #Löscht alles am Fenster, wenn Knopfdruck
        def clear_gui(event):
            ax.clear()
            ax.set_facecolor(bg_color)
            ax.axis("off")
            ax.text(
                0.45,
                0.50,
                "Willkommen im Beginn der 2D Welt!",
                ha="center",
                va="center",
                color="white",
                transform=ax.transAxes,
                fontsize=14
            )
            ax.set_title(
                "Schließe dieses Fenster, um die Story weiter zu lesen...",
                color="white"
            )
            fig.canvas.draw_idle()

        button.on_clicked(clear_gui)
        plt.show()
        