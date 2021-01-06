def Sqrt(r):
    x = r
    eplison = 10 ** (-10)

    while abs(x * x - r) > eplison:
        x = (x + r / x) / 2
    return x

def main():
    import matplotlib.pyplot as plt
    import numpy as np
    import time

    a = []
    result = []
    start_time = time.time()
    period = []

    for i in np.arange(0, 10000, 0.5):
        a.append(i)
        k = Sqrt(i)
        end_time = time.time()
        result.append(k)
        period.append(end_time-start_time)
        start_time = end_time

    plt.plot(a, period)
    plt.show()


if __name__ == '__main__':
    main()
