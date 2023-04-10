import RPI.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BCM)
dac=[26, 19, 13, 6, 5 , 11, 9, 10]
leds =[21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)


def perev(a):
   return [int(elem) for elem in bin(a) [2:].zfill(8)]
def adc():
    n = [0 for i in range(8)]
    for i in range (8):
     n_n = n.copy
     n_n[i]=1
     GPIO.output(dac, n_n)
     sleep(0.005)
     if GPIO.input(comp)==1:
         n =n_n
    r=''.join([str(i) for i in n])
    return int(r,2)
try:
    while True:
        n=adc()
        print ("Предполагаемое напряжение: {0:.2f}B".format(int(n)/255*3.3))
        kol=int(n)/255*3.3
        kol = kol*11
        kol=round(kol)
        print(kol)
        GPIO.output(leds,0)
        for i in range(kol):

           GPIO.output(leds[i],1)
finally:
    GPIO.output(dac, 0)
  
    GPIO.cleanup()