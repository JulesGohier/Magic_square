import pycsp3

n: int = int(input("Enter the value of the side of the magic square : "))

x = pycsp3.VarArray(size=[n, n], dom=range(1, n * n + 1))

nb_magic_simple_square: int = int(n * (n * n + 1) / 2)

pycsp3.satisfy(
    pycsp3.AllDifferent(x),
    [pycsp3.Sum(x[i, j] for j in range(n)) == nb_magic_simple_square for i in range(n)],
    [pycsp3.Sum(x[j, i] for j in range(n)) == nb_magic_simple_square for i in range(n)],
    [pycsp3.Sum(x[j, j] for j in range(n)) == nb_magic_simple_square for i in range(n)],
    [pycsp3.Sum(x[j, n - j - 1] for j in range(n)) == nb_magic_simple_square for i in range(n)],

)

if pycsp3.solve() is pycsp3.SAT:
    print("\n" + "The magic number for a simple square is :", nb_magic_simple_square)
    for i in range(n):
        print(pycsp3.values(x[i]))
else:
    print("\n" + "No solution found for the magic simple square !")
