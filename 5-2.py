import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BCM)
dac=[26, 19, 13, 6, 5 , 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)
def t_t(value):
   return [int(bit) for bit in bin(int(value)) [2:].zfill(8)]
def adc():
    n = [0 for i in range(8)]
    for i in range (8):
     n_n = n.copy()
     n_n[i]=1
     GPIO.output(dac, n_n)
     time.sleep(0.05)
     if GPIO.input(comp)==1:
         n = n_n
    r=''.join([str(i) for i in n])
    return int(r,2)
try:
    while True:
        n=adc()
        print ("Предполагаемое значение: {0:.2f}B".format(int(n)/256*3.3))
        GPIO.output(dac, t_t(n))
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()