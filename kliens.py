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

from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# ez a szerver neve akiehz csatlakozni szeretnél
SERVER = 'ii'

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

print('kapcsolódás...')
client.connect(SERVER)
print('Kapcsolat létrejött!')

# A kliens elküldi első üzenetét, majd vár a szerver  válaszára, és kiírja.
mbox.send('Szia!')
mbox.wait()
print(mbox.read())
