import serial, time
arduino = serial.Serial('COM3', baudrate=9600, timeout=1.0)

def readPort():
    arduino.write(b'P')
    time.sleep(1)
    rawString = arduino.readline()
    print(rawString)
    data= ()


time.sleep(2)
arduino.write(b'L')

time.sleep(2)
arduino.write(b'P')
time.sleep(1)
rawString = arduino.readline()
print(rawString)

arduino.close()




