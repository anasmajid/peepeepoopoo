import time
from serial import Serial

arduino = Serial('/dev/ttyACM1', 9600, timeout=.1)

time.sleep(1) #give the connection a second to settle

flag = True

while flag:
    userInput = input()
    if userInput == '1':
        arduino.write(b'1')
        print(arduino.readline())
        # time.sleep(1)
    elif userInput == '2':
        arduino.write(b'2')
        print(arduino.readline())
    elif userInput == '3':
        arduino.write(b'3')
        print(arduino.readline())
    elif userInput == '4':
        arduino.write(b'4')
        print(arduino.readline())
    elif userInput == '5':
        arduino.write(b'5')
        print(arduino.readline())
    elif userInput == '6':
        arduino.write(b'6')
        print(arduino.readline())

    
