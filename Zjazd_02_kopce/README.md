# Zadanie_02 - Sortowanie przez kopcowanie

## Treść zadania
Zaimplementuj algorytm sortowania przez kopcowanie z prezentacji (0.5 pkt).  
Jeśli wykorzystamy kopiec do implementacji kolejki priorytetowej typu max, potrzebne będą:  
- **`Insert(S, x)`** – wstawia element `x` do kolejki `S` (na koniec listy, a następnie przestawiamy elementy) **(0.5 pkt)**,  
- **`Maximum(S)`** – zwraca wartość elementu o największym kluczu **(0.5 pkt)**,  
- **`Extract-Max(S)`** – usuwa i daje w wyniku element ze zbioru `S` o największym kluczu,  
- **`Increase-Key(S, x, k)`** – zmienia wartość klucza elementu `x` na `k` (przy czym `k >= x`) **(0.5 pkt)**.

---

## Opis rozwiązania dla laika
### Czym jest sortowanie przez kopcowanie?
Wyobraź sobie, że musisz ułożyć książki na półce od najmniejszej do największej. **Sortowanie przez kopcowanie** działa jak sprytny robot, który:
1. **Buduje kopiec** – układ książek w taki sposób, że największa zawsze leży na wierzchu (jak stos gazet).  
2. **Sortuje** – zabiera książkę z wierzchu, odkłada na półkę i naprawia stos, by znów największa była na górze.  
Powtarza to aż do posortowania wszystkich książek.

![Animacja sortowania](https://upload.wikimedia.org/wikipedia/commons/1/1b/Sorting_heapsort_anim.gif)

---

### Kolejka priorytetowa typu max
To jak „straż pożarna dla liczb” – zawsze najpierw zajmuje się największą wartością.  
- **`Insert(S, x)`** – Dodaj nową liczbę do kolejki. Jeśli jest większa od rodzica, robot przesunie ją wyżej.  
  *Przykład:* Wstawienie `15` do `[10, 8, 7]` → `[15, 8, 10, 7]`.  
- **`Maximum(S)`** – Pokazuje największą liczbę bez jej usuwania.  
  *Przykład:* Dla `[15, 8, 10, 7]` zwróci `15`.  
- **`Extract-Max(S)`** – Zabiera największą liczbę i naprawia kolejkę.  
  *Przykład:* Dla `[15, 8, 10, 7]` zwróci `15`, a kolejka stanie się `[10, 8, 7]`.  
- **`Increase-Key(S, x, k)`** – Zamienia liczbę `x` na większą `k` i przesuwa ją w górę, jeśli trzeba.  
  *Przykład:* Zmiana `8` na `12` w `[15, 8, 10, 7]` → `[15, 12, 10, 7]`.

---

## Struktura kodu
- **Heapsort** – sortuje tablicę w dwóch krokach: budowa kopca + iteracyjne usuwanie maksimum.  
- **MaxPriorityQueue** – klasa z metodami `insert`, `maximum`, `extract_max`, `increase_key`.

---

## Przykłady użycia
### Sortowanie tablicy
```python
data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heapsort(data)  # Wynik: [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
```

---

### Kolejka priorytetowa
```python
pq = MaxPriorityQueue()
pq.insert(5)
pq.insert(3)
pq.insert(17)
print(pq.extract_max())  # Zwróci 17

pq.insert(10)
pq.increase_key(1, 25)   # Zwiększ klucz 10 → 25
print(pq.extract_max())  # Zwróci 25
```
---

## Złożoność czasowa
| Operacja               | Złożoność       | Opis                                                                 |
|------------------------|-----------------|----------------------------------------------------------------------|
| **Sortowanie (Heapsort)** | O(n log n)      | Czas sortowania całej tablicy ([dowód w Cormenie](https://example.com)) |
| `Insert`               | O(log n)        | Wstawianie nowego elementu i naprawa kopca                           |
| `Extract-Max`          | O(log n)        | Usuwanie maksimum + naprawa kopca                                    |
| `Increase-Key`         | O(log n)        | Modyfikacja klucza + ewentualne przesunięcie w górę                  |
| `Maximum`              | O(1)            | Zwraca korzeń kopca bez modyfikacji                                  |

---

## Literatura
- **Książka**: *Wprowadzenie do algorytmów* (Cormen et al.), rozdział 6 – szczegółowy opis matematyczny i dowody złożoności.
- **Prezentacja**: [Sortowanie przez kopcowanie – slajdy] – wizualizacja działania algorytmu.
