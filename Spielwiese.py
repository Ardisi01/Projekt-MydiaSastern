import numpy as np
import sys
import time
import os
import random

# Hier ist die Ablage für alle Eigenschaften und Attribute, die der Charakter hochleveln kann.
Rot = "\033[31m"
Blau = "\033[34m"
Reset = "\033[0m"
Leben = 100
Fußbruch = 35

def clean_print(text): #clean("dein Text") ruft die DEF auf // Clean ("dein Text") lässt den Text fließend darstellen
    for c in text:
        sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.002)


print = """Du weißt, je länger du brauchst, die Handys aus deren jeweiligen Kisten auszupacken und an deinem Körper zu kleben, 
        \ndesto wahrscheinlicher wirst du erwischt.
          Du kannst entscheiden, ob du 15 Geräte auspackst[1], 8 Geräte[2],4Geräte[3] oder 2 Geräte[4].

"""