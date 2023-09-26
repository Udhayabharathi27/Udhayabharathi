import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

lcd_rs = 18
lcd_en = 19
lcd_d4 = 10
lcd_d5 = 11
lcd_d6 = 12
lcd_d7 = 13

ledA = 6
ledB = 7
ledC = 8
ledD = 9
ULT1 = 2
ULT2 = 3
ULT3 = 4
ULT4 = 5
fanA1 = 14
fanA2 = 15
fanB1 = 16
fanB2 = 17
cm1 = 0
cm2 = 0
cm3 = 0
cm4 = 0
A = 0
B = 0
C = 0
D = 0
E = 0

GPIO.setup(lcd_rs, GPIO.OUT)
GPIO.setup(lcd_en, GPIO.OUT)
GPIO.setup(lcd_d4, GPIO.OUT)
GPIO.setup(lcd_d5, GPIO.OUT)
GPIO.setup(lcd_d6, GPIO.OUT)
GPIO.setup(lcd_d7, GPIO.OUT)

GPIO.setup(ledA, GPIO.OUT)
GPIO.setup(ledB, GPIO.OUT)
GPIO.setup(ledC, GPIO.OUT)
GPIO.setup(ledD, GPIO.OUT)
GPIO.setup(ULT1, GPIO.OUT)
GPIO.setup(ULT2, GPIO.OUT)
GPIO.setup(ULT3, GPIO.OUT)
GPIO.setup(ULT4, GPIO.OUT)
GPIO.setup(fanA1, GPIO.OUT)
GPIO.setup(fanA2, GPIO.OUT)
GPIO.setup(fanB1, GPIO.OUT)
GPIO.setup(fanB2, GPIO.OUT)

def bacaULT1(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.002)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(pin, GPIO.LOW)
    GPIO.setup(pin, GPIO.IN)
    return GPIO.pulseIn(pin, GPIO.HIGH)

def bacaULT2(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.002)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(pin, GPIO.LOW)
    GPIO.setup(pin, GPIO.IN)
    return GPIO.pulseIn(pin, GPIO.HIGH)

def bacaULT3(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.002)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(pin, GPIO.LOW)
    GPIO.setup(pin, GPIO.IN)
    return GPIO.pulseIn(pin, GPIO.HIGH)