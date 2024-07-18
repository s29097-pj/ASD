def recursive_print(a):
    # Sprawdzenie, czy a jest równe 100
    if a == 100:
        print('100')  # Wypisanie '100' na ekran
    # Sprawdzenie, czy a jest większe niż 100
    elif a > 100:
        print(a)  # Wypisanie wartości a na ekran
        return recursive_print(a - 3)  # Wywołanie funkcji ponownie z a pomniejszonym o 3
    else:
        # W przeciwnym wypadku (gdy a < 100)
        return recursive_print(a + 10)  # Wywołanie funkcji ponownie z a powiększonym o 10

# Zmienna a ustawiona na 108
a = 108
# Wywołanie funkcji recursive_print z a jako argument
recursive_print(a)
