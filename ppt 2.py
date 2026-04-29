import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 4*x - 9

a = 2
b = 3
tol = 0.001
iterasi = 1

print("Iter | a | b | xr | f(xr)")

while True:
    xr = (a*f(b) - b*f(a)) / (f(b)-f(a))

    print(iterasi, round(a,4), round(b,4), round(xr,4), round(f(xr),4))

    if abs(f(xr)) < tol:
        break

    if f(a)*f(xr) < 0:
        b = xr
    else:
        a = xr

    iterasi += 1

print("Akar =", xr)

# grafik
x = np.linspace(1,4,400)
y = f(x)

plt.axhline(0)
plt.plot(x,y)
plt.scatter(xr,f(xr))
plt.title("Metode Regula Falsi")
plt.grid()
plt.show()