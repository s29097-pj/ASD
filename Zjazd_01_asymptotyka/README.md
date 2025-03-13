# Zadanie_01

W pliku znajdują się definicje pięciu funkcji: `f1, f2, ..., f5` oraz pomiar sprawdzający, czy rzeczywisty czas działania funkcji `f1(n)` (wyliczony w zmiennej `Tn`) dla różnych wartości `n` (równych 2000, 4000, 8000, 16000, 32000) zmienia się zgodnie z przebiegiem funkcji liniowej (`Fn = n`). Otrzymane wyniki interpretujemy następująco: funkcja `Fn` dobrze opisuje prawdziwy czas `Tn` funkcji `f1`, jeżeli ilorazy `Fn/Tn` są mniej więcej takie same dla wszystkich wartości `n`.

---

## Definicje rzędów wielkości i notacje asymptotyczne (według Cormena, wyd. IV)

### Notacje asymptotyczne:
1. **Notacja \( O \) (górne ograniczenie)**:  
   \( f(n) = O(g(n)) \) wtedy i tylko wtedy, gdy istnieją stałe \( c > 0 \) oraz \( n_0 > 0 \), takie że:  
   \[
   0 \leq f(n) \leq c \cdot g(n) \quad \text{dla wszystkich } n \geq n_0.
   \]  
   *Interpretacja*: \( f(n) \) rośnie **nie szybciej niż** \( g(n) \).

2. **Notacja \( \Omega \) (dolne ograniczenie)**:  
   \( f(n) = \Omega(g(n)) \) wtedy i tylko wtedy, gdy istnieją stałe \( c > 0 \) oraz \( n_0 > 0 \), takie że:  
   \[
   0 \leq c \cdot g(n) \leq f(n) \quad \text{dla wszystkich } n \geq n_0.
   \]  
   *Interpretacja*: \( f(n) \) rośnie **nie wolniej niż** \( g(n) \).

3. **Notacja \( \Theta \) (ciasne ograniczenie)**:  
   \( f(n) = \Theta(g(n)) \) wtedy i tylko wtedy, gdy:  
   \[
   f(n) = O(g(n)) \quad \text{oraz} \quad f(n) = \Omega(g(n)).
   \]  
   *Interpretacja*: \( f(n) \) rośnie **tak samo jak** \( g(n) \).

4. **Notacja \( o \) (ścisłe górne ograniczenie)**:  
   \( f(n) = o(g(n)) \) wtedy i tylko wtedy, gdy dla **każdej** stałej \( c > 0 \) istnieje \( n_0 > 0 \), takie że:  
   \[
   0 \leq f(n) < c \cdot g(n) \quad \text{dla wszystkich } n \geq n_0.
   \]  
   *Interpretacja*: \( f(n) \) rośnie **wolniej niż** \( g(n) \).

5. **Notacja \( \omega \) (ścisłe dolne ograniczenie)**:  
   \( f(n) = \omega(g(n)) \) wtedy i tylko wtedy, gdy dla **każdej** stałej \( c > 0 \) istnieje \( n_0 > 0 \), takie że:  
   \[
   0 \leq c \cdot g(n) < f(n) \quad \text{dla wszystkich } n \geq n_0.
   \]  
   *Interpretacja*: \( f(n) \) rośnie **szybciej niż** \( g(n) \).

---

### Klasyczne rzędy wielkości (od najszybszych do najwolniejszych):
1. \( O(1) \) – stała,  
2. \( O(\log n) \) – logarytmiczna,  
3. \( O(n) \) – liniowa,  
4. \( O(n \log n) \) – liniowo-logarytmiczna,  
5. \( O(n^2) \) – kwadratowa,  
6. \( O(n^k) \) – wielomianowa (\( k > 2 \)),  
7. \( O(2^n) \) – wykładnicza.

---

### Jak wyznaczać złożoność?
1. **Analiza pętli**:  
   - Pojedyncza pętla z iteracjami do \( n \): \( O(n) \).  
   - Zagnieżdżone pętle: \( O(n \cdot m) \) (dla pętli zależnych od \( n \) i \( m \)).  
   - Pętla z mnożeniem/dzieleniem licznika (np. `k = k * 2`): \( O(\log n) \).

2. **Sumowanie złożoności**:  
   - Dla sekwencyjnych bloków: dominuje najwolniejszy składnik.  
   - Dla równoległych pętli: sumujemy ich złożoności.

3. **Przykłady**:  
   - Dwie zagnieżdżone pętle do \( n \): \( O(n^2) \).  
   - Pętla do \( n \) z wewnętrzną pętlą `while` logarytmiczną: \( O(n \log n) \).  

---

## Rozwiązanie

### Asymptotyczna analiza funkcji:
1. **Funkcja `f1`**  
   **Złożoność:** \( \Theta(n) \)  
   **Uzasadnienie:** Pojedyncza pętla `for` iterująca od `1` do `n-1`.

2. **Funkcja `f2`**  
   **Złożoność:** \( \Theta(n^2) \)  
   **Uzasadnienie:** Dwie zagnieżdżone pętle `for`.

3. **Funkcja `f3`**  
   **Złożoność:** \( \Theta(n^2) \)  
   **Uzasadnienie:** Analogiczna do `f2`.

4. **Funkcja `f4`**  
   **Złożoność:** \( \Theta(n \log n) \)  
   **Uzasadnienie:** Pętla `for` z wewnętrzną pętlą `while` podwajającą `k`.

5. **Funkcja `f5`**  
   **Złożoność:** \( \Theta(\log n) \)  
   **Uzasadnienie:** Pętla `while` podwajająca `k`.

---

### Wyniki pomiarów (skrócone dla czytelności):
#### f1: \( \Theta(n) \)
n=2000, Fn/Tn=13 550 135.50
n=32000, Fn/Tn=30 989 734.65


#### f3: \( \Theta(n^2) \)
n=2000, Fn/Tn=30 642 934.74
n=32000, Fn/Tn=30 363 722.98


#### f4: \( \Theta(n \log n) \)
n=2000, Fn/Tn=24 068 885.61
n=32000, Fn/Tn=23 057 983.64

---

## Wnioski końcowe
- **`f1`, `f3`, `f4`** – potwierdzono teoretyczną złożoność.  
- **`f2`, `f5`** – wyniki zaburzone przez błędy w kodzie.  
- Stałe współczynniki \( Fn/Tn \) świadczą o poprawności modelu asymptotycznego.