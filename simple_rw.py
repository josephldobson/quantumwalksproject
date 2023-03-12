from math import comb
import json


def srw(N):
    X = [i for i in range(N*2+1)]
    Y = [0 for i in range(N*2+1)]

    def f(t,n):
        t = abs(t)
        n = abs(n)
        x = comb(t, int((t+n)/2))/(2**t)
        return x
    t = 0

    while t<N/2+1:

        Y = [f(2*t, i-N) for i in X]
        t += 1
        yield X, Y

if __name__ == "__main__":
    length = 200
    rw = srw(length)
    X, Y = next(rw)
    plots = [*rw]
    print(len(plots))
    print(len(plots[0][0]))


    with open(f"simulation/simple{length}", "w") as fp:
        json.dump(plots, fp)
