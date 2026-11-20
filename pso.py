import math
import random


def sphere(x):
    return sum(a * a for a in x)


def rastrigin(x):
    return 10 * len(x) + sum(a * a - 10 * math.cos(2 * math.pi * a) for a in x)


def rosenbrock(x):
    return sum(100 * (x[i + 1] - x[i] ** 2) ** 2 + (1 - x[i]) ** 2 for i in range(len(x) - 1))


def pso(func, low, high, dim, np, maxfes, variant):
    vmax = 0.2 * (high - low)
    pos = [[random.uniform(low, high) for j in range(dim)] for i in range(np)]
    vel = [[random.uniform(-vmax, vmax) for j in range(dim)] for i in range(np)]
    pbest = [x[:] for x in pos]
    pbest_val = [func(x) for x in pos]
    fes = np

    while fes < maxfes:
        if variant == 1:
            w = 0.8 - 0.5 * (fes - np) / max(1, maxfes - np - 1)
            c1 = c2 = 2
        else:
            w = 0.7
            c1 = c2 = 1.49618

        best = min(range(np), key=lambda i: pbest_val[i])
        targets = []
        for i in range(np):
            if variant == 3:
                neighbours = [(i - 1) % np, i, (i + 1) % np]
                best_i = min(neighbours, key=lambda j: pbest_val[j])
            else:
                best_i = best
            targets.append(pbest[best_i][:])

        for i in range(np):
            for j in range(dim):
                r1 = random.random()
                r2 = random.random()
                v = w * vel[i][j] + c1 * r1 * (pbest[i][j] - pos[i][j]) + c2 * r2 * (targets[i][j] - pos[i][j])
                vel[i][j] = max(-vmax, min(vmax, v))
                pos[i][j] += vel[i][j]

            if all(low <= a <= high for a in pos[i]):
                value = func(pos[i])
                fes += 1
                if value < pbest_val[i]:
                    pbest_val[i] = value
                    pbest[i] = pos[i][:]
                if fes == maxfes:
                    break

    best = min(range(np), key=lambda i: pbest_val[i])
    return pbest[best], pbest_val[best], fes


def test():
    functions = [(sphere, -5.12, 5.12), (rastrigin, -5.12, 5.12), (rosenbrock, -5, 10)]
    for func, low, high in functions:
        print('\n' + func.__name__)
        for variant in range(1, 4):
            results = []
            for seed in range(10):
                random.seed(seed)
                x, value, fes = pso(func, low, high, 10, 40, 20000, variant)
                results.append(value)
            print(f'PSO {variant}: best = {min(results):.6e}, avg = {sum(results) / len(results):.6e}, FES = {fes}')


if __name__ == '__main__':
    test()
