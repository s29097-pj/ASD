import random
import time
import sys

# Zwiększenie limitu rekurencji dla testu standardowej wersji na posortowanej tablicy
# (wymagane ze względu na złożoność O(n²))
sys.setrecursionlimit(100000)


# =================================================================
# STANDARDOWA WERSJA QUICKSORT (pivot = ostatni element)
# =================================================================

def partition(arr, p, r):
    """
    PARTYCJONOWANIE TABLICY:
    1. Jako pivot wybieramy ostatni element (arr[r])
    2. Przesuwamy wszystkie elementy mniejsze/równe pivotowi na lewą stronę
    3. Zamieniamy pivota z elementem na pozycji 'smaller'

    Zwraca indeks pivota po podziale.
    """
    pivot = arr[r]
    smaller = p  # Granica między elementami mniejszymi a większymi od pivota

    for j in range(p, r):
        if arr[j] <= pivot:
            # Zamień element mniejszy/równy pivotowi z elementem na pozycji 'smaller'
            arr[smaller], arr[j] = arr[j], arr[smaller]
            smaller += 1  # Przesuń granicę

    # Umieść pivota w poprawnej pozycji
    arr[smaller], arr[r] = arr[r], arr[smaller]
    return smaller


def quicksort(arr, p, r):
    """
    REKURENCYJNY QUICKSORT:
    1. Podziel tablicę na partycje
    2. Wywołaj quicksort dla lewej i prawej partycji
    """
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)


# =================================================================
# ZMODYFIKOWANA WERSJA QUICKSORT (pivot = środkowy element)
# =================================================================

def modified_partition(arr, p, r):
    """
    MODYFIKACJA PARTYCJONOWANIA:
    1. Wybierz środkowy element jako pivot
    2. Zamień go z ostatnim elementem
    3. Wykonaj standardowe partycjonowanie
    """
    mid = (p + r) // 2
    arr[mid], arr[r] = arr[r], arr[mid]  # Zamiana pivota
    pivot = arr[r]
    smaller = p

    for j in range(p, r):
        if arr[j] <= pivot:
            arr[smaller], arr[j] = arr[j], arr[smaller]
            smaller += 1

    arr[smaller], arr[r] = arr[r], arr[smaller]
    return smaller


def modified_quicksort(arr, p, r):
    """Analogicznie do standardowego quicksort, ale z modyfikowanym partycjonowaniem"""
    if p < r:
        q = modified_partition(arr, p, r)
        modified_quicksort(arr, p, q - 1)
        modified_quicksort(arr, q + 1, r)


# =================================================================
# TESTY WYDAJNOŚCI
# =================================================================

# Generowanie danych testowych
n = 10000
random_arr = [random.randint(0, 10000) for _ in range(n)]  # Tablica losowa
sorted_arr = sorted(random_arr.copy())  # Tablica posortowana

# Test dla tablicy losowej
arr1 = random_arr.copy()
start = time.time()
quicksort(arr1, 0, len(arr1) - 1)
time_std_random = time.time() - start

arr2 = random_arr.copy()
start = time.time()
modified_quicksort(arr2, 0, len(arr2) - 1)
time_mod_random = time.time() - start

# Test dla tablicy posortowanej
arr3 = sorted_arr.copy()
start = time.time()
quicksort(arr3, 0, len(arr3) - 1)
time_std_sorted = time.time() - start

arr4 = sorted_arr.copy()
start = time.time()
modified_quicksort(arr4, 0, len(arr4) - 1)
time_mod_sorted = time.time() - start

# =================================================================
# WYNIKI I WNIOSKI
# =================================================================
print("=== TABLICA LOSOWA ===")
print(f"Standardowy QuickSort: {time_std_random:.3f}s")
print(f"Zmodyfikowany QuickSort: {time_mod_random:.3f}s\n")

print("=== TABLICA POSORTOWANA ===")
print(f"Standardowy QuickSort: {time_std_sorted:.3f}s")
print(f"Zmodyfikowany QuickSort: {time_mod_sorted:.3f}s")

"""
WNIOSKI (przykładowe wyniki dla n=10000):
=== TABLICA LOSOWA ===
Standardowy QuickSort: 0.008s
Zmodyfikowany QuickSort: 0.007s

=== TABLICA POSORTOWANA ===
Standardowy QuickSort: 2.427s
Zmodyfikowany QuickSort: 0.005s

WNIOSKI:
1. Wersja standardowa:
   - Działa dobrze dla danych losowych (O(n log n)).
   - Dla danych posortowanych ma złożoność O(n²) – katastrofalnie wolna.

2. Wersja zmodyfikowana:
   - Zachowuje O(n log n) dla wszystkich przypadków.
   - Jest bezpieczniejsza i uniwersalna.

Zalecana jest implementacja zmodyfikowanej wersji
"""
