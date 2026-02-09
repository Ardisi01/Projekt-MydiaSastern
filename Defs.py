import numpy as np
import sys
import time
import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Button

#-------------------------------------------------------------------------------------------------------------------------

#Mit self. rufen wir Variablen/Methoden aus der anderen Datei auf
class Defs:
    def __init__(self):#self, muss in jede def, wenn sie Werte von der anderen Datei nutzt!!
        self.state = None
        self.X = None
        self.Diebstahl_Erfolg = 0
        self.Schleichen_Erfolg = 0
        self.geschickt_Erfolg = 0
        self.Redeerfolg = 0
        self.Y = 0
        self.Beute = None
    def set_state(self, state: dict):
        self.state = state

#-------------------------------------------------------------------------------------------------------------------------

    def Übergang(self):
        input("\nDrücke eine beliebige Taste, um fortzufahren.")

#-------------------------------------------------------------------------------------------------------------------------

    def situation(self, Inventar, Skills):  # Hiermit können wir uns jederzeit ohne Schreibarbeit die Attribute, das Inventar oder beides anzeigen lassen
        if Inventar == 1:
            print("Das ist dein aktualisiertes Inventar:\n", self.state["Spieler_Inventar"])
        if Skills == 1:
            print("\n\n", self.state["Attribute"], "\n\n")
        self.Übergang()

#-------------------------------------------------------------------------------------------------------------------------

    def clean_print(self, text):  # Ruft die DEF auf // Clean ("dein Text") lässt den Text fließend darstellen
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.00006)

#-------------------------------------------------------------------------------------------------------------------------

    def Zeit_vergangen(self, text):  # Fließtext langsamer als clean_print
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.5)

#-------------------------------------------------------------------------------------------------------------------------

    def clear_screen(self):  # Löscht die vorherigen Eingaben im Terminal
        os.system("cls" if os.name == "nt" else "clear")

