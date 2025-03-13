import math
from timeit import default_timer as timer

def f1(n):
    s = 0
    for j in range(1, n):
        s = s + 1 / j
    return s

def f2(n):
    s = 0;
    for j in range(1, n):
      for k in range(1, n):
        s = s + k / j
    return s

def f3(n):
    s = 0
    for j in range(1, n):
        for k in range(1, n):
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
    k = 2
    while k <= n:
        s = s + 1 / k
        k = k * 2
    return s

nn = [2000, 4000, 8000, 16000, 32000]

# F1: O(n)
# Fn = n
print("f1")
for n in nn:
    start = timer()
    f1(n)
    stop = timer()
    Tn = stop - start
    Fn = n
    print(f"n={n}, Tn={Tn:.6f}, Fn={Fn}, Fn/Tn={Fn / Tn:.6f}")

# F2: O(n^2)
# Fn = n * n
print("f2")
for n in nn:
    start = timer()
    f5(n)
    stop = timer()
    Tn = stop - start
    Fn = n * n
    print(f"n={n}, Tn={Tn:.6f}, Fn={Fn}, Fn/Tn={Fn / Tn:.6f}")


# F3: O(n^2)
# Fn = n * n
print("f3")
for n in nn:
    start = timer()
    f3(n)
    stop = timer()
    Tn = stop - start
    Fn = n * n
    print(f"n={n}, Tn={Tn:.6f}, Fn={Fn}, Fn/Tn={Fn / Tn:.6f}")

# F4: O(n log n)
# Fn = n * math.log(n, 2)
print("f4")
for n in nn:
    start = timer()
    f4(n)
    stop = timer()
    Tn = stop - start
    Fn = n * math.log(n, 2)
    print(f"n={n}, Tn={Tn:.6f}, Fn={Fn:.6f}, Fn/Tn={Fn / Tn:.6f}")


# F5: O(log n)
# Fn = math.log(n, 2)
print("f5")
for n in nn:
    start = timer()
    f2(n)
    stop = timer()
    Tn = stop - start
    Fn = math.log(n, 2)
    print(f"n={n}, Tn={Tn:.6f}, Fn={Fn:.6f}, Fn/Tn={Fn / Tn:.6f}")

# Wnioski:
# f1: O(n) - złożoność liniowa
# f2: O(n^2) - złożoność kwadratowa
# f3: O(n^2) - złożoność kwadratowa
# f4: O(n log n) - złożoność liniowo-logarytmiczna
# f5: O(log n) - złożoność logarytmiczna

# f1
# n=2000, Tn=0.000148, Fn=2000, Fn/Tn=13550135.502168
# n=4000, Tn=0.000194, Fn=4000, Fn/Tn=20597322.334985
# n=8000, Tn=0.000254, Fn=8000, Fn/Tn=31520882.599346
# n=16000, Tn=0.000519, Fn=16000, Fn/Tn=30828516.381201
# n=32000, Tn=0.001033, Fn=32000, Fn/Tn=30989734.646071

# f2
# n=2000, Tn=0.000002, Fn=4000000, Fn/Tn=1739130430577.132812
# n=4000, Tn=0.000001, Fn=16000000, Fn/Tn=14545455033167.412109
# n=8000, Tn=0.000001, Fn=64000000, Fn/Tn=71111126561181.093750
# n=16000, Tn=0.000001, Fn=256000000, Fn/Tn=319999928048362.375000
# n=32000, Tn=0.000001, Fn=1024000000, Fn/Tn=1137777737533606.000000

# f3
# n=2000, Tn=0.130536, Fn=4000000, Fn/Tn=30642934.735155
# n=4000, Tn=0.519600, Fn=16000000, Fn/Tn=30792947.260334
# n=8000, Tn=2.048287, Fn=64000000, Fn/Tn=31245615.239347
# n=16000, Tn=8.312562, Fn=256000000, Fn/Tn=30796762.779032
# n=32000, Tn=33.724455, Fn=1024000000, Fn/Tn=30363722.975186

# f4
# n=2000, Tn=0.000911, Fn=21931.568569, Fn/Tn=24068885.611145
# n=4000, Tn=0.002021, Fn=47863.137139, Fn/Tn=23677040.385707
# n=8000, Tn=0.004439, Fn=103726.274277, Fn/Tn=23365983.573119
# n=16000, Tn=0.009675, Fn=223452.548555, Fn/Tn=23096825.559332
# n=32000, Tn=0.020770, Fn=478905.097109, Fn/Tn=23057983.644814

# f5
# n=2000, Tn=0.126674, Fn=10.965784, Fn/Tn=86.566901
# n=4000, Tn=0.533588, Fn=11.965784, Fn/Tn=22.425146
# n=8000, Tn=2.099083, Fn=12.965784, Fn/Tn=6.176880
# n=16000, Tn=8.228075, Fn=13.965784, Fn/Tn=1.697333
# n=32000, Tn=32.954620, Fn=14.965784, Fn/Tn=0.454133