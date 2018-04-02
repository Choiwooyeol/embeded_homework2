import time
from time import sleep
import RPi.GPIO as GPIO
from gpiozero import Buzzer

#gpio setting
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(16,GPIO.IN)
GPIO.setup(20,GPIO.IN)
GPIO.setup(21,GPIO.IN)

buzzer = Buzzer(2)

## Init motor
motor = GPIO.PWM(17,100)
## motor control start

motor.start(2.5)
switch = False
print ("motor ready")

pygame.init()
#sound init
#pygame.mixer.pre_init()
#pygame.mixer.init(48000, -16, -1, 1024)
#soundA = pygame.mixer.Sound("./python_games/match3.wav")
#audio device available ..? why?
#soundChannelA = pygame.mixer.Channel(1)

#password setting
arr1 = [0,1,0,1] # password
arr2 = [] #array for input

try:
	while True:
		if(GPIO.input(16) == False):
			arr2.append(0)
			print ("0 input")
			time.sleep(0.2)
		elif(GPIO.input(20) == False):
			arr2.append(1)
			print ("1 input")
			time.sleep(0.2)
		elif(GPIO.input(21) == False):
			del arr2[:]
			print ("Clear")
			motor.ChangeDutyCycle(2.5)
			if(switch == True):
				switch = False
			time.sleep(0.2)
		elif((arr1 == arr2) == True):
			print("same")
			if(switch == False):
				buzzer.on()
				sleep(0.5)
				buzzer.off()
				motor.ChangeDutyCycle(12.5)
				switch = True
			#soundChannelA.play(soundA)
		else:
			print("wait")
			time.sleep(0.2)
except KeyboardInterrupt:
	GPIO.cleanup()
