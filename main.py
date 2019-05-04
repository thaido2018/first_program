import matplotlib.pyplot as plt
import random

def f():
    x = [i for i in range(40)]
    y = [i + random.randint(-5, 5) for i in range(40)]
    print("Hello world")
    plt.plot(x, y)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    f()
