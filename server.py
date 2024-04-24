#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Mielőtt ezt a programot futtatnád párosítsd a két robotot, de ne legyen aktív kapcsolat köztük! 

# A szervert a kliens előtt kell elindítanod!

from pybricks.messaging import BluetoothMailboxServer, TextMailbox
ev3 = EV3Brick()

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# A szervert a kliens előtt kell elindítanod!
print('vár a kapcsolódásra...')
server.wait_for_connection()
print('kapcsolat létrejött!')

# A szerver vár az első üzent megérkezésére a klienstől,kiírja, majd válaszol neki.
mbox.wait()
mbox.send("start")
print("Valami01")
mbox.wait_new()
uzenet = mbox.read()
print(uzenet)
if uzenet=="stop":
    ev3.speaker.beep()




