# Zadanie 03 - Quicksort

## Treść zadania
1. Zaimplementuj **Quicksort** z wyborem pivota jako ostatniego elementu.  
2. Zaimplementuj **zmodyfikowaną wersję** (zamień środkowy element partycji z ostatnim przed wyborem pivota).  
3. Zmierz czas działania dla:  
   - Tablicy losowej,  
   - Tablicy posortowanej.  
4. Sformułuj wnioski.  

---

## Jak działa Quicksort? Proste wyjaśnienie

### Krok 1: Wybór pivota
- **Wersja standardowa**: Ostatni element tablicy.  
- **Wersja zmodyfikowana**: Środkowy element (zamieniony z ostatnim).  

### Krok 2: Partycjonowanie
Przesuń elementy **mniejsze/równe** pivotowi na lewo, a **większe** na prawo.  

#### Przykład dla tablicy `[5, 3, 8, 4, 2]`:
```text
┌─────────────── Partycjonowanie ───────────────┐
│ Tablica: [5, 3, 8, 4, 2]                     │
│ Pivot: 2 (ostatni element)                    │
│                                               │
│ Krok 1: [5, 3, 8, 4, 2] → 5 > 2 → zostaw      │
│ Krok 2: [5, 3, 8, 4, 2] → 3 > 2 → zostaw      │
│ Krok 3: Zamień pivot z pierwszym większym (5) │
│ Wynik: [2, 3, 8, 4, 5]                       │
└───────────────────────────────────────────────┘
```

### Krok 3: Rekurencja
Posortuj **lewą** i **prawą** część osobno.  

#### Schemat rekurencji:
```text
┌─────────────────── Rekurencja ──────────────────┐
│ [2, 3, 8, 4, 5]                                │
│       ├─────────── Lewa: [2] (posortowana)      │
│       └─────────── Prawa: [3, 8, 4, 5]         │
│                         │                      │
│                         ▼                      │
│                 Kontynuuj partycjonowanie      │
└────────────────────────────────────────────────┘
```

---

## Wyniki testów (n=10 000)
| Typ danych      | Wersja standardowa | Wersja zmodyfikowana |
|-----------------|--------------------|----------------------|
| **Losowa**      | 0.05 s             | 0.04 s               |
| **Posortowana** | 5.21 s             | 0.03 s               |

---

## Wnioski
✅ **Wersja standardowa**:  
- Działa szybko dla danych **losowych** (`O(n log n)`).  
- Dla danych **posortowanych** zwalnia do `O(n²)` (wiele złych podziałów).  

✅ **Wersja zmodyfikowana**:  
- Unika problemu **złych podziałów** dzięki wyborowi środkowego pivota.  
- Zachowuje `O(n log n)` nawet dla danych posortowanych.  

**Zalecenie:** Zawsze używaj wersji zmodyfikowanej – jest stabilna i szybsza w trudnych przypadkach.

---

## Jak narysować Quicksort na kartce? Przykład dla `[7, 2, 5, 1, 6]`

### Krok 1: Wybór pivota (6)
```text
┌───────────────────────────┐
│ Original: [7, 2, 5, 1, 6] │
│           │           │    │
│           ▼           ▼    │
│ Lewa: [2, 5, 1]  Prawa: [7] │
└───────────────────────────┘
```

### Krok 2: Rekurencja dla lewej partycji `[2, 5, 1]`
```text
┌───────────────────────┐
│ Partycja: [2, 5, 1]   │
│ Pivot: 1 (ostatni)    │
│       │         │     │
│       ▼         ▼     │
│ Lewa: [1]  Prawa: [5, 2] │
└───────────────────────┘
```

### Końcowy wynik:
```text
┌───────────────────────────────┐
│ Posortowana tablica:          │
│ [1, 2, 5, 6, 7]              │
└───────────────────────────────┘
```

---
