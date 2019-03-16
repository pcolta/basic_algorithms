import random


def get_number_from_input_or_default(given_number, default):
    if not given_number:
        print('wybrano domyślną wartość {}'.format(default))
        return default
    else:
        return int(given_number)


def choose_number():
    while True:
        try:
            print("Podaj liczbę: ")
            return int(input())
        except ValueError:
            print("To nie jest liczba! Spróbuj jeszcze raz")


correct_number = random.randint(1, 1000)

i = 1
number_found = False
while not number_found:
    number_answer = choose_number()
    if number_answer < correct_number:
        print("Za mało")
        i += 1
    elif number_answer == correct_number:
        print("Odpowiedz prawidłowa")
        print("Potrzeba było: {} prób".format(i))
        number_found = True
    else:
        print("Za dużo")
        i += 1
