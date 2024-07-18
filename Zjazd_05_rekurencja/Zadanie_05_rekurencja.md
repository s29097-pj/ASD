# Zadanie_05 - rekurencja

### Analiza krok po kroku, co dzieje się przy wywołaniu `tes(108)`:

1. `tes(108)`:
- `a` (108) jest większe niż 100.
- Wypisuje `108`.
- Wywołuje `tes(105)` (108 - 3).

```python
# tes(108)
# 108 > 100
print(108)
tes(105)
```

2. `tes(105)`:
- `a` (105) jest większe niż 100.
- Wypisuje `105`.
- Wywołuje `tes(102)` (105 - 3).

```python
# tes(105)
# 105 > 100
print(105)
tes(102)
```

3. `tes(102)`:
- `a` (102) jest większe niż 100.
- Wypisuje `102`.
- Wywołuje `tes(99)` (102 - 3).

```python
# tes(102)
# 102 > 100
print(102)
tes(99)
```

4. `tes(99)`:
- `a` (99) jest mniejsze niż 100.
- Wywołuje `tes(109)` (99 + 10).

```python
# tes(99)
# 99 < 100
tes(109)
```

5. `tes(109)`:
- `a` (109) jest większe niż 100.
- Wypisuje `109`.
- Wywołuje `tes(106)` (109 - 3).

```python
# tes(109)
# 109 > 100
print(109)
tes(106)
```

6. `tes(106)`:
- `a` (106) jest większe niż 100.
- Wypisuje `106`.
- Wywołuje `tes(103)` (106 - 3).

```python
# tes(106)
# 106 > 100
print(106)
tes(103)
```

7. `tes(103)`:
- `a` (103) jest większe niż 100.
- Wypisuje `103`.
- Wywołuje `tes(100)` (103 - 3).

```python
# tes(103)
# 103 > 100
print(103)
tes(100)
```

8. `tes(100)`:
- `a` (100) jest równe 100.
- Wypisuje `100`.

```python
# tes(100)
# 100 == 100
print('100')
```

Cała sekwencja wywołań zakończyła się, a wypisane wartości to:

```
108
105
102
99
109
106
103
100
```

