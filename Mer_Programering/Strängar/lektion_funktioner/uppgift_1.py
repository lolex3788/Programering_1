import numpy as np
import matplotlib

def N(t):
    return 11/(1+3.4*np.exp(-0.03*t))

# a)
print(f"Antal människor år 1950: {N(0)} miljader")

# b) övre gräns?
år = 100

t = np.arange(år)

matplotlib.plt(t, N(t))
matplotlib.ylabel("Antal människor")
matplotlib.xlabel("År efter 1950")
matplotlib.title("Modell för population")
matplotlib.show()

print(f"Övre gräns: {N(5000)} miljader")