#-------------------------------------------------------------------------------------------------------------------------

    def Diebstahl_Lvl_up(self): 
        self.state["Raub_counter"] += 1
        Lvl_up = random.choice([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        if Lvl_up == 1:
            self.state["Attribute"][0, 1] += 1
            print("Dein Glück segnet dich mit einem Level Up im Diebstahl! Glückwunsch!!")
            self.situation(0, 1)

#-------------------------------------------------------------------------------------------------------------------------
  
    def Diebstahl(self, Ziel_inventar):  # Was Ziel ist, definieren wir, wenn wir die Funktion aufrufen und es sollte immer eine Liste sein
        self.Beute = None

        if Ziel_inventar == []:
            print("Hier ist Nichts mehr zu holen")
            return Ziel_inventar

        lvl = self.state["Attribute"][0, 1]

        if 1 <= lvl <= 2:
            self.Diebstahl_Erfolg = random.choice([1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        elif 3 <= lvl <= 4:
            self.Diebstahl_Erfolg = random.choice([1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
        elif 5 <= lvl <= 6:
            self.Diebstahl_Erfolg = random.choice([1, 1, 1, 1, 1, 1, 0, 0, 0, 0])
        elif 7 <= lvl <= 8:
            self.Diebstahl_Erfolg = random.choice([1, 1, 1, 1, 1, 1, 1, 1, 0, 0])
        elif lvl >= 10:
            self.Diebstahl_Erfolg = 1

        if self.Diebstahl_Erfolg == 1:
            self.Beute = random.choice(Ziel_inventar)
            self.state["Spieler_Inventar"].append(self.Beute)
            Ziel_inventar.remove(self.Beute)
            self.Diebstahl_Lvl_up()
            print("Der Diebstahl war erfolgreich! Du hast Folgendes erbeutet:", self.Beute,"\n")
            print("-"*150)
        else:
            self.clean_print("Du hattest leider keinen Erfolg!\n")
            print("-"*150)

#-------------------------------------------------------------------------------------------------------------------------

    def Diebstahl_Schleife(self, Raublimit, Ziel_inventar):
        Y = self.Y
        zählschleife = 0
        while Y < Raublimit:

            zählschleife += 1
            self.clean_print(f"\n\n{zählschleife}.Versuch: Mit [1] kannst du stehlen, mit [2] kannst du den Raubzug abbrechen.")
            self.get_choice(2)
            if self.X == 1:
                self.Diebstahl(Ziel_inventar)
                Y += 1
                if self.Diebstahl_Erfolg == 1:
                    self.situation(1, 0)
            elif self.X == 2:
                break

#-------------------------------------------------------------------------------------------------------------------------

    def Schleichen_Lvl_up(self):
        Lvl_up = random.choice([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        if Lvl_up == 1:
            self.state["Attribute"][2, 1] += 1
            print("Dein Glück segnet dich mit einem Level Up im Schleichen! Glückwunsch!!")
            self.situation(0, 1)

#-------------------------------------------------------------------------------------------------------------------------

    def Schleichen(self):
        lvl = self.state["Attribute"][2, 1]

        if 1 <= lvl <= 3:
            self.Schleichen_Erfolg = random.choice([1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
        elif 4 <= lvl <= 6:
            self.Schleichen_Erfolg = random.choice([1, 1, 1, 1, 1, 1, 1, 0, 0, 0])
        elif 7 <= lvl <= 9:
            self.Schleichen_Erfolg = random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
        elif lvl >= 10:
            self.Schleichen_Erfolg = 1

        if self.Schleichen_Erfolg == 1:
            print("\nDu bist erfolgreich geschlichen, Niemand hat dich gehört!\n")
            self.Schleichen_Lvl_up()
        else:
            print("\nOh nein! Du bist auf irgendetwas draufgetreten und hast ein Geräusch gemacht!\n")
        self.Übergang()

#-------------------------------------------------------------------------------------------------------------------------

    def Geschicklichkeit_Lvl_up(self):
        Lvl_up = random.choice([1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        if Lvl_up == 1:
            self.state["Attribute"][6, 1] += 1
            print("Dein Glück segnet dich mit einem Level Up in der Geschicklichkeit! Glückwunsch!!")
            self.situation(0, 1)

#-------------------------------------------------------------------------------------------------------------------------

    def geschickter_zug(self):
        lvl = self.state["Attribute"][6, 1]

        if 1 <= lvl <= 3:
            self.geschickt_Erfolg = random.choice([1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
        elif 4 <= lvl <= 6:
            self.geschickt_Erfolg = random.choice([1, 1, 1, 1, 1, 1, 1, 0, 0, 0])
        elif 7 <= lvl <= 9:
            self.geschickt_Erfolg = random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
        elif lvl >= 10:
            self.geschickt_Erfolg = 1

        if self.geschickt_Erfolg == 1:
            print("Das war ein geschickter Zug und es ist Niemandem aufgefallen.")
            self.Geschicklichkeit_Lvl_up()
        else:
            print("Oh nein! Du warst nicht erfolgreich!!")

        self.Übergang()

#-------------------------------------------------------------------------------------------------------------------------

    def Überreden(self, zielinventar):
        Redeliste_1 = ["Ich glaube, wir wollen im Kern eigentlich dasselbe.", "Es gibt einen Aspekt, der mir dabei besonders wichtig erscheint.", "Was wäre, wenn wir das einmal pragmatisch betrachten?", "Ich sehe hier eine Möglichkeit, von der wir beide profitieren könnten.", "Es geht weniger um das Ob, als vielmehr um das Wie."]
        Redeliste_2 = ["Ich habe über unser letztes Gespräch noch einmal nachgedacht.", "Mir ist seitdem ein Punkt klarer geworden, den ich gern ergänzen würde.", "Vielleicht habe ich mich beim ersten Mal nicht präzise genug ausgedrückt."]
        Redeliste_3 = ["Das ist mein letzter Versuch, meine Sicht verständlich zu machen.", "Ich wollte sicherstellen, dass dieser Gedanke nicht unausgesprochen bleibt."]
        lvl = self.state["Attribute"][3, 1]

        if 1 <= lvl:
            self.Übergang()
            self.clean_print("\nDu überlegst kurz und sagst dann:\n" + random.choice(Redeliste_1) + "\n")
            self.Redeerfolg = random.choice([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
        if self.Redeerfolg == 0 and 4 <= lvl:
            self.Übergang()
            self.clean_print("\nDu überlegst kurz und sagst dann:\n" + random.choice(Redeliste_2) + "\n")
            self.Redeerfolg = random.choice([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
        if self.Redeerfolg == 0 and 7 <= lvl:
            self.Übergang()
            self.clean_print("\nDu überlegst kurz und sagst dann:\n" + random.choice(Redeliste_3) + "\n")
            self.Redeerfolg = random.choice([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])

        if self.Redeerfolg == 1:
            self.clean_print("Das Gespräch hat sich durch deine Redekunst zu deinen Gunsten gewändet, herzlichen Glückwunsch!!")
            if lvl == 10:
                self.clean_print("\nWährend dein Überredungsversuch voran geht, überkommt dich das Bedürfnis, deinen Gesprächspartner um seine persönlichen Gegenstände zu erleichtern.\n")
                self.Diebstahl_Schleife(3, zielinventar)
        else:
            self.clean_print("Dein Überredungsversuch bleibt diesmal leider ohne Erfolg, dennoch erhälst du für den Mut, es zu versuchen 5 Social Credits.")
            self.state["Social_Credits"] += 5
            print(self.state["Social_Credits"])

        self.Übergang()
        return self.Redeerfolg

#-------------------------------------------------------------------------------------------------------------------------

    def get_choice(self, option_number):  # Das ist die Funktion für alle Entscheidungen. Die Variable gibt die Anzahl der Optionen an
            while True:
                list_2 = list(range(1, option_number+1))
                choice = input("\nGib eine der oben genannten Zahlen ein:\n")
                if int(choice) in list_2:# Die möglichen Eingaben
                    self.X = int(choice)
                    return self.X# While-Schleife bricht
                else: # Falls keine der Optionen gewählt wurde, wird die Entscheidung einfach wiederholt
                    self.clean_print(random.choice([
                        "So kommst du hier nicht weiter.",
                        "Probier es anderweitig nochmal",
                        "Das ist nicht das, wonach du gefragt wurdest."
                    ]))

#-------------------------------------------------------------------------------------------------------------------------

    def Skill(self, Skill_Punkte):
        self.clear_screen()
        self.clean_print(f"Bevor du in das nächste Level startest, darfst deine {Skill_Punkte} neuen Skillpunkte ausgeben, um deine Fähigkeiten zu verbessern. Dabei hast du acht Optionen:\n\n1.Diebstahl\n2.Schlösser knacken\n3.Schleichen\n4.Redekunst\n5.Stärke\n6.Einschüchtern\n7.Geschicklichkeit\n8.Wahrnehmung\n")
        self.situation(0,1)
        while Skill_Punkte > 0:
            self.get_choice(8)
            self.Z = self.X - 1
            self.state["Attribute"][self.Z, 1] += 1
            self.clean_print("Akzeptiert, hier nochmal der aktuelle Stand:\n")
            self.situation(0,1)
            Skill_Punkte -= 1
        self.Übergang()

#-------------------------------------------------------------------------------------------------------------------------

    def Kampf(self, Spieler_HP, Feind_HP, To_the_Death):
        Rundentimer = 1
        self.clean_print("Du befindest dich nun in einem Kampf!! Viel Glück, du wirst es brauchen! ")
        if To_the_Death == True:
            B = 0
        else:
            B = 30
        while Spieler_HP > B and Feind_HP > B:
            Treffer = 0
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