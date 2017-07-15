import datetime
import itertools
from random import shuffle


def generate_exercises(limit, num_exercises):
    exercise_list = []
    for i, j in itertools.product(range(1, limit + 1), range(1, limit + 1)):
        exercise_list.append((i, j, (i) * (j)))
    while len(exercise_list) < num_exercises:
        exercise_list += exercise_list
    shuffle(exercise_list)
    return exercise_list[0:num_exercises]


def get_user_input(question, default_value):
    choice = ''
    while choice == '':
        try:
            choice = input(question + " ")
            if choice == '':
                choice = default_value
            choice = int(choice)
        except:
            choice = ''
    return choice


if __name__ == "__main__":
    gridsize = get_user_input("Bis zu welcher Zahl soll das 1*1 gehen? [10]", 10)
    print("OK, dann geht es bis %s*%s." % (gridsize, gridsize))
    num_exercises = get_user_input("Wie viele Aufgaben sollen gestellt werden? [%s] " % (gridsize ** 2),
                                   gridsize ** 2)
    print("Es werden also %i Aufgaben gestellt." % (num_exercises))
    exercise_list = generate_exercises(gridsize, num_exercises)
    incorrect_answers = 0
    started = datetime.datetime.now().replace(microsecond=0)
    while len(exercise_list) > 0:
        if len(exercise_list) % 10 == 0 and len(exercise_list) != num_exercises:
            print("Es sind noch %s Aufgaben uebrig." % (len(exercise_list)))
        exercise = exercise_list.pop(0)
        result = ''
        failed = False
        while True:
            result = input(str(exercise[0]) + " * " + str(exercise[1]) + " = ")
            if result != str(exercise[2]):
                if not failed:
                    print("Das Ergebnis ist leider nicht richtig. Versuche es noch einmal.")
                    incorrect_answers += 1
                    failed = True
                else:
                    print("Dieses Ergebnis ist leider auch falsch. Denk noch einmal in Ruhe nach!")
            else:
                break
    ended = datetime.datetime.now().replace(microsecond=0)
    print("Du hast von %s Aufgaben %s im ersten Anlauf richtig beantwortet." % (
        num_exercises, num_exercises - incorrect_answers))
    print("Insgesamt hast Du %s gebraucht." % (ended - started))
