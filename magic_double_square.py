import pycsp3

n: int = 8

x = pycsp3.VarArray(size=[n, n], dom=range(1, n * n + 1))

nb_magic_double_square: int = int(n * (n * n + 1) * (2 * n * n + 1) / 6)

clues: list[list[int]] = [
    [56, 0, 8, 0, 18, 0, 9, 0],
    [0, 20, 0, 0, 7, 0, 0, 10],
    [26, 0, 13, 23, 0, 38, 0, 0],
    [0, 0, 35, 30, 0, 12, 0, 60],
    [0, 25, 0, 0, 41, 0, 50, 0],
    [0, 0, 17, 0, 36, 0, 32, 0],
    [0, 16, 0, 52, 0, 1, 0, 0],
    [44, 0, 28, 37, 0, 0, 21, 0]
]

pycsp3.satisfy(
    pycsp3.AllDifferent(x),
    [x[i][j] == clues[i][j] for i in range(n) for j in range(n) if clues and clues[i][j] > 0],

    [pycsp3.Sum(x[i, j] ** 2 for j in range(n)) == nb_magic_double_square for i in range(n)],
    [pycsp3.Sum(x[j, i] ** 2 for j in range(n)) == nb_magic_double_square for i in range(n)],
    [pycsp3.Sum(x[j, j] ** 2 for j in range(n)) == nb_magic_double_square for i in range(n)],
    [pycsp3.Sum(x[j, n - j - 1] ** 2 for j in range(n)) == nb_magic_double_square for i in range(n)],

)

if pycsp3.solve() is pycsp3.SAT:
    print("\n" + "The magic number for a double square is :", nb_magic_double_square)
    for i in range(n):
        print(pycsp3.values(x[i]))
else:
    print("\n" + "No solution found for the magic double square !")
