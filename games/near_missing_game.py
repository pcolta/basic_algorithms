import random

def get_number_interval(default=1000):
    while True:
        try:
            print("Podaj liczbe na której ma się kończyć przedział wybranej liczby (domyślnie {}): ".format(default))
            given_number = input()
            return get_number_from_input_or_default(given_number, default)
        except ValueError:
            print("To nie jest liczba! Spróbuj jeszcze raz")


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


number_interval = get_number_interval()
if number_interval:
    correct_number = random.randint(1, number_interval)
else:
    correct_number = random.randint(1, 1000)

print(correct_number)
i = 1
number_found = False
while not number_found:
    number_answer = choose_number()
    if number_answer < correct_number:
        print("Liczba jest za mała")
        i += 1
    elif number_answer == correct_number:
        print("Odpowiedz prawidłowa")
        print("Potrzeba było: {} prób".format(i))
        number_found = True
    else:
        print("Liczba jest za duża")
        i += 1
