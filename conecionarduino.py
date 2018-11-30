import time
import warnings
from collections import deque
import serial
import numpy as np
import matplotlib.pyplot as plt
N = 200
data = deque([0] * N, maxlen=N)  # deque con longitud máxima N
#Creamos la figura
plt.ion()
fig, ax = plt.subplots()
ll, = ax.plot(data)
# Abrimos la conexión con Arduino
arduino = serial.Serial('COM3', baudrate=9600, timeout=1.0)
arduino.setDTR(False)
time.sleep(1)
arduino.flushInput()
arduino.setDTR(True)
with arduino:
    while True:
        try:
            line = arduino.readline()
            if not line:
                # HACK: Descartamos líneas vacías porque fromstring produce
                # resultados erróneos, ver
                # https://github.com/numpy/numpy/issues/1714
                continue
            xx, yy = np.fromstring(line.decode('ascii', errors='replace'),
                                   sep=' ')
            data.append(yy)
            ll.set_ydata(data)
            ax.set_ylim(min(data) - 10, max(data) + 10)
            plt.pause(0.001)
        except ValueError:
            warnings.warn("Line {} didn't parse, skipping".format(line))
        except KeyboardInterrupt:
            print("Exiting")
            break