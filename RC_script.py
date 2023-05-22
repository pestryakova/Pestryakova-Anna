import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

def tobin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]


def adc():
    global comp
    ret = 0
    for i in range(7, -1, -1):
        ret += 2**i
        GPIO.output(dac, tobin(ret))
        time.sleep(0.01)
        if GPIO.input(comp) == 0:
            ret -= 2**i
    return ret


def to_leds(x):
    binlist = tobin(x)
    GPIO.output(leds, binlist)

#Установка режима обращения к плате

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
troyka = 17
comp = 4

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

#Блок измерений

try:
    value_list = []
    start = time.time()
    GPIO.output(troyka, 1)
    value_list += [3.3 * adc()/255]
    while adc() <= 220:
        value_list += [3.3 * adc()/255]
    GPIO.output(troyka, 0)
    while adc() >= 20:
        value_list += [3.3 * adc()/255]
    end = time.time()
finally:
    GPIO.output(dac + [troyka] + leds, 0)
    GPIO.cleanup()

value_list_str = [str(i) for i in value_list]

lenght = end-start
step = lenght/len(value_list)
frequency = 1/step
dac_step = 3.3/255
print('Время эксперимента - ', lenght)
print('Период одного измерения - ', step)
print('Частота измерений - ', frequency)
print('Шаг квантования - ', dac_step)

# Запись данных в файлы

with open('data.txt', 'w') as outfile:
    outfile.write('\n'.join(value_list_str))

with open('settings.txt', 'w') as setfile:
    setfile.write(str(len(value_list)/(end-start)) + str((end-start)/len(value_list)))

#Построение графика

plt.plot(value_list)
plt.show()