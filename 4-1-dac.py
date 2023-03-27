#задание 1, аналоговое напряжение 
import RPi.GPIO as gp
import sys



#объявим переменную dac
dac=[26, 19, 13, 6, 5, 11, 9, 10]
gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)



#Бинарное представление 
def dec2bin(a, n):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]




#блок Try-Finallly
try:
    while(True):
        a=input('input 0-255: ')
        if a=='q':
            sys.exit()
        elif a.isdigit() and int(a)%1 == 0 and 0 <= int(a) <= 256:
            gp.output(dac,dec2bin(int(a), 8))
            print("{:.4f}".format(int(a) / 256 * 3.3))
        elif not a.isdigit():
            print('Allowed only 0-255!')#блок обращения к пользователю



#Вывод
except ValueError:
    print('Allowed only 0-255!')
except KeyboardInterrupt:
    print('Done!')
finally:
    gp.output(dac, 0)
    gp.cleanup()
