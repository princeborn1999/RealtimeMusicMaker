from psonic import *
try:
    from pyfirmata import Arduino, util
except:
    import pip
    pip.main(['install','pyfirmata'])
    from pyfirmata import Arduino, util
import serial
import time
import random
from threading import Thread

ArduinoSerial = serial.Serial('com4',9600)
time.sleep(2)



print(" distance = Treble /n")
print(" raindrop = bass /n")
print(" humidity = drum /n")
while 1:
    cm = ArduinoSerial.readline()
    cm = int(chr(cm[0]))
    rain = ArduinoSerial.readline()
    rain = int(chr(rain[0]))
    humi = ArduinoSerial.readline()
    humi = int(chr(humi[0])+chr(humi[1]))
    print("'",cm,":cm '",',',"'",rain,":rain '",',',"'",humi,":humi '")
    for i in range(1,2):##第一第二小節
        print("1st part")
        #高音
        if (( cm < 6) & (rain == 2)):
            if (humi > 95):
                use_synth(CHIPBASS)
                print("高音(O) 低音(X) :chipbass(O)")
            else:
                use_synth(PIANO)
                print("高音(O) 低音(X) :chipbass(X)")
            sleep(3.25)
            play(67)
            release: 0.5
            sleep (0.25)
            play(67)
            release: 0.5
            sleep (0.25)
            play(69)
            release: 0.5
            sleep (0.25)
            play(69)
            release: 0.5
            sleep (0.25)
            play(71)
            release: 0.5
            sleep (0.25)
            play(71)#4
            release: 0.5
            sleep (0.25)
            play(69)
            release: 0.5
            sleep (0.25)
            play(69)
            release: 0.5
            sleep (0.25)
            play(67)
            release: 0.5
            sleep (0.25)
            play(67)#8
            release: 0.5
            sleep (0.25)
            play(62)
            release: 0.5
            sleep (0.25)
            play(62)
            release: 0.5
            sleep (0.25)
            play(58)
            release: 0.5
            sleep (0.25)
            play(58)#12
            release: 0.5
            sleep (0.25)
            play(55)
            release: 0.5
            sleep (0.25)
            play(55)
            release: 0.5
            sleep (0.25)
            play(65)#
            release: 0.5
            sleep (0.25)
        #低音
        elif (( cm > 6 )& (rain < 2)):
            if (humi > 95):
                use_synth(CHIPBASS)
                print("高音(X) 低音(O) :chipbass(O)")
            else:
                use_synth(PIANO)
                print("高音(X) 低音(O) :chipbass(X)")
            play(43)
            release: 0.5
            sleep (0.5)
            play(50)
            release: 0.5
            sleep (0.5)
            play(59)
            release: 0.5
            sleep (0.5)
            play(50)#4
            release: 0.5
            sleep (0.5)
            play(59)
            release: 0.5
            sleep (0.5)
            play(50)
            release: 0.5
            sleep (0.5)
            play(59)
            release: 0.5
            sleep (0.5)
            play(50)#8
            release: 0.5
            sleep (0.5)
            play(43)
            release: 0.5
            sleep (0.5)
            play(50)
            release: 0.5
            sleep (0.5)
            play(59)
            release: 0.5
            sleep (0.5)
            play(50)#12
            release: 0.5
            sleep (0.5)
            play(59)
            release: 0.5
            sleep (0.5)
            play(50)
            release: 0.5
            sleep (0.5)
            play(59)
            release: 0.5
            sleep (0.5)
            play(50)#16
            release: 0.5
            sleep (0.5)
        #高音與低音
        elif (( cm < 6 )& (rain < 2)):
            if (humi > 95):
                use_synth(CHIPBASS)
                print("高音(O) 低音(O) :chipbass(O)")
            else:
                use_synth(PIANO)
                print("高音(O) 低音(O) :chipbass(X)")
            play(43,amp=2)#1-1
            release: 0.5
            sleep (0.5)
            play(50)#1-3
            release: 0.5
            sleep (0.5)
            play(59)#1-5
            release: 0.5
            sleep (0.5)
            play(50)#1-7
            release: 0.5
            sleep (0.5)
            play(59,amp=2)#1-9
            release: 0.5
            sleep (0.5)
            play(50)#1-11
            release: 0.5
            sleep (0.5)
            play(59)#1-13
            release: 0.5
            sleep (0.5)
            play(50)#1-15
            release: 0.5
            play(67)
            release: 0.5
            sleep (0.25)
            
            play(67,amp=2)#2-1
            play(43)
            release: 0.5
            sleep (0.25)
            
            play(69)#2-2
            release: 0.5
            sleep (0.25)

            play(69)#2-3
            play(50)
            release: 0.5
            sleep (0.25)

            play(71)#2-4
            release: 0.5
            sleep (0.25)

            play(71)#2-5
            play(59)
            release: 0.5
            sleep (0.25)

            play(69)#2-6
            release: 0.5
            sleep (0.25)

            play(69)#2-7
            play(50)
            release: 0.5
            sleep (0.25)

            play(67)#2-8
            release: 0.5
            sleep (0.25)

            play(67)#2-9
            play(59)
            release: 0.5
            sleep (0.25)

            play(62)#2-10
            release: 0.5
            sleep (0.25)

            play(62)#2-11
            play(50)
            release: 0.5
            sleep (0.25)

            play(58)#2-12
            release: 0.5
            sleep (0.25)

            play(58)#2-13
            play(59)
            release: 0.5
            sleep (0.25)

            play(55)#2-14
            release: 0.5
            sleep (0.25)

            play(55)#2-15
            play(50)
            release: 0.5
            sleep (0.25)

            play(65)#2-16
            release: 0.5
            sleep (0.25)
        else:
            print("高音(X) 低音(X) dark_ambience(X)")
    for j in range(1,2):
        print("3rd part")
        if (( cm < 6) & (rain == 2)):
            if (humi > 95):
                use_synth(CHIPBASS)
                print("高音(O) 低音(X) :chipbass(O)")
            else:
                use_synth(PIANO)
                print("高音(O) 低音(X) :chipbass(X)")
            play(65)#3-1
            release: 0.5
            sleep (0.25)
            
            play(63)#3-2
            release: 0.5
            sleep (0.25)
            
            play(63)#3-3
            release: 0.5
            sleep (0.25)
            
            play(62)#3-4
            release: 0.5
            sleep (0.25)
            
            play(63)#3-5
            release: 0.5
            sleep (0.25)
            
            play(65)#3-6
            release: 0.5
            sleep (0.25)
            
            play(63)#3-7
            release: 0.5
            sleep (1)

            play(63)#4-1
            release: 0.5
            sleep (0.25)
            
            play(63)#4-2
            release: 0.5
            sleep (0.25)
            
            play(67)#4-3
            release: 0.5
            sleep (0.25)
            
            play(67)#4-4
            release: 0.5
            sleep (0.25)

            play(69)#4-5
            release: 0.5
            sleep (0.25)

            play(69)#4-6
            release: 0.5
            sleep (0.25)

            play(71)#4-7
            release: 0.5
            sleep (0.25)

            play(71)#4-8
            release: 0.5
            sleep (0.25)

            play(67)#4-9
            release: 0.5
            sleep (0.25)

            play(67)#4-10
            release: 0.5
            sleep (0.25)

            play(60)#4-11
            release: 0.5
            sleep (0.25)

            play(60)#4-12
            release: 0.5
            sleep (0.25)

            play(63)#4-13
            release: 0.5
            sleep (0.25)

            sleep(0.5)
            
        elif (( cm > 6 )& (rain < 2)):
            if (humi > 95):
                use_synth(CHIPBASS)
                print("高音(X) 低音(O) :chipbass(O)")
            else:
                use_synth(PIANO)
                print("高音(X) 低音(O) :chipbass(X)")
            
            
            play(51)#3-1
            release: 0.5
            sleep (0.5)
            
            play(56)#3-3
            release: 0.5
            sleep (0.5)

            play(64)#3-5
            release: 0.5
            sleep (0.5)

            play(56)#3-7
            release: 0.5
            sleep (0.5)
            
            play(64)#3-9
            release: 0.5
            sleep (0.5)

            play(56)#3-12
            release: 0.5
            sleep (0.5)

            play(41)#4-1
            release: 0.5
            sleep (0.5)
            
            play(48)#4-3
            release: 0.5
            sleep (0.5)

            play(57)#4-5
            release: 0.5
            sleep (0.5)

            play(48)#4-7
            release: 0.5
            sleep (0.5)
            
            play(57)#4-9
            release: 0.5
            sleep (0.5)

            play(48)#4-11
            release: 0.5
            sleep (0.5)

            play(57)#4-3
            release: 0.5
            sleep (0.5)
            
        elif (( cm < 6 )& (rain < 2)):
            if (humi > 95):
                use_synth(CHIPBASS)
                print("高音(O) 低音(O) :chipbass(O)")
            else:
                use_synth(PIANO)
                print("高音(O) 低音(O) :chipbass(X)")
            play(65)#3-1
            play(51)
            release: 0.5
            sleep (0.25)
            
            play(63)#3-2
            release: 0.5
            sleep (0.25)
            
            play(63)#3-3
            play(56)
            release: 0.5
            sleep (0.25)
            
            play(62)#3-4
            release: 0.5
            sleep (0.25)
            
            play(63)#3-5
            play(64)
            release: 0.5
            sleep (0.25)
            
            play(65)#3-6
            release: 0.5
            sleep (0.25)
            
            play(63)#3-7
            play(56)
            release: 0.5
            sleep (0.25)
            
            play(64)
            release: 0.5
            sleep (0.25)
            
            play(56)
            release: 0.5
            sleep (0.25)

            play(48)
            release: 0.5
            sleep (0.25)

            
            play(63)#4-1
            release: 0.5
            sleep (0.25)
            
            play(63)#4-2
            play(48)
            release: 0.5
            sleep (0.25)
            
            play(67)#4-3
            release: 0.5
            sleep (0.25)
            
            play(67)#4-4
            play(57)
            release: 0.5
            sleep (0.25)

            play(69)#4-5
            release: 0.5
            sleep (0.25)

            play(69)#4-6
            play(48)
            release: 0.5
            sleep (0.25)

            play(71)#4-7
            release: 0.5
            sleep (0.25)

            play(71)#4-8
            play(57)
            release: 0.5
            sleep (0.25)

            play(67)#4-9
            release: 0.5
            sleep (0.25)

            play(67)#4-10
            play(48)
            release: 0.5
            sleep (0.25)

            play(60)#4-11
            release: 0.5
            sleep (0.25)

            play(60)#4-12
            play(57)
            release: 0.5
            sleep (0.25)

            play(63)#4-13
            release: 0.5
            sleep (0.25)

            sleep(0.5)
            
        else:
            print("高音(X) 低音(X) dark_ambience(X)")
    for k in range(1,2):
        print("5th part")
        if (( cm < 6) & (rain == 2)):
            if (humi > 95):
                use_synth(CHIPBASS)
                print("高音(O) 低音(X) :chipbass(O)")
            else:
                use_synth(PIANO)
                print("高音(O) 低音(X) :chipbass(X)")
            play(63)#5-1
            release: 0.5
            sleep (0.5)
            play(62)#5-2
            release: 0.5
            sleep (0.5)
            play(62)#5-3
            release: 0.5
            sleep (0.5)
            play(60)#5-4
            release: 0.5
            sleep (0.5)
            play(62)#5-5
            release: 0.5
            sleep (0.5)
            play(63)#5-6
            release: 0.5
            sleep (0.5)

        elif (( cm > 6 )& (rain < 2)):
            if (humi > 95):
                use_synth(CHIPBASS)
                print("高音(X) 低音(O) :chipbass(O)")
            else:
                use_synth(PIANO)
                print("高音(X) 低音(O) :chipbass(X)")
            play(46)#5-1
            release: 0.5
            sleep(0.5)
            play(53)#5-3
            release: 0.5
            sleep(0.5)
            play(62)#5-5
            release: 0.5
            sleep(0.5)
        elif (( cm < 6 )& (rain < 2)):
            if (humi > 95):
                use_synth(CHIPBASS)
                print("高音(O) 低音(O) :chipbass(O)")
            else:
                use_synth(PIANO)
                print("高音(O) 低音(O) :chipbass(X)")
            play(63)#5-1
            play(46)
            release: 0.5
            sleep (0.5)
            play(62)#5-2
            release: 0.5
            sleep (0.5)
            play(62)#5-3
            play(53)
            release: 0.5
            sleep (0.5)
            play(60)#5-4
            release: 0.5
            sleep (0.5)
            play(62)#5-5
            play(62)
            release: 0.5
            sleep (0.5)
            play(63)#5-6
            release: 0.5
            sleep (0.5)
        else:
            print("高音(X) 低音(X) dark_ambience(X)")   
    
   
