from random import random
import math


def von_neumann(xi):
    u = (xi**2 // 100) % 10000
    return u


def von_neumann_sequence(x0, iterations):
    sequence = [x0]
    for _ in range(iterations):
        sequence.append(von_neumann(sequence[-1]))
    return sequence[1:]


def lineal_congruential_generator(x, a, c, M):
    return (a * x + c) % M


def lineal_congruential_generator_sequence(seed, a, c, M, iterations):
    sequence = [seed]
    for _ in range(iterations):
        sequence.append(lineal_congruential_generator(sequence[-1], a, c, M))
    return sequence[1:]


# Ejercicio 2:
def ejercicio_2_b():
    def run_games(n):
        wins = 0
        for _ in range(n):
            u = random()
            result = random() + random()
            if u >= 0.5:
                result += random()
            if result >= 1:
                wins += 1
        return wins / n

    print("Ejericico 2, b)")
    print(f"N: 100, Probability: {run_games(100)}")
    print(f"N: 1000, Probability: {run_games(1000)}")
    print(f"N: 10000, Probability: {run_games(10000)}")
    print(f"N: 100000, Probability: {run_games(100000)}")
    print(f"N: 1000000, Probability: {run_games(1000000)}")


def ejercicio_3_b():
    def run_games(n):
        wins = 0
        for _ in range(n):
            u = random()
            result = random() + random()
            if u >= 1 / 3:
                result += random()
            if result <= 2:
                wins += 1
        return wins / n

    print("Ejericico 3, b)")
    print(f"N: 100, Probability: {run_games(100)}")
    print(f"N: 1000, Probability: {run_games(1000)}")
    print(f"N: 10000, Probability: {run_games(10000)}")
    print(f"N: 100000, Probability: {run_games(100000)}")
    print(f"N: 1000000, Probability: {run_games(1000000)}")


def ejercicio_4_c():

    def run_simulation_a(n):
        box_lambdas = {1: 1 / 3, 2: 1 / 4, 3: 1 / 5}
        wins = 0
        for _ in range(n):
            u = random()
            box = 1
            if u > 0.4:
                box = 1
            if u > 0.72:
                box = 2
            box_lambda = box_lambdas[box]

        return wins / n
        pass

    def run_games(n):
        wins = 0
        for _ in range(n):
            u = random()
            result = random() + random()
            if u >= 1 / 3:
                result += random()
            if result <= 2:
                wins += 1
        return wins / n

    print("Ejericico 4, c)")


def ejercicio_5():

    def funcion_a(x, _=None):
        return (1 - x**2) ** (3 / 2)

    def funcion_b(x, _=None):
        return (x + 2) / ((x + 2) ** 2 - 1)

    def funcion_c(x, _=None):
        return 1 / (x**2) * ((1 / x - 1) * (((1 / x - 1) ** 2 + 1) ** -2))

    def funcion_e(x, y):
        return math.e ** ((x + y) ** 2)

    def funcion_f(x, y):
        if x == 0 or y == 0:
            return 0
        if 1 / x - 1 >= 1 / y - 1:
            return 0
        return (math.e ** (-1 / x - 1 / y + 2)) * (1 / y - 1) * (1 / ((y**2) * (x**2)))

    def approximate(fun, iterations):
        sum = 0
        for _ in range(iterations):
            sum += fun(random(), random())
        return sum / iterations

    print("Ejercicio 5")
    print(f"Inciso a, n = 100: {approximate(funcion_a, 100)}")
    print(f"Inciso a, n = 1000: {approximate(funcion_a, 1000)}")
    print(f"Inciso a, n = 10000: {approximate(funcion_a, 10000)}")
    print(f"Inciso a, n = 100000: {approximate(funcion_a, 100000)}")
    print(f"Inciso a, n = 1000000: {approximate(funcion_a, 1000000)}")
    print(f"Inciso b, n = 100: {approximate(funcion_b, 100)}")
    print(f"Inciso b, n = 1000: {approximate(funcion_b, 1000)}")
    print(f"Inciso b, n = 10000: {approximate(funcion_b, 10000)}")
    print(f"Inciso b, n = 100000: {approximate(funcion_b, 100000)}")
    print(f"Inciso b, n = 1000000: {approximate(funcion_b, 1000000)}")
    print(f"Inciso c, n = 100: {approximate(funcion_c, 100)}")
    print(f"Inciso c, n = 1000: {approximate(funcion_c, 1000)}")
    print(f"Inciso c, n = 10000: {approximate(funcion_c, 10000)}")
    print(f"Inciso c, n = 100000: {approximate(funcion_c, 100000)}")
    print(f"Inciso c, n = 1000000: {approximate(funcion_c, 1000000)}")
    print(f"Inciso e, n = 100: {approximate(funcion_e, 100)}")
    print(f"Inciso e, n = 1000: {approximate(funcion_e, 1000)}")
    print(f"Inciso e, n = 10000: {approximate(funcion_e, 10000)}")
    print(f"Inciso e, n = 100000: {approximate(funcion_e, 100000)}")
    print(f"Inciso e, n = 1000000: {approximate(funcion_e, 1000000)}")
    print(f"Inciso f, n = 100: {approximate(funcion_f, 100)}")
    print(f"Inciso f, n = 1000: {approximate(funcion_f, 1000)}")
    print(f"Inciso f, n = 10000: {approximate(funcion_f, 10000)}")
    print(f"Inciso f, n = 100000: {approximate(funcion_f, 100000)}")
    print(f"Inciso f, n = 1000000: {approximate(funcion_f, 1000000)}")


def ejercicio_6():

    def approximate_pi(iterations):
        in_circle = 0
        for _ in range(iterations):
            if random() ** 2 + random() ** 2 < 1:
                in_circle += 1
        return 4 * in_circle / iterations

    print("Ejercicio 6")
    print(f"Valor de PI: {math.pi}")
    print(f"n = 1000, Aproximacion de PI: {approximate_pi(1000)}")
    print(f"n = 10000, Aproximacion de PI: {approximate_pi(10000)}")
    print(f"n = 100000, Aproximacion de PI: {approximate_pi(100000)}")
    print(f"n = 1000000, Aproximacion de PI: {approximate_pi(1000000)}")


def ejercicio_7():

    def approximate(iterations):
        result = 0
        for _ in range(iterations):
            sum = 0
            count = 0
            while sum <= 1:
                sum += random()
                count += 1
            result += count
        return result / iterations
    print("Ejercicio 7")
    print(f"N=100, {approximate(100)}")
    print(f"N=1000, {approximate(1000)}")
    print(f"N=10000, {approximate(10000)}")
    print(f"N=100000, {approximate(100000)}")
    print(f"N=1000000, {approximate(1000000)}")


if __name__ == "__main__":
    print("Starting program.")
    ejercicio_7()
