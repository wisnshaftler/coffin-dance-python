import os
import time
from pygame import mixer
clear = lambda: os.system('cls')

mixer.init()
mixer.music.load("1.mp3")
mixer.music.play()
clear()

time.sleep(31)
clear()

step_count = 1;
counter = 1
for n in range(5):
    print("")
print(" "*counter + "     ======= ======= ======= ")
print(" "*counter + "   ======= ======= ======= ==== ")
print(" "*counter + " == == == == == == == == == == == ")
print(" "*counter + "==_======_============_======_=====")
print(" "*counter + "\( )/  \( )/        \( )/  \( )/")
print(" "*counter + " \|/    \|/          \|/    \|/")
print(" "*counter + "  |      |            |      |")
print(" "*counter + "  |      |            |      |")
print(" "*counter + " / \    / \\          / \    / \\")
clear()

def showCoffin(counter):
    print(" "*counter + "     ======= ======= ======= ")
    print(" "*counter + "   ======= ======= ======= ==== ")
    print(" "*counter + " == == == == == == == == == == == ")
    print(" "*counter + "==_======_============_======_====")
    print(" "*counter + "\( )/  \( )/        \( )/  \( )/")
    print(" "*counter + " \|/    \|/          \|/    \|/")
    print(" "*counter + "  |      |            |      |")
    print(" "*counter + "  |      |            |      |")
    print(" "*counter + " / \    / \\          / \    / \\")

for i in range(100):
    for n in range(5):
        print("")
    if step_count == 1:
        showCoffin(counter)
        counter +=4
        time.sleep(0.4)
        step_count =2
        clear()
        for n in range(5):
            print("")
        showCoffin(counter)
        counter +=4
        time.sleep(0.4)
        step_count =2
    else:
        showCoffin(counter)
        counter -=1
        step_count = 1
        time.sleep(0.2)
        clear()
        for n in range(5):
            print("")
        showCoffin(counter)
        counter -=1
        step_count = 1
        time.sleep(0.2)
        clear()
        
    clear()
time.sleep(5)
clear()
