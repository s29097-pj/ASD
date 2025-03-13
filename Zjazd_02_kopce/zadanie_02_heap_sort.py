# -*- coding: utf-8 -*-
"""
Implementacja HeapSort i kolejki priorytetowej typu max według Cormena i prezentacji.
Indeksowanie od 0, komentarze wyjaśniają kluczowe kroki.
"""


# --------------------- HEAP SORT ---------------------
def max_heapify(arr: list, heap_size: int, i: int) -> None:
    """
    Przywraca własność kopca typu max (Cormen 6.2).
    """
    left = 2 * i + 1  # Lewe dziecko (prezentacja slajd 2)
    right = 2 * i + 2  # Prawe dziecko
    largest = i

    # Znajdź największy element między rodzicem a dziećmi
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    # Jeśli największy nie jest rodzicem - zamień i kontynuuj
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, heap_size, largest)  # Rekurencja (prezentacja slajd 2)


def build_max_heap(arr: list) -> None:
    """
    Buduje kopiec typu max z nieuporządkowanej tablicy (Cormen 6.3).
    """
    n = len(arr)
    # Iteruj od ostatniego rodzica w dół (prezentacja slajd 6)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


def heapsort(arr: list) -> None:
    """
    Sortowanie przez kopcowanie (Cormen 6.4).
    """
    build_max_heap(arr)
    heap_size = len(arr)

    # Ekstrahuj elementy od końca (prezentacja slajd 15)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Zamień max z ostatnim
        heap_size -= 1
        max_heapify(arr, heap_size, 0)  # Napraw kopiec od korzenia


# ------------------- PRIORITY QUEUE -------------------
class MaxPriorityQueue:
    """
    Kolejka priorytetowa typu max zgodna z Cormen 6.5.
    """

    def __init__(self):
        self.heap = []
        self.heap_size = 0  # Atrybut jak w książce (A.heap-size)

    def maximum(self) -> int:
        """Zwraca element o największym kluczu (Cormen 6.5.2)."""
        return self.heap[0] if self.heap_size > 0 else None

    def extract_max(self) -> int:
        """Usuwa i zwraca max element (Cormen 6.5.3)."""
        if self.heap_size < 1:
            return None

        max_val = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]  # Ostatni na początek
        self.heap_size -= 1
        max_heapify(self.heap, self.heap_size, 0)  # Napraw kopiec
        return max_val

    def insert(self, key: int) -> None:
        """Wstawianie elementu (Cormen 6.5.4)."""
        self.heap_size += 1
        if len(self.heap) < self.heap_size:
            self.heap.append(key)
        else:
            self.heap[self.heap_size - 1] = -float('inf')  # Symulacja DECREASE-KEY
        self.increase_key(self.heap_size - 1, key)  # Bubble-up

    def increase_key(self, i: int, new_key: int) -> None:
        """Zwiększ klucz (Cormen 6.5.5)."""
        if new_key < self.heap[i]:
            raise ValueError("Nowy klucz mniejszy od aktualnego")

        self.heap[i] = new_key
        # Bubble-up (prezentacja slajd 18 - pętla while)
        while i > 0 and self.heap[(i - 1) // 2] < self.heap[i]:
            parent = (i - 1) // 2
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent


# --------------------- TEST ---------------------
if __name__ == "__main__":
    print("--- HEAPSORT TEST ---")
    data = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]  # Przykład z prezentacji slajd 3
    print("Przed:", data)
    heapsort(data)
    print("Po:   ", data)

    print("\n--- PRIORITY QUEUE TEST ---")
    pq = MaxPriorityQueue()
    pq.insert(5)  # Operacje z Cormen 6.5.1
    pq.insert(3)
    pq.insert(17)
    print("Max:", pq.extract_max())  # Powinno zwrócić 17

    pq.insert(10)
    pq.increase_key(2, 25)  # Zwiększ klucz 10 → 25
    print("Nowy max:", pq.extract_max())  # 25

# --------------------- OUTPUT ---------------------
# --- HEAPSORT TEST ---
# Przed: [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
# Po:    [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]

# --- PRIORITY QUEUE TEST ---
# Max: 17
# Nowy max: 25
