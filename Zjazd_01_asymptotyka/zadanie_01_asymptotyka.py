import math
from timeit import default_timer as timer

def f1(n):
    s = 0
    for j in range(1, n):
        s = s + 1 / j
    return s

def f2(n):
    s = 0
    k = 2
    while k <= n:
        s = s + 1 / k
        k = k * 2
    return s

def f3(n):
    s = 0
    for j in range(1, n):
        for k in range(1, j):
            s = s + k / j
    return s

def f4(n):
    s = 0
    for j in range(1, n):
        k = 2
        while k <= n:
            s = s + k / j
            k = k * 2
    return s

def f5(n):
    s = 0
    for j in range(1, n):
        for k in range(1, n):
            s = s + k / j
    return s

nn = [2000, 4000, 8000, 16000, 32000]

# F1: O(n)
# Fn = n - złożoność liniowa
print("f1")
for n in nn:
    start = timer()
    f1(n)
    stop = timer()
    Tn = stop - start
    Fn = n
    print(f"n={n}, Tn={Tn:.6f}, Fn={Fn}, Fn/Tn={Fn / Tn:.6f}")

# F2: O(log n)
# Fn = math.log(n, 2) - złożoność logarytmiczna
print("f2")
for n in nn:
    start = timer()
    f2(n)
    stop = timer()
    Tn = stop - start
    Fn = math.log(n, 2)
    print(f"n={n}, Tn={Tn:.6f}, Fn={Fn:.6f}, Fn/Tn={Fn / Tn:.6f}")

# F3: O(n^2)
# Fn = n * n - złożoność kwadratowa
print("f3")
for n in nn:
    start = timer()
    f3(n)
    stop = timer()
    Tn = stop - start
    Fn = n * n
    print(f"n={n}, Tn={Tn:.6f}, Fn={Fn}, Fn/Tn={Fn / Tn:.6f}")

# F4: O(n log n)
# Fn = n * math.log(n, 2) - złożoność liniowo-logarytmiczna
print("f4")
for n in nn:
    start = timer()
    f4(n)
    stop = timer()
    Tn = stop - start
    Fn = n * math.log(n, 2)
    print(f"n={n}, Tn={Tn:.6f}, Fn={Fn:.6f}, Fn/Tn={Fn / Tn:.6f}")

# F5: O(n^2)
# Fn = n * n - złożoność kwadratowa
print("f5")
for n in nn:
    start = timer()
    f5(n)
    stop = timer()
    Tn = stop - start
    Fn = n * n
    print(f"n={n}, Tn={Tn:.6f}, Fn={Fn}, Fn/Tn={Fn / Tn:.6f}")

# Wyniki:
# f1
# n=2000, Tn=0.000069, Fn=2000, Fn/Tn=28860028.786124
# n=4000, Tn=0.000127, Fn=4000, Fn/Tn=31496063.156229
# n=8000, Tn=0.000269, Fn=8000, Fn/Tn=29739776.938777
# n=16000, Tn=0.000518, Fn=16000, Fn/Tn=30905930.167616
# n=32000, Tn=0.001028, Fn=32000, Fn/Tn=31131432.968945

# f2
# n=2000, Tn=0.000002, Fn=10.965784, Fn/Tn=4767733.700138
# n=4000, Tn=0.000001, Fn=11.965784, Fn/Tn=9971471.436185
# n=8000, Tn=0.000001, Fn=12.965784, Fn/Tn=11787064.835515
# n=16000, Tn=0.000001, Fn=13.965784, Fn/Tn=15517545.385825
# n=32000, Tn=0.000001, Fn=14.965784, Fn/Tn=16628657.019052

# f3
# n=2000, Tn=0.062122, Fn=4000000, Fn/Tn=64389012.660154
# n=4000, Tn=0.242699, Fn=16000000, Fn/Tn=65925281.933986
# n=8000, Tn=0.968831, Fn=64000000, Fn/Tn=66058958.652872
# n=16000, Tn=3.873367, Fn=256000000, Fn/Tn=66092370.438762
# n=32000, Tn=16.229078, Fn=1024000000, Fn/Tn=63096622.779150

# f4
# n=2000, Tn=0.000935, Fn=21931.568569, Fn/Tn=23446192.535048
# n=4000, Tn=0.002067, Fn=47863.137139, Fn/Tn=23159208.962277
# n=8000, Tn=0.004520, Fn=103726.274277, Fn/Tn=22949306.240220
# n=16000, Tn=0.009883, Fn=223452.548555, Fn/Tn=22608874.325907
# n=32000, Tn=0.020999, Fn=478905.097109, Fn/Tn=22806525.058280

# f5
# n=2000, Tn=0.120037, Fn=4000000, Fn/Tn=33322975.442011
# n=4000, Tn=0.503754, Fn=16000000, Fn/Tn=31761509.179831
# n=8000, Tn=2.027064, Fn=64000000, Fn/Tn=31572763.676447
# n=16000, Tn=7.762072, Fn=256000000, Fn/Tn=32980884.485477
# n=32000, Tn=31.192672, Fn=1024000000, Fn/Tn=32828223.454716
