import sys
import time
import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Button

#Mit self. rufen wir Variablen/Methoden aus der anderen Datei auf
class Defs:
    def __init__(self):#self, muss in jede def, wenn sie Werte von der anderen Datei nutzt!!
        self.state = None
        self.X = None
        self.Diebstahl_Erfolg = 0
        self.Schleichen_Erfolg = 0
        self.geschickt_Erfolg = 0
        self.Y = 0
        self.Beute = None
    def set_state(self, state: dict):
        self.state = state

    def situation(self, Inventar, Skills):  # Hiermit können wir uns jederzeit ohne Schreibarbeit die Attribute, das Inventar oder beides anzeigen lassen
        if Inventar == 1:
            print("Das ist dein aktualisiertes Inventar:\n", self.state["Spieler_Inventar"])
        if Skills == 1:
            print("\n\n", self.state["Attribute"], "\n\n")

    def clean_print(self, text):  # Ruft die DEF auf // Clean ("dein Text") lässt den Text fließend darstellen
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.06)

    def Zeit_vergangen(self, text):  # Fließtext langsamer als clean_print
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.8)

    def clear_screen(self):  # Löscht die vorherigen Eingaben im Terminal
        os.system("cls" if os.name == "nt" else "clear")

    def Diebstahl_Lvl_up(self):
        self.state["Raub_counter"] += 1
        Lvl_up = random.choice([1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        if Lvl_up == 1:
            self.state["Attribute"][0, 1] += 1
            print("Dein Glück segnet dich mit einem Level Up im Diebstahl! Glückwunsch!!")
            self.situation(0, 1)

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

    def Schleichen_Lvl_up(self):
        Lvl_up = random.choice([1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
        if Lvl_up == 1:
            self.state["Attribute"][2, 1] += 1
            print("Dein Glück segnet dich mit einem Level Up im Schleichen! Glückwunsch!!")
            self.situation(0, 1)

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

    def Geschicklichkeit_Lvl_up(self):
        Lvl_up = random.choice([1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
        if Lvl_up == 1:
            self.state["Attribute"][6, 1] += 1
            print("Dein Glück segnet dich mit einem Level Up in der Geschicklichkeit! Glückwunsch!!")
            self.situation(0, 1)

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

    def get_choice(self, option_number):  # Das ist die Funktion für alle Entscheidungen. Die Variable gibt die Anzahl der Optionen an
        while True:
            if option_number == 2:# Für zwei Optionen
                choice = input("\nGib '1' oder '2' ein.-->")
                if choice in ['1', '2']:# Die möglichen Eingaben
                    self.X = int(choice)
                    return self.X# While-Schleife bricht
                else: # Falls keine der Optionen gewählt wurde, wird die Entscheidung einfach wiederholt
                    self.clean_print(random.choice([
                        "So kommst du hier nicht weiter.",
                        "Probier es anderweitig nochmal",
                        "Das ist nicht das, wonach du gefragt wurdest."
                    ]))
            elif option_number == 3: # Für drei Optionen
                choice = input("\nGib '1', '2' oder '3' ein.-->")
                if choice in ['1', '2', '3']:
                    self.X = int(choice)
                    return self.X
                else:
                    self.clean_print(random.choice([
                        "So kommst du hier nicht weiter.",
                        "Probier es anderweitig nochmal",
                        "Das ist nicht das, wonach du gefragt wurdest."
                    ]))
            elif option_number == 4: # Für vier Optionen
                choice = input("\nGib '1', '2', '3' oder '4' ein.-->")
                if choice in ['1', '2', '3', '4']:
                    self.X = int(choice)
                    return self.X
                else:
                    self.clean_print(random.choice([
                        "So kommst du hier nicht weiter.",
                        "Probier es anderweitig nochmal",
                        "Das ist nicht das, wonach du gefragt wurdest."
                    ]))

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
            fontsize=14
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
