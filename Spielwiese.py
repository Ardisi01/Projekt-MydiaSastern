import numpy as np
import sys
import time
import os

# Hier ist die Ablage für alle Eigenschaften und Attribute, die der Charakter hochleveln kann.
Rot = "\033[31m"
Blau = "\033[34m"
Reset = "\033[0m"
Leben = 100
Fußbruch = 35

def clean_print(text): #clean("dein Text") ruft die DEF auf // Clean ("dein Text") lässt den Text fließend darstellen
    for c in text:
        sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.002)




