import datetime
import itertools
from random import shuffle


def generate_exercises(LIMIT=10):
    exercise_list = []
    for i, j in itertools.product(range(1, LIMIT + 1), range(1, LIMIT + 1)):
        exercise_list.append((i, j, (i) * (j)))

    shuffle(exercise_list)
    return exercise_list


if __name__ == "__main__":
    gridsize = 10
    incorrect_answers = 0
    exercise_list = generate_exercises(gridsize)
    num_exercises = len(exercise_list)
    print("Insgesamt gibt es %s Aufgaben." % (num_exercises))
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
