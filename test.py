# -*- coding: utf-8 -*-
import OttoBuzzer as OB
from time import sleep
pinBuzzer = 17  # pin Number 7

ottoTone = OB.Tone(pinBuzzer)
ottoTone.start()

#playSounds만큼 루프
for playSound in OB.playSounds:
    print(playSound)
    #플레이
    ottoTone.sing(playSound)

    sleep(1)

ottoTone.stop()
