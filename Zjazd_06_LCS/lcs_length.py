# Ciągi wejściowe:
# x[0], x[1], ..., x[m-1]
# y[0], y[1], ..., y[n-1]
# Tablice dwuwymiarowe c, b rozmiaru [0...m][0...n]

# Funkcja obliczająca długość najdłuższego wspólnego podciągu (LCS) dwóch ciągów x i y
def lcsLength(x, y):
    # Pobieranie długości ciągów x i y
    m = len(x)
    n = len(y)

    # Inicjalizacja dwuwymiarowych tablic c i b rozmiaru (m+1) x (n+1), wypełnionych zerami
    c = [[0 for i in range(n + 1)] for j in range(m + 1)]
    b = [[0 for i in range(n + 1)] for j in range(m + 1)]

    # Iteracja przez elementy ciągów x i y
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Jeśli bieżące elementy x i y są takie same
            if x[i - 1] == y[j - 1]:
                # Uaktualnij wartość w tablicy c na podstawie wartości z poprzednich komórek
                c[i][j] = c[i - 1][j - 1] + 1
                # Ustaw kierunek w tablicy b na ukos ('\\')
                b[i][j] = '\\'
            else:
                # Jeśli elementy są różne, wybierz większą wartość z sąsiednich komórek
                if c[i - 1][j] >= c[i][j - 1]:
                    # Uaktualnij wartość w tablicy c na podstawie wartości z poprzedniego wiersza
                    c[i][j] = c[i - 1][j]
                    # Ustaw kierunek w tablicy b na w górę ('|')
                    b[i][j] = '|'
                else:
                    # Uaktualnij wartość w tablicy c na podstawie wartości z poprzedniej kolumny
                    c[i][j] = c[i][j - 1]
                    # Ustaw kierunek w tablicy b na w lewo ('-')
                    b[i][j] = '-'

    # Zwróć tablice c i b
    return c, b

# Wyznacz ile najmniej liter należy dopisać do zadanego słowa, żeby w tak utworzonym słowie występował alfabet jako podciąg?
# - Zakładamy, że kolejność liter w alfabecie ma znaczenie.
# - Dopisywać znaki można przed słowem, pomiędzy literami słowa, po słowie.

def min_letters_to_add_for_alphabet_subsequence(word):
    # Zdefiniuj alfabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Oblicz długość LCS między słowem a alfabetem
    c, b = lcsLength(word, alphabet)

    # Długość LCS znajduje się w prawym dolnym rogu macierzy c
    lcs_length = c[len(word)][len(alphabet)]

    # Oblicz minimalną liczbę liter do dodania
    min_letters_to_add = len(alphabet) - lcs_length

    return min_letters_to_add

# Przykładowe użycie
word = "exampleword"
print("Minimalna liczba liter do dopisania dla słowa", word, "to:", min_letters_to_add_for_alphabet_subsequence(word))
